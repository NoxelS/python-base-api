# Python Base API Boilerplate

[![Release](https://img.shields.io/github/v/release/NoxelS/python-base-api)](https://img.shields.io/github/v/release/NoxelS/python-base-api)
[![Build status](https://img.shields.io/github/actions/workflow/status/NoxelS/python-base-api/main.yml?branch=main)](https://github.com/NoxelS/python-base-api/actions/workflows/main.yml?query=branch%3Amain)
[![codecov](https://codecov.io/gh/NoxelS/python-base-api/branch/main/graph/badge.svg)](https://codecov.io/gh/NoxelS/python-base-api)
[![Commit activity](https://img.shields.io/github/commit-activity/m/NoxelS/python-base-api)](https://img.shields.io/github/commit-activity/m/NoxelS/python-base-api)
[![License](https://img.shields.io/github/license/NoxelS/python-base-api)](https://img.shields.io/github/license/NoxelS/python-base-api)

This is a template repository for Python projects that use uv for their dependency management, fastapi as API server and some CI/CD pipelines 
for automated testing and code coverage.

- **Github repository**: <https://github.com/NoxelS/python-base-api/>

## Getting started with your project

### 1. Using This Template

Cick on "Use this template" to create a repository based on the python base api repository.


### 2. Set Up Your Development Environment

Then, install the environment and the pre-commit hooks with

```bash
make install
```

This will also generate your `uv.lock` file.

You are now ready to start development on your project!
The CI/CD pipeline will be triggered when you open a pull request, merge to main, or when you create a new release.


### 3. Run the pre-commit hooks

Initially, the CI/CD pipeline might be failing due to formatting issues. To resolve those run:

```bash
uv run pre-commit run -a
```

---

Repository initiated with [fpgmaas/cookiecutter-uv](https://github.com/fpgmaas/cookiecutter-uv).
