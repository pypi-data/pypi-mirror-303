FROM python:3.12-alpine
WORKDIR /usr/src/app
COPY . .
RUN SETUPTOOLS_SCM_PRETEND_VERSION=1 python -m pip install --no-cache-dir .
CMD ["python", "-m", "minder.research_data_snapshots"]
