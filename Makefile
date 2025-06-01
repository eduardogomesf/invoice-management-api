dev:
	fastapi dev main.py

run:
	uvicorn main:app --host 0.0.0.0 --port 8000

test:
	pytest tests/

lint:
	flake8 .

install:
	pip3 install -r requirements.txt