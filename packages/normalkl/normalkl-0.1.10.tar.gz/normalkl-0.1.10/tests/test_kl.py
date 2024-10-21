import unittest

import torch

from normalkl import kl


class TestKL(unittest.TestCase):
    def setUp(self):
        self.dtype = torch.float64

        d1, d2 = 3, 4
        d = d1 * d2

        self.d1 = d1
        self.d2 = d2
        self.d = d

        dtype = torch.float64

        # Full covariance
        self.L1 = torch.randn(d, d, dtype=dtype).tril()
        self.L2 = torch.randn(d, d, dtype=dtype).tril()
        self.L1_inv = torch.inverse(self.L1)
        self.L2_inv = torch.inverse(self.L2)
        self.covmat1 = self.L1 @ self.L1.T
        self.covmat2 = self.L2 @ self.L2.T

        # Cholesky factors for cholkroncov1 and cholkroncov2
        self.LU1 = torch.randn(d1, d1, dtype=dtype).tril()
        self.LV1 = torch.randn(d2, d2, dtype=dtype).tril()
        self.LU2 = torch.randn(d1, d1, dtype=dtype).tril()
        self.LV2 = torch.randn(d2, d2, dtype=dtype).tril()
        # self.LU1_inv = torch.inverse(self.LU1)
        # self.LV1_inv = torch.inverse(self.LV1)
        # self.LU2_inv = torch.inverse(self.LU2)
        # self.LV2_inv = torch.inverse(self.LV2)

        # Covariance matrices for cholkroncov1 and cholkroncov2
        self.U1 = self.LU1 @ self.LU1.T
        self.V1 = self.LV1 @ self.LV1.T
        self.U2 = self.LU2 @ self.LU2.T
        self.V2 = self.LV2 @ self.LV2.T
        self.U1_inv = torch.inverse(self.U1)
        self.V1_inv = torch.inverse(self.V1)
        self.U2_inv = torch.inverse(self.U2)
        self.V2_inv = torch.inverse(self.V2)

        # Cholesky Kronecker decompositions
        self.cholkroncov1 = (self.LU1, self.LV1)
        self.cholkroncov2 = (self.LU2, self.LV2)

        # Full covariance matrices
        self.kron_covmat1 = torch.kron(self.U1, self.V1)
        self.kron_covmat2 = torch.kron(self.U2, self.V2)
        self.kron_precmat1 = torch.kron(self.U1_inv, self.V1_inv)
        self.kron_precmat2 = torch.kron(self.U2_inv, self.V2_inv)

        # Other inputs
        self.I = torch.eye(d, dtype=dtype)
        self.v1 = torch.randn(d, dtype=dtype)
        self.v2 = torch.randn(d, dtype=dtype)
        self.s2 = torch.tensor(2.0, dtype=dtype)
        self.a2 = torch.randn(d1, dtype=dtype).square()
        self.b2 = torch.randn(d2, dtype=dtype).square()

        # Diagonal covariance and precision
        self.diagvar = torch.diag(self.covmat1)
        self.diagprec = 1.0 / self.diagvar

        # Scalar variance and precision
        self.scalarvar = torch.mean(self.diagvar).unsqueeze(0)
        self.scalarprec = 1.0 / self.scalarvar

        # Precision matrix
        self.precmat1 = torch.inverse(self.covmat1)
        self.precmat2 = torch.inverse(self.covmat2)

        self.covs2 = [('covmat', self.covmat2, self.covmat2),
                      ('precmat', self.precmat2, self.covmat2),
                      ('diagvar', self.diagvar, self.diagvar.diag()),
                      ('diagprec', self.diagprec, self.diagvar.diag()),
                      ('scalarvar', self.scalarvar, self.scalarvar * self.I),
                      ('scalarprec', self.scalarprec, self.scalarvar * self.I),
                      ('identity', None, self.I),
                      ('cholcov', self.L2, self.covmat2),
                      ('cholprec', torch.cholesky(self.precmat2), self.covmat2),
                      ('kroncov', (self.U2, self.V2), self.kron_covmat2),
                      ('kronprec', (self.U2_inv, self.V2_inv), self.kron_covmat2),
                      ('cholkroncov', (self.LU2, self.LV2), self.kron_covmat2),
                      # ('diagvarkron', (self.a2, self.b2), torch.kron(self.a2.diag(), self.b2.diag())),
                      # ('diagvarrow', self.a2, torch.kron(torch.eye(self.d1), self.b2.diag())),
                      # ('diagvarcov', self.b2, torch.kron(self.a2.diag(), torch.eye(self.d2)))
                      ]

        # Tolerances
        self.rtol = 1e-6
        self.atol = 1e-6

    def test_kl_readme_example(self):
        dtype = self.dtype
        mean1 = torch.tensor([4.0, 5.0], dtype=dtype)
        covariance1 = torch.tensor([[1.0, 1.0], [2.0, 4.0]], dtype=dtype)
        mean2 = torch.tensor([1.0, 2.0], dtype=dtype)
        scalarvar2 = torch.tensor([3.0], dtype=dtype)

        result = kl(mean1, 'covmat', covariance1, mean2, 'scalarvar', scalarvar2)

        expected = torch.tensor([3.5853720317214703], dtype=dtype)
        self.assertTrue(torch.allclose(expected, result))

    def test_kl_covmat_any(self):
        for cov_type2, cov2, expected_covmat2 in self.covs2:
            with self.subTest(case=cov_type2):
                expected = kl(self.v1, 'covmat', self.covmat1, self.v2, 'covmat', expected_covmat2)
                result = kl(self.v1, 'covmat', self.covmat1, self.v2, cov_type2, cov2)

                self.assertTrue(torch.allclose(expected, result), f"{cov_type2} fails: {expected:.4f}!={result:.4f}")



# Run the tests
if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)

