import pytest
import numpy as np
from skopt.space import Real, Integer, Categorical
from scaleup_bo.utils import initialize_random_samples, ensure_scalar


def test_initialize_random_samples_real():
    """Test initialization with Real parameters."""
    search_space = [
        Real(low=-5.0, high=5.0),
        Real(low=0.0, high=10.0)
    ]
    n_samples = 10
    
    X = initialize_random_samples(n_samples, search_space)
    
    assert X.shape == (n_samples, len(search_space))
    assert np.all(X[:, 0] >= -5.0) and np.all(X[:, 0] <= 5.0)
    assert np.all(X[:, 1] >= 0.0) and np.all(X[:, 1] <= 10.0)

def test_initialize_random_samples_integer():
    """Test initialization with Integer parameters."""
    search_space = [
        Integer(low=1, high=10),
        Integer(low=-5, high=5)
    ]
    n_samples = 10
    
    X = initialize_random_samples(n_samples, search_space)
    
    assert X.shape == (n_samples, len(search_space))
    assert np.all(X[:, 0] >= 1) and np.all(X[:, 0] <= 10)
    assert np.all(X[:, 1] >= -5) and np.all(X[:, 1] <= 5)
    assert np.all(X[:, 0].astype(int) == X[:, 0]) 

def test_initialize_random_samples_categorical():
    """Test initialization with Categorical parameters."""
    search_space = [
        Categorical(['red', 'green', 'blue']),
        Categorical([True, False])
    ]
    n_samples = 10
    
    X = initialize_random_samples(n_samples, search_space)
    
    assert X.shape == (n_samples, len(search_space))
    assert all(x in ['red', 'green', 'blue'] for x in X[:, 0])
    assert all(x in [True, False] for x in X[:, 1])

def test_initialize_random_samples_mixed():
    """Test initialization with mixed parameter types."""
    search_space = [
        Real(low=-5.0, high=5.0),
        Integer(low=1, high=10),
        Categorical(['red', 'green', 'blue'])
    ]
    n_samples = 10
    
    X = initialize_random_samples(n_samples, search_space)
    
    assert X.shape == (n_samples, len(search_space))
    assert np.all(X[:, 0] >= -5.0) and np.all(X[:, 0] <= 5.0)
    assert np.all(X[:, 1] >= 1) and np.all(X[:, 1] <= 10)
    assert all(x in ['red', 'green', 'blue'] for x in X[:, 2])

def test_initialize_random_samples_invalid_space():
    """Test initialization with invalid search space parameter."""
    search_space = [
        "invalid_parameter"
    ]
    n_samples = 10
    
    with pytest.raises(ValueError, match="Unsupported parameter type in search space"):
        initialize_random_samples(n_samples, search_space)

def test_ensure_scalar_with_scalar():
    """Test ensure_scalar with scalar input."""
    assert ensure_scalar(5.0) == 5.0
    assert ensure_scalar(42) == 42

def test_ensure_scalar_with_single_element_array():
    """Test ensure_scalar with single element numpy array."""
    assert ensure_scalar(np.array([5.0])) == 5.0
    assert ensure_scalar(np.array(42)) == 42

def test_ensure_scalar_with_invalid_input():
    """Test ensure_scalar with invalid input."""
    with pytest.raises(ValueError, match="The user-provided objective function must return a scalar value"):
        ensure_scalar(np.array([1, 2, 3]))

    with pytest.raises(ValueError, match="The user-provided objective function must return a scalar value"):
        ensure_scalar([[1, 2], [3, 4]])