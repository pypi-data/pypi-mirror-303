import torch

def dim_dtype_device_of_cov(mean, cov_type, cov):
    if cov_type in ['covmat', 'precmat', 'diagvar', 'diagprec', 'cholcov', 'cholprec']:
        return cov.size(0), cov.dtype, cov.device
    elif cov_type in ['scalarvar', 'scalarprec', 'identity', 'diagvarrow', 'diagvarcol']:
        if type(mean) == float:
            raise ValueError(f"Type '{cov_type}' requires mean tensor and not just float, because dimensionality can not be known in this case.")
        return mean.size(0), mean.dtype, mean.device
    elif cov_type in ['kroncov', 'kronprec', 'cholkroncov', 'diagvarkron']:
        return cov[0].size(0) * cov[1].size(0), cov[0].dtype, cov[0].device
    else:
        raise NotImplementedError(f"Unknown cov_type: {cov_type}")


def is_zero(x):
    if isinstance(x, float):
        return x == 0.0
    elif isinstance(x, torch.Tensor):
        return torch.all(x == 0.0)
    else:
        return False
