import torch
import math

from .logdet import *

from normalkl.util import dim_dtype_device_of_cov, is_zero


# auto_kl_*_covmat
def auto_kl_covmat_covmat(mean1, covmat1, mean2):
    """ Compute KL with automatic optimal diagonal variance according to
        argmin_v3 KL( N(v1, M1) || M(v2, diag(v3)) )
    """
    mean_diff = mean1 - mean2
    return 0.5 * torch.log(1 + (mean_diff.unsqueeze(0) @ torch.inverse(covmat1) @ mean_diff)).squeeze()

def auto_kl_precmat_covmat(mean1, precmat1, mean2):
    """ Compute KL with automatic optimal diagonal variance according to
        argmin_v3 KL( N(v1, M1) || M(v2, diag(v3)) )
    """
    mean_diff = mean1 - mean2
    return 0.5 * torch.log(1 + (mean_diff.unsqueeze(0) @ precmat1 @ mean_diff).squeeze())

def auto_kl_cholkroncov_covmat(mean1, cholkroncov1, mean2):
    """ Compute KL with automatic optimal diagonal variance according to
        argmin_v3 KL( N(v1, (LU1 LU1^T kron LV1 LV1^T)) || M(v2, diag(v3)) )
    """
    mean_diff = mean1 - mean2
    LU1, LV1 = cholkroncov1
    d1, d2 = LU1.size(0), LV1.size(0)

    M = mean_diff.view(d1, d2)
    
    # Solve LU1^{-1} * M * LV1^{-T} using triangular solves
    W_A = torch.triangular_solve(M, LU1, upper=False)[0]  # LU1^{-1} * M
    W = torch.triangular_solve(W_A.t(), LV1, upper=False)[0]  # LV1^{-1} * W_A^T
    W = W.t()  # Transpose back to the correct shape
    
    # Compute the Frobenius norm of W (which is equivalent to the quadratic form)
    result = torch.sum(W ** 2)

    return 0.5 * torch.log(1 + result)

# auto_kl_*_precmat
def auto_kl_covmat_precmat(mean1, covmat1, mean2):
    return auto_kl_covmat_covmat(mean1, covmat1, mean2)

def auto_kl_precmat_precmat(mean1, precmat1, mean2):
    return auto_kl_precmat_covmat(mean1, precmat1, mean2)

def auto_kl_cholkroncov_precmat(mean1, cholkroncov1, mean2):
    """ Compute KL with automatic optimal diagonal variance according to
        argmin_v3 KL( N(v1, (LU1 LU1^T kron LV1 LV1^T)) || M(v2, M2))
    """
    return auto_kl_cholkroncov_covmat(mean1, cholkroncov1, mean2)

# auto_kl_*_
def auto_kl_covmat_diagvar(mean1, covmat1, mean2):
    """ Compute KL with automatic optimal diagonal variance according to
        argmin_v3 KL( N(v1, M1) || M(v2, diag(v3)) )
    """
    mean_diff_square = (mean1 - mean2).square()

    covmat1_diag = covmat1.diag()
    return 0.5 * (torch.sum(torch.log(covmat1_diag + mean_diff_square)) - logdet_covmat(covmat1))

def auto_kl_cholkroncov_diagvar(mean1, cholkroncov1, mean2):
    """ Compute KL with automatic optimal diagonal variance according to
        argmin_v3 KL( N(v1, M1) || M(v2, diag(v3)) )
    """
    mean_diff_square = (mean1 - mean2).square()

    LU1, LV1 = cholkroncov1
    covmat1_diag = torch.kron(LU1.square().sum(1), LV1.square().sum(1))

    return 0.5 * (torch.sum(torch.log(covmat1_diag + mean_diff_square)) - logdet_cholkroncov(cholkroncov1))

# auto_kl_*_diagprec
def auto_kl_covmat_diagprec(mean1, covmat1, mean2):
    return auto_kl_covmat_diagvar(mean1, covmat1, mean2)

# auto_kl_*_scalarvar
def auto_kl_covmat_scalarvar(mean1, covmat1, mean2):
    """ Compute KL with automatic optimal diagonal variance according to
        argmin_v3 KL( N(v1, M1) || M(v2, v3 I))
    """
    d = mean1.size(0)
    mean_diff_square = (mean1 - mean2).square()

    total_variance = torch.trace(covmat1) + mean_diff_square.sum()
    return 0.5 * (d * torch.log(total_variance / d) - logdet_covmat(covmat1))

