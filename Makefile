install:
	pip install --upgrade pip
	pip install -r requirements.txt

test:
	pip install --upgrade pip
	pip install -r tests_requirements.txt	
	py.test --verbose

lint:
	flake8 *.py app tests

format:
	black app

start-dev:
	make install
	flask --debug run -h 0.0.0.0 -p 5000

start-docker:
	docker compose --env-file .env -p swisscom \
		-f ./docker/docker-compose.yml up -d

stop-docker:
	docker compose -p swisscom -f ./docker/docker-compose.yml down

build-docker:
	docker build --env-file .env \
		-f docker/webapp/app.Dockerfile -t passwordfactory:latest .
	docker build -f docker/nginx/nginx.Dockerfile -t nginx:latest .