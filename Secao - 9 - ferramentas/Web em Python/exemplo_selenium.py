
from selenium import webdriver
from selenium.webdriver.common.by import By

# Abre o navegador e pesquisa no Google
navegador = webdriver.Chrome()
navegador.get("https://google.com")
navegador.find_element(By.NAME, "q").send_keys("Python Selenium")
navegador.find_element(By.NAME, "q").submit()

navegador.quit()
