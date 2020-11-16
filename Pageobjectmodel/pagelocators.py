from selenium.webdriver.common.by import By

# for maintainability we separate web objects by page name

class MainPageLocators(object):

  COOMPANY_NAME = (By.ID, 'id_company_name')
  ADMIN_EMAIL= (By.ID, 'id_admin_email')
  ADMIN_FIRST_NAME = (By.ID, 'id_admin_first_name')
  ADMIN_LAST_NAME = (By.ID, 'id_admin_last_name')
  CYBER_ESSENTIALS = (By.XPATH, '// *[ @ id = "id_product_0"]')
  CYBER_ESSENTIALS_PLUS = (By.XPATH, '// *[ @ id = "id_product_1"]')
  CYBER_ESSENTIALS_GDPR= (By.XPATH, '// *[ @ id = "id_product_2"]')
  CYBER_ESSENTIALS_PLUS_GDPR = (By.XPATH, '// *[ @ id = "id_product_3"]')
  SUBMIT = (By.CSS, '/input[value='Submit']')


class SubmittedPageLocators(object):
    THANKYOU = (By.XPATH, '//div[normalize-space()= "Thank yoou"]')



