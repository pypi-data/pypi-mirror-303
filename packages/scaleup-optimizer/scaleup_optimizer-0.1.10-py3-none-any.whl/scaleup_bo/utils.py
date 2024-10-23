import numpy as np
from skopt.space import Real, Integer, Categorical

def initialize_random_samples(n_initial_points, search_space):
    """
    Generate random samples from the specified search space.

    Parameters
    ----------
    n_initial_points : int
        Number of random samples to generate.

    search_space : list
        List of dimensions specifying the search space. Each dimension can be of type:
        
        - `Real`: Continuous space with bounds `low` and `high`.
        - `Integer`: Discrete space with bounds `low` and `high`.
        - `Categorical`: Space defined by a finite set of categories.

        The function handles these types and generates random samples for each.

    """
    X_sample = []
    for dim in search_space:
        if isinstance(dim, Real):
            samples = np.random.uniform(dim.low, dim.high, n_initial_points)
        elif isinstance(dim, Integer):
            samples = np.random.randint(dim.low, dim.high + 1, n_initial_points)
        elif isinstance(dim, Categorical):
            samples = np.random.choice(dim.categories, n_initial_points)
        else:
            raise ValueError("Unsupported parameter type in search space")
        X_sample.append(samples)

    X_sample = np.array(X_sample, dtype=object).T  
    return X_sample

def ensure_scalar(y):
    """Ensure the objective function returns a scalar value."""
    if np.isscalar(y):
        return y
    elif np.size(y) == 1:
        return y.item()
    else:
        raise ValueError(f"The user-provided objective function must return a scalar value. Received: {y}")


