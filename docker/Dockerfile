# Use an official lightweight Python image
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the dependency files first (better for caching)
COPY pyproject.toml poetry.lock ./

# Copy the rest of the application code
COPY . .

COPY ./src/scripts/start.sh /start.sh
COPY ./src/app /app

# Install poetry
RUN pip install --no-cache-dir poetry

# RUN poetry config virtualenvs.in-project true

# Install dependencies (with dev dependencies)
RUN poetry install 
# Install dependencies (without dev dependencies)
# RUN poetry install --only main --no-interaction --no-ansi



EXPOSE 80

# Specify the command to run the app (modify as needed)
CMD ["poetry", "run", "python", "main.py"]
# CMD ["/start.sh"]