FROM python:3.10
RUN mkdir /flask_app
WORKDIR /flask_app
RUN pip install PyMySQL
COPY . .
RUN pip install -r requirements.txt --no-cache-dir
ENTRYPOINT ["python"]
CMD ["anime_app.py"]