FROM python:3.6
ENV PYTHONUNBUFFERED 1

RUN apt-get update -y && \
    apt-get -y install binutils libproj-dev gdal-bin && \
    apt-get install python3-psycopg2 -y

RUN mkdir /code
WORKDIR /code

COPY src/requirements.txt .

RUN export CPLUS_INCLUDE_PATH=/usr/include/gdal
RUN export C_INCLUDE_PATH=/usr/include/gdal
RUN pip install -r requirements.txt

COPY /src .

CMD './smcebi/bin/entrypoint.sh'

EXPOSE 8000

