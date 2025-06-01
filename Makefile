dev:
	fastapi dev main.py

run:
	python3 main.py

test:
	pytest tests/

lint:
	flake8 .

install:
	pip3 install -r requirements.txt