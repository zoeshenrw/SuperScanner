FROM python:3.6
COPY . .
WORKDIR .
RUN RUN apt-get -y update && apt-get install -y libzbar-dev
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["./run.py"]
