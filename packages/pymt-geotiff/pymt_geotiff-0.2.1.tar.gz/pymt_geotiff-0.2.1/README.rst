============
pymt_geotiff
============


.. image:: https://img.shields.io/badge/CSDMS-Basic%20Model%20Interface-green.svg
        :target: https://bmi.readthedocs.io/
        :alt: Basic Model Interface

.. image:: https://img.shields.io/badge/recipe-pymt_geotiff-green.svg
        :target: https://anaconda.org/conda-forge/pymt_geotiff

.. image:: https://readthedocs.org/projects/pymt-geotiff/badge/?version=latest
        :target: https://pymt-geotiff.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://github.com/pymt-lab/pymt_geotiff/actions/workflows/test.yml/badge.svg
        :target: https://github.com/pymt-lab/pymt_geotiff/actions/workflows/test.yml

.. image:: https://github.com/pymt-lab/pymt_geotiff/actions/workflows/flake8.yml/badge.svg
        :target: https://github.com/pymt-lab/pymt_geotiff/actions/workflows/flake8.yml

.. image:: https://github.com/pymt-lab/pymt_geotiff/actions/workflows/black.yml/badge.svg
        :target: https://github.com/pymt-lab/pymt_geotiff/actions/workflows/black.yml


PyMT component for accessing GeoTIFF data and metadata


* Free software: MIT License
* Documentation: https://pymt-geotiff.readthedocs.io.




========= ===================================
Component PyMT
========= ===================================
GeoTiff   `from pymt.models import GeoTiff`
========= ===================================

---------------
Installing pymt
---------------

Installing `pymt` from the `conda-forge` channel can be achieved by adding
`conda-forge` to your channels with:

.. code::

  conda config --add channels conda-forge

*Note*: Before installing `pymt`, you may want to create a separate environment
into which to install it. This can be done with,

.. code::

  conda create -n pymt python=3
  conda activate pymt

Once the `conda-forge` channel has been enabled, `pymt` can be installed with:

.. code::

  conda install pymt

It is possible to list all of the versions of `pymt` available on your platform with:

.. code::

  conda search pymt --channel conda-forge

-----------------------
Installing pymt_geotiff
-----------------------

Once `pymt` is installed, the dependencies of `pymt_geotiff` can
be installed with:

.. code::

  conda install bmi-geotiff

To install `pymt_geotiff`,

.. code::

  conda install pymt_geotiff
