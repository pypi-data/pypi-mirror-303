# Copyright 2024, INRAE, France, François Victor <francois.victor@inrae.fr>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the “Software”), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# pylint:disable=too-many-lines

"""file containing the main functions and classes of the package"""
# imports
import itertools
from typing import Optional, Generator
from dataclasses import dataclass
from functools import cached_property, reduce
import operator
from collections import deque

import numpy as np
import numpy.typing as npt
import scipy
from tqdm import tqdm

from prob_dim_red import utils

_ARD_ALPHA_INV_LOWER_BOUND = 1e-200


class NotFittedModelError(Exception):
    """
    Custom exception raised when a model has not been fitted yet.
    """


@dataclass(kw_only=True)
class _LinearGaussianPpcaResult:
    """
    Dataclass for storing the results of Linear Gaussian PPCA MLE estimation.

    Attributes
    ----------
    W : npt.NDArray[np.float64]
        Factor-loading matrix.
    """

    W: npt.NDArray[np.float64]  # pylint:disable=invalid-name


# pylint:disable=too-few-public-methods
class _LinearGaussianPPCAEstim:
    """
    Base class for Linear Gaussian PPCA estimation.

    Attributes
    ----------
    mean : npt.NDArray[np.float64]
        Mean of the data.
    centered_data : npt.NDArray[np.float64]
        Centered data.
    X_dim : int
        Dimension corresponding to the number of variables.
    Z_dim : int
        Dimension of the latent space.
    N : int
        Dimension corresponding to the number of data points.
    _result : None
        Result of the estimation.
    """

    mean: npt.NDArray[np.float64]
    centered_data: npt.NDArray[np.float64]
    X_dim: int
    Z_dim: int
    N: int
    _result: None | _LinearGaussianPpcaResult

    def __init__(self, data: npt.NDArray[np.float64], n_components: int):
        """
        Initialize the Linear Gaussian PPCA estimation object.

        Parameters
        ----------
        data : npt.NDArray[np.float64]
            Data to be modeled.
        n_components : int
            Number of latent dimensions.
        """
        if np.isnan(np.sum(data)):  # handling missing values
            mu_hat = np.nanmean(data, axis=0, keepdims=True)
            valid = np.isfinite(data)
            data = np.where(valid, data, mu_hat)

        # pylint:disable=invalid-name
        self.N, self.X_dim = data.shape
        self.Z_dim = n_components
        self.mean = data.mean(axis=0)
        self.centered_data = data - self.mean[None, :]
        self._result = None

    @property
    def result(self) -> _LinearGaussianPpcaResult:
        """
        Get the result of the estimation.

        Raises
        ------
        NotFittedModelError
            If the model has not been fitted yet.
        """
        if self._result is None:
            raise NotFittedModelError
        return self._result


@dataclass(kw_only=True)
class LinearGaussianPpcaMleResult(_LinearGaussianPpcaResult):
    """
    Dataclass for storing the results of Linear Gaussian PPCA MLE estimation.

    Attributes
    ----------
    mean : npt.NDArray[np.float64]
        Mean of the data.
    noise_var : np.float64
        Noise variance.
    log_likelihood : np.float64
        Log-likelihood of the model.
    model_var_inv : npt.NDArray[np.float64]
        Inverse of the model covariance.
    log_det_model_var : npt.NDArray[np.float64]
        Log-determinant of the model covariance.
    """

    # pylint:disable=invalid-name
    mean: npt.NDArray[np.float64]
    W: npt.NDArray[np.float64]
    noise_var: np.float64
    log_likelihood: np.float64
    model_var_inv: npt.NDArray[np.float64]
    log_det_model_var: npt.NDArray[np.float64]
    bic: np.float64


class LinearGaussianPPCAEstimMLE(_LinearGaussianPPCAEstim):
    """
    Class for Linear Gaussian PPCA estimation using Maximum Likelihood Estimation (MLE).

    Attributes
    ----------
    _result : LinearGaussianPpcaMleResult | None
        Result of the MLE estimation.
    """

    _result: Optional[LinearGaussianPpcaMleResult]

    @cached_property
    def sample_cov(self):
        """
        Cached property to compute sample covariance.
        """
        return (self.centered_data.T @ self.centered_data) / self.N

    @cached_property
    def tr_sample_cov(self):
        """
        Cached sample covariance trace.
        """
        return np.trace(self.sample_cov)

    @cached_property
    def _evd(self):
        """
        Cached truncated eigen value decomposition
        """
        # pylint:disable=duplicate-code
        eig_val, eig_vec = scipy.linalg.eigh(
            self.sample_cov, subset_by_index=(self.X_dim - self.Z_dim, self.X_dim - 1)
        )  # pylint:disable=duplicate-code
        eig_val = eig_val[::-1]
        eig_vec = eig_vec[:, ::-1]

        return eig_val, eig_vec

    def fit(self):
        """
        Fit the Linear Gaussian PPCA model using MLE.
        """
        if self._result is not None:
            return

        eig_val, eig_vec = self._evd

        # for consistancy with model selection these sums must be associative and commutative,
        # numerical errors must not depend on order of the summation
        eig_val_sum = np.float64(
            reduce(operator.add, (utils.FractionOrInf(x) for x in eig_val))
        )
        log_eig_val_sum = np.float64(
            reduce(operator.add, (utils.FractionOrInf(x) for x in np.log(eig_val)))
        )

        noise_var_mle = utils.positive_part(self.tr_sample_cov - eig_val_sum) / (
            self.X_dim - self.Z_dim
        )

        w_mle = eig_vec * np.sqrt(utils.positive_part(eig_val - noise_var_mle))[None, :]

        posterior_precision = w_mle.T @ w_mle + noise_var_mle * np.eye(self.Z_dim)
        posterior_variance = np.linalg.inv(posterior_precision)

        model_var_inv = (1 / (noise_var_mle) if noise_var_mle > 0 else np.inf) * (
            np.eye(self.X_dim) - w_mle @ posterior_variance @ w_mle.T
        )

        log_det_model_var = (self.X_dim - self.Z_dim) * (
            np.log(noise_var_mle) if noise_var_mle > 0 else -np.inf
        ) + log_eig_val_sum
        # pylint:disable=duplicate-code
        log_likelihood = (
            (
                -self.N
                / 2
                * (
                    self.X_dim * np.log(2 * np.pi)
                    + log_det_model_var
                    + utils.trace_matmul(model_var_inv, self.sample_cov, sym=True)
                )
            )
            if noise_var_mle > 0
            else -np.inf
        )  # pylint:disable=duplicate-code

        m_dim = (
            self.X_dim * self.Z_dim - (self.Z_dim * (self.Z_dim + 1)) // 2
        )  # dimension of Stiefel manifold

        log_bic = (
            (
                -(self.N / 2) * log_eig_val_sum
                - (self.N * (self.X_dim - self.Z_dim) / 2) * np.log(noise_var_mle)
                - (m_dim + self.Z_dim) / 2 * np.log(self.N)
            )
            if noise_var_mle > 0
            else -np.inf
        )

        self._result = LinearGaussianPpcaMleResult(
            mean=self.mean,
            W=w_mle,
            noise_var=noise_var_mle,
            log_likelihood=log_likelihood,
            model_var_inv=model_var_inv,
            log_det_model_var=log_det_model_var,
            bic=log_bic,
        )


