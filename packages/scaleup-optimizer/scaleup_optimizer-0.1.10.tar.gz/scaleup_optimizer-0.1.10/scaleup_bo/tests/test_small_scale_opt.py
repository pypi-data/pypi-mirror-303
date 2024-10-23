import pytest
import numpy as np
from scipy.optimize import rosen
from scaleup_bo.kernel import RBF
from scaleup_bo.optimizers import SmallScaleBayesianOptimizer
from scaleup_bo.surrogate_models import SmallScaleGaussianProcess
from skopt.space import Real, Integer, Categorical

class TestSmallScaleBayesianOptimizer:
    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup common test fixtures"""
        self.simple_search_space = [Real(-5, 5), Integer(1, 10)]
        self.n_steps = 10
        self.n_initial_points = 1
        
        # Simple quadratic objective function
        self.objective_func = lambda x: float(np.sum(np.array(x) ** 2))
        
        # Default optimizer
        self.optimizer = self._create_optimizer()

    def _create_optimizer(self, **kwargs):
        """Helper method to create optimizer with custom parameters"""
        default_params = {
            'objective_func': self.objective_func,
            'search_space': self.simple_search_space,
            'n_steps': self.n_steps,
            'n_initial_points': self.n_initial_points
        }
        default_params.update(kwargs)
        return SmallScaleBayesianOptimizer(**default_params)

    def test_initialization(self):
        """Test correct initialization of optimizer"""
        assert self.optimizer.objective_func is not None
        assert self.optimizer.search_space == self.simple_search_space
        assert self.optimizer.acq_func_type == 'EI'  # default value
        assert self.optimizer.n_steps == self.n_steps
        assert self.optimizer.n_initial_points == self.n_initial_points
        assert self.optimizer.gp is not None
        assert isinstance(self.optimizer.best_score, float)
        assert self.optimizer.X_iters is not None
        assert self.optimizer.Y_iters is not None
        assert len(self.optimizer.X_iters) == self.n_steps + self.n_initial_points

    @pytest.mark.parametrize("acq_func", ['EI', 'PI', 'UCB'])
    def test_acquisition_functions(self, acq_func):
        """Test different acquisition functions"""
        optimizer = self._create_optimizer(acq_func=acq_func)
        
        assert optimizer.acq_func_type == acq_func
        assert optimizer.best_score is not None
        assert len(optimizer.X_iters) > 0
        assert len(optimizer.Y_iters) > 0

    def test_invalid_acquisition_function(self):
        """Test invalid acquisition function raises error"""
        with pytest.raises(ValueError):
            self._create_optimizer(acq_func='INVALID')

    def test_optimization_improvement(self):
        """Test if optimization improves the solution"""
        optimizer = self._create_optimizer(
            n_steps=20,
            n_initial_points=5
        )
        
        # Initial points
        initial_points = optimizer.Y_iters[:5]
        initial_best = np.min(initial_points)
        
        # Final result
        final_best = optimizer.best_score
        
        # Assert improvement
        assert final_best <= initial_best
        assert optimizer.best_params is not None
        assert len(optimizer.best_params) == len(self.simple_search_space)

    def test_custom_gp_model(self):
        """Test optimizer with custom GP model"""
        custom_gp = SmallScaleGaussianProcess(
            kernel=RBF(1.0, (1e-5, 10)),
            alpha=0.1
        )
        
        optimizer = self._create_optimizer(gp=custom_gp)
        assert optimizer.gp == custom_gp
        assert optimizer.best_score is not None

    @pytest.mark.parametrize("n_dims", [1, 2, 5])
    def test_dimensionality(self, n_dims):
        """Test different input dimensions"""
        search_space = [Real(-5, 5)] * n_dims
        optimizer = self._create_optimizer(search_space=search_space)
        
        assert len(optimizer.best_params) == n_dims
        assert optimizer.X_iters.shape[1] == n_dims
        assert len(optimizer.Y_iters) == self.n_steps + self.n_initial_points

    def test_single_step_optimization(self):
        """Test single step optimization"""
        optimizer = self._create_optimizer(
            n_steps=1,
            n_initial_points=1
        )
        
        assert len(optimizer.Y_iters) == 2  # Initial point + 1 step
        assert optimizer.best_score is not None
        assert len(optimizer.best_params) == len(self.simple_search_space)

    def test_high_dimensional(self):
        """Test high-dimensional optimization"""
        n_dims = 10
        search_space = [Real(-5, 5)] * n_dims
        
        optimizer = self._create_optimizer(
            search_space=search_space,
            n_steps=20,
            n_initial_points=5
        )
        
        assert len(optimizer.best_params) == n_dims
        assert optimizer.best_score is not None
        assert optimizer.X_iters.shape[1] == n_dims

    def test_numerical_stability(self):
        """Test numerical stability with small values"""
        small_scale_func = lambda x: float(np.sum(np.array(x) ** 2)) * 1e-10
        
        optimizer = self._create_optimizer(objective_func=small_scale_func)
        
        assert not np.isnan(optimizer.best_score)
        assert not np.isinf(optimizer.best_score)
        assert all(not np.isnan(x) for x in optimizer.best_params)
        assert all(not np.isinf(x) for x in optimizer.best_params)

    def test_propose_next_point(self):
        """Test the point proposal mechanism"""
        next_point = self.optimizer.propose_next_point()
        
        assert isinstance(next_point, np.ndarray)
        assert len(next_point) == len(self.simple_search_space)
        assert all(0 <= x <= 1 for x in next_point)  # Should be normalized

    @pytest.mark.parametrize("invalid_steps", [-1, 0])
    def test_invalid_steps(self, invalid_steps):
        """Test invalid number of steps"""
        with pytest.raises(ValueError):
            self._create_optimizer(n_steps=invalid_steps)

    @pytest.mark.parametrize("invalid_points", [-1, 0])
    def test_invalid_initial_points(self, invalid_points):
        """Test invalid number of initial points"""
        with pytest.raises(ValueError):
            self._create_optimizer(n_initial_points=invalid_points)