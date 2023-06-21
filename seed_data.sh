rm -rf tzadik_api/migrations
rm db.sqlite3
python manage.py migrate
python manage.py makemigrations tzadik_api
python manage.py migrate tzadik_api
python manage.py loaddata users tokens modified_users artists categories instruments orders performers statuses tracks albums album_performers ordered_albums artist_performers performer_instruments recommendations 
