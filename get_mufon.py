from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup
import csv

def get_table():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://mufoncms.com/cgi-bin/report_handler.pl?req=search_page')
    time.sleep(3)
    today_button = driver.find_element_by_xpath('/html/body/center/div[2]/form/table/tbody/tr[1]/td[2]/input[2]')
    today_button.click()
    time.sleep(1)
    submit_button = driver.find_element_by_xpath('/html/body/center/div[2]/form/input[2]')
    submit_button.click()
    time.sleep(3)
    page = BeautifulSoup(driver.page_source, 'html.parser')
    rows = page.select_one('form')
    headers = [th.text.encode('utf-8') for th in rows.select('tr th')]
    with open("ENV/out.csv", "w") as f:
        wr = csv.writer(f)
        wr.writerow(headers)
        wr.writerows([[td.text.encode("utf-8") for td in row.find_all("td")] for row in rows.select("tr + tr")])
