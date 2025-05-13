# Use a slim version of Python 3.10 as the base image
FROM python:3.10-slim

# Environment variables to prevent Python from writing .pyc files 
# and to ensure output is logged directly
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies required for building Python packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    git \
    build-essential && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


# Copy requirements file and install Python dependencies
COPY requirements.txt . 
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt


COPY . .

EXPOSE 5000

CMD ["python", "app.py"]

