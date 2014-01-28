all: runaftersetup

runserver: manage.py
	. gifsong/bin/activate && \
	foreman start

runaftersetup: syncdb
	. gifsong/bin/activate && \
	foreman start

syncdb: reqs
	. gifsong/bin/activate && \
	python manage.py syncdb

reqs: cmod
	. gifsong/bin/activate && \
        pip install -r requirements.txt

cmod: venv
	chmod +x gifsong/bin/activate

venv: manage.py
	virtualenv gifsong --distribute --no-site-packages




