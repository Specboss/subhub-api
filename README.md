# 🖼️ SubHub api

Сервис для загрузки стоматологических 3D-данных, хранения в MinIO, вызова скрипта построения тепловых карт (ТКО), и получения статуса обработки.

## 📦 Стек

- Python 3.12
- Django + Django REST Framework
- Docker + Docker Compose
- MinIO (s3 совместимое хранилище)
- Gunicorn

---

## 🚀 Быстрый старт (Docker)

```bash
git clone https://gitlab.ronix.ru/picasso-storage-service.git
cd picasso-storage-service
cp .env.example .env
sudo docker compose up -d --build
