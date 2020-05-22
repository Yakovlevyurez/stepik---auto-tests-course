from selenium import webdriver
import time

link = "http://suninjuly.github.io/selects1.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("num1")
    num1 = x_element.text

    y_element = browser.find_element_by_id("num2")
    num2 = y_element.text

    summa = int(num1) + int(num2)
    print(summa)

    from selenium.webdriver.support.ui import Select
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(summa))

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
