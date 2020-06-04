# branch containing jupyterhub docker image specification
to be used with `gateway` branch (notebook content)


### Run locally
docker pull pangeo/pangeo-notebook:2020.06.03
docker run -it --name pangeo-tutorial -p 8888:8888 $IMAGE:$TAG jupyter lab --ip 0.0.0.0
docker stop pangeo-tutorial
docker rm pangeo-tutorial
