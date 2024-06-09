FROM python:3

ARG user
ARG uid

RUN apt-get update && apt-get install -y \
    git \
    curl \
    nano \
    python3 \
    socat

WORKDIR /usr/src/app

#COPY requirements.txt ./
#RUN pip install --no-cache-dir -r requirements.txt
RUN useradd -G www-data,root -u $uid -m -d /home/$user $user
RUN chown -R $user:$user /home/$user

RUN mkdir -p /var/run/dev-test

COPY pysocket.py /usr/src/app/

CMD [ "python3", "pysocket.py" ]  