# Utils for traversing through DOM and getting related webelements
from typing import List

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


def get_parent(child_element: WebElement) -> WebElement:
    return child_element.find_element(By.XPATH, '..')


def get_grandparent(grandchild_element: WebElement) -> WebElement:
    return grandchild_element.find_element(By.XPATH, '../..')


def get_children(parent_element: WebElement) -> List[WebElement]:
    return parent_element.find_elements(By.XPATH, '*')