# Use the official Python image
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . /app/

# Expose the port on which the app will run
EXPOSE 5000

# Run the application using Gunicorn
CMD ["gunicorn", "Application.app:app", "-b", "0.0.0.0:5000"]
