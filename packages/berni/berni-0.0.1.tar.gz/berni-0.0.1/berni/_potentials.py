from math import exp, log

__all__ = ['inverse_power', 'sum_inverse_power', 'yukawa', 'lennard_jones', 'fene', 'gaussian', 'harmonic']

def inverse_power(r, epsilon=1.0, sigma=1.0, exponent=12):
    return \
        epsilon*(sigma/r)**exponent, \
        epsilon*exponent*(sigma/r)**exponent/r**2, \
        (-epsilon*exponent**2*(sigma/r)**exponent/r**2 - epsilon*exponent*(sigma/r)**exponent/r**2)/r

def sum_inverse_power(r, epsilon=(1.0, ), sigma=(1.0, ), exponent=(12, )):
    return 0.0, 0.0, 0.0

def yukawa(r, epsilon=1.0, kappa=1.0, sigma=1.0):
    return \
        epsilon*exp(kappa*(-r + sigma))/(kappa*r), \
        epsilon*(kappa*r + 1)*exp(-kappa*(r - sigma))/(kappa*r**3), \
        epsilon*(-kappa**2*r**2 - 2*kappa*r - 2)*exp(-kappa*(r - sigma))/(kappa*r**4)

def lennard_jones(r, epsilon=1.0, sigma=1.0):
    return \
        4*epsilon*(-sigma**6/r**6 + sigma**12/r**12), \
        -4*epsilon*(6*sigma**6/r**7 - 12*sigma**12/r**13)/r, \
        -4*epsilon*(-42*sigma**6/r**8 + 156*sigma**12/r**14)/r

def fene(r, epsilon=1.0, kappa=1.0, R=1.0, sigma=1.0):
    u = -R**2*kappa*log(-r**2/sigma**2 + 1)
    w = 2*R**2*kappa/(r**2 - sigma**2)
    h = 2*R**2*kappa*(-r**2 - sigma**2)/(r*(r**2 - sigma**2)**2)
    if (r**2 < 2**(1./6)):
        u += 4*epsilon*(-sigma**6/r**6 + sigma**12/r**12) + epsilon
        w += 24*epsilon*sigma**6*(-r**6 + 2*sigma**6)/r**14
        h += 24*epsilon*sigma**6*(7*r**6 - 26*sigma**6)/r**15
    return u, w, h

def gaussian(r, epsilon=1.0, sigma=1.0):
    return \
        epsilon*exp(-r**2/sigma**2), \
        2*epsilon*exp(-r**2/sigma**2)/sigma**2, \
        2*epsilon*(-2*r**2 + sigma**2)*exp(-r**2/sigma**2)/(r*sigma**4)
    return 0.0

def harmonic(r, epsilon=1.0, sigma=1.0):
    return \
        0.5*epsilon*(-r/sigma + 1)**2, \
        1.0*epsilon*(-r + sigma)/(r*sigma**2), \
        -1.0*epsilon/(r*sigma**2)
