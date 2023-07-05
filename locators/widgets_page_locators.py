from selenium.webdriver.common.by import By


class AccordianPageLocators:

    SECTION_1 = (By.CSS_SELECTOR, "#section1Heading")
    SECTION_1_CONTENT = (By.CSS_SELECTOR, "#section1Content p")
    SECTION_2 = (By.CSS_SELECTOR, "#section2Heading")
    SECTION_2_CONTENT = (By.CSS_SELECTOR, "#section2Content p")
    SECTION_3 = (By.CSS_SELECTOR, "#section3Heading")
    SECTION_3_CONTENT = (By.CSS_SELECTOR, "#section3Content p")