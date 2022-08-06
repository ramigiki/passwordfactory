# python3.7.2 container image
FROM python:3.7.2-stretch

# set the working directory to /application
WORKDIR /application

# copy the current directory contents into the container
ADD . /application

# Install the dependencies
RUN pip install -r requirements.txt

# start uWSGI
CMD [ "uwsgi", "docker/webapp/app.ini" ]
