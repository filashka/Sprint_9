FROM python:3.12-slim

WORKDIR /tests

# Install dependencies first to leverage Docker layer caching.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Tests run against Selenoid over the network, so no local browser/driver is
# needed in this image. The compose file overrides this command if required.
CMD ["pytest", "--selenoid-uri=http://selenoid:4444/wd/hub", "--browser-version=128.0"]