@dataclass
class _DataDescFixed:
    """
    Dataclass for storing fixed data descriptors.

    Attributes
    ----------
    N : int
        Number of data points.
    X_dim : int
        Dimension of the data.
    Z_dim : int | None
        Dimension of the latent.
    sample_cov : npt.NDArray[np.float64]
        Sample covariance of the data.
    """

    # pylint:disable=invalid-name
    N: int
    X_dim: int
    Z_dim: int | None
    centered_data: npt.NDArray[np.float64]

    @cached_property
    def tr_sample_cov(self):
        """
        Cached property to compute the trace of the sample covariance: N⁻¹XᵀX.
        """
        return utils.trace_matmul(self.centered_data.T, self.centered_data) / self.N

    @cached_property
    def _sample_cov(self):
        """
        Cached property to compute sample covariance.
        """
        return (self.centered_data.T @ self.centered_data) / self.N

    def sample_cov_matmul_smth(self, smth):
        """
        Method to compute the matrix product between the sample covariance and another matrix.
        """
        if self.N < self.X_dim:
            return self.centered_data.T @ ((self.centered_data @ smth) / self.N)
        return (smth.T @ self._sample_cov).T


@dataclass
# pylint:disable=invalid-name
class _EM_state:
    """
    Dataclass for storing the state of the EM algorithm.

    Attributes
    ----------
    W : npt.NDArray[np.float64]
        Factor-loading matrix.
    noise_var : np.float64
        Noise variance σ².
    fixed : _DataDescFixed
        Fixed data description.
    """

    # pylint:disable=invalid-name
    W: npt.NDArray[np.float64]
    noise_var: np.float64
    fixed: _DataDescFixed

    @cached_property
    def noiseless_posterior_precision(self) -> npt.NDArray[np.float64]:
        """Noiseless posterior precision matrix: Wᵀ W"""
        return self.W.T @ self.W

    @cached_property
    def posterior_precision(self) -> npt.NDArray[np.float64]:
        """Posterior precision matrix: M = Wᵀ W + σ² I"""
        return self.noiseless_posterior_precision + self.noise_var * np.eye(
            self.W.shape[1]
        )

    @cached_property
    def posterior_variance(self) -> npt.NDArray[np.float64]:
        """Posterior variance matrix: (Wᵀ W + σ²I)⁻¹ = M⁻¹"""
        return np.linalg.inv(self.posterior_precision)

    @cached_property
    def sample_cov_factor_load_mat_prod(self) -> npt.NDArray[np.float64]:
        """Sample covariance and factor loading matrix product: (Wᵀ Sᵀ)ᵀ= SW"""
        return self.fixed.sample_cov_matmul_smth(self.W)

    @cached_property
    def factor_load_sample_cov_factor_load_mat_prod(self) -> npt.NDArray[np.float64]:
        """Factor loading, sample covariance, and factor loading matrix product: Wᵀ(WᵀSᵀ)ᵀ= Wᵀ SW"""
        return self.W.T @ self.sample_cov_factor_load_mat_prod

    @cached_property
    def posterior_variance_factor_load_sample_cov_factor_load_mat_prod(
        self,
    ) -> npt.NDArray[np.float64]:
        """Posterior variance, factor loading, sample covariance
        and factor loading matrix product: M⁻¹ Wᵀ S W"""
        return (
            self.posterior_variance @ self.factor_load_sample_cov_factor_load_mat_prod
        )

    @cached_property
    def posterior_variance_factor_load_sample_cov_factor_load_posterior_variance_mat_prod(
        self,
    ) -> npt.NDArray[np.float64]:
        """Posterior variance, factor loading, sample covariance,
        factor loading, and posterior variance matrix product: M⁻¹ Wᵀ S W M⁻¹"""
        return (
            self.posterior_variance_factor_load_sample_cov_factor_load_mat_prod
            @ self.posterior_variance
        )  # M⁻¹ Wᵀ S W M⁻¹

    @cached_property
    def model_var(self) -> npt.NDArray[np.float64]:
        """Model covariance matrix: W Wᵀ + σ²I = C"""
        return self.W @ self.W.T + self.noise_var * np.eye(self.fixed.X_dim)

    @cached_property
    def log_det_model_var(self) -> npt.NDArray[np.float64]:
        """Log-determinant of the model covariance matrix: log |C|"""
        return np.linalg.slogdet(self.model_var)[1]

    @cached_property
    def model_var_inv(self) -> npt.NDArray[np.float64]:
        """Inverse of the model covariance matrix: C⁻¹ = (W Wᵀ + σ²I)⁻¹"""
        return np.linalg.inv(self.model_var)

    @cached_property
    def complete_log_likelihood(self) -> np.float64:
        """
        Complete log-likelihood of the model.
        """
        # pylint:disable=line-too-long
        if self.noise_var == 0:
            return -np.inf

        return (-self.fixed.N / 2) * (
            self.fixed.Z_dim * np.log(2 * np.pi)
            + self.fixed.X_dim * np.log(2 * np.pi * self.noise_var)
            + self.noise_var * np.trace(self.posterior_variance)
            + np.trace(
                self.posterior_variance_factor_load_sample_cov_factor_load_posterior_variance_mat_prod
            )
            + (1 / self.noise_var)
            * (
                self.fixed.tr_sample_cov
                - 2
                * np.trace(
                    self.posterior_variance_factor_load_sample_cov_factor_load_mat_prod
                )
                + utils.trace_matmul(
                    self.posterior_variance_factor_load_sample_cov_factor_load_posterior_variance_mat_prod,
                    self.noiseless_posterior_precision,
                    sym=True,
                )
            )
            + utils.trace_matmul(
                self.posterior_variance, self.noiseless_posterior_precision, sym=True
            )
        )

    @cached_property
    def log_likelihood(self) -> np.float64:
        """
        Log-likelihood of the model.
        """
        if self.noise_var == 0:
            return -np.inf
        return (
            -self.fixed.N
            / 2
            * (
                self.fixed.X_dim * np.log(2 * np.pi)
                + self.log_det_model_var
                + 1
                / self.noise_var
                * (
                    self.fixed.tr_sample_cov
                    - np.trace(
                        self.posterior_variance_factor_load_sample_cov_factor_load_mat_prod
                    )
                )
            )
        )


