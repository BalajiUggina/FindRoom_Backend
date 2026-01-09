#!/usr/bin/env bash
set -o errexit

echo "Starting FindRoom backend..."

# Apply database migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Start Gunicorn
gunicorn config.wsgi:application
