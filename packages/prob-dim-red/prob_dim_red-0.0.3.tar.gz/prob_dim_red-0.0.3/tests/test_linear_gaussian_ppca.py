# pylint: disable=invalid-name,missing-module-docstring,missing-function-docstring

import pytest

import numpy as np

from prob_dim_red import linear_gaussian_ppca

ALL_PARAMS_MLE_EM = [
    pytest.param(
        (n, xd, zd, st, sd), marks=(pytest.mark.minimal if (n, xd) == (100, 10) else ())
    )
    for n in (100, 1000, 10000)
    for xd in (10, 50, 100)
    for zd in (1, 2, 5, 50)
    for st in (1e-2, 0.1, 10)
    for sd in (1, 2, 3)
    if zd < xd
]


@pytest.mark.parametrize("param", ALL_PARAMS_MLE_EM)
def test_mle(param):
    N, X_DIM, Z_DIM, sigma_true, seed = param
    random = np.random.RandomState(seed)  # pylint: disable=no-member
    mu_true = random.normal(size=X_DIM)
    W_true = random.normal(size=(X_DIM, Z_DIM))
    Z_true = random.normal(size=(N, Z_DIM))
    X = (
        mu_true[None, :]
        + (W_true @ Z_true.T).T
        + sigma_true * random.normal(size=(N, X_DIM))
    )
    res_mle = linear_gaussian_ppca.ppca_mle(X, n_components=Z_DIM)
    mean_mle = res_mle.mean
    w_mle = res_mle.W
    noise_var_mle = res_mle.noise_var
    _log_likelihood = res_mle.log_likelihood
    _model_var_inv = res_mle.model_var_inv
    _log_det = res_mle.log_det_model_var

    assert ((mu_true - mean_mle) ** 2).mean() ** 0.5 < 1000 * sigma_true / N**0.5
    assert np.abs(np.log(noise_var_mle) - 2 * np.log(sigma_true)) < 50 / N**0.5
    assert (
        (W_true @ W_true.T - w_mle @ w_mle.T) ** 2
    ).mean() ** 0.5 < 1000 * sigma_true * (Z_DIM / N) ** 0.5


# pylint: disable=too-many-locals
@pytest.mark.parametrize("param", ALL_PARAMS_MLE_EM)
def test_em(param):
    N, X_DIM, Z_DIM, sigma_true, seed = param
    random = np.random.RandomState(seed)  # pylint: disable=no-member
    mu_true = random.normal(size=X_DIM)
    W_true = random.normal(size=(X_DIM, Z_DIM))
    Z_true = random.normal(size=(N, Z_DIM))
    X = (
        mu_true[None, :]
        + (W_true @ Z_true.T).T
        + sigma_true * random.normal(size=(N, X_DIM))
    )

    res_mle = linear_gaussian_ppca.ppca_mle(X, n_components=Z_DIM)

    # pylint: disable=protected-access

    model = max(
        (
            linear_gaussian_ppca.LinearGaussianPPCAEstimEM(X, Z_DIM).fit()
            for _ in range(3)
        ),
        key=lambda x: x._result.log_likelihood,
    )
    res_em = model._result  # pylint: disable=protected-access

    mean_em = res_em.mean
    w_em = res_em.W
    noise_var_em = res_em.noise_var
    log_likelihood_em = res_em.log_likelihood
    _complete_log_likelihood = res_em.complete_log_likelihood
    _model_var_inv = res_em.model_var_inv
    _log_det = res_em.log_det_model_var

    mean_mle = res_mle.mean
    w_mle = res_mle.W
    noise_var_mle = res_mle.noise_var
    log_likelihood_mle = res_mle.log_likelihood
    _model_var_inv = res_mle.model_var_inv
    _log_det = res_mle.log_det_model_var

    assert ((mean_em - mean_mle) ** 2).mean() < 1e-4 * (mean_mle**2).mean()
    assert np.abs(np.log(noise_var_em) - np.log(noise_var_mle)) < 0.2
    assert ((w_mle @ w_mle.T - w_em @ w_em.T) ** 2).mean() < 1e-2 * (
        (w_mle @ w_mle.T) ** 2
    ).mean()
    assert np.abs(log_likelihood_em - log_likelihood_mle) <= 1e-1
