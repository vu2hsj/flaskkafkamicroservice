FROM python:3.6
COPY .  /flask_project
WORKDIR /flask_project
#RUN pip install -r requirements.txt
#RUN add-apt-repository ppa:jonathonf/vim && sudo apt update && sudo apt install vim


RUN pip install flask
RUN pip install kafka-python
RUN pip install mysql-connector
RUN pip install requests
#RUN apt install --assume-yes vim
#RUN pip install telnetd -y

#EXPOSE  8000
EXPOSE 8000
CMD ["python3", "app_latest.py"]

