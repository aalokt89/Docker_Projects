FROM ubuntu

#update, install curl, zip/unzip
RUN apt-get update -y \
    && apt-get install curl -y \
    && apt-get install zip unzip

#install aws cli
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" \
    && unzip awscliv2.zip \
    && ./aws/install -i /usr/local/aws-cli -b /usr/local/bin

#install python and boto3
RUN apt-get install python3-pip -y \
    && pip install boto3

CMD [ "python3" ]