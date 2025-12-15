# GitHub Copilot Instructions for dp_ucph

This codebase contains teaching materials and research code for "Dynamic Programming and Structural Econometrics". It mixes Python (Jupyter Notebooks, JAX/NumPy) and MATLAB.

## Project Structure

- **Topic-based Organization**: Folders are numbered by topic (e.g., `1_theory_tools`, `2_dynamic_discrete_choice`).
- **Python Core**: `1_theory_tools/lib/` contains shared Python utilities (`dpsolver.py`, `integrate.py`, `optimize.py`).
- **MATLAB Core**: `2_dynamic_discrete_choice/zurcher_matlab/` and `eqb_matlab/` contain structural estimation code.
- **Notebooks**: Used extensively for teaching and examples (e.g., `*.ipynb`).

## Python Development

### Core Libraries
- **NumPy & JAX**: The project supports both. `dpsolver.py` uses NumPy, while `dpsolver_jax.py` uses JAX for hardware acceleration/autodiff.
- **SciPy**: Used for statistics (`scipy.stats`) and some optimization.

### Solver Pattern (`dpsolver`)
The `dpsolver` class (in both NumPy and JAX versions) implements generic Dynamic Programming algorithms.
- **Interface**: Solvers expect a `model` object.
- **Model Requirements**:
  - `model.bellman(V)`: Returns updated value function and policy.
  - `model.n_x`: Number of state points.
  - `model.n_choices`: Number of choices.
  - `model.x`: State grid.
- **Usage Example**:
  ```python
  from lib.dpsolver import dpsolver
  V, policy = dpsolver.vfi(model, maxiter=1000, tol=1e-6)
  ```

### Integration & Optimization
- **Integration**: Use `lib.integrate.quad_xw` for generating quadrature weights and nodes.
- **Optimization**: `lib.optimize.newton` implements Newton's method with optional derivative support.

## MATLAB Development

### Model Structure
- **Class-based**: Models are often implemented as `classdef` (e.g., `zurcher.m`).
- **Static Methods**:
  - `setup(mpopt)`: Initializes parameters and grids.
  - `u(mp)`: Computes utility and derivatives.
- **Globals**: `global ev0 V0` are often used for storing starting values across iterations.

## Workflow & Conventions

- **Educational Code**: Implementations often build algorithms from scratch (e.g., VFI, Newton) rather than wrapping external libraries, to demonstrate the theory.
- **JAX vs NumPy**: When working in `1_theory_tools`, check if the context implies JAX (e.g., `import jax.numpy as jnp`) or standard NumPy.
- **Notebooks**: Ensure cells are independent where possible, but respect the flow of `setup` -> `solve` -> `plot`.
