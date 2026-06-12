# cloud-ci-lab-project

A small cloud service with an automated **CI pipeline** built using GitHub Actions.
Every code change pushed to the repository is automatically validated before deployment.

## Project structure

```
cloud-ci-lab-project/
├── app.py                     # The cloud app — prints "Cloud CI Pipeline Running"
├── test_app.py                # Basic validation tests (pytest)
├── .gitignore                 # Python-specific ignores
├── .github/
│   └── workflows/
│       └── ci.yml             # GitHub Actions CI pipeline
└── README.md
```

## Run locally

```bash
python app.py
# -> Cloud CI Pipeline Running
```

## Test locally

```bash
pip install pytest
pytest -v
```

## CI Pipeline (`.github/workflows/ci.yml`)

The pipeline runs automatically **on every push** and pull request. It:

1. Triggers on push
2. Runs on an Ubuntu runner (`ubuntu-latest`)
3. Checks out the code
4. Sets up the Python runtime
5. Echoes a build message and prints the runtime version (intermediate step)
6. Installs test dependencies
7. Runs the app
8. Runs the test command

## What did the pipeline automate?

The pipeline automates **validation of every code change**: on each push it
provisions a clean Ubuntu environment, installs the correct Python runtime,
runs the application, and executes the test suite. This means broken code is
caught automatically — before it ever reaches deployment — applying GitOps
principles where the repository is the single source of truth and the pipeline
enforces quality on every change.
