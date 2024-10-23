# ruff: noqa: F401 ignore unused imports, they are imported to check if they are available
from __future__ import annotations

from typing import NoReturn

try:
    import dimod
    import dwave
    import pyqubo
    import qiskit
    import qiskit_optimization
except ImportError:
    print("QUBO extra is not enabled.")
    QUBO_EXTRA_ENABLED = False
else:
    print("QUBO extra is enabled.")
    QUBO_EXTRA_ENABLED = True


def raise_qubo_extras_error() -> NoReturn:
    error_message = "The qubo extra is not enabled. Please install via 'pip install quantagonia[qubo]'."
    raise ImportError(error_message)
