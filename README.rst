===============================
uxtbpy
===============================

.. image:: https://dl.circleci.com/status-badge/img/gh/hkneiding/uxtbpy/tree/main.svg?style=svg
    :target: https://dl.circleci.com/status-badge/redirect/gh/hkneiding/uxtbpy/tree/main
.. image:: https://codecov.io/gh/hkneiding/uxtbpy/branch/main/graph/badge.svg?token=FDUVWAQGYT
    :target: https://codecov.io/gh/hkneiding/uxtbpy


This is an unofficial Python API for the Semiempirical Extended Tight-Binding Program Package `xTB <https://github.com/grimme-lab/xtb>`_ and `sTDA program for excited states <https://github.com/grimme-lab/std2>`_ developed by the Grimme group in Bonn, Germany. Since the official Python API only offers limited functionality this package is meant as a tool for the convenient integration of *xTB* and *sTDA* jobs in Python pipelines.

The package (ab-)uses Pythons capabilities to directly call binaries and capture their standard output. The *xTB* and *sTDA* outputs are automatically parsed into a dictionary containing entries for the different calculated properties.

Usage
-----------

The package requires working installations of the *xTB*, *xTB4sTDA* and *sTDA* programs obtainable from the corresponding GitHub pages. The package itself can be directly installed from this repository using ``pip``::

    pip install git+https://github.com/hkneiding/uxtbpy

A quick reference for usage is summarized below::

    import uxtbpy


    working_directory = "./wd/"

    xtb_runner = uxtbpy.XtbRunner(working_directory=working_directory)
    xtb_result_dict = xtb_runner.run_from_file("path/to/file.xyz", parameters=["--opt", "--chrg 0"])

    stda_runner = uxtbpy.StdaRunner(working_directory=working_directory)
    stda_result_dict = stda_runner.run_from_file("path/to/file.xyz", xtb4stda_parameters=[], stda_parameters=[])

For a comprehensive guide on how to install and use *uxtbpy* please refer to the `tutorial <./tutorial/tutorial.ipynb>`_.
