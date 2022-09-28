from numpy import exp, sqrt, log
from scipy.stats import norm
from scipy.optimize import brentq

def bs(sigma, S, K, tau = 1.0, r = 1.75*0.01, call = True):
    """
    Returns the price of a european (call) option under Black-Scholes
    
    Parameters:
    sigma (float): volatility
    S (float): current price of underlying
    K (float): strike price
    tau (float): time until expiry (in years)
    r (float): risk-free rate (over one year)
    call (bool): true if call option, false if a put option

    Returns:
    C (float): price of the call option
    OR
    P (float): price of the put option
    """
    d_1 = (1/(sigma*sqrt(tau))*( log(S/K) +(r + 0.5*sigma**2)*tau))
    d_2 = d_1 - sigma*sqrt(tau)
    N_1 = norm.cdf(d_1)
    N_2 = norm.cdf(d_2)
    C = S*N_1 - exp(-r)*N_2*K
    if call:
        return C
    if not call:
        P = C - S + K*exp(-r*tau)
        return P

def solve_impl_vol(price, S, K, tau = 1.0 ,r = 1.75*0.01, call = True):
    """
    Gives the volatility needed to obtain a given european call option price with
    given strike pirce, price of underlying, time until expiry, and risk-free rate

    Parameters:
    price (float): price of the (call)option
    S (float): current price of underlying
    K (float): strike price
    tau (float): time until expiry (in years)
    r (float): risk-free rate (over one year)

    Returns:
    sigma (float): implied volatility
    
    """
    if not call:
        C = price + S - K*exp(-r*tau)
    def f(sigma):
        return bs(sigma, S,K, tau, r = 1.75*0.01) - C

    sigma = brentq(f, 2**(-5) , 2**2)
    return sigma
        
    

