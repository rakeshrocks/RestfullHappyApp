FROM python:3.6.5-slim
WORKDIR /app
ADD . /app
RUN pip install --trusted-host pypi.python.org -r requirements.txt
#expose port so that flask app can run
EXPOSE 80
# This is the command which will invoke our application
CMD ["python", "app.py"]