def auto_kl_cholkroncov_scalarvar(mean1, cholkroncov1, mean2):
    """ Compute KL with automatic optimal diagonal variance according to
        argmin_v3 KL( N(v1, M1) || M(v2, v3 I))
    """
    d = mean1.size(0)
    LU, LV = cholkroncov1
    cov1_trace = LU.square().sum() * LV.square().sum()

    mean_diff_square = (mean1 - mean2).square()

    total_variance = cov1_trace + mean_diff_square.sum()
    return 0.5 * (d * torch.log(total_variance / d) - logdet_cholkroncov(cholkroncov1))

# auto_kl_*_scalarprec
def auto_kl_covmat_scalarprec(mean1, covmat1, mean2):
    return auto_kl_covmat_scalarvar(mean1, covmat1, mean2)

def auto_kl_cholkroncov_scalarprec(mean1, cholkroncov1, mean2):
    return auto_kl_cholkroncov_scalarvar(mean1, cholkroncov1, mean2)

# auto_kl_*_diagvarrow
def auto_kl_covmat_diagvarrow(mean1, covmat1, mean2, d1, d2):
    both_means_float = is_zero(mean1) and is_zero(mean2)
    mean_diff_square = (mean1 - mean2).square()
    mean_diff_rows = mean_diff_square.view(d1, d2).sum(1)
    covmat1_rows = torch.diagonal(covmat1.view(d1, d2, d1, d2), dim1=1, dim2=3).sum(-1)

    optimal_diagvarrow = (covmat1_rows.diag() + mean_diff_rows) / d2

    return 0.5 * (d2 * torch.log(optimal_diagvarrow).sum() - logdet_covmat(covmat1))

def auto_kl_cholkroncov_diagvarrow(mean1, cholkroncov1, mean2, d1, d2):
    both_means_float = is_zero(mean1) and is_zero(mean2)
    mean_diff_square = (mean1 - mean2).square()
    mean_diff_rows = mean_diff_square.view(d1, d2).sum(1)

    LU1, LV1 = cholkroncov1
    U1 = LU1 @ LU1.T

    covmat1_rows = U1 * LV1.square().sum()

    optimal_diagvarrow = (covmat1_rows.diag() + mean_diff_rows) / d2

    return 0.5 * (d2 * torch.log(optimal_diagvarrow).sum() - logdet_cholkroncov(cholkroncov1))

# auto_kl_*_diagvarcol
def auto_kl_covmat_diagvarcol(mean1, covmat1, mean2, d1, d2):
    both_means_float = is_zero(mean1) and is_zero(mean2)
    mean_diff_square = (mean1 - mean2).square()
    mean_diff_cols = mean_diff_square.view(d1, d2).sum(0)
    covmat1_cols = torch.diagonal(covmat1.view(d1, d2, d1, d2), dim1=0, dim2=2).sum(-1)

    optimal_diagvarrow = (covmat1_cols.diag() + mean_diff_cols) / d1

    return 0.5 * (d1 * torch.log(optimal_diagvarcol).sum() - logdet_covmat(covmat1))

def auto_kl_cholkroncov_diagvarcol(mean1, cholkroncov1, mean2, d1, d2):
    mean_diff_square = (mean1 - mean2).square()
    mean_diff_cols = mean_diff_square.view(d1, d2).sum(0)

    LU1, LV1 = cholkroncov1
    V1 = LV1 @ LV1.T

    covmat1_cols = V1 * LU1.square().sum()

    optimal_diagvarcol = (covmat1_cols.diag() + mean_diff_cols) / d1

    return 0.5 * (d1 * torch.log(optimal_diagvarcol).sum() - logdet_cholkroncov(cholkroncov1))


def auto_kl(mean1, cov_type1, cov1, mean2, cov_type2, d1=None, d2=None):
    """ Compute KL with automatic optimal covariance according to
            argmin_cov2 KL( N(mean1, cov1) || N(mean2, cov2))
        and constrained by type of covariance (cov_type2)
    """
    func_name = f"auto_kl_{cov_type1}_{cov_type2}"

    func = globals()[func_name]

    dim1, dtype, device = dim_dtype_device_of_cov(mean1, cov_type1, cov1)
    dim2, _, _ = dim_dtype_device_of_cov(mean1, cov_type1, cov1)
    assert dim1 == dim2, f"Dimensions of first covariance ({dim1}) does not match other covariance ({dim2})"
    if isinstance(mean1, float):
        mean1 = torch.zeros(dim1, dtype=dtype, device=device)
    if isinstance(mean2, float):
        mean2 = torch.zeros(dim2, dtype=dtype, device=device)

    if cov_type2 in ['diagvarkron', 'diagvarrow', 'diagvarcol']:
        assert (d1 is not None) and (d2 is not None), f"auto_kl: {cov_type2} requires dimensions when computing optimal variance (Got: d1={d1}, d2={d2})"
        return func(mean1, cov1, mean2, d1, d2)
    else:
        return func(mean1, cov1, mean2)


