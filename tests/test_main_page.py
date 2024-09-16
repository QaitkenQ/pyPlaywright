import pytest, allure

@allure.feature('Test Main Page')
@allure.story('Verify the header')
@allure.title('Verify the correct list of options are shown')
def test_1(main_page):
    with allure.step('Open main Page'):
        main_page.navigate()
    with allure.step('Verify list of options'):
        main_page.ver_links()


@allure.feature('Test Main Page')
@allure.story('Verify the header')
@allure.title('Verify the correct quantity is shown')
def test_2(main_page):
    with allure.step('Open main Page'):
        main_page.navigate()
    with allure.step('Verify the number is incorrect'):
        main_page.ver_links_fail()