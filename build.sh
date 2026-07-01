#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r requirements.txt

# Convert static asset files
python uv run manage.py collectstatic --no-input

# Apply any outstanding database migrations
uv run manage.py migrate
uv run manage.py populate_db
