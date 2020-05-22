from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_css_selector('[placeholder="Enter first name"]')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector('[placeholder="Enter last name"]')
    input2.send_keys("Ivanov")
    input3 = browser.find_element_by_css_selector('[placeholder="Enter email"]')
    input3.send_keys("912030123123")

    option1 = browser.find_element_by_id("file")
    #option1.send_keys('/Users/yuriy/PycharmProjects/selenium_course/file_for_2_2_step8')

    # получаем путь к директории текущего исполняемого файла
    current_dir = os.path.abspath(os.path.dirname(__file__))


    # добавляем к этому пути имя файла
    file_path = os.path.join(current_dir, 'file_for_2_2_step8')
    option1.send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
