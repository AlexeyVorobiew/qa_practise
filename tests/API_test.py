import pytest
import allure
from data_for_test import key_header

@allure.feature('breeds search')
@allure.story('Тест поиска пород')
@pytest.mark.parametrize("breed", ['Aegean', 'sib', 'Balinese', 'Chartreux', 'Oriental'])
def test_search(api_request, breed):
    response = api_request.GET(path=f"/v1/breeds/search?q={breed}", headers=key_header)
    with allure.step("Запрос отправлен. Тест доступности"):
        assert response.status_code == 200

@allure.story('Проверка содержимого описания пород')
@pytest.mark.parametrize("breed", ['Aegean', 'sib', 'Balinese', 'Chartreux', 'Oriental'])
@pytest.mark.parametrize("field", ['description', 'temperament', 'wikipedia_url'])
def test_search_fields_check(api_request, breed, field):
    response = api_request.GET(path=f"/v1/breeds/search?q={breed}", headers=key_header)
    with allure.step("Проверка основных полей"):
        assert response.json()[0][f'{field}'] != None
        print(response.json()[0][f'{field}'])