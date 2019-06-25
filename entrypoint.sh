echo "waiting for postgres"

while ! netcat -z db 5432; do
    sleep 0.1
done

python3 manage.py migrate

exit 0