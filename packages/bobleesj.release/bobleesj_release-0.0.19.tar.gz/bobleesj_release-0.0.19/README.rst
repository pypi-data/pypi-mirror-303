|Icon| |title|_
===============

.. |title| replace:: bobleesj.release
.. _title: https://bobleesj-test-org.github.io/bobleesj.release

.. |Icon| image:: https://avatars.githubusercontent.com/bobleesj-test-org
        :target: https://bobleesj-test-org.github.io/bobleesj.release
        :height: 100px

|PyPi| |Forge| |PythonVersion| |PR|

|CI| |Codecov| |Black| |Tracking|

.. |Black| image:: https://img.shields.io/badge/code_style-black-black
        :target: https://github.com/psf/black

.. |CI| image:: https://github.com/bobleesj-test-org/bobleesj.release/actions/workflows/matrix-and-codecov-on-merge-to-main.yml/badge.svg
        :target: https://github.com/bobleesj-test-org/bobleesj.release/actions/workflows/matrix-and-codecov-on-merge-to-main.yml

.. |Codecov| image:: https://codecov.io/gh/bobleesj-test-org/bobleesj.release/branch/main/graph/badge.svg
        :target: https://codecov.io/gh/bobleesj-test-org/bobleesj.release

.. |Forge| image:: https://img.shields.io/conda/vn/conda-forge/bobleesj.release
        :target: https://anaconda.org/conda-forge/bobleesj.release

.. |PR| image:: https://img.shields.io/badge/PR-Welcome-29ab47ff

.. |PyPi| image:: https://img.shields.io/pypi/v/bobleesj.release
        :target: https://pypi.org/project/bobleesj.release/

.. |PythonVersion| image:: https://img.shields.io/pypi/pyversions/bobleesj.release
        :target: https://pypi.org/project/bobleesj.release/

.. |Tracking| image:: https://img.shields.io/badge/issue_tracking-github-blue
        :target: https://github.com/bobleesj-test-org/bobleesj.release/issues

Python package for doing science.

* LONGER DESCRIPTION HERE

For more information about the bobleesj.release library, please consult our `online documentation <https://bobleesj-test-org.github.io/bobleesj.release>`_.

Citation
--------

If you use bobleesj.release in a scientific publication, we would like you to cite this package as

        bobleesj.release Package, https://github.com/bobleesj-test-org/bobleesj.release

Installation
------------

The preferred method is to use `Miniconda Python
<https://docs.conda.io/projects/miniconda/en/latest/miniconda-install.html>`_
and install from the "conda-forge" channel of Conda packages.

To add "conda-forge" to the conda channels, run the following in a terminal. ::

        conda config --add channels conda-forge

We want to install our packages in a suitable conda environment.
The following creates and activates a new environment named ``bobleesj.release_env`` ::

        conda create -n bobleesj.release_env python=3
        conda activate bobleesj.release_env

Then, to fully install ``bobleesj.release`` in our active environment, run ::

        conda install bobleesj.release

Another option is to use ``pip`` to download and install the latest release from
`Python Package Index <https://pypi.python.org>`_.
To install using ``pip`` into your ``bobleesj.release_env`` environment, type ::

        pip install bobleesj.release

If you prefer to install from sources, after installing the dependencies, obtain the source archive from
`GitHub <https://github.com/bobleesj-test-org/bobleesj.release/>`_. Once installed, ``cd`` into your ``bobleesj.release`` directory
and run the following ::

        pip install .

Support and Contribute
----------------------

`Diffpy user group <https://groups.google.com/g/diffpy-users>`_ is the discussion forum for general questions and discussions about the use of bobleesj.release. Please join the bobleesj.release users community by joining the Google group. The bobleesj.release project welcomes your expertise and enthusiasm!

If you see a bug or want to request a feature, please `report it as an issue <https://github.com/bobleesj-test-org/bobleesj.release/issues>`_ and/or `submit a fix as a PR <https://github.com/bobleesj-test-org/bobleesj.release/pulls>`_. You can also post it to the `Diffpy user group <https://groups.google.com/g/diffpy-users>`_. 

Feel free to fork the project and contribute. To install bobleesj.release
in a development mode, with its sources being directly used by Python
rather than copied to a package directory, use the following in the root
directory ::

        pip install -e .

To ensure code quality and to prevent accidental commits into the default branch, please set up the use of our pre-commit
hooks.

1. Install pre-commit in your working environment by running ``conda install pre-commit``.

2. Initialize pre-commit (one time only) ``pre-commit install``.

Thereafter your code will be linted by black and isort and checked against flake8 before you can commit.
If it fails by black or isort, just rerun and it should pass (black and isort will modify the files so should
pass after they are modified). If the flake8 test fails please see the error messages and fix them manually before
trying to commit again.

Improvements and fixes are always appreciated.

Before contribuing, please read our `Code of Conduct <https://github.com/bobleesj-test-org/bobleesj.release/blob/main/CODE_OF_CONDUCT.rst>`_.

Contact
-------

For more information on bobleesj.release please visit the project `web-page <https://bobleesj-test-org.github.io/>`_ or email Prof. Simon Billinge at sb2896@columbia.edu.
