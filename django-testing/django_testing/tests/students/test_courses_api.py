import pytest
from django.urls import reverse
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT


# проверка получения одного курса
@pytest.mark.django_db
def test_new_course(client, course_factory):
    # создаём один курс
    course = course_factory()
    url = reverse("courses-list")
    # совершаем запрос GET к API по URL
    resp = client.get(url)
    resp_json = resp.json()
    assert resp.status_code == HTTP_200_OK
    assert resp_json
    test_course = resp_json[0]
    # проверяем, что вернулся именно тот курс, который запрашивали
    assert test_course['name'] == course.name


# проверка получения списка курсов
@pytest.mark.django_db
def test_courses_list(client, course_factory):
    # создаём десять курсов
    courses = course_factory(_quantity=10)
    url = reverse("courses-list")
    # совершаем запрос GET к API по URL
    resp = client.get(url)
    resp_json = resp.json()
    assert resp.status_code == HTTP_200_OK
    assert resp_json
    # проверяем, что вернувшийся json содержит десять записей
    assert len(resp_json) == 10


# assert resp_json["results"]
# results = resp_json["results"]
# assert len(results) == 2

# проверка фильтрации списка курсов по id
@pytest.mark.django_db
def test_filter_course_id(client, course_factory):
    # создаём десять курсов
    courses = course_factory(_quantity=10)
    url = reverse("courses-list")
    test_id = 9
    # прописываем в URL id = 9 (для примера),можно любой от 1 до 10
    # совершаем запрос GET к API по URL
    resp = client.get(url, args=[test_id])
    resp_json = resp.json()
    assert resp.status_code == HTTP_200_OK
    assert resp_json


# проверка фильтрации списка курсов по name
@pytest.mark.django_db
def test_filter_course_name(client, course_factory):
    # создаём курс
    name = 'I-am-TEST-name'
    course = course_factory(name=name)
    url = reverse("courses-list")
    # прописываем в URL название курса (name), по которому будет
    # производиться фильтрация
    # совершаем запрос GET к API по URL
    resp = client.get(url, {'name': name})
    resp_json = resp.json()
    assert resp.status_code == HTTP_200_OK
    assert resp_json[0]['name'] == name


# тест успешного создания курса
@pytest.mark.django_db
def test_new_course_creation(client):
    # создаём один курс
    url = reverse("courses-list")
    new_test_course = {
        'name': 'TEST 12345'
    }
    # совершаем запрос POST к API по URL
    resp = client.post(url, new_test_course)
    # проверяем код ответа,
    # если курс создан успешно, код будет 201
    assert resp.status_code == HTTP_201_CREATED


@pytest.mark.django_db
def test_update_course(client, course_factory):
    # создаём курс
    name = 'TEST-name'
    course = course_factory(name=name)
    url1 = reverse("courses-list")
    resp1 = client.get(url1, {'name': name})
    resp1_json = resp1.json()
    assert resp1_json
    test_id = resp1_json[0]['id']
    # создаём словарь с небходимыми изменениями
    updated_info = {
        'name': 'UPDATED test name'
    }
    url2 = reverse('courses-detail', args=[test_id])
    # совершаем запрос PATCH к API по URL
    resp2 = client.patch(url2, updated_info)
    resp2_json = resp2.json()
    assert resp2.status_code == HTTP_200_OK
    assert resp2_json
    assert resp2_json['name'] == updated_info['name']


# тест успешного удаления курса
@pytest.mark.django_db
def test_delete_course(client, course_factory):
    # создаём курс
    name = 'Deleted_course'
    course = course_factory(name=name)
    url1 = reverse("courses-list")
    resp1 = client.get(url1, {'name': name})
    resp1_json = resp1.json()
    assert resp1_json
    test_id = resp1_json[0]['id']

    url2 = reverse('courses-detail', args=[test_id])
    # совершаем запрос DELETE к API по URL
    resp2 = client.delete(url2)
    assert resp2.status_code == HTTP_204_NO_CONTENT
    resp3 = client.get(url1, {'name': name})
    assert resp3.json() == []

