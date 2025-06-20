import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_login_tomsmith():
    # 1. Initialisation du driver Chrome (force la version 137)
    service = Service(ChromeDriverManager(driver_version="137.0.7151.119").install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()

    # 2. Aller sur la page de login
    driver.get("https://the-internet.herokuapp.com/login")

    # 3. Saisir nom d’utilisateur et mot de passe
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")

    # 4. Cliquer sur le bouton Login
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # 5. Vérifier l’affichage du message de succès
    flash_text = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".flash.success"))
    ).text
    assert "You logged into a secure area!" in flash_text

    # 6. Fermer le navigateur
    driver.quit()
