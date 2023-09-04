APP = comundevops-restapi

test:
	@bandit -r . -x '*/.venv/*','*/tests/*'
	@black .
	@flake8 . --exclude .venv
	@pytest -v --disable-warnings

compose:
	@docker-compose build
	@docker-compose up
	

setup-dev:
	@kind create cluster --config kubernetes/config/config.yaml
	@kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/kind/deploy.yaml
	@kubectl wait --namespace ingress-nginx \
		--for=condition=ready pod \
		--selector=app.kubernetes.io/component=controller \
		--timeout=1300s
	@helm upgrade \
		--install \
		--set image.tag=5.0.8 \
		--set auth.rootPassword="root" \
		mongodb kubernetes/charts/mongodb
	@kubectl wait \
		--for=condition=ready pod \
		--selector=app.kubernetes.io/component=mongodb \
		--timeout=1300s

teardown-dev:
	@kind delete clusters kind