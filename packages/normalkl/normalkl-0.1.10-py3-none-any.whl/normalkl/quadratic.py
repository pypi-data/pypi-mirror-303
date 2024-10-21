""" Functions that compute quadratic term of the KL divergence for different covariance types. """

import torch



def is_zero(x):
    if isinstance(x, float):
        return x == 0.0
    elif isinstance(x, torch.Tensor):
        return torch.equal(x, torch.tensor(0.0)) and x.numel() == 1
    else:
        return False


# Precision versions of the above functions:

def quadratic_covmat(v1, covmat2):
    """ Return quadratic term: v1^T covmat22^{-1} v1 / 2 """

    return 0.5 * (v1.unsqueeze(0) @ torch.inverse(covmat2) @ v1).squeeze()

def quadratic_precmat(v1, precmat2):
    """ Return quadratic term: v1^T precmat2 v1 / 2 """
    return 0.5 * (v1.unsqueeze(0) @ precmat2 @ v1).squeeze()

def quadratic_diagvar(v1, diagvar2):
    """ Return quadratic term: v1^T diag(var)^{-1} v1 / 2"""
    v1_square = 0.0 if is_zero(v1) else v1.square()
    return 0.5 * torch.sum(v1_square / diagvar2).squeeze()

def quadratic_diagprec(v1, diagprec2):
    """ Return quadratic term: v1^T diag(prec2) v1 / 2 """
    v1_square = 0.0 if is_zero(v1) else v1.square()
    return 0.5 * torch.sum(v1_square * diagprec2).squeeze()

def quadratic_scalarvar(v1, scalarvar2):
    """ Return quadratic term: v1^T (scalarvar2 * I)^{-1} v1 / 2 """
    v1_square = 0.0 if is_zero(v1) else v1.square()
    return 0.5 * torch.sum(v1_square / scalarvar2).squeeze()

def quadratic_scalarprec(v1, scalarprec2):
    """ Return quadratic term: v1^T (scalarprec * I) v1 / 2 """
    v1_square = 0.0 if is_zero(v1) else v1.square()
    return 0.5 * torch.sum(v1_square * scalarprec2).squeeze()

def quadratic_identity(v1, _ignore):
    """ Return quadratic term: v1^T v1 / 2 """
    v1_square = 0.0 if is_zero(v1) else v1.square()
    return 0.5 * v1_square.sum().squeeze()

def quadratic_cholcov(v1, cholcov2):
    """ Return quadratic term: v1^T (L2 L2.T )^{-1} v1 / 2 
    = v1^T L2^{-1}^T L2^{-1} v1 / 2 
    = (L2^{-1} v1)^2 / 2
    """
    L_inv = torch.inverse(cholcov2) 
    return 0.5 * torch.sum((L_inv @ v1) ** 2)

def quadratic_cholprec(v1, cholprec2):
    """ Return quadratic term: v1^T (L2 L2^T) v1 / 2 
    = v1^T L2 (L2^T v1)
    = (L2^T v1)^T (L2^T v1)
    """
    LTv = cholprec2.T @ v1
    return 0.5 * torch.sum(LTv.square())

def quadratic_kroncov(v1, kroncov2):
    """ Return quadratic term: v1^T (U2 kron V2)^{-1} v1 / 2 """
    U2, V2 = kroncov2
    d1, d2 = len(U2), len(V2)
    v1_mat = v1.view(d1, d2)  # Reshape v1 to a matrix of shape (d1, d2)
    U2_inv = torch.inverse(U2)
    V2_inv = torch.inverse(V2)
    return 0.5 * torch.trace(U2_inv @ v1_mat @ V2_inv @ v1_mat.T)

def quadratic_kronprec(v1, kronprec2):
    """ Return quadratic term: v1^T (U2 kron V2) v1 / 2 """
    U2, V2 = kronprec2
    d1, d2 = len(U2), len(V2)
    v1_mat = v1.view(d1, d2)  # Reshape v1 to a matrix of shape (d1, d2)
    return 0.5 * torch.trace(U2 @ v1_mat @ V2 @ v1_mat.T)

def quadratic_cholkroncov(v1, cholkroncov2):
    """ Return quadratic term: v1^T (L_U2 L_U2.T kron L_V2 L_V2.T)^{-1} v1 / 2 """
    LU2, LV2 = cholkroncov2
    d1, d2 = len(LU2), len(LV2)
    v1_mat = v1.view(d1, d2)  # Reshape v1 to a matrix of shape (d1, d2)
    LU2_inv = torch.inverse(LU2)
    LV2_inv = torch.inverse(LV2)
    return 0.5 * v1.unsqueeze(0) @ torch.kron(LU2_inv.T @ LU2_inv, LV2_inv.T @ LV2_inv) @ v1

def quadratic_diagvarkron(v1, a2, b2):
    """ Return quadratic term: v1^T diag(vec(b2 a2^T))^{-1} v1 / 2 """
    v1_square = 0.0 if is_zero(v1) else v1.square()
    ab = torch.outer(a2, b2)
    ab_diag = ab.view(-1)
    return 0.5 * torch.sum(v1_square / ab_diag)

def quadratic_diagvarrow(v1, a2):
    """ Return quadratic term: v1^T diag(vec(1 a2^T))^{-1} v1 / 2 """
    v1_square = 0.0 if is_zero(v1) else v1.square()
    d1 = len(a2)
    d2 = len(v1) // d1
    return 0.5 * torch.sum(v1_square.view(d1, d2) / a2.unsqueeze(1))

def quadratic_diagvarcol(v1, b2):
    """ Return quadratic term: v1^T diag(vec(b2 1^T))^{-1} v1 / 2"""
    v1_square = 0.0 if is_zero(v1) else v1.square()
    d2 = len(b2)
    d1 = len(v1) // d2
    return 0.5 * torch.sum(v1_square.view(d1, d2) / b2.view(1, -1))





