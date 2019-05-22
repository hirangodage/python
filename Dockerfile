#baseimage - ex: linux image with basic python
from python:alpine
run mkdir -p /var/[foldernameinserver]
#run any other command in shell
#copy content into server
COPY ./ /var/[foldernameinserver]
#install dependancy
RUN pip install /var/[foldernameinserver]/requirements.txt
ENTRYPOINT python /var/[foldernameinserver]/[main scrip that ecpose the service].py

#[port number that exposed by that main script]
EXPOSE 80

#build the image using docker command
#docker build -t [imagename] .

#run that image in docker host
#docker run -d -p [destinationport]:[sourceport] -t [image name]