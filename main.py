from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement

import pickle
# import requests

def save_webdriver(webElement, filename):
    with open(filename, 'wb') as f:
        pickle.dump(webElement, f)


def filter_list_element(li_element: WebElement) -> bool:
    el_class = li_element.get_attribute("class")
    if not el_class:
        return False
    return el_class.isdigit()


def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    # options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument("--enable-javascript")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)

    # driver.get("https://www.jobs.bg/front_job_search.php?subm=1&categories%5B%5D=56&techs%5B%5D=Python&last=5")
    driver.get("http://127.0.0.1:5500/JOBS.BG%20-%20IT%20%D0%9E%D0%B1%D1%8F%D0%B2%D0%B8%20%D0%B7%D0%B0%20%D0%A0%D0%B0%D0%B1%D0%BE%D1%82%D0%B0%20%D1%81%20%D0%BA%D1%80%D0%B8%D1%82%D0%B5%D1%80%D0%B8%D0%B8_%20_Python_;%20%D0%9F%D0%BE%D1%81%D0%BB%D0%B5%D0%B4%D0%BD%D0%B8%D1%82%D0%B5%207%20%D0%B4%D0%BD%D0%B8.html")


    time.sleep(2)
    
    actions = ActionChains(driver)
    # Scroll down slowly
    for _ in range(1000):  # Adjust the range to control the scroll distance
        try:
            close_button = driver.find_element(
                by="xpath",
                value='//*[@id="fav-popup-dialog"]/div[1]/div[2]/div[2]/button[1]/div',
            )
        except:
            actions.send_keys(Keys.ARROW_DOWN).perform()
            time.sleep(0.001)  # Adjust the sleep time to control the scroll speed
        else:
            close_button.click()
            break


    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    
    time.sleep(5)
    for _ in range(1000):  # Adjust the range to control the scroll distance
        actions.send_keys(Keys.ARROW_DOWN).perform()
        time.sleep(0.001)  # Adjust the sleep time to control the scroll speed
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # time.sleep(2)

    jobs_list_container = driver.find_element(
        by="xpath",
        value='//*[@id="listContainer"]',
    )
    # time.sleep(2)
    # save_webdriver(jobs_list_container, "first_try.pkl")

    
    # print(jobs_list_container.find_element)
    ul_list = jobs_list_container.find_elements(by="xpath", value='./ul')
    jobs_list_container.get_attribute
    job_titles = []
    for ul in ul_list:
        li_list = ul.find_elements(by="xpath", value='./li')
        filtered_li_list = list(filter(filter_list_element, li_list))
        for li in filtered_li_list:
            job_title = li.find_element(by="class name", value="card-title").find_element(by="xpath", value="./span[2]").text
            company_name = li.find_element(by="class name", value="secondary-text").text
            skills_els = li.find_element(by="class name", value="card-tags").find_elements(by="xpath", value="./div/div")
            skills = []
            for skill_el in skills_els:
                try:
                    skill_name = skill_el.find_element(by="xpath", value="./img").get_attribute("alt")
                except:
                    pass
                else:
                    skills.append(skill_name)
                    continue
                try:
                    skill_name = skill_el.find_element(by="xpath", value="./div").text
                except:
                    pass
                else:
                    skills.append(skill_name)
                    
            print(job_title)
            print(company_name)
            print(skills)


    print(ul_list)


    driver.quit()

get_driver()