créer la base de donné sur postgres (sans créer de tables)

unzip postgresTest.rar et ouvrir le dossier

python -m venv env

pip install -r requirements.txt


pour spécifier les paramètres du db:
postgresTest\postgresTest\.env


python manage.py makemigrations

python manage.py migrate

python manage.py runserver


vérifier la table network dans la bd et ajouter quelques lignes


voir l'url http://127.0.0.1:8000/testdb/network/