@dataclass(kw_only=True)
class LinearGaussianPpcaEMResult(_LinearGaussianPpcaResult):
    """
    Dataclass for storing the results of Linear Gaussian PPCA EM estimation.

    Attributes
    ----------
    mean : npt.NDArray[np.float64]
        Mean of the data.
    noise_var : np.float64
        Noise variance.
    complete_log_likelihood : np.float64
        Complete log-likelihood of the model.
    log_likelihood : np.float64
        Marginal log-likelihood of the model.
    model_var_inv : npt.NDArray[np.float64]
        Inverse of the model covariance.
    log_det_model_var : npt.NDArray[np.float64]
        Log-determinant of the model covariance.
    """

    # pylint:disable=invalid-name
    mean: npt.NDArray[np.float64]
    noise_var: np.float64
    complete_log_likelihood: np.float64
    log_likelihood: np.float64
    model_var_inv: npt.NDArray[np.float64]
    log_det_model_var: npt.NDArray[np.float64]


class LinearGaussianPPCAEstimEM(_LinearGaussianPPCAEstim):
    """
    Class for Linear Gaussian PPCA estimation using the Expectation-Maximization (EM) algorithm.

    Attributes
    ----------
    fixed : _DataDescFixed
        Fixed data descriptors.
    state : _EM_state | None
        State of the EM algorithm.
    _result : LinearGaussianPpcaEMResult | None
        Result of the EM estimation.
    """

    fixed: _DataDescFixed
    state: Optional[_EM_state]
    _result: Optional[LinearGaussianPpcaEMResult]

    def __init__(self, *args, **kwargs):
        """
        Initialize the Linear Gaussian PPCA EM estimation object.
        """
        super().__init__(*args, **kwargs)
        self.fixed = _DataDescFixed(
            N=self.N,
            X_dim=self.X_dim,
            Z_dim=self.Z_dim,
            centered_data=self.centered_data,
        )
        self.state = None

    def _em_init(self):
        """
        Initialize the EM algorithm.
        """
        alpha = 0.5
        scaling_factor_w = (
            alpha * self.fixed.tr_sample_cov / (self.fixed.X_dim * self.fixed.Z_dim)
        ) ** 0.5

        # pylint:disable=invalid-name
        W = scaling_factor_w * np.random.normal(size=(self.X_dim, self.Z_dim))

        # U, S, _ = np.linalg.svd(W, full_matrices=False)
        # W = U * S[None,:]

        noise_var = (1 - alpha) * self.fixed.tr_sample_cov / self.fixed.X_dim
        # the convergence is slower if the init value is greater than true noise var.

        self.state = _EM_state(W=W, noise_var=noise_var, fixed=self.fixed)

    def _em_step(self):
        """
        Perform one step of the EM algorithm.
        """
        # pylint:disable=invalid-name
        # pylint:disable=line-too-long
        W_new = self.state.sample_cov_factor_load_mat_prod @ np.linalg.inv(
            self.state.noise_var * np.eye(self.Z_dim)
            + self.state.posterior_variance_factor_load_sample_cov_factor_load_mat_prod
        )

        noise_var_new = (
            1
            / self.X_dim
            * (
                self.fixed.tr_sample_cov
                - utils.trace_matmul(
                    self.state.sample_cov_factor_load_mat_prod,
                    self.state.posterior_variance @ W_new.T,
                )
            )
        )

        self.state = _EM_state(W=W_new, noise_var=noise_var_new, fixed=self.fixed)

    def _em_states(
        self, max_iterations, error_tolerance, tolerance_window
    ) -> Generator[_EM_state, None, None]:
        """
        early stopping
        """
        self._em_init()
        yield self.state
        que_crit = deque()
        crit = self.state.log_likelihood
        que_crit.append(crit)
        for _ in (
            range(max_iterations) if max_iterations is not None else itertools.count()
        ):
            self._em_step()

            # if count % 120 == 0:
            #     U, S, _ = np.linalg.svd(self.state.W, full_matrices=False)
            #     self.state.W = U * S[None,:]

            yield self.state
            crit = self.state.log_likelihood
            que_crit.append(crit)

            if len(que_crit) > tolerance_window:
                if (crit - que_crit.popleft()) / tolerance_window < error_tolerance:
                    break

        U, S, _ = np.linalg.svd(self.state.W, full_matrices=False)
        self.state.W = U * S[None, :]

        self._result = LinearGaussianPpcaEMResult(
            mean=self.mean,
            W=self.state.W,
            noise_var=self.state.noise_var,
            complete_log_likelihood=self.state.complete_log_likelihood,
            log_likelihood=self.state.log_likelihood,
            model_var_inv=self.state.model_var_inv,
            log_det_model_var=self.state.log_det_model_var,
        )

    def fit(  # pylint:disable=too-many-positional-arguments, too-many-arguments
        self,
        max_iterations=None,
        error_tolerance=1e-6,
        tolerance_window=10,
        trace=False,
        progress=True,
    ) -> Optional[list[_EM_state]]:
        """
        Fit the Linear Gaussian PPCA model using the EM algorithm.

        Parameters
        ----------
        max_iterations : int | None
            Maximum number of iterations for the EM algorithm.
        error_tolerance : float
            Tolerance for the convergence of the EM algorithm.
        tolerance_window : int
            Window size for moving average over criterion.
        trace : bool
            Whether to store the intermediate states of the EM algorithm.
        progress : bool
            Show progress with tqdm (not compatible with trace).

        Returns
        -------
        Generator[_EM_state] | None
            intermediate states of the EM algorithm if trace is True, otherwise None.
        """
        states = self._em_states(max_iterations, error_tolerance, tolerance_window)
        if trace:
            return states

        if progress:
            last_comp_lik = 0
            scale = 0
            for state in (progress_bar := tqdm(states, unit_scale=True)):
                gap, last_comp_lik, last_lik = (
                    state.complete_log_likelihood - last_comp_lik,
                    state.complete_log_likelihood,
                    state.log_likelihood,
                )
                scale += 0.1 * (np.log10(np.abs(gap)) - scale)
                dscale = max(int(-np.floor(scale - 0.5)), 0)
                fmt_comp_lik = "comp-log-lik={" + f":.{dscale:d}f" + "}"
                fmt_marg_lik = "marg-log-lik={" + f":.{dscale:d}f" + "}"
                progress_bar.set_postfix_str(
                    fmt_comp_lik.format(last_comp_lik)
                    + " - "
                    + fmt_marg_lik.format(last_lik),
                    refresh=False,
                )
        else:
            for _ in states:
                pass

        return self


