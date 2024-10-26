# Contributing

## Issues

Please report bugs or feature requests by [creating GitHub issues].

[creating GitHub issues]: https://github.com/aas-core-works/aas-core-protobuf/issues

## In Code

If you want to contribute in code, pull requests are welcome!

Please do [create a new issue] before you dive into coding.
It can well be that we already started working on the feature, or that there are upstream or downstream complexities involved which you might not be aware of.

[create a new issue]: https://github.com/aas-core-works/aas-core-protobuf/issues

## Definition Generation

All the generation logic lives in [dev_scripts/](dev_scripts/) (short for "development scripts").
Dev. scripts are a Python project.

To install the dev. scripts, create a virtual environment:

```
python3 -m venv venv
```

Activate it (on Linux):

```
source venv/bin/activate
```

Or on Windows:

```
venv/bin/Scripts/activate
```

Once in a virtual environment, install the dependencies to run the generation:

```
cd dev_scripts
pip3 install -e .
```

Run the definition generation:

```
python dev_scripts/aas_core_protobuf_generation/main.py
```

If you want to propagate the changes from aas-core-meta or aas-core-codegen, update the dependencies in [dev_scripts/pyproject.toml](dev_scripts/pyproject.toml).

### Development

Install a couple of development dependencies (*e.g.*, tools for static code analysis):

```
pip3 install -e .[dev]
```

Make changes to the code.

Run the precommit checks:

```
python dev_scripts/precommit.py
```

If you want to automatically re-format:

```
python dev_scripts/precommit.py --overwrite
```

### Pull Requests

**Feature branches**.
We develop using the feature branches, see [this section of the Git book].

[this section of the Git book]: https://git-scm.com/book/en/v2/Git-Branching-Branching-Workflows

If you are a member of the development team, create a feature branch directly within the repository.

Otherwise, if you are a non-member contributor, fork the repository and create the feature branch in your forked repository.
See [this GitHub tutorial] for more guidance.

[this GitHub tutorial]: https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request-from-a-fork

**Branch Prefix**.
Please prefix the branch with your Github user name (*e.g.,* ``mristin/Add-some-feature``).

**Continuous Integration**. 
GitHub will run the continuous integration (CI) automatically through GitHub actions.
The CI includes running the tests, inspecting the code, re-building the documentation *etc.*

### Commit Messages

The commit messages follow the guidelines from https://chris.beams.io/posts/git-commit:

* Separate subject from body with a blank line,
* Limit the subject line to 50 characters,
* Capitalize the subject line,
* Do not end the subject line with a period,
* Use the imperative mood in the subject line,
* Wrap the body at 72 characters, and
* Use the body to explain *what* and *why* (instead of *how*).
