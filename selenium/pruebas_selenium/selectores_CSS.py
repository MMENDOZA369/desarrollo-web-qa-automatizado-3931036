from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

try:
    driver.get("http://localhost:5174/")

    titular = driver.find_element(By.CSS_SELECTOR , '.navbar-brand')

    assert titular.text == "Super Mega App", f"El texto del enlace es '{titular.text}', pero se esperaba 'Home'."

    print("La prueba pasó exitosamente.")


except Exception as e:
    print(f"Error en la prueba: {e}")

finally:
    time.sleep(6)
    driver.quit()