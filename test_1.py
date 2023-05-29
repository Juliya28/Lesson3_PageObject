from testpage import Operations
import logging
import time


def test_step1(browser):
    
    logging.info('Starting')
    testpage = Operations(browser)
    testpage.go_to_site()
    testpage.enter_login('testtest1')
    testpage.enter_pass('c23b2ed66e')
    testpage.click_login_button()
    testpage.click_contact_button()
    time.sleep(2)
    testpage.enter_name('Ivanov Ivan')
    testpage.enter_email('ivanov.privet@mail.ru')
    testpage.enter_content('information')
    time.sleep(2)
    testpage.click_contact_button3()
    time.sleep(2)
    assert testpage.alert() == 'Form successfully submitted'