@dataclass
# pylint:disable=invalid-name
class no_cov_EM_state:
    """
    Dataclass for storing the state of the EM algorithm.

    Attributes
    ----------
    W : npt.NDArray[np.float64]
        Factor-loading matrix.
    noise_var : np.float64
        Noise variance σ².
    fixed : _DataDescFixed
        Fixed data description.
    """

    # pylint:disable=invalid-name
    W: npt.NDArray[np.float64]
    noise_var: np.float64
    fixed: _DataDescFixed

    @cached_property
    def noiseless_posterior_precision(self) -> npt.NDArray[np.float64]:
        """Noiseless posterior precision matrix: Wᵀ W"""
        return self.W.T @ self.W

    @cached_property
    def posterior_precision(self) -> npt.NDArray[np.float64]:
        """Posterior precision matrix: M = Wᵀ W + σ² I"""
        return self.noiseless_posterior_precision + self.noise_var * np.eye(
            self.W.shape[1]
        )

    @cached_property
    def posterior_variance(self) -> npt.NDArray[np.float64]:
        """Posterior variance matrix: (Wᵀ W + σ²I)⁻¹ = M⁻¹"""
        return np.linalg.inv(self.posterior_precision)

    @cached_property
    def centered_data_factor_load_mat_prod(self) -> npt.NDArray[np.float64]:
        """Matrix product of centered data and factor loading matrix: (Wᵀ Xᵀ)ᵀ"""
        return (self.W.T @ self.fixed.centered_data.T).T

    @cached_property
    def posterior_mean(self) -> npt.NDArray[np.float64]:
        """Posterior: X W M⁻¹"""
        return self.centered_data_factor_load_mat_prod @ self.posterior_variance

    @cached_property
    def tr_inter_calc_comp_lik(self) -> npt.NDArray[np.float64]:
        """Trace of intermediary calculation in complete likelihood: Tr(Wᵀ Xᵀ X W M⁻¹)"""
        return np.sum(
            (
                (self.centered_data_factor_load_mat_prod).T
                @ self.centered_data_factor_load_mat_prod
            )
            * self.posterior_variance
        )

    @cached_property
    def inter_calc_uninv(self) -> npt.NDArray[np.float64]:
        """Intermediary calculation not inverted: N σ² M⁻¹ + M⁻¹ Wᵀ Xᵀ X W M⁻¹"""
        return (self.posterior_mean.T @ self.posterior_mean) + (
            self.noise_var * self.posterior_variance * self.fixed.N
        )

    @cached_property
    def tr_inter_calc_uninv(self) -> npt.NDArray[np.float64]:
        """Trace of intermediary calculation not inverted: Tr(N σ² M⁻¹ + M⁻¹ N⁻¹ Wᵀ Xᵀ X W M⁻¹)"""
        return np.trace(self.inter_calc_uninv)

    @cached_property
    def tr_inter_calc_uninv_noiseless_posterior_precision_mat_prod(
        self,
    ) -> npt.NDArray[np.float64]:
        """Trace of matrix prod of intermediary calculation
        not inverted and noiseless posterior precision:
        Tr((N σ² M⁻¹ + M⁻¹ N⁻¹ Wᵀ Xᵀ X W M⁻¹) Wᵀ W)
        """
        return utils.trace_matmul(
            self.inter_calc_uninv, self.noiseless_posterior_precision, sym=True
        )

    @cached_property
    def inter_calc_inv(self) -> npt.NDArray[np.float64]:
        """intermediary calculation not inverted: (N σ² M⁻¹ + M⁻¹ N⁻¹ Wᵀ Xᵀ X W M⁻¹)⁻¹"""
        return np.linalg.inv(self.inter_calc_uninv)

    @cached_property
    def model_var(self) -> npt.NDArray[np.float64]:
        """Model covariance matrix: W Wᵀ + σ²I = C"""
        return self.W @ self.W.T + self.noise_var * np.eye(self.fixed.X_dim)

    @cached_property
    def log_det_model_var(self) -> npt.NDArray[np.float64]:
        """Log-determinant of the model covariance matrix: log |C|"""
        return np.linalg.slogdet(self.model_var)[1]

    @cached_property
    def model_var_inv(self) -> npt.NDArray[np.float64]:
        """Inverse of the model covariance matrix: C⁻¹ = (W Wᵀ + σ²I)⁻¹"""
        return np.linalg.inv(self.model_var)

    @cached_property
    def complete_log_likelihood(self) -> np.float64:
        """
        Complete log-likelihood of the model.
        """
        # pylint:disable=line-too-long
        if self.noise_var == 0:
            return -np.inf

        return (
            -(
                self.fixed.N
                / 2
                * (self.fixed.X_dim * np.log(2 * np.pi * self.noise_var))
            )
            - (self.fixed.N / 2 * (+self.fixed.Z_dim * np.log(2 * np.pi)))
            - self.tr_inter_calc_uninv / 2
            - (
                self.tr_inter_calc_uninv_noiseless_posterior_precision_mat_prod
                / (2 * self.noise_var)
            )
            - self.fixed.N * (self.fixed.tr_sample_cov / (2 * self.noise_var))
            + self.tr_inter_calc_comp_lik / self.noise_var
        )

    @cached_property
    def log_likelihood(self) -> np.float64:
        """
        Log-likelihood of the model.
        """
        if self.noise_var == 0:
            return -np.inf
        return (
            -self.fixed.N
            / 2
            * (
                self.fixed.X_dim * np.log(2 * np.pi)
                + self.log_det_model_var
                + 1
                / self.noise_var
                * (
                    self.fixed.tr_sample_cov
                    - self.tr_inter_calc_comp_lik / self.fixed.N
                )
            )
        )


