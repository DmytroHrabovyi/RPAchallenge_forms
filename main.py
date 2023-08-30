from selenium import webdriver
import time
from driver import Driver
from data_manager import DataManager
from mapper import Mapper

xpath_field = {
    'First Name': 'labelFirstName',
    'Last Name': 'labelLastName',
    'Company Name': 'labelCompanyName',
    'Role in Company': 'labelRole',
    'Address': 'labelAddress',
    'Email': 'labelEmail',
    'Phone Number': 'labelPhone'
}

driver = Driver(webdriver.Chrome(), 'https://rpachallenge.com/?lang=EN')
driver.download_data()
path = DataManager.get_file_path()
data = DataManager.extract_data(path)
mapper = Mapper(xpath_field)
driver.upload_data(data, mapper)
time.sleep(5)
