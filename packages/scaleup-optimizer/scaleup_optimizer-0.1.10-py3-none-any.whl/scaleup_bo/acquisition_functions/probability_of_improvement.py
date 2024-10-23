import numpy as np
from scipy.stats import norm
from .base import BaseAcquisitionFunction

class ProbabilityOfImprovement(BaseAcquisitionFunction):
    def __init__(self, xi=0.1):
        self.xi = xi

    def evaluation(self, X, Y_sample, model):
        """
        Computes probability of improvement acquisition function.
        """
        mu, sigma = model.predict(X, return_std=True)
        mu_sample_opt = np.min(Y_sample)

        with np.errstate(divide='warn', invalid='ignore'):
            Z = np.zeros_like(mu) # Initialize Z as zeros
            mask = sigma > 0
            Z[mask] = (mu_sample_opt - mu[mask] - self.xi) / sigma[mask]

            pi = np.zeros_like(mu)
            pi[mask] = norm.cdf(Z[mask])

        return pi