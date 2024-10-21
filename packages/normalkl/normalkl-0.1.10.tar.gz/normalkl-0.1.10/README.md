# `normalkl`: KL divergences between normal distributions, without the stress

A PyTorch package for computing KL divergences between multivariate normal distributions.

Fully unit tested, so you don't have to worry about making sign errors.

# How to use?

The function `kl` can be used to compute regular KL divergence between two normal distributions.

```
from normalkl import kl

mean1 = torch.tensor([4.0, 5.0])
covariance1 = torch.tensor([[1.0, 1.0], [2.0, 4.0]])
mean2 = torch.tensor([1.0, 2.0])
scalarvar2 = torch.tensor([3.0])

kl_div = kl(mean1, 'covmat', covariance1, mean2, 'scalarvar', scalarvar2)
print(kl_div)
```

# Installation

Package available in pip:

```
pip install normalkl
```

# Auto KL

The `auto_kl` computes KL divergence with prior variance automatically chosen such that the KL is minimized.

```
from normalkl import auto_kl
kl_div2 = auto_kl(mean1, 'cov', covariance1, mean2)
```

We can also separately compute the optimal prior variance using `optimal_covariance`,

```
from normalkl import kl, optimal_covariance, auto_kl

optimal_scalarvar = optimal_covariance(mean1, 'cov', cov1, mean2, 'scalarvar')
kl_div1 = kl(mean1, 'cov', covariance1, mean2, 'scalarvar', optimal_scalarvar)

kl_div2 = auto_kl(mean1, 'cov', covariance1, mean2)

print(kl_div1 == kl_div2) # True

```

# Covariance types

For the first distribution (e.g. variational posterior), we support regular normal and Cholesky Kronecker Covariance (= matrix normal) parameterizations.
For the second distribution (e.g. prior distribution), the following full, Kronecker and isotropic priors are supported.

| Covariance Type                        | Abbreviation     | Mathematical Formula                            | Expected Type (Shape)            | cov1 | cov2 |
|----------------------------------------|------------------|------------------------------------------------|----------------------------------|------|------|
| Full Covariance Matrix                 | `covmat`         | $\Sigma$                                       | Full matrix (PSD), shape: $(D, D)$ |  ✓   | ✓    |
| Full Precision Matrix                  | `precmat`        | $\Sigma^{-1}$                                  | Full matrix (PSD), shape: $(D, D)$ |     | ✓    |
| Diagonal Covariance Matrix (Vector)    | `diagvar`        | $\text{diag}(\mathbf{d})$, where $\mathbf{d}$ is a vector | Vector, shape: $(D,)$             |   | ✓    |
| Diagonal Precision Matrix (Vector)     | `diagprec`       | $\text{diag}(\mathbf{d})^{-1}$, where $\mathbf{d}$ is a vector | Vector, shape: $(D,)$             |     | ✓    |
| Scalar Variance                        | `scalarvar`      | $\sigma^2 \mathbf{I}$, where $\sigma^2$ is a scalar | Scalar, shape: $(1,)$             |     | ✓    |
| Scalar Precision                       | `scalarprec`     | $\tau^{-1} \mathbf{I}$, where $\tau^{-1}$ is a scalar | Scalar, shape: $(1,)$             |     | ✓    |
| Identity Matrix                        | `identity`       | $\mathbf{I}$, the identity matrix              | Flag or Boolean, shape: $(D, D)$  |     | ✓    |
| Cholesky of Covariance Matrix          | `cholcov`        | $\mathbf{L}$, where $\Sigma = \mathbf{L}\mathbf{L}^\top$ | Lower triangular matrix, shape: $(D, D)$ |     | ✓    |
| Cholesky of Precision Matrix           | `cholprec`       | $\mathbf{L}$, where $\Sigma^{-1} = \mathbf{L}\mathbf{L}^\top$ | Lower triangular matrix, shape: $(D, D)$ |     | ✓    |
| Kronecker-Factored Covariance Matrix   | `kroncov`        | $\Sigma = \mathbf{A} \otimes \mathbf{B}$       | Pair of matrices, shapes: $(D_1, D_1)$, $(D_2, D_2)$ |     | ✓    |
| Kronecker-Factored Precision Matrix    | `kronprec`       | $\Sigma^{-1} = \mathbf{A} \otimes \mathbf{B}$  | Pair of matrices, shapes: $(D_1, D_1)$, $(D_2, D_2)$ |     | ✓    |
| Cholesky Kronecker Covariance  (recommended)     | `cholkroncov`    | $\Sigma = (\mathbf{L}_A \mathbf{L}_A^\top \otimes \mathbf{L}_B \mathbf{L}_B^\top)$ | Pair of lower triangular matrices, shapes: $(D_1, D_1)$, $(D_2, D_2)$ | ✓    | ✓    |
| Diagonal row+column variances           | `diagvarkron`  | $\text{diag}(\text{vec}(\mathbf{b} \mathbf{a}^T))$ | Pair of vectors, shapes: $(D_1,)$, $(D_2,)$             |     | ✓    |
| Diagonal row variances                  | `diagvarrow`     | $\text{diag}(\text{vec}(\mathbf{1} \mathbf{a}^T))$ | Vector, shape: $(D_1,)$             |     | ✓    |
| Diagonal column variances               | `diagvarcol`     | $\text{diag}(\text{vec}(\mathbf{b} \mathbf{1}^T))$ | Vector, shape: $(D_2,)$             |     | ✓    |

