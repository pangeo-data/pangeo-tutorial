# Pangeo Tutorial

<div><center>
  <img src="./images/pangeo_card_white.png" height="150"> 
  <img src="./images/dask.png" height="125">
  <img src="./images/xarray.png" height="125"> 
  <img src="./images/holoviz.png" height="125">
  <img src="./images/jupyter.png" height="125"> 
</center></div>



This repository tutorial materials for half- to full-day workshops that showcase Pangeo JupyterHub deployments. The `notebooks` directory has Jupyter notebooks that illustrate key python libraries including geopandas, xarray, dask, holoviz and intake. You can run these notebooks interactively on BinderHub services like [MyBinder.org](https://mybinder.org). **Note that these are emphermal computing environments on Public infrastructure, so you may lose work, and don't store passwords!**

| Basic content  | 
| ------------- | 
| [![badge](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/pangeo-data/pangeo-tutorial/binder-agu2019?urlpath=git-pull?repo=https://github.com/pangeo-data/pangeo-tutorial%26amp%3Bbranch=usgs_workshop_mar2020%26amp%3Burlpath=lab/tree/pangeo-tutorial/notebooks/%3Fautodecode) |

Notebooks in subfolders `amazon-web-services` and `google-cloud` combine all these Python libraries and use cluster configurations and datasets stored on Google Cloud (GCP) or Amazon Cloud (AWS). The following binder links launch a [predefined computational environment](https://hub.docker.com/r/pangeo/pangeo-notebook/tags) in different Cloud data centers, allowing us to upload our computation rather than download data:

| AWS-specific content  | GCP-specific content |
| ------------- | ------------- |
| [![badge](https://img.shields.io/static/v1.svg?logo=Jupyter&label=Pangeo+Binder&message=AWS+us-west-2&color=orange)](https://aws-uswest2-binder.pangeo.io/v2/gh/pangeo-data/pangeo-tutorial/binder-agu2019?urlpath=git-pull?repo=https://github.com/pangeo-data/pangeo-tutorial%26amp%3Bbranch=usgs_workshop_mar2020%26amp%3Burlpath=lab/tree/pangeo-tutorial/notebooks/%3Fautodecode) |[![badge](https://img.shields.io/static/v1.svg?logo=Jupyter&label=Pangeo+Binder&message=GCE+us-central1&color=blue)](https://binder.pangeo.io/v2/gh/pangeo-data/pangeo-tutorial/binder-agu2019?urlpath=git-pull?repo=https://github.com/pangeo-data/pangeo-tutorial%26amp%3Bbranch=usgs_workshop_mar2020%26amp%3Burlpath=lab/tree/pangeo-tutorial/notebooks/%3Fautodecode) |

## Tutorial Components

<div><center>
  <img src="./images/pangeo_card_white.png" height="150"> 
  <img src="./images/dask.png" height="125">
  <img src="./images/xarray.png" height="125"> 
  <img src="./images/holoviz.png" height="125">
  <img src="./images/jupyter.png" height="125"> 
</center></div>

-----

- **[About Pangeo](https://pangeo.io/):** Pangeo is a community effort for big data in the geosciences using Python. A key component of the Pangeo effort is the improved integration of Xarray, Dask and Holoviz to enable analysis and visualization of very large datasets.
- **[About Dask](http://dask.pydata.org/en/latest/index.html):** Dask is a flexible parallel computing library for analytic computing.
- **[About Xarray](http://xarray.pydata.org/en/latest/index.html):** Xarray is an open source project and Python package that aims to bring the labeled data power of pandas to the physical sciences, by providing N-dimensional variants of the core pandas data structures.
- **[About HoloViz](https://holoviz.org/):** HoloViz provides a coordinated set of high-level tools for visualizing data:  Panel for making apps and dashboards, hvPlot to easily generate interactive plots, HoloViews to make data visualizable, GeoViews to extend HoloViews for geographic data, Datashader for rendering large datasets, Param to create declarative user-configurable objects, and Colorcet for perceptually uniform colormaps.
- **[About Jupyter](http://jupyter.org/):** Project Jupyter exists to develop open-source software, open-standards, and services for interactive computing across dozens of programming languages. The Jupyter Notebook is an open-source web application that allows you to create and share documents that contain live code, equations, visualizations and narrative text. Uses include: data cleaning and transformation, numerical simulation, statistical modeling, data visualization, machine learning, and much more.

- **[About Geopandas](http://geopandas.org):** Geopandas is a library to facilitate analysis of geospatial vector data
- **[About Intake](https://intake.readthedocs.io/en/latest/index.html):** Intake is a cataloging system designed to "Take the pain out of data access and distribution"

## Workshops

* 2018 AGU workshop: [Scalable Geoscience Tools in Python — Xarray, Dask, and Jupyter](https://agu.confex.com/agu/fm18/meetingapp.cgi/Session/52170).
* 2019 AGU workshop: [Pangeo: Hands on with JupyterHub and Open-source Python Tools for Scalable Analysis of Big Data in the Geosciences](https://www.agu.org/Events/SCIWS12-Pangeo)

## Acknowledgements

At its core, Pangeo is a community effort built around open-source software. As such, the credit for the developments of the software described here belongs with the community that created it.

Elements of this tutorial were taken from the xarray, Dask, Cartopy, Holoviews, and GeoPandas documentation. Some pieces of text in the xarray portion of the tutorial were adapted from Hoyer and Hamman (2016).

Pangeo is [supported](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1740633&HistoricalAwards=false) by the [National Science Foundation (NSF)](https://www.nsf.gov/) via the [EarthCube Program](https://www.earthcube.org/) and the [National Aeronautics and Space Administration](https://www.nasa.gov/) via the [ACCESS Program](https://earthdata.nasa.gov/community/community-data-system-programs/access-projects).  NCAR is separately supported by the [National Science Foundation (NSF)](https://www.nsf.gov/).

Google provided compute credits on [Google Compute Engine](https://cloud.google.com/). Amazon provided compute credits on [AWS](https://aws.amazon.com)

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.
