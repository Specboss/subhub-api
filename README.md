# 🖼️ SubHub api

## 📦 Стек

- Python 3.12
- Django + Django REST Framework
- Docker
- MinIO (s3 совместимое хранилище)
- Gunicorn
- Redis + Celery

---

## 📦 Метрики

- Prometheus + Grafana

---

## 🚀 Быстрый старт (Docker)

```bash
git clone https://github.com/Specboss/subhub-api.git
cd subhub-api
cp .env_example .env
sudo docker compose -f local-compose.yml up -d --build
