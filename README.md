# branch containing jupyterhub docker image specification
to be used with `agu2019` branch (notebook content)


### Run locally
docker pull pangeo/pangeo-notebook:2019.12.03
docker run -it --name pangeo-tutorial -p 8888:8888 $IMAGE:$TAG jupyter lab --ip 0.0.0.0
docker stop pangeo-tutorial
docker rm pangeo-tutorial