@dataclass(kw_only=True)
class LinearGaussianPpcaNoCovEMResult(_LinearGaussianPpcaResult):
    """
    Dataclass for storing the results of Linear Gaussian PPCA EM estimation.

    Attributes
    ----------
    mean : npt.NDArray[np.float64]
        Mean of the data.
    noise_var : np.float64
        Noise variance.
    complete_log_likelihood : np.float64
        Complete log-likelihood of the model.
    log_likelihood : np.float64
        Marginal log-likelihood of the model.
    model_var_inv : npt.NDArray[np.float64]
        Inverse of the model covariance.
    log_det_model_var : npt.NDArray[np.float64]
        Log-determinant of the model covariance.
    """

    # pylint:disable=invalid-name
    mean: npt.NDArray[np.float64]
    noise_var: np.float64
    complete_log_likelihood: np.float64
    log_likelihood: np.float64
    model_var_inv: npt.NDArray[np.float64]
    log_det_model_var: npt.NDArray[np.float64]


class LinearGaussianPPCAEstimNoCovEM(_LinearGaussianPPCAEstim):
    """
    Class for Linear Gaussian PPCA estimation using the Expectation-Maximization (EM) algorithm.

    Attributes
    ----------
    fixed : _DataDescFixed
        Fixed data descriptors.
    state : no_cov_EM_state | None
        State of the EM algorithm.
    _result : LinearGaussianPpcaEMResult | None
        Result of the EM estimation.
    """

    fixed: _DataDescFixed
    state: Optional[no_cov_EM_state]
    _result: Optional[LinearGaussianPpcaNoCovEMResult]

    def __init__(self, *args, **kwargs):
        """
        Initialize the Linear Gaussian PPCA EM estimation object.
        """
        super().__init__(*args, **kwargs)
        self.fixed = _DataDescFixed(
            N=self.N,
            X_dim=self.X_dim,
            Z_dim=self.Z_dim,
            centered_data=self.centered_data,
        )
        self.state = None

    def _em_init(self):
        """
        Initialize the EM algorithm.
        """
        alpha = 0.5
        scaling_factor_w = (
            alpha * self.fixed.tr_sample_cov / (self.fixed.X_dim * self.fixed.Z_dim)
        ) ** 0.5

        # pylint:disable=invalid-name
        W = scaling_factor_w * np.random.normal(size=(self.X_dim, self.Z_dim))

        # U, S, _ = np.linalg.svd(W, full_matrices=False)
        # W = U * S[None,:]

        noise_var = (1 - alpha) * self.fixed.tr_sample_cov / self.fixed.X_dim
        # the convergence is slower if the init value is greater than true noise var.

        self.state = no_cov_EM_state(W=W, noise_var=noise_var, fixed=self.fixed)

    def _em_step(self):
        """
        Perform one step of the EM algorithm.
        """
        # pylint:disable=invalid-name
        # pylint:disable=line-too-long
        W_new = self.fixed.centered_data.T @ (
            self.state.posterior_mean @ self.state.inter_calc_inv
        )

        noise_var_new = (
            1
            / (self.X_dim * self.fixed.N)
            * (
                self.fixed.tr_sample_cov * self.fixed.N
                - 2
                * utils.trace_matmul(
                    self.fixed.centered_data.T @ self.state.posterior_mean,
                    W_new.T,
                    sym=False,
                )
                + utils.trace_matmul(
                    self.state.inter_calc_uninv, W_new.T @ W_new, sym=True
                )
            )
        )

        self.state = no_cov_EM_state(W=W_new, noise_var=noise_var_new, fixed=self.fixed)

    def _em_states(
        self, max_iterations, error_tolerance, tolerance_window
    ) -> Generator[no_cov_EM_state, None, None]:
        """
        early stopping
        """
        self._em_init()
        yield self.state
        que_crit = deque()
        crit = self.state.log_likelihood
        que_crit.append(crit)
        for _ in (
            range(max_iterations) if max_iterations is not None else itertools.count()
        ):
            self._em_step()

            # if count % 120 == 0:
            #     U, S, _ = np.linalg.svd(self.state.W, full_matrices=False)
            #     self.state.W = U * S[None,:]

            yield self.state
            crit = self.state.log_likelihood
            que_crit.append(crit)

            if len(que_crit) > tolerance_window:
                if (crit - que_crit.popleft()) / tolerance_window < error_tolerance:
                    break

        U, S, _ = np.linalg.svd(self.state.W, full_matrices=False)
        self.state.W = U * S[None, :]

        self._result = LinearGaussianPpcaNoCovEMResult(
            mean=self.mean,
            W=self.state.W,
            noise_var=self.state.noise_var,
            complete_log_likelihood=self.state.complete_log_likelihood,
            log_likelihood=self.state.log_likelihood,
            model_var_inv=self.state.model_var_inv,
            log_det_model_var=self.state.log_det_model_var,
        )

    def fit(  # pylint:disable=too-many-positional-arguments, too-many-arguments
        self,
        max_iterations=None,
        error_tolerance=1e-6,
        tolerance_window=10,
        trace=False,
        progress=True,
    ) -> Optional[list[no_cov_EM_state]]:
        """
        Fit the Linear Gaussian PPCA model using the EM algorithm.

        Parameters
        ----------
        max_iterations : int | None
            Maximum number of iterations for the EM algorithm.
        error_tolerance : float
            Tolerance for the convergence of the EM algorithm.
        tolerance_window : int
            Window size for moving average over criterion.
        trace : bool
            Whether to store the intermediate states of the EM algorithm.
        progress : bool
            Show progress with tqdm (not compatible with trace).

        Returns
        -------
        Generator[_EM_state] | None
            intermediate states of the EM algorithm if trace is True, otherwise None.
        """
        states = self._em_states(max_iterations, error_tolerance, tolerance_window)
        if trace:
            return states

        if progress:
            last_comp_lik = 0
            scale = 0
            for state in (progress_bar := tqdm(states, unit_scale=True)):
                gap, last_comp_lik, last_lik = (
                    state.complete_log_likelihood - last_comp_lik,
                    state.complete_log_likelihood,
                    state.log_likelihood,
                )
                scale += 0.1 * (np.log10(np.abs(gap)) - scale)
                dscale = max(int(-np.floor(scale - 0.5)), 0)
                fmt_comp_lik = "comp-log-lik={" + f":.{dscale:d}f" + "}"
                fmt_marg_lik = "marg-log-lik={" + f":.{dscale:d}f" + "}"
                progress_bar.set_postfix_str(
                    fmt_comp_lik.format(last_comp_lik)
                    + " - "
                    + fmt_marg_lik.format(last_lik),
                    refresh=False,
                )
        else:
            for _ in states:
                pass

        return self


