from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import HTMLTestRunner
import unittest, time

class main_script(unittest.TestCase):
    driver = webdriver.Firefox()
    driver.get("http://www.cskud.com")

    def test01_script(self):
        browser = self.driver
        print "Open Me Page"
        browser.find_element_by_id("mainimg")
        browser.close()

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(main_script))
    dateTimeStamp = time.strftime("%Y%m%d_%H_%M_%S")
    buf = file("report\TestReport" + "_" + dateTimeStamp + ".html", "wb")
    runner = HTMLTestRunner.HTMLTestRunner(
        stream = buf,
        title = "Test the Report",
        description = "Result of tests"
    )
    runner.run(suite)