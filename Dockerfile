FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy only requirements.txt first for caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your app files into the container
COPY . .

# Start the app using Gunicorn (use 'app:app' if your file is app.py and app = Flask(...))
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:6000", "app:app"]
