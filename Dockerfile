# 1. Use an official, lightweight Python base image
FROM python:3.12-slim

# 2. Set environment variables to optimize Python performance inside Docker
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3. Set the working directory inside the container
WORKDIR /app

# 4. Copy only the dependency file first to leverage Docker layer caching
COPY requirements.txt .

# 5. Install dependencies without saving local cache to keep the image small
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copy the rest of the application source code
COPY . .

# 7. Expose the port your application listens on (optional, e.g., for web apps)
EXPOSE 8000

# 8. Define the default command to execute your application
CMD ["python", "app.py",]
