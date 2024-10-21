import torch

import normalkl.trace
import normalkl.logdet
import normalkl.quadratic

from normalkl.util import dim_dtype_device_of_cov, is_zero


def trace_term_func(cov_type1, cov1, cov_type2, cov2):
    func_name = f"trace_{cov_type1}_{cov_type2}"
    trace_func = getattr(normalkl.trace, func_name)
    
    if trace_func:
        return trace_func(cov1, cov2)
    else:
        raise NotImplementedError(f"trace term not implemented yet for covariances of type '{cov_type1}' to '{cov_type2}' (please add a pull request on Github)")
    

def volume_term_func(cov_type1, cov1, cov_type2, cov2, dim=None):
    q_logdet_func_name = f"logdet_{cov_type1}"
    p_logdet_func_name = f"logdet_{cov_type2}"

    q_logdet_func = getattr(normalkl.logdet, q_logdet_func_name, None)
    p_logdet_func = getattr(normalkl.logdet, p_logdet_func_name, None)
    
    if q_logdet_func:
        if any([substring in q_logdet_func_name for substring in ['scalar', 'covrow', 'covcol']]):
            q_logdet = q_logdet_func(cov1, dim)
        else:
            q_logdet = q_logdet_func(cov1)
    else:
        raise NotImplementedError(f"log determinant not implemented yet for covariances of type '{cov_type1}' (please add a pull request on Github)")
    
    if p_logdet_func:
        if any([substring in p_logdet_func_name for substring in ['scalar', 'row', 'col']]):
            p_logdet = p_logdet_func(cov2, dim)
        else:
            p_logdet = p_logdet_func(cov2)
    else:
        raise NotImplementedError(f"log determinant not implemented yet for covariances of type '{cov_type2}' (please add a pull request on Github)")

    return 0.5 * (p_logdet - q_logdet)


def quadratic_term_func(mean_diff, cov_type2, cov2):
    func_name = f"quadratic_{cov_type2}"

    quadratic_func = getattr(normalkl.quadratic, func_name)

    if quadratic_func:
        return quadratic_func(mean_diff, cov2)
    else:
        raise NotImplementedError(f"quadratic term not implemented yet for covariances of type '{cov_type2}' (please add a pull request on Github)")
    

def kl(mean1, cov_type1, cov1, mean2, cov_type2, cov2, verbose=False):
    """ Computes the KL divergence between two multivariate normals
            KL( N(mean1, cov1) || N(mean2, cov2) )

        Input:
            mean1: mean of first multivariate normal 
            cov_typ1: covariance type of first multivariate normal
            cov1: covariance of first multivariate normal
            mean2: mean of first multivariate normal 
            cov_typ2: covariance type of first multivariate normal
            cov2: covariance of first multivariate normal

        Returns: the KL (scalar number)
    """ 

    
    dim1, dtype, device = dim_dtype_device_of_cov(mean1, cov_type1, cov1)
    dim2, _, _ = dim_dtype_device_of_cov(mean1, cov_type1, cov1)
    assert dim1 == dim2, f"Dimensions of first covariance ({dim1}) does not match other covariance ({dim2})"
    if isinstance(mean1, float):
        mean1 = torch.zeros(dim1, dtype=dtype, device=device)
    if isinstance(mean2, float):
        mean2 = torch.zeros(dim2, dtype=dtype, device=device)

    trace_term = trace_term_func(cov_type1, cov1, cov_type2, cov2)
    volume_term = volume_term_func(cov_type1, cov1, cov_type2, cov2, dim=dim1)
    quadratic_term = quadratic_term_func(mean1 - mean2, cov_type2, cov2)
    dimension_term = -0.5 * dim1

    kl_div = trace_term + volume_term + quadratic_term + dimension_term
    kl_div = kl_div.squeeze()

    if verbose:
        print(f"KL = {kl_div.item():.2f}  [trace: {trace_term.item():.2f}, volume: {volume_term.item():.2f}, quadratic: {quadratic_term.item()}, dimension: {dimension_term:.2f}")
    

    return kl_div

