import numpy as np
import matplotlib.pyplot as plt

def plot_performance(optimizer):
    """Plots the minimum objective function value achieved over iterations.
    
    Args:
        optimizer: Optimizer object with Y_iters attribute containing objective func values.
        
    The plot shows the convergence of the optimization process by tracking the
    minimum value found up to each iteration.
    """
    min_f = np.minimum.accumulate(optimizer.Y_iters)

    plt.plot(min_f, marker='o', label='f(x)')
    plt.xlabel('Number of steps (n)')
    plt.ylabel('min f(x) after n steps')
    plt.title('Performance Improvement Over Iteration')
    plt.grid(True)
    plt.legend()
    plt.show()

def plot_opt_process(optimizer):
    """Plots the optimization process by showing objective function values over iterations.
    
    Args:
        optimizer: Optimizer object with Y_iters attribute containing objective func values.
        
    The plot visualizes how the objective function values change across optimization steps.
    """
    plt.plot(optimizer.Y_iters, marker='o', label='f(x)')
    plt.xlabel('Number of steps (n)')
    plt.ylabel('f(x) after n steps')
    plt.title('Optimization Process')
    plt.grid(True)
    plt.legend()
    plt.show()