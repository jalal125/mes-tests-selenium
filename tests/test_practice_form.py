# tests/test_practice_form.py

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="function")
def driver():
    service = Service(ChromeDriverManager(driver_version="137.0.7151.119").install())
    drv = webdriver.Chrome(service=service)
    drv.maximize_window()
    yield drv
    drv.quit()

def test_practice_form(driver):
    # 1. Accéder au site
    driver.get("https://testautomationpractice.blogspot.com/")

    # 2. Remplir Name, Email, Phone
    inputs = driver.find_elements(By.CSS_SELECTOR, "input[type='text']")
    inputs[0].send_keys("Jalal Eddine Bouchrit")
    inputs[1].send_keys("jalal.bouchrit@example.com")
    inputs[2].send_keys("0612345678")

    # 3. Remplir l'adresse
    driver.find_element(By.TAG_NAME, "textarea") \
          .send_keys("1 rue de Paris, 75000 Paris")

    # 4. Sélectionner le pays
    Select(driver.find_element(By.ID, "country")) \
        .select_by_visible_text("France")

    # 5. Choisir Gender (premier radio = Male)
    driver.find_elements(By.CSS_SELECTOR, "input[type='radio']")[0].click()

    # 6. Cocher la première checkbox (Automation Tester)
    driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")[0].click()

    # 7. Soumettre le formulaire
    submit_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_btn.click()

    # 8. Vérifier que le bouton Submit est toujours présent et activable
    assert driver.find_element(By.CSS_SELECTOR, "button[type='submit']").is_enabled()
