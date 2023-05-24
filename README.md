# Dummy package

This dummy package has been created solely to make sure that the framework to create and share a package works.
We namely use:

1. **poetry** to manage the dependencies and packages.
2. **sphinx** to handle the documentation.
3. **git** to enable version controlling.

# Use with poetry

1. Make sure that `poetry` is installed.
2. Type the following
  ```{code-block} console
  poetry install
  cd docs
  poetry run make html
  ```
3. The documentation is then created: `docs\build\index.html`.
