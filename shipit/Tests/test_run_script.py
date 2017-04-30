from selenium import webdriver

from AddressDao import Addressdao

import Address

from config import config

from selenium.webdriver.support.ui import WebDriverWait

import unittest

class clicknameTest(unittest.TestCase):


    def test_click(self):
        db_values = []

        self.driver = webdriver.Firefox()
        self.driver.get("http://localhost:8080/index.html")
        vzfield = '//*[@id="package-table"]/tbody/tr[4]/td[4]'
        click_vz = WebDriverWait(self.driver, 5).until(lambda driver: driver.find_element_by_xpath(vzfield))
        # vz_value = self.driver.find_element_by_xpath(vzfield)
        click_vz.click()
        # print(vz_value.get_attribute('id'))
        dst_id = self.driver.find_element_by_id("detail_dst_id")
        dst_person = self.driver.find_element_by_id("detail_dst_name")
        dst_street = self.driver.find_element_by_id("detail_dst_street")
        dst_state = self.driver.find_element_by_id("detail_dst_state")
        dst_zip = self.driver.find_element_by_id("detail_dst_zip")

        addressdao = Addressdao(**config)
        address = addressdao.query_address(dst_id.get_attribute('value'))

        self.assertEqual(str(address.adrid), dst_id.get_attribute('value'))

        # # separating string given from address object into a list
        # for word in repr(address).split(','):
        #     db_values.append(word)
        # print(db_values)
        # self.assertEqual(db_values[0], dst_id.get_attribute('value'))
        # self.assertEqual(db_values[1], dst_person.get_attribute('value'))
        # self.assertEqual(db_values[2], dst_street.get_attribute('value'))
        # self.assertEqual(db_values[3], dst_zip.get_attribute('value'))
        # self.assertEqual(db_values[5], dst_state.get_attribute('value'))

    def stoptest(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

