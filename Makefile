.PHONY: install
install:
	poetry install

.PHONY: start
start:
	poetry run python src/app/main.py

.PHONY: test
test:
	poetry run python -m pytest src/tests

.PHONY: build
build:
	docker-compose -f docker/docker-compose.yml build  

.PHONY: run
run:
	docker run -e MAX_WORKERS=2 -p 80:80 python_api

.PHONY: up
up: 
	docker-compose -f docker/docker-compose.yml up