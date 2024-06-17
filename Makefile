all:
	@mkdir -p ./srcs/db
	@docker compose -f srcs/docker-compose.yml up --build #-d

clean:
	@docker compose -f srcs/docker-compose.yml stop

fclean: clean
	@docker compose -f srcs/docker-compose.yml down
	@docker volume rm django_skeleton_db django_skeleton_app || echo "no volume to delete"
	@sudo rm -rf ./srcs/db

re: fclean all
