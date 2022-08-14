from selenium import webdriver
from selenium.webdriver.common.by import By


def start_page():
    driver = webdriver.Chrome(executable_path="..lib/chromedriver.exe)")
    driver.maximize_window()
    driver.get("https://www.python.org/")
    return driver


def test_pop_up_window_appearance():
    driver = start_page()
    hover = driver.find_element(By.XPATH, "//*[@id='news']/a")
    assert hover.is_displayed(), "Новостей нет на странице"




if __name__ == "__main__":
    test_pop_up_window_appearance()





