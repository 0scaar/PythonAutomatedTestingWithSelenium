from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import csv

driver = webdriver.Chrome("C:/WebDriver/chromedriver.exe")

url = "https://docs.google.com/forms/d/e/1FAIpQLSfhcJ90nvGzsWuIIGttoriaCyWpkhHL1mNfkSGWx8t0Ezi5ig/viewform"

driver.get(url)

def fill_form(codigo, nombre, ciudad, estaDeAcuerdo):
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located)
    (
        (By.CLASS_NAME, "exportButtonContent")
    )

    inputs = driver.find_elements(By.CLASS_NAME, "whsOnd")
    radioButtons = driver.find_elements(By.CLASS_NAME, "Od2TWd")

    time.sleep(1)

    inputs_array = [
        codigo, nombre, ciudad
    ]

    for i in range(len(inputs)):
        inputs[i].clear()
        inputs[i].send_keys(inputs_array[i])

    for radio in radioButtons:
        if radio.get_attribute("data-value") == estaDeAcuerdo:
            radio.click()            

    time.sleep(1)

    submit = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
    submit.click()

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located)
    (
        (By.CLASS_NAME, "vHW8K")
    )

    another_response = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    another_response.click()

#fill_form("234534", "oscar", "sao paulo", "Si")
file = open("infoTest.csv")
reader = csv.reader(file, delimiter=";")

for row in reader:
    fill_form(row[0], row[1], row[2], row[3])
    
print("Completed")
driver.close()

input("Press ENTER to exit\n")