# Todo
# 1. Create Django Project (project name: Room8_ScreenSavor)
# 2. Change Database to MySQL
# 'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'screensavor',
#         'USER': 'root',
#         'PASSWORD': '',
#         'HOST': 'localhost',
#         'PORT': '3306',
#         'OPTIONS': {'init_command': "SET SQL_MODE='STRICT_TRANS_TABLES'"}
# 3. Install mysqlclient (done)
# - Create Database locally
# 4. Migrate: py manage.py migrate
# 5. Create Super User: py manage.py createsuperuser
# 6. Create 5 apps: py manage.py startapp <<app name>>
#           a. User    b. Movie    c.Recommendation  d.Review  e.Collection
# 7. Add Models (On the apps)
# 8. Migrate
# 9. Add Apps to settings.py
# 10. Submit

# Note:
# To make it work
# 1. Delete all migrations folder
# 2. Drop database and create it again
# 3. Run this for each app: py manage.py makemigrations <<appname>>
# 4. Migrate: py manage.py migrate
