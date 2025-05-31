FROM python:3.10-slim

WORKDIR /app

COPY viaje.py .

# Solución: Desactiva barra de progreso y simplifica instalación
RUN pip install --no-cache-dir --progress-bar off requests

CMD ["python", "viaje.py"]

