# SubHub api

## Стек

- Python 3.12
- Django + Django REST Framework
- Docker
- MinIO
- Gunicorn
- Redis + Celery

---

## Метрики

- Prometheus + Grafana

---

## Деплой (Docker)

```bash
git clone https://github.com/Specboss/subhub-api.git
cd subhub-api
cp .env_example .env
sudo docker compose -f local-compose.yml up -d --build
