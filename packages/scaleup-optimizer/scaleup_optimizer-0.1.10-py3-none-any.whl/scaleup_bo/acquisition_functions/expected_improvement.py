import numpy as np
from scipy.stats import norm
from .base import BaseAcquisitionFunction

class ExpectedImprovement(BaseAcquisitionFunction):
    def __init__(self, xi=0.1):
        self.xi = xi

    def evaluation(self, X, Y_sample, model):
        """
        Computes the Expected Improvement acquisition function.
        """
        mu, sigma = model.predict(X, return_std=True)
        mu_sample_opt = np.min(Y_sample)

        with np.errstate(divide='warn', invalid='ignore'):
            imp = mu_sample_opt - mu - self.xi
            ei = np.zeros_like(imp)  # Initialize ei as zeros
    
            mask = sigma > 0  
            Z = np.zeros_like(imp) 
            Z[mask] = imp[mask] / sigma[mask] 
            
            ei[mask] = imp[mask] * norm.cdf(Z[mask]) + sigma[mask] * norm.pdf(Z[mask])


        return ei
