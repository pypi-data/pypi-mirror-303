import unittest

import torch

from normalkl import kl, optimal_covariance


class TestOptimalCov2(unittest.TestCase):
    def setUp(self):
        torch.manual_seed(0)

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
        self.covmat2 = self.L2 @ self.L2.T
            
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

        self.cov1_list = [('covmat', self.covmat1),
                     ('precmat', self.covmat1),
                     ('diagvar', self.v1),
                     ('diagprec', self.v1),
                     ('scalarvar', self.s2),
                     ('scalarprec', self.s2),
                     ('identity', None),
                     ('cholcov', self.L1),
                     ('cholprec', self.L1),
                     ('kroncov', (self.U1, self.V1)),
                     ('kronprec', (self.U1, self.U2)),
                     ('cholkroncov', (self.LU1, self.LV1)),
                     ('cholkronprec', (self.LU1, self.LV1)),
                     ('diagvarkron', (self.a1, self.b1)),
                     ('diagvarrow', self.a1),
                     ('diagvarcol', self.b1)]



    def _is_optimum(self, objective_function, point, tolerance=1e-3):
        """
        Check if the point is at an optimum of the objective function.

        Args:
            point (torch.Tensor): The point to check.
            objective_function (callable): The objective function to minimize or maximize.
            tolerance (float): The tolerance for checking if the gradient is close to zero.

        Returns:
            bool: True if the point is at the optimum, False otherwise.
        """
        # Ensure the point requires gradients for optimization checking
        point = point.clone().detach().requires_grad_(True)

        # Compute the objective function value at the given point
        obj_value = objective_function(point)
        
        # Compute the gradients with respect to the point
        obj_value.backward()

        # Check if the gradients are close to zero within the specified tolerance
        is_at_optimum = torch.all(torch.abs(point.grad) < tolerance)

        return is_at_optimum

    # test_optimal_*_covmat

    def test_optimal_covmat_covmat(self):
        optimal_covmat2 = optimal_covariance(self.mean1, 'covmat', self.covmat1, self.mean2, 'covmat')
        kl_func = lambda covmat2: kl(self.mean1, 'covmat', self.covmat1, self.mean2, 'covmat', covmat2)

        self.assertTrue(self._is_optimum(kl_func, optimal_covmat2))

    def test_optimal_cholkroncov_covmat(self):
        optimal_covmat2 = optimal_covariance(self.mean1, 'cholkroncov', self.cholkroncov1, self.mean2, 'covmat')
        kl_func = lambda covmat2: kl(self.mean1, 'cholkroncov', self.cholkroncov1, self.mean2, 'covmat', covmat2)

        self.assertTrue(self._is_optimum(kl_func, optimal_covmat2))

    # test_optimal_*_precmat

    def test_optimal_covmat_precmat(self):
        optimal_precmat2 = optimal_covariance(self.mean1, 'covmat', self.covmat1, self.mean2, 'precmat')
        kl_func = lambda precmat2: kl(self.mean1, 'covmat', self.covmat1, self.mean2, 'precmat', precmat2)

        self.assertTrue(self._is_optimum(kl_func, optimal_precmat2))

    def test_optimal_cholkroncov_precmat(self):
        optimal_precmat2 = optimal_covariance(self.mean1, 'cholkroncov', self.cholkroncov1, self.mean2, 'precmat')
        kl_func = lambda precmat2: kl(self.mean1, 'cholkroncov', self.cholkroncov1, self.mean2, 'precmat', precmat2)

        self.assertTrue(self._is_optimum(kl_func, optimal_precmat2))

    # test_optimal_*_diagprec

    def test_optimal_covmat_diagprec(self):
        optimal_diagprec2 = optimal_covariance(self.mean1, 'covmat', self.covmat1, self.mean2, 'diagprec')
        kl_func = lambda diagprec2: kl(self.mean1, 'covmat', self.covmat1, self.mean2, 'diagprec', diagprec2)

        self.assertTrue(self._is_optimum(kl_func, optimal_diagprec2))


    # test_optimal_*_diagvar

    def test_optimal_covmat_diagvar(self):
        optimal_diagvar2 = optimal_covariance(self.mean1, 'covmat', self.covmat1, self.mean2, 'diagvar')
        kl_func = lambda diagvar2: kl(self.mean1, 'covmat', self.covmat1, self.mean2, 'diagvar', diagvar2)

        self.assertTrue(self._is_optimum(kl_func, optimal_diagvar2))

    # test_optimal_*_diagprec

    def test_optimal_covmat_diagprec(self):
        optimal_diagprec2 = optimal_covariance(self.mean1, 'covmat', self.covmat1, self.mean2, 'diagprec')
        kl_func = lambda diagprec2: kl(self.mean1, 'covmat', self.covmat1, self.mean2, 'diagprec', diagprec2)

        self.assertTrue(self._is_optimum(kl_func, optimal_diagprec2))

    # test_optimal_*_scalarvar

    def test_optimal_covmat_scalarvar(self):
        optimal_scalarvar2 = optimal_covariance(self.mean1, 'covmat', self.covmat1, self.mean2, 'scalarvar')
        kl_func = lambda scalarvar2: kl(self.mean1, 'covmat', self.covmat1, self.mean2, 'scalarvar', scalarvar2)

        self.assertTrue(self._is_optimum(kl_func, optimal_scalarvar2))

    def test_optimal_cholkroncov_scalarvar(self):
        optimal_scalarvar2 = optimal_covariance(self.mean1, 'cholkroncov', self.cholkroncov1, self.mean2, 'scalarvar')
        kl_func = lambda scalarvar2: kl(self.mean1, 'cholkroncov', self.cholkroncov1, self.mean2, 'scalarvar', scalarvar2)

        self.assertTrue(self._is_optimum(kl_func, optimal_scalarvar2))

    # test_optimal_*_scalarprec

    def test_optimal_covmat_scalarprec(self):
        optimal_scalarprec2 = optimal_covariance(self.mean1, 'covmat', self.covmat1, self.mean2, 'scalarprec')
        kl_func = lambda scalarprec2: kl(self.mean1, 'covmat', self.covmat1, self.mean2, 'scalarprec', scalarprec2)

        self.assertTrue(self._is_optimum(kl_func, optimal_scalarprec2))


    def test_optimal_cholkroncov_scalarprec(self):
        optimal_scalarprec2 = optimal_covariance(self.mean1, 'cholkroncov', self.cholkroncov1, self.mean2, 'scalarprec')
        kl_func = lambda scalarprec2: kl(self.mean1, 'cholkroncov', self.cholkroncov1, self.mean2, 'scalarprec', scalarprec2)

        self.assertTrue(self._is_optimum(kl_func, optimal_scalarprec2))

    # test_optimal_*_diagvarrow

    def test_optimal_covmat_diagvarrow(self):
        optimal_diagvarrow2 = optimal_covariance(self.mean1, 'covmat', self.covmat1, self.mean2, 'diagvarrow', d1=self.d1, d2=self.d2)
        kl_func = lambda diagvarrow2: kl(self.mean1, 'covmat', self.covmat1, self.mean2, 'diagvarrow', diagvarrow2)

        print(optimal_diagvarrow2, kl_func(optimal_diagvarrow2))
        #self.assertTrue(False)

        self.assertTrue(self._is_optimum(kl_func, optimal_diagvarrow2))

    def test_optimal_cholkroncov_diagvarrow(self):
        optimal_diagvarrow2 = optimal_covariance(self.mean1, 'cholkroncov', self.cholkroncov1, self.mean2, 'diagvarrow', d1=self.d1, d2=self.d2)
        kl_func = lambda diagvarrow2: kl(self.mean1, 'cholkroncov', self.cholkroncov1, self.mean2, 'diagvarrow', diagvarrow2)

        print(optimal_diagvarrow2, kl_func(optimal_diagvarrow2))
        #self.assertTrue(False)

        self.assertTrue(self._is_optimum(kl_func, optimal_diagvarrow2))

    # test_optimal_*_diagvarrow


    def test_optimal_covmat_diagvarcol(self):
        optimal_diagvarcol2 = optimal_covariance(self.mean1, 'covmat', self.covmat1, self.mean2, 'diagvarcol', d1=self.d1, d2=self.d2)
        kl_func = lambda diagvarcol2: kl(self.mean1, 'covmat', self.covmat1, self.mean2, 'diagvarcol', diagvarcol2)

        print(optimal_diagvarcol2, kl_func(optimal_diagvarcol2))
        #self.assertTrue(False)

        self.assertTrue(self._is_optimum(kl_func, optimal_diagvarcol2))

    def test_optimal_cholkroncov_diagvarcol(self):
        optimal_diagvarcol2 = optimal_covariance(self.mean1, 'cholkroncov', self.cholkroncov1, self.mean2, 'diagvarcol', d1=self.d1, d2=self.d2)
        kl_func = lambda diagvarcol2: kl(self.mean1, 'cholkroncov', self.cholkroncov1, self.mean2, 'diagvarcol', diagvarcol2)

        print(optimal_diagvarcol2, kl_func(optimal_diagvarcol2))
        #self.assertTrue(False)

        self.assertTrue(self._is_optimum(kl_func, optimal_diagvarcol2))



# Run the tests
if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)

