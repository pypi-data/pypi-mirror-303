import pytest
import numpy as np
from scipy.stats import norm
from unittest.mock import Mock
from scaleup_bo.acquisition_functions import ExpectedImprovement

class TestExpectedImprovement:
    @pytest.fixture
    def acquisition_function(self):
        # Import here to avoid potential circular imports in test
        return ExpectedImprovement(xi=0.1)

    @pytest.fixture
    def mock_model(self):
        """Fixture to create a mock model"""
        model = Mock()
        return model

    def test_initialization(self):
        """Test proper initialization of ExpectedImprovement"""
        ei = ExpectedImprovement(xi=0.01)
        assert ei.xi == 0.01

        ei_default = ExpectedImprovement()
        assert ei_default.xi == 0.1

    def test_evaluation_simple_case(self, acquisition_function, mock_model):
        """Test evaluation with simple prediction values"""
        X = np.array([[1.0], [2.0], [3.0]])
        Y_sample = np.array([1.0, 0.5, 2.0])
        
        # Mock model predictions
        mu = np.array([0.0, 0.0, 0.0])
        sigma = np.array([1.0, 1.0, 1.0])
        mock_model.predict.return_value = (mu, sigma)
        
        ei = acquisition_function.evaluation(X, Y_sample, mock_model)
        
        # Verify shape
        assert ei.shape == (3,)
        # Verify all values are non-negative
        assert np.all(ei >= 0)
        # Verify model was called correctly
        mock_model.predict.assert_called_once_with(X, return_std=True)

    def test_ei_correctness(self, acquisition_function, mock_model):
        """Test EI calculation correctness"""
        X = np.array([[1.0]])
        Y_sample = np.array([1.0]) 
        
        mu = np.array([0.8])
        sigma = np.array([0.2]) 
        mock_model.predict.return_value = (mu, sigma)
        
        imp = 1.0 - 0.8 - 0.1 
        Z = imp / sigma[0]
        expected_ei = imp * norm.cdf(Z) + sigma[0] * norm.pdf(Z)
        
        actual_ei = acquisition_function.evaluation(X, Y_sample, mock_model)
        np.testing.assert_array_almost_equal(actual_ei, expected_ei)

    def test_evaluation_zero_sigma(self, acquisition_function, mock_model):
        """Test evaluation when sigma is zero"""
        X = np.array([[1.0]])
        Y_sample = np.array([1.0])
        
        # Mock model predictions with zero uncertainty
        mu = np.array([0.0])
        sigma = np.array([0.0])
        mock_model.predict.return_value = (mu, sigma)
        
        ei = acquisition_function.evaluation(X, Y_sample, mock_model)
        
        assert ei[0] == 0.0

    def test_evaluation_improvement(self, acquisition_function, mock_model):
        """Test evaluation when there is clear improvement"""
        X = np.array([[1.0]])
        Y_sample = np.array([1.0])
        
        # Mock model predictions suggesting improvement
        mu = np.array([0.0]) 
        sigma = np.array([0.1])
        mock_model.predict.return_value = (mu, sigma)
        
        ei = acquisition_function.evaluation(X, Y_sample, mock_model)
        
        assert ei[0] > 0.0

    def test_evaluation_no_improvement(self, acquisition_function, mock_model):
        """Test evaluation when there is no improvement"""
        X = np.array([[1.0]])
        Y_sample = np.array([0.0])
        
        # Mock model predictions suggesting no improvement
        mu = np.array([1.0]) 
        sigma = np.array([0.1])
        mock_model.predict.return_value = (mu, sigma)
        
        ei = acquisition_function.evaluation(X, Y_sample, mock_model)
        
        assert ei[0] < 0.1

    def test_evaluation_batch_input(self, acquisition_function, mock_model):
        """Test evaluation with batch input"""
        X = np.random.rand(10, 2) 
        Y_sample = np.random.rand(5) 
        
        mu = np.random.rand(10)
        sigma = np.abs(np.random.rand(10))
        mock_model.predict.return_value = (mu, sigma)
        
        ei = acquisition_function.evaluation(X, Y_sample, mock_model)
        
        assert ei.shape == (10,)
        assert np.all(ei >= 0)

    @pytest.mark.parametrize("xi", [0.0, 0.01, 0.1, 1.0])
    def test_different_xi_values(self, mock_model, xi):
        """Test behavior with different xi values"""
        ei = ExpectedImprovement(xi=xi)
        X = np.array([[1.0]])
        Y_sample = np.array([1.0])
        
        mu = np.array([0.5])
        sigma = np.array([0.1])
        mock_model.predict.return_value = (mu, sigma)
        
        result = ei.evaluation(X, Y_sample, mock_model)
        
        assert not np.isnan(result[0])
        assert not np.isinf(result[0])