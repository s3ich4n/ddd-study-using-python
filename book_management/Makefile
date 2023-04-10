# PROD
build-prod: prod-clean
	docker compose -f production.yml build --no-cache
prod-shell-redis:
	docker compose -f production.yml exec redis redis-cli
prod-shell-postgres:
	docker compose -f production.yml exec postgres psql -Upostgres
prod-up:
	docker compose -f production.yml up -d
prod-ps:
	docker compose -f production.yml ps
prod-down:
	docker compose -f production.yml down --remove-orphans
prod-clean: prod-down
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

# DEV
build-dev: dev-clean
	docker compose -f local.yml build
build-dev-nocache: dev-clean
	docker compose -f local.yml build --no-cache
dev-shell-redis:
	docker compose -f local.yml exec redis redis-cli
dev-shell-postgres:
	docker compose -f local.yml exec postgres psql -Upostgres
dev-up:
	docker compose -f local.yml up -d
dev-ps:
	docker compose -f local.yml ps
dev-down:
	docker compose -f local.yml down --remove-orphans
dev-clean: dev-down
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

# TEST
#	TODO use pytest-docker-compose instead
test:
	docker compose -f local.yml create postgres
	docker compose -f local.yml start postgres
	sleep 5
	pytest
	docker compose -f local.yml stop postgres
	docker compose -f local.yml rm postgres -f

cov:
	pytest --cov=. tests/
cov-html:
	pytest --cov-report html --cov=. tests/
