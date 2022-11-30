
FROM python:3.9.7
LABEL maintainer="Christos Mavrogiannis"

WORKDIR .
COPY . .

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

CMD [ "python", "main.py" ]