APP = retapi

test:
	@flake8 . --exclude .venv
	@pytest -v --disable-warnings

compose:
	@docker-compose build
	@docker-compose up
	

heroku:
	@heroku container:login
	@heroku container:push -a comundevops-restapi web
	@heroku container:release -a comundevops-restapi web