class MLE_Model_Selection(LinearGaussianPPCAEstimMLE):
    """
    Class for model selection of MLE Linear Gaussian PPCA using Minka's
    Bayesian Entropy Criterion approximation.

    Attributes
    ----------
    n_components_max: int | None
        Maximum number of components specified by the user
    """

    n_components_max: int | None

    def __init__(self, data, n_components_max=None):
        super().__init__(data, n_components=None)
        self.n_components_max = (
            n_components_max if n_components_max is not None else self.X_dim - 1
        )
        self.n_components_max = min(self.n_components_max, self.X_dim)

    def fit(self):
        if self.Z_dim is not None:
            return super().fit()

        lambdas, eig_vecs = np.empty(0), np.empty((self.X_dim, 0))

        # computing bics by blocks of powers of 2 until max bic
        for upper, lower in itertools.pairwise(
            2**k if k > 0 else 0 for k in itertools.count()
        ):
            lower = min(lower, self.n_components_max)

            # computing eigvals by blocks bounded by lower and upper
            # s.t. eigval[n - lower] < eigval[n - upper]
            eig_val, eig_vec = scipy.linalg.eigh(
                self.sample_cov,
                subset_by_index=(self.X_dim - lower, self.X_dim - upper - 1),
            )

            lambdas = np.append(lambdas, eig_val[::-1])
            eig_vecs = np.append(eig_vecs, eig_vec[:, ::-1], axis=1)

            vec_k = np.arange(1, lower + 1)

            bic = (
                -self.N / 2 * np.cumsum(np.log(lambdas))
                - self.N
                * (self.X_dim - vec_k)
                / 2
                * np.log(
                    (self.tr_sample_cov - np.cumsum(lambdas)) / (self.X_dim - vec_k)
                )
                - (self.X_dim * vec_k - vec_k * (vec_k + 1) / 2 + vec_k)
                / 2
                * np.log(self.N)
            )

            if (bic.max() != bic[-1]) or (lower >= self.n_components_max + 1):
                break

        self.Z_dim = bic.argmax() + 1
        self._evd = lambdas[: self.Z_dim], eig_vecs[:, : self.Z_dim]
        return super().fit()


class MLE_Model_Selection_v2(LinearGaussianPPCAEstimMLE):
    """
    Class for model selection of MLE Linear Gaussian PPCA using
    Minka's Bayesian Entropy Criterion approximation.

    Attributes
    ----------
    n_components_max: int | None
        Maximum number of components specified by the user
    strategy: str
        Strategy to compute BICs, either 'grow' or 'all'
    """

    n_components_max: int | None
    strategy: str
    _bics: np.ndarray

    def __init__(
        self,
        data: np.ndarray,
        n_components_max: Optional[int] = None,
        strategy: str = "grow",
    ):
        super().__init__(data, n_components=None)
        self.n_components_max = (
            n_components_max if n_components_max is not None else self.X_dim - 1
        )
        self.n_components_max = min(self.n_components_max, self.X_dim - 1)
        self.strategy = strategy
        self._bics = np.empty(0)

    def fit(self):
        if self.Z_dim is not None:
            return super().fit()

        lambdas, eig_vecs = np.empty(0), np.empty((self.X_dim, 0))

        if self.strategy == "grow":
            # computing bics by blocks of powers of 2 until max bic
            for upper, lower in itertools.pairwise(
                2**k if k > 0 else 0 for k in itertools.count()
            ):
                lower = min(lower, self.n_components_max)

                # computing eigvals by blocks bounded by lower and upper
                # s.t. eigval[n - lower] < eigval[n - upper]
                eig_val, eig_vec = scipy.linalg.eigh(
                    self.sample_cov,
                    subset_by_index=(self.X_dim - lower, self.X_dim - upper - 1),
                )

                lambdas = utils.positive_part(np.append(lambdas, eig_val[::-1]))
                eig_vecs = np.append(eig_vecs, eig_vec[:, ::-1], axis=1)

                # for consistancy with model selection these sums must be associative and
                # commutative, numerical errors must not depend on order of the summation
                lambdas_cumsum = np.array(
                    list(
                        itertools.accumulate(
                            (utils.FractionOrInf(x) for x in lambdas),
                            operator.add,
                        )
                    ),
                    dtype=np.float64,
                )
                log_lambdas_cumsum = np.array(
                    list(
                        itertools.accumulate(
                            (
                                utils.FractionOrInf(x)
                                for x in utils.log_with_zeros(lambdas)
                            ),
                            operator.add,
                        )
                    ),
                    dtype=np.float64,
                )

                vec_k = np.arange(1, lower + 1)
                bics = (
                    -self.N / 2 * log_lambdas_cumsum
                    - self.N
                    * (self.X_dim - vec_k)
                    / 2
                    * utils.log_with_zeros(
                        utils.positive_part(self.tr_sample_cov - lambdas_cumsum)
                        / (self.X_dim - vec_k)
                    )
                    - (self.X_dim * vec_k - vec_k * (vec_k + 1) / 2 + vec_k)
                    / 2
                    * np.log(self.N)
                )

                if (bics.max() != bics[-1]) or (lower >= self.n_components_max + 1):
                    break

        elif self.strategy == "all":
            lower = self.n_components_max

            eig_val, eig_vec = scipy.linalg.eigh(
                self.sample_cov,
                subset_by_index=(self.X_dim - lower, self.X_dim - 1),
            )
            lambdas = utils.positive_part(np.append(lambdas, eig_val[::-1]))
            eig_vecs = np.append(eig_vecs, eig_vec[:, ::-1], axis=1)

            vec_k = np.arange(1, lower + 1)

            # for consistancy with model selection these sums must be associative and commutative,
            # numerical errors must not depend on order of the summation
            lambdas_cumsum = np.array(
                list(
                    itertools.accumulate(
                        (utils.FractionOrInf(x) for x in lambdas),
                        operator.add,
                    )
                ),
                dtype=np.float64,
            )
            log_lambdas_cumsum = np.array(
                list(
                    itertools.accumulate(
                        (utils.FractionOrInf(x) for x in utils.log_with_zeros(lambdas)),
                        operator.add,
                    )
                ),
                dtype=np.float64,
            )

            bics = (
                -self.N / 2 * log_lambdas_cumsum
                - self.N
                * (self.X_dim - vec_k)
                / 2
                * utils.log_with_zeros(
                    utils.positive_part(self.tr_sample_cov - lambdas_cumsum)
                    / (self.X_dim - vec_k)
                )
                - (self.X_dim * vec_k - vec_k * (vec_k + 1) / 2 + vec_k)
                / 2
                * np.log(self.N)
            )

        self._bics = bics
        self.Z_dim = self._bics.argmax() + 1
        self._evd = lambdas[: self.Z_dim], eig_vecs[:, : self.Z_dim]
        return super().fit()

    @property
    def bics(self) -> np.ndarray:
        """
        Get the BICs computed during the model selection.

        Returns
        -------
        np.ndarray
            Array of BIC values.
        """
        if self.Z_dim is None:
            raise NotFittedModelError

        return self._bics


