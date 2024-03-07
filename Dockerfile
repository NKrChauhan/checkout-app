# Stage 1: build the image with dependancy and run tests
# Use a lightweight Python base image to create a python environment
FROM python:3.9-slim AS builder

# Set working directory inside the container to ensure correct entrypoint to code
WORKDIR /app

# Copy requirements file
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy code to working directory
COPY . .

# Run unit tests
RUN python -m unittest

# Stage 2: Final image (built only if tests pass)
FROM builder AS final

# Only copy application code if tests passed (prevents building a failing image)
# Conditional copy based on previous stage success
COPY --from=builder /app .


# Define the entrypoint command
ENTRYPOINT ["python", "main.py"]
