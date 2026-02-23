.PHONY: ps psa stop start compose-up

ps:
	docker ps

psa:
	docker ps -a

sta:
	docker start $(filter-out $@,$(MAKECMDGOALS))

sto:
	docker stop $(filter-out $@,$(MAKECMDGOALS))


compose-up:
	docker compose up -d
