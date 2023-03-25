build: clean
	docker-compose build

shell-redis:
	docker-compose exec redis redis-cli

shell-postgres:
	docker-compose exec postgres psql -Upostgres

up:
	docker-compose up -d

ps:
	docker-compose ps

down:
	docker-compose down --remove-orphans

test:
	pytest

clean: down
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +
