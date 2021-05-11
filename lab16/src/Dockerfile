FROM python:3.9

RUN mkdir -p /usr/src/app/

WORKDIR /usr/src/app/
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . /usr/src/app/

ENTRYPOINT ["python", "/usr/src/app/main.py"]
#CMD ["python", "/usr/src/app/main.py"]