# Pangeo Tutorial Materials

This repository tutorial materials for half-day workshops that showcase Pangeo JupyterHub deployments. The `notebooks` directory has Jupyter notebooks that illustrate key python libraries including xarray and dask. Notebooks in subfolders `amazon-web-services` and `google-cloud` utilize configuration and datasets stored on those commercial Cloud providers and are meant to be run as binders:

### GCP-specfic content

[![badge](https://img.shields.io/static/v1.svg?logo=Jupyter&label=Pangeo+Binder&message=GCE+us-central1&color=blue)](https://binder.pangeo.io/v2/gh/pangeo-data/pangeo-tutorialmaster?urlpath=git-pull?repo=https://github.com/pangeo-data/pangeo-tutorial%26amp%3Bbranch=master%26amp%3Burlpath=lab/tree/pangeo-tutorial/notebooks/google-cloud/%3Fautodecode)

### AWS-specific content

[![badge](https://img.shields.io/static/v1.svg?logo=Jupyter&label=Pangeo+Binder&message=AWS+us-west-2&color=orange)](https://aws-uswest2-binder.pangeo.io/v2/gh/pangeo-tutorial/master?urlpath=git-pull?repo=https://github.com/pangeo-data/pangeo-tutorial%26amp%3Bbranch=master%26amp%3Burlpath=lab/tree/pangeo-tutorial/notebooks/amazon-web-services/%3Fautodecode)


Workshops using this material:

* 2018 AGU workshop: [Scalable Geoscience Tools in Python — Xarray, Dask, and Jupyter](https://agu.confex.com/agu/fm18/meetingapp.cgi/Session/52170).
* 2019 AGU workshop: [Pangeo: Hands on with JupyterHub and Open-source Python Tools for Scalable Analysis of Big Data in the Geosciences](https://www.agu.org/Events/SCIWS12-Pangeo)


## Front Matter

<div><center><img src="./images/pangeo_card_white.png" height="150"> <img src="./images/xarray.png" height="125"> <img src="./images/dask.png" height="125"> <img src="./images/jupyter.png" height="125"></center></div>

-----

- **[About Pangeo](https://pangeo.io/):** Pangeo is a community effort for big data in the geosciences using Python. A key component of the Pangeo effort is the improved integration of [Xarray](http://xarray.pydata.org/en/latest/index.html) and [Dask](http://dask.pydata.org/en/latest/index.html) to enable analysis of very large datasets.
- **[About Xarray](http://xarray.pydata.org/en/latest/index.html):** Xarray is an open source project and Python package that aims to bring the labeled data power of pandas to the physical sciences, by providing N-dimensional variants of the core pandas data structures.
- **[About Dask](http://dask.pydata.org/en/latest/index.html):** Dask is a flexible parallel computing library for analytic computing.
- **[About Jupyter](http://jupyter.org/):** Project Jupyter exists to develop open-source software, open-standards, and services for interactive computing across dozens of programming languages. The Jupyter Notebook is an open-source web application that allows you to create and share documents that contain live code, equations, visualizations and narrative text. Uses include: data cleaning and transformation, numerical simulation, statistical modeling, data visualization, machine learning, and much more.

## Acknowledgements

At its core, Pangeo is a community effort built around open-source software. As such, the credit for the developments of the software described here belongs with the community that created it.

Elements of this tutorial were taken from the xarray, Dask, Cartopy, Holoviews, and Geoviews documentation. Some pieces of text in the xarray portion of the tutorial were adapted from Hoyer and Hamman (2016).

Pangeo is [supported](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1740633&HistoricalAwards=false) by the [National Science Foundation (NSF)](https://www.nsf.gov/) via the [EarthCube Program](https://www.earthcube.org/) and the [National Aeronautics and Space Administration](https://www.nasa.gov/) via the [ACCESS Program](https://earthdata.nasa.gov/community/community-data-system-programs/access-projects).  NCAR is separately supported by the [National Science Foundation (NSF)](https://www.nsf.gov/).

Google provided compute credits on [Google Compute Engine](https://cloud.google.com/). Amazon provided compute credits on [AWS](https://aws.amazon.com)

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.
