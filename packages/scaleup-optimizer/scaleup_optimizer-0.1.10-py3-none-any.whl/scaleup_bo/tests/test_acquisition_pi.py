import pytest
import numpy as np
from scipy.stats import norm
from unittest.mock import Mock, patch
import warnings
from scaleup_bo.acquisition_functions import ProbabilityOfImprovement

class TestProbabilityOfImprovement:
    @pytest.fixture
    def acquisition_function(self):
        """Fixture to create a ProbabilityOfImprovement instance"""
        return ProbabilityOfImprovement(xi=0.1)

    @pytest.fixture
    def mock_model(self):
        """Fixture to create a mock model"""
        model = Mock()
        return model

    def test_initialization(self):
        """Test proper initialization of ProbabilityOfImprovement"""
        pi = ProbabilityOfImprovement(xi=0.5)
        assert pi.xi == 0.5

        # Test default value
        pi_default = ProbabilityOfImprovement()
        assert pi_default.xi == 0.1

    def test_evaluation_simple_case(self, acquisition_function, mock_model):
        """Test evaluation with simple inputs where sigma > 0"""
        X = np.array([[1.0], [2.0], [3.0]])
        Y_sample = np.array([0.5, 0.3, 0.4])
        
        # Mock model predictions
        mu = np.array([0.2, 0.3, 0.4])
        sigma = np.array([0.1, 0.2, 0.1])
        mock_model.predict.return_value = (mu, sigma)

        result = acquisition_function.evaluation(X, Y_sample, mock_model)

        # Calculate expected values
        mu_sample_opt = 0.3  # min of Y_sample
        Z = (mu_sample_opt - mu - acquisition_function.xi) / sigma
        expected = norm.cdf(Z)

        np.testing.assert_array_almost_equal(result, expected)
        mock_model.predict.assert_called_once_with(X, return_std=True)

    def test_pi_correctness(self, acquisition_function, mock_model):
        """Test PI calculation correctness"""
        X = np.array([[1.0]])
        Y_sample = np.array([1.0])
        
        mu = np.array([0.8])
        sigma = np.array([0.2]) 
        mock_model.predict.return_value = (mu, sigma)
        
        z_score = (1.0 - 0.8 - 0.1) / 0.2
        expected_pi = norm.cdf(z_score)
        
        actual_pi = acquisition_function.evaluation(X, Y_sample, mock_model)
        np.testing.assert_array_almost_equal(actual_pi, expected_pi)

    def test_evaluation_zero_sigma(self, acquisition_function, mock_model):
        """Test evaluation when sigma contains zeros"""
        X = np.array([[1.0], [2.0]])
        Y_sample = np.array([0.5, 0.3])
        
        # Mock model predictions with one zero sigma
        mu = np.array([0.2, 0.3])
        sigma = np.array([0.1, 0.0])
        mock_model.predict.return_value = (mu, sigma)

        result = acquisition_function.evaluation(X, Y_sample, mock_model)

        assert result.shape == mu.shape
        assert result[1] == 0

        Z = (0.3 - mu[0] - acquisition_function.xi) / sigma[0]
        expected_nonzero = norm.cdf(Z)
        assert np.isclose(result[0], expected_nonzero)

    def test_mixed_sigma_values(self, acquisition_function, mock_model):
        """Test with mixed sigma values (zero, small, large)"""
        X = np.array([[1.0], [2.0], [3.0], [4.0]])
        Y_sample = np.array([0.5, 0.3, 0.4, 0.6])
        
        mu = np.array([0.2, 0.3, 0.4, 0.5])
        sigma = np.array([0.0, 1e-10, 1.0, 1e5])
        mock_model.predict.return_value = (mu, sigma)

        result = acquisition_function.evaluation(X, Y_sample, mock_model)
        assert result.shape == (4,)
        assert result[0] == 0  # Zero sigma should give zero probability
        assert np.all((0 <= result) & (result <= 1))

    def test_multidimensional_input(self, acquisition_function, mock_model):
        """Test with multi-dimensional input features"""
        X = np.array([[1.0, 2.0], [2.0, 3.0], [3.0, 4.0]])  # 2D features
        Y_sample = np.array([0.5, 0.3, 0.4])
        
        mu = np.array([0.2, 0.3, 0.4])
        sigma = np.array([0.1, 0.2, 0.1])
        mock_model.predict.return_value = (mu, sigma)
        
        result = acquisition_function.evaluation(X, Y_sample, mock_model)
        assert result.shape == (3,)


