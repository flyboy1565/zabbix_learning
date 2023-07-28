FROM python:3.11.4-alpine3.18


COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app/

ENTRYPOINT [ "python" ]

CMD [ "view.py" ]