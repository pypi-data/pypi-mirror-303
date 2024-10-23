import pytest
import numpy as np
from unittest.mock import Mock, patch
from scaleup_bo.acquisition_functions import UpperConfidenceBound

class TestUpperConfidenceBound:
    @pytest.fixture
    def ucb_function(self):
        """Fixture to create a default UCB instance"""
        return UpperConfidenceBound()

    @pytest.fixture
    def custom_ucb_function(self):
        """Fixture to create a UCB instance with custom kappa"""
        return UpperConfidenceBound(kappa=3.0)

    @pytest.fixture
    def mock_model(self):
        """Fixture to create a mock model with predict method"""
        model = Mock()
        return model

    def test_init_default_kappa(self, ucb_function):
        """Test initialization with default kappa value"""
        assert ucb_function.kappa == 2.0
    
    def test_ucb_correctness(self, ucb_function, mock_model):
        """Test UCB calculation correctness"""
        X = np.array([[1.0]])
        Y_sample = np.array([0.5])
        
        mu = np.array([2.5])
        sigma = np.array([0.5])
        mock_model.predict.return_value = (mu, sigma)
        
        expected_ucb = np.array([3.5]) 
        actual_ucb = ucb_function.evaluation(X, Y_sample, mock_model)
        
        np.testing.assert_array_almost_equal(actual_ucb, expected_ucb)

    def test_evaluation_1d(self, ucb_function, mock_model):
        """Test UCB evaluation with 1D input"""
        # Setup test data
        X = np.array([[1.0], [2.0], [3.0]])
        Y_sample = np.array([0.5, 1.0, 1.5])
        
        # Mock model predictions
        mu = np.array([0.1, 0.2, 0.3])
        sigma = np.array([0.01, 0.02, 0.03])
        mock_model.predict.return_value = (mu, sigma)
        
        expected_ucb = mu + ucb_function.kappa * sigma
        
        actual_ucb = ucb_function.evaluation(X, Y_sample, mock_model)
        
        mock_model.predict.assert_called_once_with(X, return_std=True)
        
        np.testing.assert_array_almost_equal(actual_ucb, expected_ucb)

    def test_evaluation_2d(self, ucb_function, mock_model):
        """Test UCB evaluation with 2D input"""
        # Setup test data
        X = np.array([[1.0, 2.0], [2.0, 3.0], [3.0, 4.0]])
        Y_sample = np.array([0.5, 1.0, 1.5])
        
        # Mock model predictions
        mu = np.array([0.1, 0.2, 0.3])
        sigma = np.array([0.01, 0.02, 0.03])
        mock_model.predict.return_value = (mu, sigma)
        
        expected_ucb = mu + ucb_function.kappa * sigma
        
        actual_ucb = ucb_function.evaluation(X, Y_sample, mock_model)
        
        np.testing.assert_array_almost_equal(actual_ucb, expected_ucb)
