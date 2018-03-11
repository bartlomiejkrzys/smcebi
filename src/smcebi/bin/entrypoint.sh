#!/bin/bash
project_path=/code/smcebi

pass="${SMCEBI_ADMIN_PASSWORD:-smcebiadmin}"
user="${SMCEBI_ADMIN_USERNAME:-root}"
email="${SMCEBI_ADMIN_EMAIL:-admin@admin.com}"

timeout=1
timeout_limit=180
connected=false

echo "INFO: Starting SMCEBI_MAP application.."

echo "INFO: Database URI: '$POSTGRES_HOSTNAME:$POSTGRES_PORT'"

while ! python $project_path/manage.py makemigrations 2>/dev/null | python $project_path/manage.py migrate 2>/dev/null; do
    if [ $timeout -ge $timeout_limit ]; then
        echo "ERROR: Database is still not ready, giving up.."
        exit 1
    fi
    echo "WARNING: Can't apply migrations. Are you sure that database is running?"
    timeout=$((timeout * 2))
    echo "INFO: Waiting for DB connection up for $timeout s"
    sleep $timeout
done

python $project_path/manage.py migrate 2>/dev/null

echo "INFO: Database connection up, migrations applied."

echo "INFO: Creating superuser. Username: $user Email: $email"

echo "from django.contrib.auth.models import User;  User.objects.filter(email='$email').delete();  User.objects.create_superuser('$user', '$email', '$pass')" | python $project_path/manage.py shell

python $project_path/manage.py runserver 0.0.0.0:$DJANGO_PORT