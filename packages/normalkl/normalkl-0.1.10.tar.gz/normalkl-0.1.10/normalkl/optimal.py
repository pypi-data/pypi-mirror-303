import torch

def is_zero(x):
    if isinstance(x, float):
        return x == 0.0
    elif isinstance(x, torch.Tensor):
        return torch.equal(x, torch.tensor(0.0)) and x.numel() == 1
    else:
        return False

# optimal_*_covmat
def optimal_covmat_covmat(mean_diff, covmat1):
    """ Compute optimal diagonal variance of
        argmin_M2 KL( N(v1, M1) || M(v2, M2))
    """
    mean_diff_outer = 0.0 if is_zero(mean_diff) else torch.outer(mean_diff, mean_diff) 

    return covmat1 + mean_diff_outer

def optimal_precmat_covmat(mean_diff, precmat1):
    """ Compute optimal diagonal variance of
        argmin_M2 KL( N(v1, M1) || M(v2, M2))
    """
    mean_diff_outer = 0.0 if is_zero(mean_diff) else torch.outer(mean_diff, mean_diff) 

    return torch.inverse(precmat1) + mean_diff_outer

def optimal_cholkroncov_covmat(mean_diff, cholkroncov1):
    """ Compute optimal diagonal variance of
        argmin_M2 KL( N(v1, M1) || M(v2, M2))
    """
    mean_diff_outer = 0.0 if is_zero(mean_diff) else torch.outer(mean_diff, mean_diff) 

    LU1, LV1 = cholkroncov1
    U1 = LU1 @ LU1.T
    V1 = LV1 @ LV1.T
    covmat1 = torch.kron(U1, V1)
    return covmat1 + mean_diff_outer

# optimal_*_precmat
def optimal_covmat_precmat(mean_diff, covmat1):
    """ Compute optimal diagonal variance of
        argmin_M2 KL( N(v1, M1) || M(v2, M2))
    """
    mean_diff_outer = 0.0 if is_zero(mean_diff) else torch.outer(mean_diff, mean_diff) 

    return torch.inverse(covmat1 + mean_diff_outer)

def optimal_precmat_precmat(mean_diff, covmat1):
    """ Compute optimal diagonal variance of
        argmin_M2 KL( N(v1, M1) || M(v2, M2))
    """
    mean_diff_outer = 0.0 if is_zero(mean_diff) else torch.outer(mean_diff, mean_diff) 

    return torch.inverse(torch.inverse(covmat1) + mean_diff_outer)

def optimal_cholkroncov_precmat(mean_diff, cholkroncov1):
    """ Compute optimal diagonal variance of
        argmin_M2 KL( N(v1, M1) || M(v2, M2))
    """
    mean_diff_outer = 0.0 if is_zero(mean_diff) else torch.outer(mean_diff, mean_diff) 
    LU1, LV1 = cholkroncov1
    U1 = LU1 @ LU1.T
    V1 = LV1 @ LV1.T
    covmat1 = torch.kron(U1, V1)
    return torch.inverse(covmat1 + mean_diff_outer)


# optimal_*_diagvar
def optimal_covmat_diagvar(mean_diff, covmat1):
    """ Compute optimal diagonal variance of
        argmin_v3 KL( N(v1, M1) || M(v2, diag(v3)) )
    """
    mean_diff_square = 0.0 if is_zero(mean_diff) else mean_diff.square()
    return covmat1.diag() + mean_diff_square

def optimal_cholkroncov_diagvar(mean_diff, cholkroncov1):
    """ Compute optimal diagonal variance of
        argmin_v3 KL( N(v1, (LU1 LU1^T kron LV1 LV1^T)) || M(v2, diag(v3)) )
    """
    mean_diff_square = 0.0 if is_zero(mean_diff) else mean_diff.square()
    LU1, LV1 = cholkroncov1
    covmat1_diag = torch.kron(LU1.square().sum(1), LV1.square().sum(1))
    return covmat1_diag + mean_diff_square

# optimal_*_diagprec
def optimal_covmat_diagprec(mean_diff, covmat1):
    """ Compute optimal diagonal precision of
        argmin_v3 KL( N(v1, M1) || M(v2, diag(v3)^{-1}) )
    """
    mean_diff_square = 0.0 if is_zero(mean_diff) else mean_diff.square()
    return 1 / (covmat1.diag() + mean_diff_square)

