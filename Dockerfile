
FROM python:3.7
RUN apt-get update
RUN mkdir /app
COPY . /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirement.txt
EXPOSE 5001
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]