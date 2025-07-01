# Use a Python 3.13 base (use a more specific image if available)
FROM python:3.13-slim

# Install uv
RUN pip install uv

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Set up the environment
RUN uv init --lib .
RUN uv python pin 3.13.2
RUN uv venv
RUN uv pip install -e .
RUN uv add icecream pillow uvicorn fastapi typing-extensions python-multipart PyPDF2 reportlab requests

COPY /app /app/src/loto

# Expose port
EXPOSE 8000

# Run the FastAPI app
CMD ["uv", "run", "uvicorn", "src.loto.main:app", "--reload", "--host", "0.0.0.0"]
