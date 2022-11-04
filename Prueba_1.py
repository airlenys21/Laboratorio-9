from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome('C:/Users/riuni/OneDrive/Escritorio/Portafolio de las materias/Portafolio de Mantenimiento & Pruebas/4. Actividades Desarrolladas durante el curso/3. Laboratorios/Lab 9/chromedriver.exe')
driver.maximize_window()
driver.delete_all_cookies()
driver.get("https://www.amazon.com/")

time.sleep(100)
driver.close()