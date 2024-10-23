Start by importing the GeoTiff class from ``pymt`` and creating an
instance.

.. code:: ipython3

    from pymt.models import GeoTiff
    m = GeoTiff()

Next, use the *setup* method to assign values to the parameters needed
by GeoTiff.

.. code:: ipython3

    args = m.setup(
        "test",
        filename="https://github.com/mapbox/rasterio/raw/master/tests/data/RGB.byte.tif",
    )

Pass the results from *setup* into the *initialize* method. (This step
may take a moment as data are fetched from the internet.)

.. code:: ipython3

    m.initialize(*args)


.. parsed-literal::

    *** <xarray.Rectilinear>
    Dimensions:     (rank: 3)
    Dimensions without coordinates: rank
    Data variables:
        mesh        int64 0
        node_shape  (rank) int32 3 718 791


Note that the parameters have been correctly assigned in the component:

.. code:: ipython3

    for param in m.parameters:
        print(param)


.. parsed-literal::

    ('filename', 'https://github.com/mapbox/rasterio/raw/master/tests/data/RGB.byte.tif')


What variables can be accessed from this component?

.. code:: ipython3

    for var in m.output_var_names:
        print(var)


.. parsed-literal::

    gis__raster_data
    gis__coordinate_reference_system
    gis__gdal_geotransform


Get the raster data values.

.. code:: ipython3

    raster = m.var["gis__raster_data"].data

Let’s visualize these data.

The *pymt_geotiff* component contains not only data values, but also the
grid on which they’re located. Start by getting the identifier for the
grid used for the raster data.

.. code:: ipython3

    gid = m.var_grid("gis__raster_data")

Using the grid identifier, we can get the grid dimensions and the
locations of the grid nodes.

.. code:: ipython3

    shape = m.grid_shape(gid)
    x = m.grid_x(gid)
    y = m.grid_y(gid)
    print("shape:", shape)
    print("x:", x)
    print("y:", y)


.. parsed-literal::

    shape: [  3 718 791]
    x: [ 102135.01896334  102435.05689001  102735.09481669  103035.13274336
      ...
      338564.90518331  338864.94310999  339164.98103666]
    y: [ 2826764.97910863  2826464.93732591  2826164.89554318  2825864.85376045
      ...
      2611935.06267409  2611635.02089137]


We’re almost ready to make a plot. Note, however, that the default
behavior of ``pymt`` components is to flatten data arrays.

.. code:: ipython3

    raster.shape




.. parsed-literal::

    (1703814,)



Make a new variable that restores the dimensionality of the data.

.. code:: ipython3

    raster3D = raster.reshape(shape)
    raster3D.shape




.. parsed-literal::

    (3, 718, 791)



Extract the red band from the image.

.. code:: ipython3

    red_band = raster3D[0,:,:]
    red_band.shape




.. parsed-literal::

    (718, 791)



What information do we have about how the data are projected?

.. code:: ipython3

    projection = m.var["gis__coordinate_reference_system"].data
    projection




.. parsed-literal::

    array(['+init=epsg:32618'],
          dtype='<U16')



.. code:: ipython3

    transform = m.var["gis__gdal_geotransform"].data
    transform




.. parsed-literal::

    array([  3.00037927e+02,   0.00000000e+00,   1.01985000e+05,
             0.00000000e+00,  -3.00041783e+02,   2.82691500e+06])



We’ll use
`cartopy <https://scitools.org.uk/cartopy/docs/v0.5/index.html>`__ to
help display the data in a map projection.

.. code:: ipython3

    import cartopy.crs as ccrs

The data are in `UTM zone 18N <https://epsg.io/32618>`__, but the
projection must be set manually. (A
`note <http://xarray.pydata.org/en/stable/examples/visualization_gallery.html#imshow()-and-rasterio-map-projections>`__
in the *xarray* documentation describes this.)

.. code:: ipython3

    crs = ccrs.UTM('18N')

Display the red band of the image in the appropriate projection.

.. code:: ipython3

    import matplotlib.pyplot as plt
    
    ax = plt.subplot(projection=crs)
    ax.imshow(red_band, transform=crs, extent=[x.min(),x.max(),y.min(),y.max()], cmap="pink")




.. parsed-literal::

    <matplotlib.image.AxesImage at 0x1a23b4be0>




.. image:: _static/pymt_geotiff_parameters_ex_32_1.png


Complete the example by finalizing the component.

.. code:: ipython3

    m.finalize()
