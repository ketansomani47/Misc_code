FROM public.ecr.aws/docker/library/python:3.10 as build-image
RUN apt show openssh-client

COPY html_template/ ./html_template/
RUN apt update -y && apt upgrade openssl -y

RUN apt show openssh-client
CMD [ "app.lambda_handler" ]
