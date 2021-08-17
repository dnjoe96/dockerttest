# set the base container image
FROM python:3.6-alpine

LABEL maintainer="joseph"

# creating a new user
RUN adduser -D joseph

#setting the workdir to be the home of the new user
WORKDIR /home/joseph

# copy requirements.txt from the project file to the home dir
COPY requirements.txt requirements.txt

# create a virtual environment
RUN python3 -m venv venv

# enter venv
RUN source venv/bin/activate

# install requirements
RUN pip install -r requirements.txt

# copy app folder to working dir
COPY app app

# copy run.py and config.py and boot.sh to working dir
COPY run.py config.py boot.sh ./

# set permission of sh file
RUN chmod +x boot.sh

# set the environment variable
ENV FLASK_APP run.py

RUN chown -R joseph:joseph ./
USER joseph

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]