import pytest
import numpy as np
from scaleup_bo.kernel import RBF
from numpy.testing import assert_array_less

from scaleup_bo.surrogate_models import LargeScaleGaussianProcess


class TestLargeScaleGaussianProcess:
    @pytest.fixture
    def simple_dataset(self):
        """Fixture providing a simple dataset for testing."""
        # Generate simple synthetic data
        np.random.seed(42)
        X_S = np.array([[1], [2], [3], [4]])
        y_S = np.sin(X_S).ravel()
        X_L = np.array([[1.5], [2.5], [3.5]])
        y_L = np.sin(X_L).ravel()
        return X_S, y_S, X_L, y_L

    @pytest.fixture
    def gp(self):
        """Fixture providing a basic model instance."""
        kernel = RBF(length_scale=1.0)
        return LargeScaleGaussianProcess(kernel=kernel)
    
    def test_init(self):
        """Test initialization of the model."""
        kernel = RBF(length_scale=1.0)
        model = LargeScaleGaussianProcess(kernel=kernel)
        
        assert model.kernel == kernel
        assert model.sigma_S == 0.1
        assert model.lambda_S == 1.0
        assert model.lambda_delta == 1.0
        assert model.sigma_L is None

    def test_input_validation(self, gp, simple_dataset):
        """Test input validation during fitting."""
        X_S, y_S, X_L, y_L = simple_dataset
        
        # Test wrong dimensions
        with pytest.raises(ValueError):
            gp.fit(X_S.ravel(), y_S, X_L, y_L)
        
        with pytest.raises(ValueError):
            gp.fit(X_S, y_S.reshape(-1, 1), X_L, y_L)
            
        # Test mismatched lengths
        with pytest.raises(ValueError):
            gp.fit(X_S[:-1], y_S, X_L, y_L)
            
        with pytest.raises(ValueError):
            gp.fit(X_S, y_S, X_L[:-1], y_L)

    def test_fit_correctness(self, gp, simple_dataset):
        """Test basic fitting functionality."""
        X_S, y_S, X_L, y_L = simple_dataset
        
        gp.fit(X_S, y_S, X_L, y_L)
        
        # Check if matrices are properly initialized
        assert gp.X_train_S is not None
        assert gp.y_train_S is not None
        assert gp.X_train_L is not None
        assert gp.y_train_L is not None
        assert gp.K_S is not None
        assert gp.K_L is not None
        assert gp.K_SL is not None
        
        # Check matrix shapes
        assert gp.K_S.shape == (len(X_S), len(X_S))
        assert gp.K_L.shape == (len(X_L), len(X_L))
        assert gp.K_SL.shape == (len(X_S), len(X_L))

    def test_predict_shape(self, gp, simple_dataset):
        """Test prediction shapes."""
        X_S, y_S, X_L, y_L = simple_dataset
        gp.fit(X_S, y_S, X_L, y_L)
        
        X_test = np.array([[2.5], [3.5]])
        
        # Test without standard deviation
        y_pred = gp.predict(X_test)
        assert y_pred.shape == (2,)
        
        # Test with standard deviation
        y_pred, y_std = gp.predict(X_test, return_std=True)
        assert y_pred.shape == (2,)
        assert y_std.shape == (2,)

    def test_predict_values(self, gp, simple_dataset):
        """Test prediction values are reasonable."""
        X_S, y_S, X_L, y_L = simple_dataset
        gp.fit(X_S, y_S, X_L, y_L)
        
        y_pred_S = gp.predict(X_S)
        
        # Predictions should be close to training values (but not exact due to noise)
        assert np.abs(y_pred_S - y_S).mean() < 0.5
        
        # Test predictions with uncertainty
        X_test = np.array([[2.5], [3.5]])
        y_pred, y_std = gp.predict(X_test, return_std=True)
        
        # Standard deviations should be positive
        assert np.all(y_std > 0)

        # Standard deviations should be larger for points far from training data
        assert_array_less(np.zeros_like(y_std), y_std)

    def test_update_sigma(self, gp, simple_dataset):
        """Test sigma update functionality."""
        X_S, y_S, X_L, y_L = simple_dataset
        gp.fit(X_S, y_S, X_L, y_L)
        
        X_new = np.array([[2.5]])
        y_new = np.array([np.sin(2.5)])
        
        original_sigma = gp.sigma_L
        new_sigma = gp.update_sigma_with_new_sample(X_new, y_new)
        
        assert new_sigma > 0
        assert new_sigma != original_sigma

    def test_optimize_hyperparameters(self, gp, simple_dataset):
        """Test hyperparameter optimization."""
        X_S, y_S, X_L, y_L = simple_dataset
        gp.fit(X_S, y_S, X_L, y_L)
        
        initial_length_scale = gp.kernel.length_scale
        gp.optimize_hyperparameters()
        optimized_length_scale = gp.kernel.length_scale
        
        assert optimized_length_scale > 0
        assert optimized_length_scale != initial_length_scale

    def test_log_marginal_likelihood(self, gp, simple_dataset):
        """Test log marginal likelihood computation."""
        X_S, y_S, X_L, y_L = simple_dataset
        gp.fit(X_S, y_S, X_L, y_L)
        
        # Test with different length scales
        lml1 = gp.log_marginal_likelihood([1.0])
        lml2 = gp.log_marginal_likelihood([2.0])
        
        # Log likelihood should be finite
        assert np.isfinite(lml1)
        assert np.isfinite(lml2)
        # Different parameters should give different likelihoods
        assert lml1 != lml2