def optimal_cholkroncov_diagprec(mean_diff, cholkroncov1):
    """ Compute optimal diagonal variance of
        argmin_v3 KL( N(v1, (LU1 LU1^T kron LV1 LV1^T)) || M(v2, diag(v3)) )
    """
    mean_diff_square = 0.0 if is_zero(mean_diff) else mean_diff.square()
    LU1, LV1 = cholkrncov1
    covmat1_diag = torch.kron(LU1.square().sum(1), LV1.square().sum(1))
    return 1 / (covmat1_diag + mean_diff_square)

# optimal_*_scalarvar
def optimal_covmat_scalarvar(mean_diff, covmat1):
    """ Compute optimal scalar variance of
        argmin_v3 KL( N(v1, covmat1) || M(v2, v3 I))
    """
    mean_diff_square = 0.0 if is_zero(mean_diff) else mean_diff.square()
    return (torch.trace(covmat1) + mean_diff_square.sum()) / len(mean_diff)

def optimal_precmat_scalarvar(mean_diff, precmat1):
    """ Compute optimal scalar variance of
        argmin_v3 KL( N(v1, precmat1^{-1}) || M(v2, v3 I))
    """
    mean_diff_square = 0.0 if is_zero(mean_diff) else mean_diff.square()
    return (torch.trace(torch.inverse(precmat1)) + mean_diff_square.sum()) / len(mean_diff)

def optimal_diagvar_scalarvar(mean_diff, diagvar1):
    """ Compute optimal scalar variance of
        argmin_v3 KL( N(v1, diagvar1) || M(v2, v3 I))
    """
    mean_diff_square = 0.0 if is_zero(mean_diff) else mean_diff.square()
    return (torch.sum(diagvar1) + mean_diff_square.sum()) / len(mean_diff)

def optimal_diagprec_scalarvar(mean_diff, diagprec1):
    """ Compute optimal scalar variance of
        argmin_v3 KL( N(v1, diagprec1) || M(v2, v3 I))
    """
    mean_diff_square = 0.0 if is_zero(mean_diff) else mean_diff.square()
    return (torch.sum(1/diagprec1) + mean_diff_square.sum()) / len(mean_diff)

def optimal_scalarvar_scalarvar(mean_diff, scalarvar1):
    """ Compute optimal scalar variance of
        argmin_v3 KL( N(v1, scalarvar1 I ) || M(v2, v3 I))
    """
    mean_diff_square = 0.0 if is_zero(mean_diff) else mean_diff.square()
    d = mean_diff.size(0)
    return (d * scalarvar1 + mean_diff_square.sum()) / len(mean_diff)

def optimal_scalarprec_scalarvar(mean_diff, scalarprec1):
    """ Compute optimal scalar variance of
        argmin_v3 KL( N(v1, scalarprec1^{-1} I ) || M(v2, v3 I))
    """
    mean_diff_square = 0.0 if is_zero(mean_diff) else mean_diff.square()
    d = mean_diff.size(0)
    return (d * scalarprec1 + mean_diff_square.sum()) / len(mean_diff)

def optimal_identity_scalarvar(mean_diff, _ignore):
    """ Compute optimal scalar variance of
        argmin_v3 KL( N(v1, I ) || M(v2, v3 I))
    """
    mean_diff_square = 0.0 if is_zero(mean_diff) else mean_diff.square()
    d = mean_diff.size(0)
    return (mean_diff_square.sum()) / len(mean_diff)

def optimal_cholcov_scalarvar(mean_diff, cholcov1):
    """ Compute optimal scalar variance of
        argmin_v3 KL( N(v1, L1 L1^T ) || M(v2, v3 I))
    """
    mean_diff_square = 0.0 if is_zero(mean_diff) else mean_diff.square()
    trace1 = cholcov.square().sum()
    return (trace1 + mean_diff_square.sum()) / len(mean_diff)

def optimal_cholprec_scalarvar(mean_diff, cholcov1):
    """ Compute optimal scalar variance of
        argmin_v3 KL( N(v1, L1 L1^T ) || M(v2, v3 I))
    """
    mean_diff_square = 0.0 if is_zero(mean_diff) else mean_diff.square()
    trace1 = torch.inverse(cholcov1).square().sum()
    return (trace1 + mean_diff_square.sum()) / len(mean_diff)

