FROM python:3.6.4-alpine3.7

RUN pip install pipenv

WORKDIR /home/node/app

# Copy pip files to workdir
COPY Pipfile* /home/node/app/
# Update .lock file
RUN pipenv lock
# Install packages
RUN pipenv install --deploy --system

# Copy content to workdir
COPY . /home/node/app/

# Run script 
CMD python3 seed-sql.py