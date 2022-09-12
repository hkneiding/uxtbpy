===============================
uxtbpy
===============================

.. image:: https://dl.circleci.com/status-badge/img/gh/hkneiding/uxtbpy/tree/main.svg?style=svg
    :target: https://dl.circleci.com/status-badge/redirect/gh/hkneiding/uxtbpy/tree/main
.. image:: https://codecov.io/gh/hkneiding/uxtbpy/branch/main/graph/badge.svg?token=FDUVWAQGYT
    :target: https://codecov.io/gh/hkneiding/uxtbpy


This is an unofficial Python API for the Semiempirical Extended Tight-Binding Program Package `xTB <https://github.com/grimme-lab/xtb>`_ developed by the Grimme group in Bonn. Since the official Python API only offers limited functionality this package is meant as a dirty hack for easy integration of xTB results in Python pipelines.

The package (ab-)uses Pythons capabilities to directly call binaries and capture their standard output. The xTB output can either be returned raw for custom processing or as a dictionary containing entries for the different calculated properties. 

How to use
-----------

First, make sure that you have a functional version of the xTB program installed and that it is globally available on your system with the ``xtb`` command. You can verify this by making sure that you can run::

    xtb -version

The package can then be installed directly from this repository using ``pip``::
    
    pip install git+https://github.com/hkneiding/uxtbpy

which installs ``uxtbpy`` as a library to your Python installation or virtual environment.

Usage for ``xyz`` data is as simple as::

    import uxtbpy 

    xtb_runner = uxtbpy.XtbRunner(output_format='dict')
    result = xtb_runner.run_xtb_from_xyz('2\n\nO 0 0 0\nO 1.2 0 0', parameters='--ohess')