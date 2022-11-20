import pytest


@pytest.fixture()
def choice_user():
    user_id = 123
    return user_id

@pytest.fixture(scope='session' , autouse=True)
def open_browser():
    print('Я вызываюсь перед тестом!')

@pytest.fixture()
def configure_mobile_browser():
    """Устанавливает мобильное соотношение сторон браузера"""
    print('Я мобильный')

@pytest.fixture()
def configure_desktop_browser():
    """Устанавливает десктопное соотношение сторон браузера"""
    print('Я десктопный')


# Авторизуемся в github
# Создаем репозиторий
# Открываем readme


def test_first(configure_mobile_browser):
    pass


def test_second(configure_desktop_browser):
    assert 1 == 1


def test_third(choice_user):
    print(choice_user)
    assert choice_user == 123
