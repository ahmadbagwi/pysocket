FROM python:3

WORKDIR /usr/src/app

#COPY requirements.txt ./
#RUN pip install --no-cache-dir -r requirements.txt
RUN mkdir -p /var/run/dev-test

COPY pysocket.py ./

CMD [ "python", "./pysocket.py" ]