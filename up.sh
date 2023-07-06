for i in "home/static/" "home/templates/" "lesgv/settings/" "lesgv/static/" "lesgv/templates/" "search/"
do
  echo $i
  rsync -a /mnt/d/work/wagtail/lesgv/$i /home/mannchri/wagtail/lesgv/$i
done
for i in "home" "lesgv" 
do
  echo $i
  rm /home/mannchri/wagtail/lesgv/$i/*.py
  cp -a /mnt/d/work/wagtail/lesgv/$i/*.py /home/mannchri/wagtail/lesgv/$i/
done
cp /mnt/d/work/wagtail/lesgv/* /home/mannchri/wagtail/lesgv/
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8000