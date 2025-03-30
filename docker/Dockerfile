# Use an official lightweight Python image
FROM python:3.12

# Set the working directory inside the container
WORKDIR /app

# Copy the dependency files first (better for caching)
COPY pyproject.toml poetry.lock ./

# Install poetry
RUN pip install --no-cache-dir poetry && \
    poetry config virtualenvs.in-project true &&


# Install dependencies (without dev dependencies)
RUN poetry install --no-dev --no-interaction --no-ansi

# Copy the rest of the application code
COPY . .

EXPOSE 80

# Specify the command to run the app (modify as needed)
# CMD ["poetry", "run", "python", "main.py"]
CMD ["/start.sh"]