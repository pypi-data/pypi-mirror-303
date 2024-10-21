import unittest

from normalkl.logdet import *

class TestLogDet(unittest.TestCase):
    def setUp(self):
        d1, d2 = 3, 4
        d = d1 * d2
        self.d1 = d1
        self.d2 = d2
        self.d = d

        dtype = torch.float64

        self.LU1 = torch.randn(d1, d1, dtype=dtype).tril()
        self.LV1 = torch.randn(d2, d2, dtype=dtype).tril()
        self.U1 = self.LU1 @ self.LU1.T
        self.V1 = self.LV1 @ self.LV1.T
        self.kron_covmat1 = torch.kron(self.U1, self.V1)
        
        self.L1 = torch.randn(d, d, dtype=dtype).tril() + torch.eye(d, dtype=dtype)
        self.covmat1 = self.L1 @ self.L1.T
        self.precmat1 = torch.inverse(self.covmat1)
        
        self.I = torch.eye(d)
        self.s2 = torch.tensor(2.0)
        self.v1 = torch.rand(d)
        self.a = torch.rand(d1)
        self.b = torch.rand(d2)

    def test_logdet_covmat(self):
        expected = torch.logdet(self.covmat1)
        result = logdet_covmat(self.covmat1)
        self.assertTrue(torch.allclose(expected, result))

    def test_logdet_precmat(self):
        expected = logdet_covmat(self.covmat1)
        result = logdet_precmat(self.precmat1)
        self.assertTrue(torch.allclose(expected, result))

    def test_logdet_diagvar(self):
        expected = self.v1.abs().log().sum()
        result = logdet_diagvar(self.v1)
        self.assertTrue(torch.allclose(expected, result))

    def test_logdet_diagprec(self):
        expected = -self.v1.abs().log().sum()
        result = logdet_diagprec(self.v1)
        self.assertTrue(torch.allclose(expected, result))

    def test_logdet_scalarvar(self):
        dim = self.covmat1.size(0)
        expected = dim * self.s2.abs().log()
        result = logdet_scalarvar(self.s2, dim)
        self.assertTrue(torch.allclose(expected, result))

    def test_logdet_scalarprec(self):
        dim = self.covmat1.size(0)
        expected = -dim * self.s2.log()
        result = logdet_scalarprec(self.s2, dim)
        self.assertTrue(torch.allclose(expected, result))

    def test_logdet_cholcov(self):
        expected = self.L1.diag().square().log().sum()
        result = logdet_cholcov(self.L1)
        self.assertTrue(torch.allclose(expected, result))

    def test_logdet_cholprec(self):
        expected = -self.L1.diag().square().log().sum()
        result = logdet_cholprec(self.L1)
        self.assertTrue(torch.allclose(expected, result))

    def test_logdet_kroncov(self):
        expected = len(self.V1) * logdet_covmat(self.U1) + len(self.U1) * logdet_covmat(self.V1)
        result = logdet_kroncov((self.U1, self.V1))
        self.assertTrue(torch.allclose(expected, result))

    def test_logdet_kronprec(self):
        expected = len(self.V1) * logdet_precmat(self.U1) + len(self.U1) * logdet_precmat(self.V1)
        result = logdet_kronprec((self.U1, self.V1))
        self.assertTrue(torch.allclose(expected, result))

    def test_logdet_cholkroncov(self):
        expected = len(self.LV1) * logdet_cholcov(self.LU1) + len(self.LU1) * logdet_cholcov(self.LV1)
        result = logdet_cholkroncov((self.LU1, self.LV1))
        self.assertTrue(torch.allclose(expected, result))

    def test_logdet_diagvarrowcol(self):
        expected = logdet_covmat(torch.kron(self.a.diag(), self.b.diag()))
        result = logdet_diagvarkron((self.a, self.b))
        self.assertTrue(torch.allclose(expected, result))

    def test_logdet_diagvarrow(self):
        expected = logdet_covmat(torch.kron(self.a.diag(), torch.eye(self.d2)))
        result = logdet_diagvarrow(self.a, self.d)
        self.assertTrue(torch.allclose(expected, result))

    def test_logdet_diagvarcol(self):
        expected = logdet_covmat(torch.kron(torch.eye(self.d1), self.b.diag()))
        result = logdet_diagvarcol(self.b, self.d)
        self.assertTrue(torch.allclose(expected, result))



# Run the tests
if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)

