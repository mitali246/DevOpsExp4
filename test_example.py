import pytest
from selenium import webdriver

def test_website_title():
    driver = webdriver.Chrome() 

    driver.get("https://www.google.com")

    assert "Google" in driver.title

    driver.quit()