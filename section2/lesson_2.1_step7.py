from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    #берем значение атрибута
    sunduk_element = browser.find_element_by_id("treasure")
    sunduk_value = sunduk_element.get_attribute("valuex")
    print(sunduk_value)
    x = calc(sunduk_value)

    #вставляем результат мат выражения
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(x)

    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()

    option2 = browser.find_element_by_id("robotsRule")
    option2.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
