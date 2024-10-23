import pytest
import numpy as np
from skopt.space import Real, Integer, Categorical
from scaleup_bo.scale import Scale

@pytest.fixture
def mixed_search_space():
    return [
        Real(1e-4, 1.0, name='learning_rate'),
        Integer(1, 100, name='num_layers'),
        Categorical(['adam', 'sgd', 'rmsprop'], name='optimizer'),
        Real(0.1, 0.9, name='dropout')
    ]

@pytest.fixture
def numeric_search_space():
    return [
        Real(1e-4, 1.0, name='learning_rate'),
        Real(0.1, 0.9, name='dropout'),
        Integer(1, 10, name='conv_pool_size')
    ]

def test_identify_log_indices():
    space = [
        Real(1e-4, 1.0), 
        Real(0.1, 0.9),  
        Integer(1, 10),
        Categorical(['a', 'b', 'c'])
    ]
    scale = Scale(space)
    assert scale.log_indices == [0]

def test_normalize_mixed_parameters(mixed_search_space):
    scale = Scale(mixed_search_space)
    X = np.array([
        [1e-3, 50, 'adam', 0.5],
        [1e-2, 75, 'sgd', 0.7]
    ])
    
    X_norm = scale.normalize(X)

    assert X_norm.shape == (2, 4)
    
    # Ensure all values are in the scale [0,1]
    assert np.all((X_norm >= 0) & (X_norm <= 1))
    
    # Check categorical encoding
    assert X_norm[0, 2] == 0
    assert X_norm[1, 2] == 0.5  

def test_denormalize_mixed_parameters(mixed_search_space):
    scale = Scale(mixed_search_space)
    X_norm = np.array([
        [0.5, 0.5, 0.0, 0.5],
        [0.7, 0.7, 1.0, 0.7]
    ])
    
    X = scale.denormalize(X_norm)
    
    # Check shape
    assert X.shape == (2, 4)
    
    # Check categorical values are correctly recovered
    assert X[0, 2] == 'adam'
    assert X[1, 2] == 'rmsprop'
    
    # Check integer values are integers
    assert isinstance(X[0, 1], (int, np.integer))
    assert isinstance(X[1, 1], (int, np.integer))

def test_normalize_denormalize_conversion(numeric_search_space):
    scale = Scale(numeric_search_space)
    X_original = np.array([
        [1e-3, 0.5, 5],
        [1e-2, 0.7, 8]
    ])

    X_norm = scale.normalize(X_original)
    X_denorm = scale.denormalize(X_norm).astype(float)

    # Check numerical values are close to original
    np.testing.assert_allclose(X_original[:, :2], X_denorm[:, :2], rtol=1e-10)
    # Check integers are exactly equal
    np.testing.assert_array_equal(X_original[:, 2], X_denorm[:, 2])

def test_edge_cases(mixed_search_space):
    scale = Scale(mixed_search_space)
    
    # Test with min values
    X_min = np.array([[1e-4, 1, 'adam', 0.1]], dtype=object)
    X_norm = scale.normalize(X_min)
    assert np.allclose(X_norm[0, :2], [0, 0])
    
    # Test with max values
    X_max = np.array([[1.0, 100, 'rmsprop', 0.9]], dtype=object)
    X_norm = scale.normalize(X_max)
    assert np.allclose(X_norm[0, :2], [1, 1])

def test_invalid_input():
    space = [Real(1e-4, 1.0), Categorical(['a', 'b', 'c'])]
    scale = Scale(space)
    
    # Test with invalid categorical value
    with pytest.raises(ValueError):
        scale.normalize(np.array([[1e-3, 'd']], dtype=object))
    
    # Test with out of bounds numerical value
    with pytest.raises(ValueError):
        scale.normalize(np.array([[2.0, 'a']], dtype=object))