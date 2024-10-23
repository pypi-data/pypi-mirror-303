# result.py

class AdtributorResult:
    def __init__(self, root_cause, impact, sep = ","):
        """
        root_cause: a group of dimension and specific values
        impact: the impact of the root cause
        sep: separator for root_cause
        """
        self.root_cause = root_cause
        self.impact = impact
        self.sep = sep
        self.n_factors = len(root_cause.split(self.sep))
