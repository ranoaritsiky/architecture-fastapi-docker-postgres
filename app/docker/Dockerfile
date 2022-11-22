# 
FROM python:3.10.6-slim-bullseye


# 
WORKDIR  /usr/src/app

# 
COPY ./requirements.txt  .

RUN  pip install --upgrade pip
# 
RUN pip install --no-cache-dir --upgrade -r  /usr/src/app/requirements.txt

EXPOSE 8000
# 
COPY . .