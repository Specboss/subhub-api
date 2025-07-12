# SubHub API

## 📦 Стек технологий

- **Язык:** Python 3.12  
- **Фреймворк:** Django + Django REST Framework  
- **Очереди:** Redis + Celery  
- **Хранилище файлов:** MinIO  
- **Контейнеризация:** Docker + Docker Compose  
- **WSGI сервер:** Gunicorn
- **Метрики и мониторинг:** Prometheus + Grafana  

---

## 📁 Структура конфигурации

- `.env` — переменные окружения для **продакшн-сборки**
- `.env.local` — переменные окружения для **локальной разработки**
- `prod.yml` — продовый Compose-файл
- `local.yml` — расширение для локального запуска

---

## 🚀 Деплой

### 🔧 Локальный запуск

```bash
git clone https://github.com/Specboss/subhub-api.git
cd subhub-api
cp .env_example .env.local
sudo docker compose -f local.yml up -d --build
```

### 🔧 Продакшн запуск

```bash
git clone https://github.com/Specboss/subhub-api.git
cd subhub-api
cp .env_example .env
sudo docker compose -f prod.yml up -d --build
```