def ppca_mle(
    data: npt.NDArray[np.float64], n_components: int
) -> LinearGaussianPpcaMleResult:
    """
    Perform Linear Gaussian PPCA estimation using Maximum Likelihood Estimation (MLE).

    Parameters
    ----------
    data : npt.NDArray[np.float64]
        Data to be modeled.
    n_components : int
        Number of latent dimensions.

    Returns
    -------
    LinearGaussianPpcaMleResult
        Result of the MLE estimation.
    """
    model_object = LinearGaussianPPCAEstimMLE(data=data, n_components=n_components)
    model_object.fit()
    return model_object.result


@dataclass
# pylint:disable=invalid-name
class _ARD_state:
    """
    Dataclass for storing the state of the ARD version of EM algorithm.

    Attributes
    ----------
    W : npt.NDArray[np.float64]
        Factor-loading matrix.
    noise_var : np.float64
        Noise variance σ².
    fixed : _DataDescFixed
        Fixed data description.
    """

    # pylint:disable=invalid-name
    W: npt.NDArray[np.float64]
    noise_var: np.float64
    fixed: _DataDescFixed
    alpha: npt.NDArray[np.float64]

    @classmethod
    def from_raw_parameters(
        cls, W: npt.NDArray[np.float64], noise_var: np.float64, fixed: _DataDescFixed
    ) -> "_ARD_state":
        """
        Classmethod constructor of _ARD_state that takes in input parameters and
        prevents numerical errors (e.g divide by zero, divide by infinity).
        It computes the ARD matrix : diag(X_dim/wᵢᵀwᵢ)
        It also modifies the class by discarding the 'irrelevant' dimensions of W.
        """
        alpha_inv = np.einsum("ji,ji->i", W, W) / fixed.X_dim
        mask = alpha_inv > _ARD_ALPHA_INV_LOWER_BOUND
        return cls(W[:, mask], noise_var, fixed, 1 / alpha_inv[mask])

    @cached_property
    def noiseless_posterior_precision(self) -> npt.NDArray[np.float64]:
        """Noiseless posterior precision matrix: Wᵀ W"""
        return self.W.T @ self.W

    @cached_property
    def posterior_precision(self) -> npt.NDArray[np.float64]:
        """Posterior precision matrix: M = Wᵀ W + σ² I"""
        return self.noiseless_posterior_precision + self.noise_var * np.eye(
            self.W.shape[1]
        )

    @cached_property
    def posterior_variance(self) -> npt.NDArray[np.float64]:
        """Posterior variance matrix: (Wᵀ W + σ²I)⁻¹ = M⁻¹"""
        return np.linalg.inv(self.posterior_precision)

    @cached_property
    def alpha_posterior_precision_prod(self) -> npt.NDArray[np.float64]:
        """ARD matrix and posterior precision matrix product : AM"""
        return self.alpha[:, None] * self.posterior_precision

    @cached_property
    def sample_cov_factor_load_mat_prod(self) -> npt.NDArray[np.float64]:
        """Sample covariance and factor loading matrix product: (Wᵀ Sᵀ)ᵀ= SW"""
        return self.fixed.sample_cov_matmul_smth(self.W)

    @cached_property
    def factor_load_sample_cov_factor_load_mat_prod(self) -> npt.NDArray[np.float64]:
        """Factor loading, sample covariance, and factor loading matrix product: Wᵀ(WᵀSᵀ)ᵀ= Wᵀ SW"""
        return self.W.T @ self.sample_cov_factor_load_mat_prod

    @cached_property
    def posterior_variance_factor_load_sample_cov_factor_load_mat_prod(
        self,
    ) -> npt.NDArray[np.float64]:
        """Posterior variance, factor loading, sample covariance
        and factor loading matrix product: M⁻¹ Wᵀ S W"""
        return (
            self.posterior_variance @ self.factor_load_sample_cov_factor_load_mat_prod
        )

    @cached_property
    def posterior_variance_factor_load_sample_cov_factor_load_posterior_variance_mat_prod(
        self,
    ) -> npt.NDArray[np.float64]:
        """Posterior variance, factor loading, sample covariance,
        factor loading, and posterior variance matrix product: M⁻¹ Wᵀ S W M⁻¹"""
        return (
            self.posterior_variance_factor_load_sample_cov_factor_load_mat_prod
            @ self.posterior_variance
        )  # M⁻¹ Wᵀ S W M⁻¹

    @cached_property
    def model_var(self) -> npt.NDArray[np.float64]:
        """Model covariance matrix: W Wᵀ + σ²I = C"""
        return self.W @ self.W.T + self.noise_var * np.eye(self.fixed.X_dim)

    @cached_property
    def log_det_model_var(self) -> npt.NDArray[np.float64]:
        """Log-determinant of the model covariance matrix: log |C|"""
        return np.linalg.slogdet(self.model_var)[1]

    @cached_property
    def model_var_inv(self) -> npt.NDArray[np.float64]:
        """Inverse of the model covariance matrix: C⁻¹ = (W Wᵀ + σ²I)⁻¹"""
        return np.linalg.inv(self.model_var)

    @cached_property
    def complete_log_likelihood(self) -> np.float64:
        """
        Complete log-likelihood of the model.
        """
        # pylint:disable=line-too-long
        return (
            (
                -self.fixed.N
                * self.fixed.X_dim
                / 2
                * np.log(2 * np.pi * self.noise_var)
                - self.fixed.N
                / 2
                * self.noise_var
                * (
                    np.trace(self.posterior_variance)
                    + np.trace(
                        self.posterior_variance_factor_load_sample_cov_factor_load_posterior_variance_mat_prod
                    )
                )
                - 1 / 2 * self.fixed.N * self.fixed.tr_sample_cov
            )
            + 1
            / self.noise_var
            * np.trace(
                self.fixed.N
                * self.posterior_variance_factor_load_sample_cov_factor_load_mat_prod
            )
            - self.fixed.N
            / 2
            * utils.trace_matmul(
                self.posterior_variance, self.noiseless_posterior_precision, sym=True
            )
            - self.fixed.N
            / (2 * self.noise_var)
            * utils.trace_matmul(
                self.posterior_variance_factor_load_sample_cov_factor_load_posterior_variance_mat_prod,
                self.noiseless_posterior_precision,
                sym=True,
            )
        )

    @cached_property
    def log_likelihood(self) -> np.float64:
        """
        Log-likelihood of the model.
        """
        return (
            -self.fixed.N
            / 2
            * (
                self.fixed.X_dim * np.log(2 * np.pi)
                + self.log_det_model_var
                + 1
                / self.noise_var
                * (
                    self.fixed.tr_sample_cov
                    - np.trace(
                        self.posterior_variance_factor_load_sample_cov_factor_load_mat_prod
                    )
                )
            )
        )


