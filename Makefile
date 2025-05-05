build-image:
	docker build -t dummy_bot .

setup-container:
	docker run -d --name commercial_agent -p 80:80 dummy_bot

lambda-layer:
	mkdir -p python && \
	pip3 install -r src/requirements.txt --platform manylinux2014_x86_64 --target python --only-binary=:all: && \
	zip -r9 dependencies.zip python

publish-lambda-layer:
	aws lambda publish-layer-version --layer-name test_layer --compatible-runtime python3.9 --compatible-architectures x86_64 --zip-file fileb://dependencies.zip --no-cli-pager

setup-local:
	cd src && \
	python3 -m venv .venv && \
	source .venv/bin/activate && \
	pip3 install -r requirements.txt && \
	fastapi dev server.py

deploy-service:
	cd infraestructure && terraform init && terraform apply -auto-approve

destroy-service:
	cd infraestructure && terraform init && terraform destroy -auto-approve
