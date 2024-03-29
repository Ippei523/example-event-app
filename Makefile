dc = docker compose

.PHONY: setup rebuild build up ps down stop start restart logs

setup:
	@make up

rebuild:
	@make down
	@make build
	@make up

build:
	$(dc) build

up:
	$(dc) up -d

ps:
	$(dc) ps


down:
	$(dc) down

stop:
	$(dc) stop

start:
	$(dc) start

restart:
	$(dc) restart

logs:
	$(dc) logs -f