from T9AutWeb import SwagLabs
import pytest

url = "https://www.saucedemo.com/"
slPage = SwagLabs(url)

#Testcase1 : To validate if login is working fine with valid credentials.
def test_valid_login():
    assert slPage.pageLogin() == True
#Testcase2 : To validate if web page details are matching the test data
def test_url_Details():
    test_data = ('Swag Labs', 'https://www.saucedemo.com/inventory.html')
    assert slPage.urlDetails() == test_data
#Testcase3 : To validate if webdrive is closing properly
def test_close():
    assert slPage.shutdown() == None
    print("Done with getting webpage details, BYE!!!")