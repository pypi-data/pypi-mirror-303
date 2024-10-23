import math
import numpy as np
import scipy.stats as stats


def safe_div(a, b):
    if a == 0 and b == 0:
        return 0
    if b == 0:
        return 1
    return a / b

# z-test
def get_pvalue( mean1, mean2, std1, std2, n1, n2):
    se = np.sqrt((std1/np.sqrt(n1))**2 + (std2/np.sqrt(n2))**2)
    z = (mean1 - mean2) / se
    p = 2 * (1 - stats.norm.cdf(abs(z)))
    return p
