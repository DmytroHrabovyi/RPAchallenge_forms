from selenium import webdriver
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

url = 'https://rpachallenge.com/?lang=EN'
filename = 'data.xlsx'
download_url = 'https://rpachallenge.com/assets/downloadFiles/challenge.xlsx'

driver = Driver(webdriver.Chrome(), url)
DataManager.download_file(download_url, filename)
data = DataManager.extract_data(filename)
mapper = Mapper(xpath_field)
driver.upload_data(data, mapper)
