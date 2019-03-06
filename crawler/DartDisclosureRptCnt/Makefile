clean:
	rm -rf src/__pycache__
	rm -rf src/__init__.py
	rm -rf src/modules/__pycache__

fetch-dependencies:
	mkdir -p bin/

	# Get Chromedriver
	curl -SL https://chromedriver.storage.googleapis.com/2.42/chromedriver_linux64.zip > chromedriver.zip
	unzip chromedriver.zip -d bin/
 
	# Get Headless-chrome
	curl -SL https://github.com/adieuadieu/serverless-chrome/releases/download/v1.0.0-53/stable-headless-chromium-amazonlinux-2017-03.zip > headless-chromium.zip
	unzip headless-chromium.zip -d bin/

	# Clean
	rm headless-chromium.zip chromedriver.zip

delete-dependencies:
	rm -rf bin/

docker-build:
	docker build --force-rm=true --no-cache=false -t [AWS_ACCOUNT_ID].dkr.ecr.ap-northeast-2.amazonaws.com/dart-disclosure-crawler:latest .
	docker rmi $$(docker images -f "dangling=true" -q)

docker-run:
	docker run --rm -it [AWS_ACCOUNT_ID].dkr.ecr.ap-northeast-2.amazonaws.com/dart-disclosure-crawler:latest

docker-push: clean
	$$(aws ecr get-login --no-include-email --region ap-northeast-2)
	docker push [AWS_ACCOUNT_ID].dkr.ecr.ap-northeast-2.amazonaws.com/dart-disclosure-crawler:latest