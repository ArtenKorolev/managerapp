FROM python

WORKDIR /manager

COPY . /manager/

ENTRYPOINT [ "python", "main.py" ]