"""
Simple Page Object Model for the www.automationpractice.pl website
"""

ALERT_DANGER_CSS = ".alert.alert-danger"
ALERT_SUCCESS_CSS = ".alert.alert-success"
AVAILABLE_DIF_CSS = ".available-dif"
CART_EMPTY_CSS = ".cart_block_no_products"
CREATE_FNAME_NAME = "customer_firstname"
CREATE_LNAME_NAME = "customer_lastname"
DRESSES_XPATH = "//*[contains(@class, 'sf-with-ul') and contains(text(), 'Dresses')]"
EMAIL_LOGIN_NAME = "email"
EMAIL_CREATE_NAME = "email_create"
EMPTY_CART_XPATH = (
    "//*[contains(@class, 'ajax_cart_no_product') and contains(text(), '(empty)')]"
)
EXAMPLE_DRESS_HREF = (
    "http://www.automationpractice.pl/index.php?id_product=7&amp;controller=product"
)
HOME_PAGE_HREF = "http://www.automationpractice.pl/index.php"
LOGIN_PAGE_HREF = "http://www.automationpractice.pl/index.php?controller=authentication&back=my-account"
PRODUCT_CONTAINER_CLASS = "product-container"
PSWD_LOGIN_NAME = "passwd"
SUBMIT_LOGIN_NAME = "SubmitLogin"
SUBMIT_CREATE_NAME = "SubmitCreate"
REGISTER_ACCOUNT_NAME = "submitAccount"
