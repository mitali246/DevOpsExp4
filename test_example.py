import pytest
from selenium import webdriver

def test_website_title():
    driver = webdriver.Safari()   # switched from Chrome → Safari
    driver.get("https://www.google.com")
    assert "Google" in driver.title
    driver.quit()
