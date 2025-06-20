import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    # Télécharge et utilise le ChromeDriver 137 compatible
    service = Service(ChromeDriverManager(driver_version="137.0.7151.119").install())
    drv = webdriver.Chrome(service=service)
    drv.maximize_window()
    yield drv
    drv.quit()

def test_app_login(driver):
    # 1. Charger la page de login de l'app Flask
    driver.get("http://localhost:5000/login")

    # 2. Saisir les identifiants valides
    driver.find_element(By.NAME, "username").send_keys("tomsmith")
    driver.find_element(By.NAME, "password").send_keys("SuperSecretPassword!")

    # 3. Cliquer sur Login
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # 4. Vérifier le message de bienvenue sur /index
    heading = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.TAG_NAME, "h1"))
    ).text
    assert "Bienvenue" in heading
