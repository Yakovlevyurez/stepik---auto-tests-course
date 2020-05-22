import pytest
from selenium import webdriver
import time
import math


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('number', ["236898", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_many_links(browser, number):
    link = f"https://stepik.org/lesson/{number}/step/1/"
    browser.get(link)
    browser.implicitly_wait(5)
    answer = math.log(int(time.time()))

    input_answer = browser.find_element_by_css_selector('[placeholder="Type your answer here..."]')
    input_answer.send_keys(str(answer))

    button = browser.find_element_by_css_selector(".submit-submission")
    button.click()

    feedback = browser.find_element_by_css_selector(".smart-hints__hint")
    feedback_text = feedback.text

    assert ("Correct!" == feedback_text)