# Optimal prior variances

Analytically optimal cov2 variances are available for the following types:

| Type of cov1 \ Type of optimized cov2 | `covmat` | `precmat` | `diagvar` | `diagprec` | `scalarvar` | `scalarprec` | `identity` | `cholcov` | `cholprec` | `kroncov` | `kronprec` | `cholkroncov` | `diagcovkron` | `diagcovrow` | `diagcovcol` |
|---------------------------|----------|-----------|-----------|------------|-------------|--------------|------------|-----------|------------|-----------|------------|--------------|-----------------|--------------|--------------|
| `covmat`                  |     ✓     |    ✓       |    ✓      |      ✓     |      ✓      |    ✓         |            |           |            |           |            |               |                |     ✓      |  ✓        |         
| `precmat`                 |     ✓     |     ✓     |           |            |             |              |            |           |            |           |            |               |                |                 |              |            
| `diagvar`                 |          |           |           |            |             |              |            |           |            |           |            |               |                |                 |              |           
| `diagprec`                |          |           |           |            |             |              |            |           |            |           |            |               |                |                 |              |           
| `scalarvar`               |          |           |           |            |             |              |            |           |            |           |            |               |                |                 |              |           
| `scalarprec`              |          |           |           |            |             |              |            |           |            |           |            |               |                |                 |              |           
| `identity`                |          |           |           |            |             |              |            |           |            |           |            |               |                |                 |              |           
| `cholcov`                 |          |           |           |            |             |              |            |           |            |           |            |               |                |                 |              |           
| `cholprec`                |          |           |           |            |             |              |            |           |            |           |            |               |                |                 |              |           
| `kroncov`                 |          |           |           |            |             |              |            |           |            |           |            |               |                |                 |              |           
| `kronprec`                |          |           |           |            |             |              |            |           |            |           |            |               |                |                 |              |           
| `cholkroncov` (recommended) |  ✓     |      ✓    |     ✓      |   ✓       |    ✓       |      ✓       |     ✓        |           |          |            |           |              |               |   ✓             |    ✓             |         
| `diagvarkron`             |          |           |           |            |             |              |            |           |            |           |            |               |                |                 |              |             
| `diagvarrow`              |          |           |           |            |             |              |            |           |            |           |            |               |                |                 |              |           
| `diagvarcol`              |          |           |           |            |             |              |            |           |            |           |            |               |                |                 |              |            

