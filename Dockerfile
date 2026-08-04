FROM python:3.12-slim

WORKDIR /app

# Install dependencies first so Docker can cache this layer
# (only re-runs if requirements.txt changes, not on every code change)
COPY . .

# Copy the rest of the application code
COPY . .
RUN pip install "fastapi[standard]"

EXPOSE 8000

CMD ["uvicorn", "fast:app", "--host", "0.0.0.0", "--port", "8000"]
