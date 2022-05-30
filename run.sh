run_server:
#	 rm -vf __pycache__/*
	source .venv/bin/activate
	pip install -r requirements.txt
	./manage.py migrate
	./manage.py runserver 0.0.0.0:8000 &

