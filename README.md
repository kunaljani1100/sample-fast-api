# Sample FastAPI Application

This is a simple FastAPI application with two endpoints:

1. `GET /` - Returns a "Hello World" message.
2. `POST /items/` - Accepts an `Item` object with `name` and `price` fields and returns the same object.

## Requirements

- Python 3.7+
- FastAPI

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd sample-fast-api
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install fastapi
   ```

## Running the Application with Docker

1. Build the Docker image:
   ```bash
   docker build -t sample-fastapi .
   ```

2. Run the Docker container:
   ```bash
   docker run -p 8000:8000 sample-fast-api
   ```

The application will be available at `http://127.0.0.1:8000`.

## Testing the Endpoints

1. Open your browser or use a tool like `curl` or Postman to test the endpoints.

2. `GET /`
   - URL: `http://127.0.0.1:8000/`
   - Response:
     ```json
     {
       "message": "Hello World"
     }
     ```

3. `POST /items/`
   - URL: `http://127.0.0.1:8000/items/`
   - Body (JSON):
     ```json
     {
       "name": "Sample Item",
       "price": 10.5
     }
     ```
   - Response:
     ```json
     {
       "item": {
         "name": "Sample Item",
         "price": 10.5
       }
     }
     ```

## API Documentation

FastAPI automatically generates interactive API documentation for your application. You can access it by navigating to the following URL in your browser:

- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

These interfaces allow you to explore and test your API endpoints directly from the browser.

## License

This project is licensed under the MIT License.
