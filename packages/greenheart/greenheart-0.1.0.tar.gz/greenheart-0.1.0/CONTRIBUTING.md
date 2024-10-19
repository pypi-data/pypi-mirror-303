# Contributing

We welcome contributions in the form of bug reports, bug fixes, improvements to the documentation,
ideas for enhancements (or the enhancements themselves!).

You can find a [list of current issues](https://github.com/NREL/GreenHEART/issues) in the project's
GitHub repo. Feel free to tackle any existing bugs or enhancement ideas by submitting a
[pull request](https://github.com/NREL/GreenHEART/pulls).

## Bug Reports

* Please include a short (but detailed) Python snippet or explanation for reproducing the problem.
  Attach or include a link to any input files that will be needed to reproduce the error.
* Explain the behavior you expected, and how what you got differed.

## Pull Requests

* Please reference relevant GitHub issues in your commit message using `GH123` or `#123`.
* Changes should be [PEP8](http://www.python.org/dev/peps/pep-0008/) compatible.
* Keep style fixes to a separate commit to make your pull request more readable.
* Docstrings are required and should follow the
  [Google style](https://www.sphinx-doc.org/en/master/usage/extensions/example_google.html).
* When you start working on a pull request, start by creating a new branch pointing at the latest
  commit on [main](https://github.com/NREL/GreenHEART).
* The GreenHEART copyright policy is detailed in the [`LICENSE`](https://github.com/NREL/GreenHEART/blob/main/LICENSE).

## Documentation

NOTE: There is currently no documentation for GreenHEART, so instructions are forthcoming.

## Tests

The test suite can be run using `pytest tests/greenheart`. Individual test files can be run by specifying them:

```bash
pytest tests/greenheart/test_hybrid.py
```

and individual tests can be run within those files

```bash
pytest tests/greenheart/test_hybrid.py::test_greenheart_system
```

When you push to your fork, or open a PR, your tests will be run against the
[Continuous Integration (CI)](https://github.com/NREL/HOPP/actions) suite. This will start a build
that runs all tests on your branch against multiple Python versions, and will also test
documentation builds.
