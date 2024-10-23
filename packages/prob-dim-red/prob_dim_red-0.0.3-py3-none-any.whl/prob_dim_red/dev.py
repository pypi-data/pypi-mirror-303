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

"""pPCA draft version with simulated data"""


# imports
import numpy as np
import matplotlib.pyplot as plt
import scipy
from sklearn import datasets
from sklearn.decomposition import PCA, FactorAnalysis


iris_dataset = datasets.load_iris().data  # pylint: disable=no-member


def get_near_psd(A):
    """Function returning the nearest positive semi-definite matrix from the input"""
    C = (A + A.T) / 2
    eigval, eigvec = np.linalg.eigh(C)
    eigval[eigval < 1e-4] = 1e-4

    return eigvec * eigval[np.newaxis, :] @ eigvec.T


# data simulation
# in high dimension, for instance , data X with dim(X)=(n,x) xith n=2000, x=1000
N, X_DIM = iris_dataset.shape
Z_DIM = 3

# generating random mean and covariance for distribution a and b
mean_a = np.random.rand(X_DIM)
cov_a = get_near_psd(np.random.rand(X_DIM, X_DIM))

mean_b = np.random.rand(X_DIM)
cov_b = get_near_psd(np.random.rand(X_DIM, X_DIM))

data = scipy.stats.multivariate_normal.rvs(
    mean=mean_a, cov=cov_a, size=N
) + scipy.stats.multivariate_normal.rvs(mean=mean_b, cov=cov_b, size=N)

simulated_centered_data = np.array([i - data.mean(axis=0) for i in data])

centered_data = iris_dataset - iris_dataset.mean(axis=0)[None, :]

# Maximum likelihood estimation of mean m, variance sigma^2, factor loading matrix W

# 1) MLE mean : sample mean
mean_mle = iris_dataset.mean()

# 2) sample covariance
sample_cov = np.cov(centered_data, bias=True, rowvar=False)

# 3) Computing the right eigenvectors of sample covariance matrix and their associated eigenvalues # pylint:disable=duplicate-code
eig_val, eig_vec = scipy.linalg.eigh(
    sample_cov, subset_by_index=(X_DIM - Z_DIM, X_DIM - 1)
)  # pylint:disable=duplicate-code
eig_val = eig_val[::-1]
eig_vec = eig_vec[:, ::-1]


# 4) sorting the eigen values in ascending order to compute the variance mle
noise_var_mle = (np.trace(sample_cov) - eig_val.sum()) / (X_DIM - Z_DIM)

# Pierre normalised the eigen vectors matrix, idk why ??
# 5) computing the W mle by first computing U_L then L_L
# in order to do that, as the eigen vectors are the right ones,
# we select them based on their corresponding ordered eigen values.

w_mle = eig_vec * np.sqrt(eig_val - noise_var_mle)[None, :]


# Computing the actual likelihood of the recently estimated parameters under the data
# using C matrix inverse formula, we don't need to inverse as it only depends on inverting
# the diagonal matrix. We call the C matrix the model variance WW^t+sigma^2I.
posterior_precision = w_mle.T @ w_mle + noise_var_mle * np.eye(Z_DIM)
posterior_variance = np.linalg.inv(posterior_precision)

model_var_inv = (
    1 / noise_var_mle * (np.eye(X_DIM) - w_mle @ posterior_variance @ w_mle.T)
)

# we also need to compute the log determinant of the matrix C
log_det_model_var = (X_DIM - Z_DIM) * np.log(noise_var_mle) + np.log(eig_val).sum()
print(log_det_model_var)
# pylint:disable=duplicate-code
log_likelihood = (
    -N
    / 2
    * (
        X_DIM * np.log(2 * np.pi)
        + log_det_model_var
        + (model_var_inv * sample_cov).sum()  #
    )
)  # pylint:disable=duplicate-code
print(log_likelihood)


# Projecting X datamatrix on Z subspace: M^-1 W^t (x-mu)
ppca_proj_data = (posterior_variance @ w_mle.T @ centered_data.T).T

FA = FactorAnalysis(n_components=Z_DIM)
PPCA_SKLEARN = PCA(n_components="mle")

fa_proj_data = FA.fit_transform(centered_data)
sklearn_ppca_proj_data = PPCA_SKLEARN.fit_transform(centered_data)

print(
    f"log likelihood scores:\nppca in-house: {log_likelihood}\n\
    factor analysis: {FA.score_samples(centered_data).sum()}\n\
    sklearn pca: {PPCA_SKLEARN.score_samples(centered_data).sum()}"
)

datasets = [
    ("In-house pPCA", ppca_proj_data),
    ("Factor analysis", fa_proj_data),
    ("sklearn pPCA", sklearn_ppca_proj_data),
]


fig, axes = plt.subplots(
    nrows=len(datasets),
    ncols=Z_DIM - 1,
    figsize=(20, 10 * len(datasets)),
    sharex=True,
    sharey=True,
)

for ax, (method, dataset, comp_x, comp_y) in zip(
    axes.ravel(),
    [
        (method, dataset, x, y + 1)
        for (method, dataset) in datasets
        for x, y in zip(range(Z_DIM - 1), range(Z_DIM - 1))
    ],
):
    ax.scatter(dataset[:, comp_x], dataset[:, comp_y])
    ax.set_xlabel(f"PC {comp_x+1}")
    ax.set_ylabel(f"PC {comp_y+1}")
    ax.set_aspect("equal")
    ax.grid()
    ax.set_title(method)

fig.suptitle(
    "Comparison of several factor analysers on the 3 first PCs", fontsize="xx-large"
)

fig.tight_layout()

fig.savefig(
    "/home/francois/code/pPCA/plots/comparison_ppca_in_house_VS_fa_VS_ppca_sklearn.svg"
)
