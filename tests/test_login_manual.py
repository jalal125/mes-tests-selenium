import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="function")
def driver():
    # Initialise ChromeDriver en une seule fois par test
    service = Service(ChromeDriverManager(driver_version="137.0.7151.119").install())
    drv = webdriver.Chrome(service=service)
    drv.maximize_window()
    yield drv
    drv.quit()

def test_login_manual(driver):
    # 1. Aller sur la page de login
    driver.get("https://the-internet.herokuapp.com/login")

    # 2. Saisir nom d’utilisateur et mot de passe
    username = driver.find_element(By.ID, "username")
    password = driver.find_element(By.ID, "password")
    username.send_keys("tomsmith")
    password.send_keys("SuperSecretPassword!")

    # 3. Clic sur Login
    submit_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_btn.click()

    # 4. Vérification du message de succès
    flash = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".flash.success"))
    )
    assert "You logged into a secure area!" in flash.text
