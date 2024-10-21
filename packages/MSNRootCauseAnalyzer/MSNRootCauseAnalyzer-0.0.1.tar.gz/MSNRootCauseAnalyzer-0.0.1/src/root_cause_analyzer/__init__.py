# Define API for root cause analyzer

from .algorithms.adtributor import Adtributor, RecursiveAdtributor

def get_analyzer(name, top_n_factors=5, verbose=0):
    if name == 'adtributor':
        return Adtributor(top_n_factors, verbose)
    elif name == 'r_adtributor':
        return RecursiveAdtributor(top_n_factors, verbose)
    else:
        raise ValueError(f"Unknown algorithm: {name}, available algorithms: ['adtributor', 'r_adtributor']")