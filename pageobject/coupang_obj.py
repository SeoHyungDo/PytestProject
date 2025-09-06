from selenium.webdriver.common.by import By


class coupang_main :
    def __init__(self, driver):
        self.driver = driver

    favorite_name = (By.XPATH,'//*[@id="wa-bookmark"]')
    apply_store = (By.XPATH,'//*[@id="subscribeHeader"]/li[2]/a')
    apply_store_select_box = (By.XPATH, '//*[@id="subscribeHeader"]/li[2]/a')
    apply_store_select_box_data = (By.XPATH, '//*[@id="subscribeHeader"]/li[2]/p')

    def favorite_name_obj(self):
        return self.driver.find_element(*coupang_main.favorite_name)

    def apply_store_obj(self):
        return self.driver.find_element(*coupang_main.apply_store)

    def apply_store_select_box_obj(self):
        return self.driver.find_element(*coupang_main.apply_store_select_box)

    def apply_store_select_box_data_obj(self):

        return self.driver.find_element(*coupang_main.apply_store_select_box_data)