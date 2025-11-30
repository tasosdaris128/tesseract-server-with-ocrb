all: up

up:
	docker compose build
	docker compose up -d

close:
	docker compose stop

clean:
	docker compose down
	docker rmi tessaract-server-tserver
