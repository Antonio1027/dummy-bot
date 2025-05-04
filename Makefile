build-image:
	docker build -t dummy_bot .

setup-container:
	docker run -d --name commercial_agent -p 80:80 dummy_bot

setup-local:
	cd src && python3 -m venv .venv && source .venv/bin/activate && pip3 install -r requirements.txt && fastapi dev server.py

start-local-server:
	fastapi dev src/server.py

deploy-service:
	cd infraestructure && terraform init && terraform apply -auto-approve

destroy-service:
	cd infraestructure && terraform init && terraform destroy -auto-approve
