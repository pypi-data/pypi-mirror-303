import pytest
import numpy as np
from numpy.testing import assert_array_almost_equal
from scipy.optimize import rosen
from skopt.space import Real, Integer
from scaleup_bo.kernel import RBF
from skopt.space import Real, Integer, Categorical

from scaleup_bo.surrogate_models import LargeScaleGaussianProcess
from scaleup_bo.optimizers import LargeScaleBayesianOptimizer

class TestLargeScaleBayesianOptimizer:
    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup common test fixtures"""
        # Define search space
        self.simple_search_space = [Real(-5, 5), Integer(1, 10)]
        self.n_steps = 10
        
        # Simple quadratic objective function
        self.objective_func = lambda x: float(np.sum(np.array(x) ** 2))
        
        # Generate sample experimental data
        self.X_iters_small = np.array([
            [-2, 3],
            [0, 5],
            [2, 7]
        ])
        self.Y_iters_small = np.array([self.objective_func(x) for x in self.X_iters_small])
        
        # Best parameters from small-scale
        self.best_params = [0, 5]  # Example best params
        
        # Default optimizer
        self.optimizer = self._create_optimizer()

    def _create_optimizer(self, **kwargs):
        """Helper method to create optimizer with custom parameters"""
        default_params = {
            'objective_func': self.objective_func,
            'search_space': self.simple_search_space,
            'best_params': self.best_params,
            'X_iters_small': self.X_iters_small,
            'Y_iters_small': self.Y_iters_small,
            'n_steps': self.n_steps
        }
        default_params.update(kwargs)
        return LargeScaleBayesianOptimizer(**default_params)

    def test_initialization(self):
        """Test correct initialization of optimizer"""
        assert callable(self.optimizer.objective_funcL)
        assert self.optimizer.search_space == self.simple_search_space
        assert self.optimizer.acq_func_type == 'EI'  # default value
        assert self.optimizer.n_steps == self.n_steps
        assert self.optimizer.gpL is not None
        assert isinstance(self.optimizer.best_score, float)
        assert np.array_equal(self.optimizer.X_iters_small, self.X_iters_small)
        assert np.array_equal(self.optimizer.Y_iters_small, self.Y_iters_small)
        assert np.array_equal(self.optimizer.best_params_S, self.best_params)

    @pytest.mark.parametrize("acq_func", ['EI', 'PI', 'UCB'])
    def test_acquisition_functions(self, acq_func):
        """Test different acquisition functions"""
        optimizer = self._create_optimizer(acq_func=acq_func)
        
        assert optimizer.acq_func_type == acq_func
        assert optimizer.best_score is not None
        assert len(optimizer.X_iters) > 0
        assert len(optimizer.Y_iters) > 0

    def test_custom_gp_model(self):
        """Test optimizer with custom GP model"""
        custom_gp = LargeScaleGaussianProcess(
            kernel=RBF(1.0, (1e-5, 10))
        )
        
        optimizer = self._create_optimizer(gpL=custom_gp)
        
        # Compare GP model attributes
        assert isinstance(optimizer.gpL, LargeScaleGaussianProcess)
        assert optimizer.gpL == custom_gp
        
        # Check if optimization still works
        assert optimizer.best_score is not None
        assert optimizer.best_params is not None

    def test_single_step_optimization(self):
        """Test single step optimization"""
        optimizer = self._create_optimizer(n_steps=1)
        
        assert len(optimizer.Y_iters) == 2  # Initial point + 1 step
        assert optimizer.best_score is not None
        assert len(optimizer.best_params) == len(self.simple_search_space)
        assert optimizer.X_iters.shape == (2, len(self.simple_search_space))

    def test_high_dimensional(self):
        """Test high-dimensional optimization"""
        n_dims = 10
        search_space = [Real(-5, 5)] * n_dims
        
        # Create appropriate high-dimensional experimental data
        X_small = np.random.uniform(-5, 5, (5, n_dims))
        Y_small = np.array([self.objective_func(x) for x in X_small])
        best_params = np.zeros(n_dims)
        
        optimizer = self._create_optimizer(
            search_space=search_space,
            X_iters_small=X_small,
            Y_iters_small=Y_small,
            best_params=best_params,
            n_steps=20
        )
        
        assert len(optimizer.best_params) == n_dims
        assert optimizer.best_score is not None
        assert optimizer.X_iters.shape[1] == n_dims
        assert optimizer.X_iters.shape[0] == optimizer.n_steps + 1  # Initial point + n_steps

    def test_propose_next_point(self):
        """Test the point proposal mechanism"""
        next_point = self.optimizer.propose_next_point()
        
        assert isinstance(next_point, np.ndarray)
        assert len(next_point) == len(self.simple_search_space)
        assert all(0 <= x <= 1 for x in next_point)  # Should be normalized

    def test_model_updates(self):
        """Test if the model properly updates during optimization"""
        optimizer = self._create_optimizer(n_steps=5)
        
        # Check if iterations were performed
        assert len(optimizer.X_iters) == 6  # initial point + 5 steps
        assert len(optimizer.Y_iters) == 6
        
        # Check if values are properly stored
        assert isinstance(optimizer.X_iters, np.ndarray)
        assert isinstance(optimizer.Y_iters, np.ndarray)
        assert all(isinstance(x, (int, float)) for x in optimizer.best_params)

    @pytest.mark.parametrize("invalid_steps", [-1, 0])
    def test_invalid_steps(self, invalid_steps):
        """Test invalid number of steps"""
        with pytest.raises(ValueError):
            self._create_optimizer(n_steps=invalid_steps)