def optimal_kroncov_scalarvar(mean_diff, kroncov1):
    """ Compute optimal scalar variance of
        argmin_v3 KL( N(v1, (U1 kron V1) ) || M(v2, v3 I))
    """
    mean_diff_square = 0.0 if is_zero(mean_diff) else mean_diff.square()
    U1, V1 = kroncov1
    trace1 = torch.trace(U1) * torch.trace(V1)
    return (trace1 + mean_diff_square.sum()) / len(mean_diff)

def optimal_kronprec_scalarvar(mean_diff, kronprec1):
    """ Compute optimal scalar variance of
        argmin_v3 KL( N(v1, (U1 kron V1) ) || M(v2, v3 I))
    """
    mean_diff_square = 0.0 if is_zero(mean_diff) else mean_diff.square()
    U1, V1 = kronprec1
    trace1 = torch.trace(torch.inverse(U1)) * torch.trace(torch.inverse(V1))
    return (trace1 + mean_diff_square.sum()) / len(mean_diff)

def optimal_cholkroncov_scalarvar(mean_diff, cholkroncov1):
    """ Compute optimal scalar variance of
        argmin_v3 KL( N(v1, (LU1 LU1^T kron LV1 LV1^T) ) || M(v2, v3 I))
    """
    mean_diff_square = 0.0 if is_zero(mean_diff) else mean_diff.square()
    LU1, LV1 = cholkroncov1
    trace1 = LU1.square().sum() * LV1.square().sum()
    return (trace1 + mean_diff_square.sum()) / len(mean_diff)


def optimal_diagvarkron_scalarvar(mean_diff, diagvarkron1):
    """ Compute optimal scalar variance of
        argmin_v3 KL( N(v1, diag(a) kron diag(b) ) || M(v2, v3 I))
    """
    mean_diff_square = 0.0 if is_zero(mean_diff) else mean_diff.square()
    a, b = diagvarkron1
    trace1 = torch.outer(a, b).sum()
    return (trace1 + mean_diff_square.sum()) / len(mean_diff)

def optimal_diagvarrow_scalarvar(mean_diff, diagvarrow1):
    """ Compute optimal scalar variance of
        argmin_v3 KL( N(v1, diag(a) kron diag(1) ) || M(v2, v3 I))
    """
    mean_diff_square = 0.0 if is_zero(mean_diff) else mean_diff.square()
    d = mean_diff.size(0)
    d1 = diagvarrow1.size(0)
    d2 = d // d1
    trace1 = diagvarrow1.sum() * d2
    return (trace1 + mean_diff_square.sum()) / len(mean_diff)

def optimal_diagvarcol_scalarvar(mean_diff, diagvarcol1):
    """ Compute optimal scalar variance of
        argmin_v3 KL( N(v1, diag(1) kron diag(b) ) || M(v2, v3 I))
    """
    mean_diff_square = 0.0 if is_zero(mean_diff) else mean_diff.square()
    d = mean_diff.size(0)
    d2 = diagvarcol1.size(0)
    d1 = d // d2
    trace1 = d1 * diagvarcol1.sum()
    return (trace1 + mean_diff_square.sum()) / len(mean_diff)


# optimal_*_scalarprec
def optimal_covmat_scalarprec(mean_diff, covmat1):
    """ Compute optimal scalar precision of
        argmin_v3 KL( N(v1, covmat1) || M(v2, v3 I))
    """
    mean_diff_square = 0.0 if is_zero(mean_diff) else mean_diff.square()
    return len(mean_diff) / (torch.trace(covmat1) + mean_diff_square.sum()) 

def optimal_precmat_scalarprec(mean_diff, precmat1):
    """ Compute optimal scalar precision of
        argmin_v3 KL( N(v1, precmat1^{-1}) || M(v2, v3 I))
    """
    mean_diff_square = 0.0 if is_zero(mean_diff) else mean_diff.square()
    return len(mean_diff) / (torch.trace(torch.inverse(precmat1)) + mean_diff_square.sum()) 

def optimal_diagvar_scalarprec(mean_diff, diagvar1):
    """ Compute optimal scalar precision of
        argmin_v3 KL( N(v1, diagvar1) || M(v2, v3 I))
    """
    mean_diff_square = 0.0 if is_zero(mean_diff) else mean_diff.square()
    return len(mean_diff) / (torch.sum(diagvar1) + mean_diff_square.sum()) 

def optimal_diagprec_scalarprec(mean_diff, diagprec1):
    """ Compute optimal scalar precision of
        argmin_v3 KL( N(v1, diagprec1) || M(v2, v3 I))
    """
    mean_diff_square = 0.0 if is_zero(mean_diff) else mean_diff.square()
    return len(mean_diff) / (torch.sum(1/diagprec1) + mean_diff_square.sum()) 

