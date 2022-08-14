def test_community_link():
    driver = start_page()
    community_button = driver.find_element(By.XPATH, "//li[@class='shop-meta ']/a")
    community_button.click()
    community_title = driver.find_element(By.XPATH, "//*[@id='the-python-community']/h1")
    assert community_title.is_displayed(), "Отсутствует"
    assert community_title.text == "The Python Community"


def test_docs_side_menu_collapse():
    driver = start_page()
    docs_link = driver.find_element(By.XPATH, "//div[@class='small-widget documentation-widget']//a")
    assert docs_link.size != 0, "Ссылка не была найдена"
    assert docs_link.is_displayed(), "Ссылка не видна"
    docs_link.click()
    documentation_parts = driver.find_element(By.XPATH, "//*[text()='Parts of the documentation:']")
    assert documentation_parts.size != 0, "Не на странице документации"
    side_menu_arrow = driver.find_element(By.XPATH, "//*[@id='sidebarbutton']")
    side_menu = driver.find_element(By.XPATH, "//div[@class='sphinxsidebarwrapper']")
    side_menu_arrow.click()
    assert not side_menu.is_displayed(), "Меню всё еще видно"


def test_search_python_documentation():
    driver = start_page()
    search = driver.find_element(By.XPATH, "//input[@id='id-search-field']")
    assert search.is_displayed(), "Нет поиска на главной страницы"
    search.send_keys("Download Python 2.5.3 Documentation")
    button_search = driver.find_element(By.XPATH, "//button[@type='submit']")
    button_search.click()
    documentation_tab = driver.find_element(By.XPATH, "// a[ @ href = '/doc/2.5.3/download']")
    assert documentation_tab.is_displayed()
    documentation_tab.click()
    download_link = driver.find_element(By.XPATH, "//a[@class='reference external']")
    assert download_link.is_displayed()


def test_pop_up_window_appearance():
    driver = webdriver.Chrome(executable_path="../lib/chromedriver.exe")
    driver.maximize_window()
    driver.get("https://www.python.org/")
    news = driver.find_element(By.XPATH, "//*[@id='news']/a")
    assert news.is_displayed(), "Новостей нет на странице"
    element_in_window = driver.find_element(By.XPATH, "//*[@id='news']/ul/li[4]/a")
    action = ActionChains(driver)
    action.move_to_element(news).perform()
    action.click(element_in_window).perform()
    psf_news = driver.find_element(By.XPATH, "//*[text()='Distinguished Service Award Granted to Naomi Ceder']")
    assert psf_news.is_displayed(), "Не перешел на страницу PSF News"


def test_changelog_filter_search():
    driver = start_page()
    button_learn_more = driver.find_element(By.XPATH, "//div[@class='introduction']//a")
    assert button_learn_more.is_displayed(),"Кнопка 'Узнать больше' отсутствует на странице"
    button_learn_more.click()
    button_python_docs = driver.find_element(By.XPATH, "//*[@id='touchnav-wrapper']/header/div/div[2]/div/p[3]/a")
    assert button_python_docs.is_displayed(),"Не перешли на страницу 'Узнать больше'"
    button_python_docs.click()
    link_whats_new_in_python = driver.find_element(By.XPATH, "//p[@class='biglink']/a")
    assert link_whats_new_in_python.is_displayed(), "Не перешли на страницу 'python docs'"
    link_whats_new_in_python.click()
    link_on_changelog = driver.find_element(By.XPATH, "//*[@id='what-s-new-in-python-3-10']/p/a/span")
    assert link_on_changelog.is_displayed(), 'Не перешли на страницу "Whats new in Python 3.10?"'
    link_on_changelog.click()
    filter_search = driver.find_element(By.XPATH, "//*[@id='searchbox']")
    button_filter = driver.find_element(By.XPATH, "//*[@id='searchbox-submit']")
    assert filter_search.is_displayed(), "Поиска нет на странице"
    filter_search.send_keys("2020")
    button_filter.click()
    link_python_3_10_0 = driver.find_element(By.XPATH, "//*[@id='python-3-10-0-alpha-1']/h2")
    link_python_3_9_0 = driver.find_element(By.XPATH, "//*[@id='python-3-9-0-alpha-6']/h2")
    assert link_python_3_10_0.is_displayed(), "Поиск работает некорректно"
    assert link_python_3_9_0.is_displayed(), "Поиск работает некорректно"