# Common Mistake: ImportError with unittest and Relative Imports

## Context

When structuring LeetCode solutions with separate `solution.py` and `test_solution.py` files within the same directory (e.g., `problems/problem_name/`), a common issue arises when trying to run the tests using the standard `python -m unittest` command.

If the test file (`test_solution.py`) imports the solution class using a direct import like:

```python
# test_solution.py
import unittest
from solution import Solution # <--- Direct import
# ... rest of the test class ...
```

Running the tests from the workspace root:

```bash
python -m unittest problems/problem_name/test_solution.py
```

Often results in an `ImportError`:

```
E
======================================================================
ERROR: test_solution (unittest.loader._FailedTest)
----------------------------------------------------------------------
ImportError: Failed to import test module: test_solution
Traceback (most recent call last):
  File ".../unittest/loader.py", line 154, in loadTestsFromName
    module = __import__(module_name)
  File ".../problems/problem_name/test_solution.py", line 2, in <module>
    from solution import Solution
ModuleNotFoundError: No module named 'solution'

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (errors=1)
```

## Cause

The `python -m unittest` command discovers tests and modules differently than running a script directly. When executed this way, Python might not automatically recognize the `solution.py` file in the same directory as a module accessible by the direct name `solution`.

## Solution: Relative Import

To fix this reliably, use a relative import within the test file:

```python
# test_solution.py
import unittest
from .solution import Solution # <--- Relative import using '.'

class TestMySolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    # ... tests ...

if __name__ == '__main__':
    unittest.main()
```

The leading dot (`.`) in `from .solution import Solution` explicitly tells Python to look for the `solution` module within the *current package* (the directory `problems/problem_name/` in this case).

## When to Use

Always prefer relative imports (`from .module import Class`) when importing sibling modules within the same directory structure, especially when using test runners like `python -m unittest` or `pytest` that operate from a higher-level directory. 