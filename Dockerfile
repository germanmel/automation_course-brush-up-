FROM python:3.8-alpine

WORKDIR /tests_project/
#копируем из текущей корневой директории в корневую WORKDIR
COPY . .

RUN pip install -r requirements.txt

CMD pytest -m test --alluredir=allure_results
