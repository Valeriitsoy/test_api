# API Testing Project for JSONPlaceholder

Этот проект содержит автоматизированные тесты для API JSONPlaceholder (https://jsonplaceholder.typicode.com/) с использованием Python и Pytest.

## Технологии

- Python 3.12
- Pytest
- Requests
- Allure для отчетности

## CI/CD

В этом проекте настроены GitHub Actions для автоматизации процессов CI/CD.

1. Перейдите на вкладку "Actions" в репозитории
2. Перейдите на tets_api
3. Нажать кнопку Run workflow

### Allure отчеты

После каждого запуска тестов автоматически генерируются отчеты Allure.

Для просмотра последнего отчета Allure:

1. Перейдите на вкладку "Actions" в репозитории
2. All workflows
3. Выберите последний pages build deployment
4. build -> deploy -> link

## Установка и запуск

1. Клонируйте репозиторий:

https://github.com/Valeriitsoy/test_api.git

2. Перейдите в директорию проекта:

cd test_api

3. Установите зависимости:

pip install -r requirements.txt

4. Запустите тесты (возможен опциональный запуск тестов на разном окружение, default=chromium):

pytest --alluredir=allure-results

5. Для генерации Allure-отчета выполните:

allure serve allure-results


## Группы тестов

Тесты разделены на две основные группы:

- Smoke тесты: `pytest -m smoke`
- Regression тесты: `pytest -m regress`

## Отчетность (локально)

Проект использует Allure для генерации подробных отчетов о выполнении тестов.
После запуска тестов вы можете просмотреть отчет, выполнив команду `allure serve allure-results`.


