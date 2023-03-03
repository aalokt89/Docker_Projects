FROM alpine

#update, install curl, zip/unzip
RUN apk update \
    && apk add curl zip unzip \
    && apk add git

#install aws cli & python/boto3
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" \
    && unzip awscliv2.zip \
    && ./aws/install -i /usr/local/aws-cli -b /usr/local/bin

#install python/boto3
RUN apk add python3 py3-pip \
    && pip install boto3 \
    && rm awscliv2.zip \
    && rm -rf /var/lib/apt/lists/*

ENTRYPOINT ["tail", "-f", "/dev/null"]