@dataclass(kw_only=True)
# pylint:disable=too-many-instance-attributes
class LinearGaussianPpcaARDResult(_LinearGaussianPpcaResult):
    """
    Dataclass for storing the results of Linear Gaussian PPCA ARD estimation via EM.

    Attributes
    ----------
    mean : npt.NDArray[np.float64]
        Mean of the data.
    A : npt.NDArray[np.float64]
        automatic relevance determination matrix.
    noise_var : np.float64
        Noise variance.
    complete_log_likelihood : np.float64
        Complete log-likelihood of the model.
    log_likelihood : np.float64
        Marginal log-likelihood of the model.
    model_var_inv : npt.NDArray[np.float64]
        Inverse of the model covariance.
    log_det_model_var : npt.NDArray[np.float64]
        Log-determinant of the model covariance.
    """

    # pylint:disable=invalid-name
    mean: npt.NDArray[np.float64]
    A: npt.NDArray[np.float64]
    noise_var: np.float64
    complete_log_likelihood: np.float64
    log_likelihood: np.float64
    model_var_inv: npt.NDArray[np.float64]
    log_det_model_var: npt.NDArray[np.float64]


class LinearGaussianPPCAEstimARD(_LinearGaussianPPCAEstim):
    """
    Class for Linear Gaussian PPCA estimation using the Expectation-Maximization (EM) algorithm.

    Attributes
    ----------
    fixed : _DataDescFixed
        Fixed data descriptors.
    state : _EM_state | None
        State of the EM algorithm.
    _result : LinearGaussianPpcaEMResult | None
        Result of the EM estimation.
    """

    fixed: _DataDescFixed
    state: Optional[_ARD_state]
    _result: Optional[LinearGaussianPpcaARDResult]

    def __init__(self, *args, **kwargs):
        """
        Initialize the Linear Gaussian PPCA EM estimation object.
        """
        super().__init__(*args, **(kwargs | {"n_components": None}))
        self.fixed = _DataDescFixed(
            N=self.N,
            X_dim=self.X_dim,
            Z_dim=self.fixed.Z_dim,
            centered_data=self.centered_data,
        )
        self.state = None

    def _ard_init(self):
        """
        Initialize the EM algorithm.
        """
        # pylint:disable=invalid-name
        W = np.random.normal(size=(self.X_dim, self.X_dim - 1))
        # W, _ = np.linalg.qr(W)

        U, S, _ = np.linalg.svd(W, full_matrices=False)
        W = U * S[None, :]

        noise_var = 1e-05
        # the convergence is slower if the init value is greater than true noise var.

        self.state = _ARD_state.from_raw_parameters(
            W=W, noise_var=noise_var, fixed=self.fixed
        )

    def _ard_step(self):
        """
        Perform one step of the EM algorithm.
        """
        # pylint:disable=invalid-name
        W_new = self.state.sample_cov_factor_load_mat_prod @ np.linalg.inv(
            self.state.noise_var * np.eye(self.state.W.shape[1])
            + self.state.posterior_variance_factor_load_sample_cov_factor_load_mat_prod
            + self.state.noise_var / self.N * self.state.alpha_posterior_precision_prod
        )

        # W_new, _r = np.linalg.qr(W_new)

        noise_var_new = (
            1
            / self.X_dim
            * (
                self.fixed.tr_sample_cov
                - utils.trace_matmul(
                    self.state.sample_cov_factor_load_mat_prod,
                    (self.state.posterior_variance @ W_new.T),
                )
            )
        )

        self.state = _ARD_state.from_raw_parameters(
            W=W_new, noise_var=noise_var_new, fixed=self.fixed
        )

    def _ard_states(
        self, max_iterations, error_tolerance
    ) -> Generator[_ARD_state, None, None]:
        """
        Method that performs the EM ARD algorithm and and returns
        the orthonalized and ordered factor loading matrix W
        """
        self._ard_init()
        yield self.state
        likelihood = self.state.complete_log_likelihood
        for count in (
            range(max_iterations) if max_iterations is not None else itertools.count()
        ):
            self._ard_step()

            if count % 100 == 0:
                U, S, _ = np.linalg.svd(self.state.W, full_matrices=False)
                self.state.W = U * S[None, :]

            yield self.state
            likelihood, old_likelihood = self.state.complete_log_likelihood, likelihood
            if np.abs(likelihood - old_likelihood) < error_tolerance:
                break

        # ordering W and alpha
        desc_ordering = np.argsort(self.state.alpha)

        U, S, _ = np.linalg.svd(self.state.W[:, desc_ordering], full_matrices=False)
        self.state.W = U * S[None, :]

        self._result = LinearGaussianPpcaARDResult(
            mean=self.mean,
            W=self.state.W,
            A=self.state.alpha[desc_ordering],
            noise_var=self.state.noise_var,
            complete_log_likelihood=self.state.complete_log_likelihood,
            log_likelihood=self.state.log_likelihood,
            model_var_inv=self.state.model_var_inv,
            log_det_model_var=self.state.log_det_model_var,
        )

    def fit(
        self,
        max_iterations=None,
        error_tolerance=1e-6,
        trace=False,
    ) -> Optional[list[_ARD_state]]:
        """
        Fit the Linear Gaussian PPCA model using the EM algorithm.

        Parameters
        ----------
        max_iterations : int | None
            Maximum number of iterations for the EM algorithm.
        error_tolerance : float
            Tolerance for the convergence of the EM algorithm.
        trace : bool
            Whether to store the intermediate states of the EM algorithm.

        Returns
        -------
        list[_ARD_state] | None
            List of intermediate states of the EM algorithm if trace is True, otherwise None.
        """
        states = self._ard_states(max_iterations, error_tolerance)
        if trace:
            return states

        for _ in states:
            pass

        return None
