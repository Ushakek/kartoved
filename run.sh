run_server:
	# rm -vf __pycache__/*
	source .venv/bin/activate
	./manage.py migrate
	pip install -r requirements.txt
	./manage.py runserver

