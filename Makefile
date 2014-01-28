all: runaftersetup

runserver: manage.py
	. gifsong/bin/activate && \
	foreman start

runaftersetup: reqs
	. gifsong/bin/activate && \
	foreman start

reqs: cmod
	. gifsong/bin/activate && \
        pip install -r requirements.txt

cmod: venv
	chmod +x gifsong/bin/activate

venv: manage.py
	virtualenv gifsong --distribute --no-site-packages