def optimal_scalarprec_scalarprec(mean_diff, scalarvar1):
    """ Compute optimal scalar precision of
        argmin_v3 KL( N(v1, scalarvar1 I ) || M(v2, v3 I))
    """
    mean_diff_square = 0.0 if is_zero(mean_diff) else mean_diff.square()
    d = mean_diff.size(0)
    return len(mean_diff) / (d * scalarvar1 + mean_diff_square.sum()) 

def optimal_scalarprec_scalarprec(mean_diff, scalarprec1):
    """ Compute optimal scalar precision of
        argmin_v3 KL( N(v1, scalarprec1^{-1} I ) || M(v2, v3 I))
    """
    mean_diff_square = 0.0 if is_zero(mean_diff) else mean_diff.square()
    d = mean_diff.size(0)
    return len(mean_diff) / (d * scalarprec1 + mean_diff_square.sum()) 

def optimal_identity_scalarprec(mean_diff, _ignore):
    """ Compute optimal scalar precision of
        argmin_v3 KL( N(v1, I ) || M(v2, v3 I))
    """
    mean_diff_square = 0.0 if is_zero(mean_diff) else mean_diff.square()
    d = mean_diff.size(0)
    return len(mean_diff) / (mean_diff_square.sum()) 

def optimal_cholcov_scalarprec(mean_diff, cholcov1):
    """ Compute optimal scalar precision of
        argmin_v3 KL( N(v1, L1 L1^T ) || M(v2, v3 I))
    """
    mean_diff_square = 0.0 if is_zero(mean_diff) else mean_diff.square()
    trace1 = cholcov.square().sum(1)
    return len(mean_diff) / (trace1 + mean_diff_square.sum()) 

def optimal_cholprec_scalarprec(mean_diff, cholcov1):
    """ Compute optimal scalar precision of
        argmin_v3 KL( N(v1, L1 L1^T ) || M(v2, v3 I))
    """
    mean_diff_square = 0.0 if is_zero(mean_diff) else mean_diff.square()

    trace1 = torch.inverse(cholcov1).square().sum(1)
    return len(mean_diff) / (trace1 + mean_diff_square.sum()) 

def optimal_kroncov_scalarprec(mean_diff, kroncov1):
    """ Compute optimal scalar precision of
        argmin_v3 KL( N(v1, (U1 kron V1) ) || M(v2, v3 I))
    """
    mean_diff_square = 0.0 if is_zero(mean_diff) else mean_diff.square()

    U1, V1 = kroncov1
    trace1 = torch.trace(U1) * torch.trace(V1)
    return len(mean_diff) / (trace1 + mean_diff_square.sum()) 

def optimal_kronprec_scalarprec(mean_diff, kronprec1):
    """ Compute optimal scalar precision of
        argmin_v3 KL( N(v1, (U1 kron V1) ) || M(v2, v3 I))
    """
    mean_diff_square = 0.0 if is_zero(mean_diff) else mean_diff.square()

    U1, V1 = kronprec1
    trace1 = torch.trace(torch.inverse(U1)) * torch.trace(torch.inverse(V1))
    return len(mean_diff) / (trace1 + mean_diff_square.sum()) 

def optimal_cholkroncov_scalarprec(mean_diff, cholkroncov1):
    """ Compute optimal scalar precision of
        argmin_v3 KL( N(v1, (LU1 LU1^T kron LV1 LV1^T) ) || M(v2, v3 I))
    """
    mean_diff_square = 0.0 if is_zero(mean_diff) else mean_diff.square()

    LU1, LV1 = cholkroncov1
    trace1 = LU1.square().sum() * LV1.square().sum()
    return len(mean_diff) / (trace1 + mean_diff_square.sum()) 


def optimal_diagvarkron_scalarprec(mean_diff, diagvarkron1):
    """ Compute optimal scalar precision of
        argmin_v3 KL( N(v1, diag(a) kron diag(b) ) || M(v2, v3 I))
    """
    mean_diff_square = 0.0 if is_zero(mean_diff) else mean_diff.square()

    a, b = diagvarkron1
    trace1 = torch.outer(a, b).sum()
    return len(mean_diff) / (trace1 + mean_diff_square.sum()) 

