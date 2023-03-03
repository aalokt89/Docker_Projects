FROM ubuntu

#update, install curl, zip/unzip
RUN apt-get update -y \
    && apt-get install -y curl \
    && apt-get install -y zip unzip

#install aws cli
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" \
    && unzip awscliv2.zip \
    && ./aws/install -i /usr/local/aws-cli -b /usr/local/bin \
    && rm awscliv2.zip

#install python and boto3
RUN apt-get install -y python3-pip \
    && pip install boto3 \
    && rm -rf /var/lib/apt/lists/*

ENTRYPOINT ["tail", "-f", "/dev/null"]