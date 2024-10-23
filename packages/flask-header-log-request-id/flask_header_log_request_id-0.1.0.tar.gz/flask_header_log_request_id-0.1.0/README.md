## Flask Header Log Request ID
A Flask middleware to log and set Request ID in the HTTP header.

### Overview
This project provides a Flask middleware that ensures a unique Request ID is generated and logged for each incoming request. The Request ID is also included in the response back to the client.

#### Features
Generates a unique Request ID for each incoming request
Logs the Request ID using a log filter
Includes the Request ID in the response back to the client
Installation
To install the middleware, run the following command:

```bash
pip install flask_header_log_request_id
```

#### Usage
To use the middleware in your Flask application, simply import and initialize it:

```python
from flask import Flask
from flask_header_log_request_id import RequestID

app = Flask(__name__)
RequestID(app)
```

#### Configuration

The middleware can be configured using the following settings:

- `REQUEST_ID_UNIQUE_VALUE_PREFIX`: a prefix that indicates a request ID should be considered unique

#### Logging

The middleware uses a log filter to inject the current request ID into log records. To use the log filter, add it to your logging configuration:

```python
from flask_header_log_request_id.log_filter import RequestIDLogFilter

logging.basicConfig()
logger = logging.getLogger()
logger.addFilter(RequestIDLogFilter())
```


#### Example
Here is an example of how to use the middleware in a Flask application:

```python
from flask import Flask
from flask_header_log_request_id import RequestID

app = Flask(__name__)
RequestID(app)

@app.route("/")
def index():
    return "Hello, World!"

if __name__ == "__main__":
    app.run()
```

In this example, the middleware will generate a unique Request ID for each incoming request and log it using the log filter. The Request ID will also be included in the response back to the client.