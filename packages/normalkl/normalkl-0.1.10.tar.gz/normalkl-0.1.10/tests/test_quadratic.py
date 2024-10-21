import unittest
import torch

from normalkl.quadratic import *

class TestQuadratic(unittest.TestCase):
    def setUp(self):
        torch.manual_seed(0)

        d1, d2 = 3, 4
        d = d1 * d2

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
        self.LU1_inv = torch.inverse(self.LU1)
        self.LV1_inv = torch.inverse(self.LV1)
        self.LU2_inv = torch.inverse(self.LU2)
        self.LV2_inv = torch.inverse(self.LV2)

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

        # Tolerances
        self.rtol = 1e-6
        self.atol = 1e-6

    def test_quadratic_covmat(self):
        result = quadratic_covmat(self.v1, self.covmat1)
        expected = quadratic_covmat(self.v1, self.covmat1)
        self.assertTrue(torch.isclose(result, expected, rtol=self.rtol, atol=self.atol))

    def test_quadratic_precmat(self):
        result = quadratic_precmat(self.v1, self.precmat1)
        expected = quadratic_covmat(self.v1, self.covmat1)
        self.assertTrue(torch.isclose(result, expected, rtol=self.rtol, atol=self.atol))

    def test_quadratic_diagvar(self):
        result = quadratic_diagvar(self.v1, self.diagvar)
        expected = quadratic_covmat(self.v1, torch.diag(self.diagvar))
        self.assertTrue(torch.isclose(result, expected, rtol=self.rtol, atol=self.atol))

    def test_quadratic_diagprec(self):
        result = quadratic_diagprec(self.v1, self.diagprec)
        expected = quadratic_covmat(self.v1, torch.diag(1.0 / self.diagprec))
        self.assertTrue(torch.isclose(result, expected, rtol=self.rtol, atol=self.atol))

    def test_quadratic_scalarvar(self):
        result = quadratic_scalarvar(self.v1, self.scalarvar)
        expected = quadratic_covmat(self.v1, self.scalarvar * torch.eye(self.v1.shape[0], dtype=self.v1.dtype))
        self.assertTrue(torch.isclose(result, expected, rtol=self.rtol, atol=self.atol))

    def test_quadratic_scalarprec(self):
        result = quadratic_scalarprec(self.v1, self.scalarprec)
        expected = quadratic_covmat(self.v1, torch.eye(self.v1.shape[0], dtype=self.v1.dtype) / self.scalarprec.item())
        self.assertTrue(torch.isclose(result, expected, rtol=self.rtol, atol=self.atol))

    def test_quadratic_identity(self):
        result = quadratic_identity(self.v1, self.I)
        expected = quadratic_covmat(self.v1, torch.eye(self.v1.shape[0], dtype=self.v1.dtype))
        self.assertTrue(torch.isclose(result, expected, rtol=self.rtol, atol=self.atol))

    def test_quadratic_cholcov(self):
        result = quadratic_cholcov(self.v1, self.L2)
        expected = quadratic_covmat(self.v1, self.covmat2)
        self.assertTrue(torch.isclose(result, expected, rtol=self.rtol, atol=self.atol))

    def test_quadratic_cholprec(self):
        result = quadratic_cholprec(self.v1, self.L2)
        expected = quadratic_covmat(self.v1, self.precmat2)
        self.assertTrue(torch.isclose(result, expected, rtol=self.rtol, atol=self.atol))

    def test_quadratic_kroncov(self):
        result = quadratic_kroncov(self.v1, (self.U2, self.V2))
        expected = quadratic_covmat(self.v1, self.kron_covmat2)
        self.assertTrue(torch.isclose(result, expected, rtol=self.rtol, atol=self.atol))

    def test_quadratic_kronprec(self):
        result = quadratic_kronprec(self.v1, (self.U2_inv, self.V2_inv))
        expected = quadratic_covmat(self.v1, self.kron_covmat2)
        self.assertTrue(torch.isclose(result, expected, rtol=self.rtol, atol=self.atol))

    def test_quadratic_cholkroncov(self):
        result = quadratic_cholkroncov(self.v1, (self.LU2, self.LV2))
        expected = quadratic_covmat(self.v1, self.kron_covmat2)
        print(result, expected)
        self.assertTrue(torch.isclose(result, expected, rtol=self.rtol, atol=self.atol))





# Run the tests
if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)

