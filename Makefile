all: up

up:
	docker compose build
	docker compose up -d

logs:
	docker compose logs -f

close:
	docker compose stop

clean:
	docker compose down
	docker rmi tessaract-server-proxy
	docker rmi tessaract-server-tserver
