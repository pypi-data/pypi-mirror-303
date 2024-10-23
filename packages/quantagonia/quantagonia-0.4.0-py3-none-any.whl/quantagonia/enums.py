from enum import Enum


class HybridSolverOptSenses(Enum):
    """An enumeration class representing the optimization senses for the hybrid solver.

    Attributes:
    ----------
        MAXIMIZE: Holds a string representing maximization.
        MINIMIZE: Holds a string representing minimization.

    """

    MAXIMIZE = "MAXIMIZE"
    MINIMIZE = "MINIMIZE"


class HybridSolverProblemType(str, Enum):
    MIP = "MIP"
    QUBO = "QUBO"
