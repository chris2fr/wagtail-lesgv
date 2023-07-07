for i in "home/static/" "home/templates/" "lesgv/settings/" "lesgv/static/" "lesgv/templates/" "search/"
do
  echo $i
  rsync -a /mnt/d/work/wagtail/wagtail-lesgv/$i /home/mannchri/wagtail/wagtail-lesgv/$i
done
for i in "home" "lesgv"
do
  echo $i
  rm /home/mannchri/wagtail/wagtail-lesgv/$i/*.py
  cp -a /mnt/d/work/wagtail/wagtail-lesgv/$i/*.py /home/mannchri/wagtail/wagtail-lesgv/$i/
done
cp /mnt/d/work/wagtail/wagtail-lesgv/* /home/mannchri/wagtail/wagtail-lesgv/
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --no-input
python manage.py runserver 0.0.0.0:8000