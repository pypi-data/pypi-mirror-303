GeoTiff data component
======================

The GeoTiff data component, *pymt_geotiff*,
is a `Python Modeling Toolkit`_ (*pymt*) library for 
accessing data (and metadata) from a GeoTIFF file,
through either a local filepath or a remote URL.

The *pymt_geotiff* component provides `BMI`_-mediated access to GeoTIFF data as a service,
allowing them to be coupled in *pymt* with other data or model components that expose a BMI.


Installation
------------

*pymt*, and components that run within it,
are distributed through `Anaconda`_ and the `conda`_ package manager.
Instructions for `installing`_ Anaconda can be found on their website.
In particular,
*pymt* components are available through the community-led `conda-forge`_ organization.

Install the `pymt` and `pymt_geotiff` packages in a new environment with:

.. code::

  $ conda create -n pymt -c conda-forge python=3 pymt pymt_geotiff
  $ conda activate pymt

*conda* automatically resolves and installs any required dependencies.


Use
---

The *pymt_geotiff* data component is designed to access data in a GeoTIFF file,
with the user providing the location of the file
through either a filepath or an URL.
This information can be provided through a configuration file
or specified through parameters.

With a configuration file
.........................

The *pymt_geotiff* configuration file is a `YAML`_ file
containing keys that map to parameter names.
An example is :download:`bmi-geotiff.yaml`:

.. include:: bmi-geotiff.yaml
   :literal:

:download:`Download <bmi-geotiff.yaml>` this file
for use in the following example.

.. include:: pymt_geotiff_config_file_ex.rst


With parameters
...............

Configuration information can also be passed directly to *pymt_geotiff* as parameters.

.. include:: pymt_geotiff_parameters_ex.rst


API documentation
-----------------

Looking for information on a particular function, class, or method?
This part of the documentation is for you.

.. toctree::
   :maxdepth: 2

   modules


Help
----

Depending on your need, CSDMS can provide advice or consulting services.
Feel free to contact us through the `CSDMS Help Desk <https://github.com/csdms/help-desk>`_.


Acknowledgments
---------------

This work is supported by the National Science Foundation
under Award No. `1831623 <https://nsf.gov/awardsearch/showAward?AWD_ID=1831623>`_,
*Community Facility Support: The Community Surface Dynamics Modeling System (CSDMS)*.


Indices and tables
------------------
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


.. Links:

.. _Python Modeling Toolkit: https://pymt.readthedocs.io
.. _BMI: https://bmi.readthedocs.io
.. _Anaconda: https://www.anaconda.com/products/individual
.. _conda: https://docs.conda.io/en/latest/
.. _installing: https://docs.anaconda.com/anaconda/install/
.. _conda-forge: https://conda-forge.org/
.. _YAML: https://en.wikipedia.org/wiki/YAML
