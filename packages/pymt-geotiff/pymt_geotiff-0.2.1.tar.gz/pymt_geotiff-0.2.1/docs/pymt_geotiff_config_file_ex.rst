Start by importing the GeoTiff class from ``pymt``.

.. code:: ipython3

    from pymt.models import GeoTiff

Create an instance.

.. code:: ipython3

    m = GeoTiff()

In this case, we’ll initialize the GeoTiff component with information
from a configuration file.
(This may take a moment as data are fetched from the internet.)

.. code:: ipython3

    m.initialize("bmi-geotiff.yaml")

Note that the configurtation information has been read from the
configuration file into the component as parameters.

What variables can be accessed from this component?

.. code:: ipython3

    for var in m.output_var_names:
        print(var)


.. parsed-literal::

    gis__raster_data
    gis__coordinate_reference_system
    gis__gdal_geotransform


Get the GDAL GeoTransform used by the data.

.. code:: ipython3

    m.var["gis__gdal_geotransform"].data




.. parsed-literal::

    array([  3.00037927e+02,   0.00000000e+00,   1.01985000e+05,
             0.00000000e+00,  -3.00041783e+02,   2.82691500e+06])



What are the units of the transformation?

.. code:: ipython3

    m.var["gis__gdal_geotransform"].units




.. parsed-literal::

    'm'



Finish by finalizing the component.

.. code:: ipython3

    m.finalize()
