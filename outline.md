# ATMOSPHERIC DATA ANALYSIS WITH DASK AND XARRAY

### Outline

1. **Xarray**
    1. Data structures for multi-dimensional data
    1. Working with labeled data
        1. Named dimensions/axes
        1. Coordinate labels
        1. Label based indexing
    1. Computation with xarray
        1. Arithmetic
        1. Aggregation
        1. Group-by and Resample
    1. Plotting and Visualization
        1. Integration with Matplotlib
        1. Making Maps with Cartopy
        1. Bokeh/Holoviews/Geoviews
    1. Input and Output
        1. NetCDF 3/4
        1. RasterIO
        1. Zarr
1. **Dask**
    1. Dynamic task scheduling
        1. Dask Delayed Functions
        1. Dask Delayed Objects
        1. Dask Schedulers
        1. Dask Parallelism
        1. Profiling & Diagnostics
        1. Dask Collections (`array`, `bag`, and `dataframe`)
        1. Dask Distributed
    1. Dask and Xarray
        1. Parallel/streaming/lazy computation using `dask.array`
        1. Reading and writing data
    1. Automatic parallelization with `xarray.apply_ufunc`
    1. Distributed scheduler for HPC and cloud computing environments
1. **Applications**
    1. CMIP5 data
    1. CESM Large Ensemble
