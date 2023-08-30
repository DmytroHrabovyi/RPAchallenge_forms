from selenium.webdriver.common.by import By
from mapper import Mapper


class Driver:
    def __init__(self, driver, website):
        self.driver = driver
        self.driver.get(website)
        self.driver.maximize_window()

    def upload_data(self, data: dict, mapper: Mapper):
        start_button = self.driver.find_element(By.XPATH, '/html/body/app-root/div[2]/app-rpa1/div/div[1]/div[6]/button')
        start_button.click()

        max_value = 0
        for value in data.values():
            if len(value) > max_value:
                max_value = len(value)

        for i in range(0, max_value):
            for key, value in data.items():
                xpath = mapper.get_xpath(key)
                if not xpath:
                    continue
                field = self.driver.find_element(By.XPATH, f'//*[@ng-reflect-name="{xpath}"]')
                field.click()
                field.send_keys(value[i])
            submit_button = self.driver.find_element(By.CLASS_NAME, 'btn.uiColorButton')
            submit_button.click()
