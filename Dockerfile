FROM python:3.8-slim

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8
ENV PORT 6060
ENV USERNAME admin
ENV PASSWORD admin
ENV OPENSSL_CONF /etc/ssl/

COPY . /app

WORKDIR /app
RUN rm -Rf .git
RUN rm -Rf venv

RUN pip install playwright \
&& playwright install --with-deps firefox

RUN set -x; buildDeps='wget build-essential' \
&& apt-get update && apt-get install -y ${buildDeps} chrpath libssl-dev libxft-dev libfreetype6 libfreetype6-dev libfontconfig1 libfontconfig1-dev \
&& rm -rf /var/lib/apt/lists/* \
&& export OS_ARCH=$(uname -m) \
&& pip install -r requirements.txt && pip cache purge \
&& apt-get purge -y --auto-remove $buildDeps

EXPOSE $PORT

RUN chmod +x run.sh
CMD ./run.sh $PORT $USERNAME $PASSWORD