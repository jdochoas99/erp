FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /erp
WORKDIR /erp
RUN pip install  Django
RUN pip install  pymysql
ADD . /erp/