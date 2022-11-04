from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
driver = webdriver.Chrome('C:/Users/Airlenys/OneDrive - Universidad Tecnológica de Panamá/Documentos/II Semestre/MANTENIMIENTO Y PRUEBAS DE SOFTWARE/Laboratorio-9/chromedriver.exe')
driver.maximize_window()
driver.delete_all_cookies()
driver.get("https://www.amazon.com/")


time.sleep(100)
driver.quit()