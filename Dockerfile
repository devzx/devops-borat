FROM alpine:3.6
RUN apk add --no-cache python3 && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    rm -r /root/.cache

# Pass a Hipchat Integration URL as the second argument to ENV
ENV BORAT 

COPY ./src /src

RUN pip3 install -r /src/requirements.txt \
    && touch crontab.tmp \
    && echo '0 8 * * * /usr/bin/python3 /src/app.py' > crontab.tmp \
    && echo '0 15 * * * /usr/bin/python3 /src/app.py' >> crontab.tmp \
    && crontab crontab.tmp \
    && rm -rf crontab.tmp

CMD 'crond' '-f'
