# Step 1: Use a Python base image
FROM python:3.8-slim

# Step 2: Set working directory to /app
WORKDIR /app

# Step 3: Copy the entire project into the /app directory in the container
COPY . /app

# Step 4: Install Python dependencies from the requirements.txt
# Update pip and install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Step 5: Expose port 5000 (Flask default port)
EXPOSE 5000

# Step 6: Set environment variables for Flask
ENV FLASK_APP=Application.app:app
ENV FLASK_ENV=production

# Step 7: Set the command to run Gunicorn with your Flask app
CMD ["gunicorn", "Application.app:app", "-b", "0.0.0.0:5000"]

