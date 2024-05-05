from selenium import webdriver
import time
# import requests


def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    # options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)

    driver.get("https://www.jobs.bg/front_job_search.php?subm=1&categories%5B%5D=56&techs%5B%5D=Python&last=5")


    time.sleep(1)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    jobs_list_container = driver.find_element(
        by="xpath",
        value='//*[@id="fav-popup-dialog"]/div[1]/div[2]/div[2]/button[1]/div',
    ).click()
    time.sleep(20)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

    jobs_list_container = driver.find_element(
        by="xpath",
        value='//*[@id="listContainer"]',
    )
    time.sleep(2)

    
    # print(jobs_list_container.find_element)
    ul_count = len(jobs_list_container.find_elements(by="xpath", value='./ul'))

    print("Number of ul elements:", ul_count)


    driver.quit()

get_driver()