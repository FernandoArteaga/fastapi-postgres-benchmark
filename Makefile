include .env

start:
	@docker compose up -d

stop:
	@docker compose down

seed:
	@docker cp seed.sql fastapi-postgres-benchmark-postgres-1:/tmp/seed.sql
	@docker exec -it fastapi-postgres-benchmark-postgres-1 psql -U $(DB_USERNAME) -d $(DB_NAME) -f /tmp/seed.sql
