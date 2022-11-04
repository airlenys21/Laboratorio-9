from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome('C:/Users/Airlenys/OneDrive - Universidad Tecnológica de Panamá/Documentos/II Semestre/MANTENIMIENTO Y PRUEBAS DE SOFTWARE/Laboratorio-9/chromedriver.exe')
driver.maximize_window()
driver.delete_all_cookies()
driver.get("https://www.amazon.com/")

barradebusqueda = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "field-keywords")))
time.sleep(2)

busqueda = ("HP Pavilon azul")
barradebusqueda.send_keys(busqueda)
time.sleep(2)

lupa = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "nav-search-submit-button")))
lupa.click()
time.sleep(2)

articulo = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/div/div/div/div[2]/div/div/div[1]/h2/a/span")))
articulo.click()
time.sleep(2)

time.sleep(100)
driver.close()