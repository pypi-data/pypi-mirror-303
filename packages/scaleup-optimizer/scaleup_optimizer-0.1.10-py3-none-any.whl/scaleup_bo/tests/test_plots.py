import pytest
import numpy as np
import matplotlib.pyplot as plt
from unittest.mock import Mock, patch

from scaleup_bo.plots import plot_performance, plot_opt_process

@pytest.fixture
def mock_optimizer():
    """Creates a mock optimizer with sample iteration data."""
    optimizer = Mock()
    optimizer.Y_iters = np.array([5.0, 4.0, 3.0, 2.0, 1.0])
    return optimizer

@pytest.fixture
def mock_figure():
    """Creates and returns a new figure for each test."""
    fig = plt.figure()
    yield fig
    plt.close(fig)

def test_plot_performance_creates_correct_plot(mock_optimizer, mock_figure):
    """Test if plot_performance creates a plot with correct data and elements."""
    with patch('matplotlib.pyplot.show'):  # Prevent plot from showing during tests
        plot_performance(mock_optimizer)
        
        # Get the current axis
        ax = plt.gca()
        
        # Test if the plot contains the correct data
        line = ax.get_lines()[0]
        expected_y_data = np.minimum.accumulate(mock_optimizer.Y_iters)
        np.testing.assert_array_equal(line.get_ydata(), expected_y_data)
    

def test_plot_opt_process_creates_correct_plot(mock_optimizer, mock_figure):
    """Test if plot_opt_process creates a plot with correct data and elements."""
    with patch('matplotlib.pyplot.show'):  # Prevent plot from showing during tests
        plot_opt_process(mock_optimizer)
        
        # Get the current axis
        ax = plt.gca()
        
        # Test if the plot contains the correct data
        line = ax.get_lines()[0]
        np.testing.assert_array_equal(line.get_ydata(), mock_optimizer.Y_iters)
        