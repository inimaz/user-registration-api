FROM python:3.10

WORKDIR /code

# Copy the requirements file
COPY ./requirements.txt /code/requirements.txt

# Install the dependencies
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy the app files
COPY ./src /code/src

# 
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80"]