import pytest
import numpy as np
from scaleup_bo.kernel import RBF
from numpy.testing import assert_array_almost_equal, assert_array_less

from scaleup_bo.surrogate_models import SmallScaleGaussianProcess

class TestSmallScaleGaussianProcess:
    @pytest.fixture
    def simple_dataset(self):
        """Fixture to create a simple dataset for testing"""
        np.random.seed(42)
        X = np.random.randn(10, 2)
        y = np.sin(X[:, 0]) + np.cos(X[:, 1])
        return X, y

    @pytest.fixture
    def gp(self):
        """Fixture to create a basic GP instance"""
        kernel = RBF(length_scale=1.0)
        return SmallScaleGaussianProcess(kernel=kernel, alpha=0.1)
    
    def test_initialization(self, gp):
        """Test if the GP is initialized correctly"""
        assert gp.alpha == 0.1
        assert isinstance(gp.kernel, RBF)
        assert gp.X_train is None
        assert gp.y_train is None

    def test_fit_invalid_input_dimensions(self, gp):
        """Test if fit method raises appropriate errors for invalid inputs"""
        with pytest.raises(ValueError, match="X_train must be a 2D array"):
            gp.fit(np.array([1, 2, 3]), np.array([1, 2, 3]))

        with pytest.raises(ValueError, match="y_train must be a 1D array"):
            gp.fit(np.random.randn(3, 2), np.random.randn(3, 1))

        with pytest.raises(ValueError, match="Number of samples in X_train and y_train must be equal"):
            gp.fit(np.random.randn(3, 2), np.random.randn(4))

    def test_fit_correctness(self, gp, simple_dataset):
        """Test if fit method works correctly with valid inputs"""
        X, y = simple_dataset
        gp.fit(X, y)
        
        assert gp.X_train is not None
        assert gp.y_train is not None
        assert hasattr(gp, 'L')
        assert hasattr(gp, 'alpha_')
        assert gp.K.shape == (len(X), len(X))

    def test_predict_mean_shape(self, gp, simple_dataset):
        """Test if predict returns correct shapes"""
        X, y = simple_dataset
        gp.fit(X, y)
        
        X_test = np.random.randn(5, 2)
        y_pred = gp.predict(X_test)
        
        assert y_pred.shape == (5,)

    def test_predict_with_std(self, gp, simple_dataset):
        """Test if predict returns both mean and std with correct shapes"""
        X, y = simple_dataset
        gp.fit(X, y)
        
        X_test = np.random.randn(5, 2)
        y_pred, y_std = gp.predict(X_test, return_std=True)
        
        assert y_pred.shape == (5,)
        assert y_std.shape == (5,)
        assert_array_less(0, y_std)  # Standard deviations should be positive

    def test_log_marginal_likelihood(self, gp, simple_dataset):
        """Test if log marginal likelihood computation works"""
        X, y = simple_dataset
        gp.fit(X, y)
        
        # Test with initial length scale
        lml = gp.log_marginal_likelihood([1.0])
        assert isinstance(lml, float)

        # Log likelihood should be finite
        assert np.isfinite(lml)

    def test_optimize_hyperparameters(self, gp, simple_dataset):
        """Test if hyperparameter optimization works"""
        X, y = simple_dataset
        gp.fit(X, y)
        
        initial_length_scale = gp.kernel.length_scale
        gp.optimize_hyperparameters()
        optimized_length_scale = gp.kernel.length_scale
        
        assert optimized_length_scale > 0
        assert optimized_length_scale != initial_length_scale

    def test_prediction_consistency(self, gp, simple_dataset):
        """Test if predictions are consistent with training data"""
        X, y = simple_dataset
        gp.fit(X, y)
        
        # Predict at training points
        y_pred = gp.predict(X)
        
        # Due to noise (alpha), predictions won't be exact but should be close
        assert_array_almost_equal(y_pred, y, decimal=1)