def optimal_diagvarrow_scalarprec(mean_diff, diagvarrow1):
    """ Compute optimal scalar precision of
        argmin_v3 KL( N(v1, diag(a) kron diag(1) ) || M(v2, v3 I))
    """
    mean_diff_square = 0.0 if is_zero(mean_diff) else mean_diff.square()

    d = mean_diff.size(0)
    d1 = diagvarrow1.size(0)
    d2 = d // d1
    trace1 = diagvarrow1.sum() * d2
    return len(mean_diff) / (trace1 + mean_diff_square.sum())

def optimal_diagvarcol_scalarprec(mean_diff, diagvarcol1):
    """ Compute optimal scalar precision of
        argmin_v3 KL( N(v1, diag(1) kron diag(b) ) || M(v2, v3 I))
    """
    mean_diff_square = 0.0 if is_zero(mean_diff) else mean_diff.square()

    d = mean_diff.size(0)
    d2 = diagvarcol1.size(0)
    d1 = d // d2
    trace1 = d1 * diagvarcol1.sum()
    return len(mean_diff) / (trace1 + mean_diff_square.sum()) 

# optimal_*_diagvarrow
def optimal_covmat_diagvarrow(mean_diff, covmat1, d1, d2):
    """ Compute optimal row diagonal of
        argmin_v3 KL( N(v1, M1 ) || M(v2, diag(v3) kron I))
    """
    mean_diff_square = 0.0 if is_zero(mean_diff) else mean_diff.square()

    mean_diff_rows = mean_diff_square.view(d1, d2).sum(1)
    covmat1_rows = torch.diagonal(covmat1.view(d1, d2, d1, d2), dim1=1, dim2=3).sum(-1)

    return (covmat1_rows.diag() + mean_diff_rows) / d2

def optimal_cholkroncov_diagvarrow(mean_diff, cholkroncov1, d1, d2):
    """ Compute optimal row diagonal of
        argmin_v3 KL( N(v1, (LU1 LU1^T kron LV1 LV1^T) ) || M(v2, diag(v3) kron I))
    """
    mean_diff_square = 0.0 if is_zero(mean_diff) else mean_diff.square()
    mean_diff_rows = mean_diff_square.view(d1, d2).sum(1)

    LU1, LV1 = cholkroncov1
    U1 = LU1 @ LU1.T

    covmat1_rows = U1 * LV1.square().sum()

    return (covmat1_rows.diag() + mean_diff_rows) / d2

# optimal_*_diagvarcol
def optimal_covmat_diagvarcol(mean_diff, covmat1, d1, d2):
    """ Compute optimal row diagonal of
        argmin_v3 KL( N(v1, M1 ) || M(v2, I kron diag(v3)))
    """
    mean_diff_square = 0.0 if is_zero(mean_diff) else mean_diff.square()
    mean_diff_cols = mean_diff_square.view(d1, d2).sum(0)
    covmat1_cols = torch.diagonal(covmat1.view(d1, d2, d1, d2), dim1=0, dim2=2).sum(-1)

    return (covmat1_cols.diag() + mean_diff_cols) / d1

def optimal_cholkroncov_diagvarcol(mean_diff, cholkroncov1, d1, d2):
    """ Compute optimal row diagonal of
        argmin_v3 KL( N(v1, (LU1 LU1^T kron LV1 LV1^T) ) || M(v2, I kron diag(v3)))
    """
    mean_diff_square = 0.0 if is_zero(mean_diff) else mean_diff.square()
    mean_diff_cols = mean_diff_square.view(d1, d2).sum(0)

    LU1, LV1 = cholkroncov1
    V1 = LV1 @ LV1.T

    covmat1_cols = V1 * LU1.square().sum()

    return (covmat1_cols.diag() + mean_diff_cols) / d1

def optimal_covariance(mean1, cov_type1, cov1, mean2, cov_type2, d1=None, d2=None):
    """ Find optimal cov2 that solves
            argmin_cov2 KL( N(mean1, cov1) || N(mean2, cov2))
    """
    func_name = f"optimal_{cov_type1}_{cov_type2}"

    func = globals()[func_name]

    mean_diff = mean1 - mean2

    if cov_type2 in ['diagvarkron', 'diagvarrow', 'diagvarcol']:
        assert (d1 is not None) and (d2 is not None), f"optimal_covariance: {cov_type2} requires dimensions when computing optimal variance (Got: d1={d1}, d2={d2})"
        return func(mean_diff, cov1, d1, d2)
    else:
        return func(mean_diff, cov1)


