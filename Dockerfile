FROM python:3.10-slim-buster as base
RUN python -m pip install --upgrade pip
WORKDIR /app

FROM base as builder
RUN pip install poetry
COPY poetry.lock pyproject.toml /app/
RUN poetry install --no-dev --no-interaction --no-ansi && poetry export -f requirements.txt -o requirements.txt --with-credentials
COPY truck_manager truck_manager
RUN poetry build

FROM base as final
COPY --from=builder /app/requirements.txt requirements.txt
RUN pip install -r requirements.txt && rm requirements.txt
COPY --from=builder /app/dist/*.whl /app/dist/
RUN pip install /app/dist/*.whl && rm -rf /app/dist
EXPOSE 8000
CMD [ "uvicorn", "--host", "0.0.0.0", "--port", "8000", "truck_manager.main:app"]
