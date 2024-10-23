import pytest
import numpy as np
from numpy.testing import assert_array_almost_equal, assert_array_equal
from scaleup_bo.kernel import RBF

@pytest.fixture
def rbf_kernel():
    """Fixture to create a default RBF kernel instance."""
    return RBF(length_scale=1.0)

def test_rbf_init():
    """Test RBF kernel initialization with different parameters."""
    # Test default initialization
    rbf = RBF()
    assert rbf.length_scale == 1.0
    assert rbf.length_scale_bounds == (1e-5, 10)
    
    # Test custom initialization
    rbf = RBF(length_scale=2.0, length_scale_bounds=(1e-3, 100))
    assert rbf.length_scale == 2.0
    assert rbf.length_scale_bounds == (1e-3, 100)

def test_rbf_single_point():
    """Test RBF kernel computation for single points."""
    rbf = RBF(length_scale=1.0)
    X = np.array([[1.0]])
    
    # Test self-kernel
    K = rbf(X)
    assert_array_almost_equal(K, np.array([[1.0]]))
    
    # Test with another point
    Y = np.array([[2.0]])
    K = rbf(X, Y)
    expected = np.exp(-0.5 * (1.0) ** 2)
    assert_array_almost_equal(K, np.array([[expected]]))

def test_rbf_1d_array():
    """Test RBF kernel computation for 1D arrays."""
    rbf = RBF(length_scale=1.0)
    X = np.array([[1.0], [2.0], [3.0]])
    
    # Test self-kernel
    K = rbf(X)
    expected = np.exp(-0.5 * np.array([
        [0.0, 1.0, 4.0],
        [1.0, 0.0, 1.0],
        [4.0, 1.0, 0.0]
    ]))
    assert_array_almost_equal(K, expected)

def test_rbf_2d_array():
    """Test RBF kernel computation for 2D arrays."""
    rbf = RBF(length_scale=2.0)
    X = np.array([[1.0, 1.0], [2.0, 2.0]])
    Y = np.array([[1.0, 1.0], [2.0, 2.0], [3.0, 3.0]])
    
    K = rbf(X, Y)
    # Calculate expected distances manually
    dists = np.array([
        [0.0, 2.0, 8.0],
        [2.0, 0.0, 2.0]
    ])
    expected = np.exp(-0.5 * dists / 4.0)  # length_scale=2.0, so divide by 4
    assert_array_almost_equal(K, expected)
    assert K.shape == (2, 3)

def test_rbf_different_scales():
    """Test RBF kernel with different length scales."""
    X = np.array([[1.0], [2.0]])
    
    # Test with small length scale
    rbf_small = RBF(length_scale=0.1)
    K_small = rbf_small(X)
    
    # Test with large length scale
    rbf_large = RBF(length_scale=10.0)
    K_large = rbf_large(X)

    assert_array_almost_equal(np.diag(K_small), np.ones(2))
    assert_array_almost_equal(np.diag(K_large), np.ones(2))
    off_diag_mask = ~np.eye(2, dtype=bool)

    # Kernel values should be smaller for smaller length scale
    assert np.all(K_small[off_diag_mask] < K_large[off_diag_mask])


def test_rbf_symmetry():
    """Test symmetry of RBF kernel when X=Y."""
    rbf = RBF()
    X = np.array([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
    
    K = rbf(X)
    assert_array_almost_equal(K, K.T)
    
    # Diagonal elements should all be 1.0
    assert_array_almost_equal(np.diag(K), np.ones(len(X)))

def test_rbf_edge_cases():
    """Test RBF kernel edge cases."""
    rbf = RBF()
    
    # Test with empty arrays
    X_empty = np.array([]).reshape(0, 1)
    K = rbf(X_empty)
    assert K.shape == (0, 0)
    
    # Test with zero vectors
    X_zero = np.zeros((3, 2))
    K = rbf(X_zero)
    assert_array_equal(K, np.ones((3, 3)))
    
    # Test with very large distances
    X_large = np.array([[1e5], [-1e5]])
    K = rbf(X_large)
    assert np.all(K[~np.eye(2, dtype=bool)] < 1e-10)