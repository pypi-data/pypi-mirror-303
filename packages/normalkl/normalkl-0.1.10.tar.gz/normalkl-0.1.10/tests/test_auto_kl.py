import unittest

import torch

from normalkl import kl, auto_kl
from normalkl import optimal_covariance


class TestAutoKL(unittest.TestCase):
    def setUp(self):
        dtype = torch.float64

        d1, d2 = 3, 4
        d = d1 * d2

        self.d1 = d1
        self.d2 = d2
        self.d = d

        dtype=torch.float64

        # Means
        self.mean1 = torch.randn(d, dtype=dtype)
        self.mean2 = torch.randn(d, dtype=dtype)

        # Full covariance 
        self.L1 = torch.randn(d, d, dtype=dtype).tril()
        self.L2 = torch.randn(d, d, dtype=dtype).tril()
        self.covmat1 = self.L1 @ self.L1.T
        self.precmat1 = torch.inverse(self.covmat1)
        self.covmat2 = self.L2 @ self.L2.T
        self.precmat2 = torch.inverse(self.covmat2)
            
        # Cholesky factors for cholkroncov1 and cholkroncov2
        self.LU1 = torch.randn(d1, d1, dtype=dtype).tril()
        self.LV1 = torch.randn(d2, d2, dtype=dtype).tril()
        self.LU2 = torch.randn(d1, d1, dtype=dtype).tril()
        self.LV2 = torch.randn(d2, d2, dtype=dtype).tril()

        # Covariance matrices for cholkroncov1 and cholkroncov2
        self.U1 = self.LU1 @ self.LU1.T
        self.V1 = self.LV1 @ self.LV1.T
        self.U2 = self.LU2 @ self.LU2.T
        self.V2 = self.LV2 @ self.LV2.T

        # Cholesky Kronecker decompositions
        self.cholkroncov1 = (self.LU1, self.LV1)
        self.cholkroncov2 = (self.LU2, self.LV2)

        # Full covariance matrices
        self.kron_covmat1 = torch.kron(self.U1, self.V1)
        self.kron_covmat2 = torch.kron(self.U2, self.V2)

        # Other inputs
        self.I = torch.eye(d, dtype=dtype)
        self.v1 = torch.randn(d, dtype=dtype)
        self.v2 = torch.randn(d, dtype=dtype)
        self.s2 = torch.tensor(2.0, dtype=dtype)
        self.a1 = torch.randn(d1, dtype=dtype).square()
        self.b1 = torch.randn(d2, dtype=dtype).square()

        self.rtol = 1e-6
        self.atol = 1e-6


    # auto_kl_*_covmat
    def test_auto_kl_covmat_covmat(self):
        optimal_covmat2 = optimal_covariance(self.mean1, 'covmat', self.covmat1, self.mean2, 'covmat')
        result_manual = kl(self.mean1, 'covmat', self.covmat1, self.mean2, 'covmat', optimal_covmat2, verbose=True)
        result_auto = auto_kl(self.mean1, 'covmat', self.covmat1, self.mean2, 'covmat')

        self.assertTrue(torch.allclose(result_manual, result_auto))

    def test_auto_kl_precmat_covmat(self):
        optimal_covmat2 = optimal_covariance(self.mean1, 'precmat', self.precmat1, self.mean2, 'covmat')
        result_manual = kl(self.mean1, 'precmat', self.precmat1, self.mean2, 'covmat', optimal_covmat2, verbose=True)
        result_auto = auto_kl(self.mean1, 'precmat', self.precmat1, self.mean2, 'covmat')

        self.assertTrue(torch.allclose(result_manual, result_auto))

    def test_auto_kl_cholkroncov_covmat(self):
        optimal_covmat2 = optimal_covariance(self.mean1, 'cholkroncov', self.cholkroncov1, self.mean2, 'covmat')
        result_manual = kl(self.mean1, 'cholkroncov', self.cholkroncov1, self.mean2, 'covmat', optimal_covmat2, verbose=True)
        result_auto = auto_kl(self.mean1, 'cholkroncov', self.cholkroncov1, self.mean2, 'covmat')

        self.assertTrue(torch.allclose(result_manual, result_auto))

    # auto_kl_*_precmat
    def test_auto_kl_covmat_precmat(self):
        optimal_precmat2 = optimal_covariance(self.mean1, 'covmat', self.covmat1, self.mean2, 'precmat')
        result_manual = kl(self.mean1, 'covmat', self.covmat1, self.mean2, 'precmat', optimal_precmat2, verbose=True)
        result_auto = auto_kl(self.mean1, 'covmat', self.covmat1, self.mean2, 'precmat')

        self.assertTrue(torch.allclose(result_manual, result_auto))

    def test_auto_kl_precmat_precmat(self):
        optimal_precmat2 = optimal_covariance(self.mean1, 'precmat', self.precmat1, self.mean2, 'precmat')
        result_manual = kl(self.mean1, 'precmat', self.precmat1, self.mean2, 'precmat', optimal_precmat2, verbose=True)
        result_auto = auto_kl(self.mean1, 'precmat', self.precmat1, self.mean2, 'precmat')

        self.assertTrue(torch.allclose(result_manual, result_auto))

    def test_auto_kl_cholkroncov_precmat(self):
        optimal_precmat2 = optimal_covariance(self.mean1, 'cholkroncov', self.cholkroncov1, self.mean2, 'precmat')
        result_manual = kl(self.mean1, 'cholkroncov', self.cholkroncov1, self.mean2, 'precmat', optimal_precmat2, verbose=True)
        result_auto = auto_kl(self.mean1, 'cholkroncov', self.cholkroncov1, self.mean2, 'precmat')

        self.assertTrue(torch.allclose(result_manual, result_auto))

    # auto_kl_*_diagvar
    def test_auto_kl_covmat_diagvar(self):
        optimal_diagvar2 = optimal_covariance(self.mean1, 'covmat', self.covmat1, self.mean2, 'diagvar')
        result_manual = kl(self.mean1, 'covmat', self.covmat1, self.mean2, 'diagvar', optimal_diagvar2, verbose=True)
        result_auto = auto_kl(self.mean1, 'covmat', self.covmat1, self.mean2, 'diagvar')

        self.assertTrue(torch.allclose(result_manual, result_auto))

    def test_auto_kl_cholkroncov_diagvar(self):
        optimal_diagvar2 = optimal_covariance(self.mean1, 'cholkroncov', self.cholkroncov1, self.mean2, 'diagvar')
        result_manual = kl(self.mean1, 'cholkroncov', self.cholkroncov1, self.mean2, 'diagvar', optimal_diagvar2, verbose=True)
        result_auto = auto_kl(self.mean1, 'cholkroncov', self.cholkroncov1, self.mean2, 'diagvar')

        self.assertTrue(torch.allclose(result_manual, result_auto))

    def test_auto_kl_cholkroncov_diagvar_zero(self):
        optimal_diagvar2 = optimal_covariance(0.0, 'cholkroncov', self.cholkroncov1, 0.0, 'diagvar')
        result_manual = kl(0.0, 'cholkroncov', self.cholkroncov1, 0.0, 'diagvar', optimal_diagvar2, verbose=True)
        result_auto = auto_kl(0.0, 'cholkroncov', self.cholkroncov1, 0.0, 'diagvar')

        self.assertTrue(torch.allclose(result_manual, result_auto))

    # auto_kl_*_diagprec
    def test_auto_kl_covmat_diagprec(self):
        optimal_diagprec2 = optimal_covariance(self.mean1, 'covmat', self.covmat1, self.mean2, 'diagprec')
        result_manual = kl(self.mean1, 'covmat', self.covmat1, self.mean2, 'diagprec', optimal_diagprec2)
        result_auto = auto_kl(self.mean1, 'covmat', self.covmat1, self.mean2, 'diagprec')

        self.assertTrue(torch.allclose(result_manual, result_auto))

    # auto_kl_*_scalarvar
    def test_auto_kl_covmat_scalarvar(self):
        optimal_scalarvar2 = optimal_covariance(self.mean1, 'covmat', self.covmat1, self.mean2, 'scalarvar')
        result_manual = kl(self.mean1, 'covmat', self.covmat1, self.mean2, 'scalarvar', optimal_scalarvar2)
        result_auto = auto_kl(self.mean1, 'covmat', self.covmat1, self.mean2, 'scalarvar')

        self.assertTrue(torch.allclose(result_manual, result_auto))

    def test_auto_kl_cholkroncov_scalarvar(self):
        optimal_scalarvar2 = optimal_covariance(self.mean1, 'cholkroncov', self.cholkroncov1, self.mean2, 'scalarvar')
        result_manual = kl(self.mean1, 'cholkroncov', self.cholkroncov1, self.mean2, 'scalarvar', optimal_scalarvar2)
        result_auto = auto_kl(self.mean1, 'cholkroncov', self.cholkroncov1, self.mean2, 'scalarvar')

        self.assertTrue(torch.allclose(result_manual, result_auto))

    # auto_kl_*_scalarprec
    def test_auto_kl_covmat_scalarprec(self):
        optimal_scalarprec2 = optimal_covariance(self.mean1, 'covmat', self.covmat1, self.mean2, 'scalarprec')
        result_manual = kl(self.mean1, 'covmat', self.covmat1, self.mean2, 'scalarprec', optimal_scalarprec2)
        result_auto = auto_kl(self.mean1, 'covmat', self.covmat1, self.mean2, 'scalarprec')

        self.assertTrue(torch.allclose(result_manual, result_auto))

    def test_auto_kl_cholkroncov_scalarprec(self):
        optimal_scalarprec2 = optimal_covariance(self.mean1, 'cholkroncov', self.cholkroncov1, self.mean2, 'scalarprec')
        result_manual = kl(self.mean1, 'cholkroncov', self.cholkroncov1, self.mean2, 'scalarprec', optimal_scalarprec2)
        result_auto = auto_kl(self.mean1, 'cholkroncov', self.cholkroncov1, self.mean2, 'scalarprec')

        self.assertTrue(torch.allclose(result_manual, result_auto))

    # auto_kl_*_diagvarrow
    def test_auto_kl_covmat_diagvarrow(self):
        optimal_diagvarrow2 = optimal_covariance(self.mean1, 'covmat', self.covmat1, self.mean2, 'diagvarrow', d1=self.d1, d2=self.d2)
        result_manual = kl(self.mean1, 'covmat', self.covmat1, self.mean2, 'diagvarrow', optimal_diagvarrow2)
        result_auto = auto_kl(self.mean1, 'covmat', self.covmat1, self.mean2, 'diagvarrow', d1=self.d1, d2=self.d2)

        self.assertTrue(torch.allclose(result_manual, result_auto))

    def test_auto_kl_cholkroncov_diagvarrow(self):
        optimal_diagvarrow2 = optimal_covariance(self.mean1, 'cholkroncov', self.cholkroncov1, self.mean2, 'diagvarrow', d1=self.d1, d2=self.d2)
        result_manual = kl(self.mean1, 'cholkroncov', self.cholkroncov1, self.mean2, 'diagvarrow', optimal_diagvarrow2)
        result_auto = auto_kl(self.mean1, 'cholkroncov', self.cholkroncov1, self.mean2, 'diagvarrow', d1=self.d1, d2=self.d2)

        self.assertTrue(torch.allclose(result_manual, result_auto))

    # auto_kl_*_diagvarcol
    def test_auto_kl_covmat_diagvarcol(self):
        optimal_diagvarrow2 = optimal_covariance(self.mean1, 'covmat', self.covmat1, self.mean2, 'diagvarrow', d1=self.d1, d2=self.d2)
        result_manual = kl(self.mean1, 'covmat', self.covmat1, self.mean2, 'diagvarrow', optimal_diagvarrow2)
        result_auto = auto_kl(self.mean1, 'covmat', self.covmat1, self.mean2, 'diagvarrow', d1=self.d1, d2=self.d2)

        self.assertTrue(torch.allclose(result_manual, result_auto))

    def test_auto_kl_cholkroncov_diagvarcol(self):
        optimal_diagvarrow2 = optimal_covariance(self.mean1, 'cholkroncov', self.cholkroncov1, self.mean2, 'diagvarrow', d1=self.d1, d2=self.d2)
        result_manual = kl(self.mean1, 'cholkroncov', self.cholkroncov1, self.mean2, 'diagvarrow', optimal_diagvarrow2)
        result_auto = auto_kl(self.mean1, 'cholkroncov', self.cholkroncov1, self.mean2, 'diagvarrow', d1=self.d1, d2=self.d2)

        self.assertTrue(torch.allclose(result_manual, result_auto))


# Run the tests
if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)

