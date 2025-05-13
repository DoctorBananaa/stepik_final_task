DOMAIN = 'selenium1py.pythonanywhere.com'

class LinkProtocol:
    HTTP = 'http://'
    HTTPS = 'https://'

class MainPageLinks:
    PRODUCT_LINK = f'{LinkProtocol.HTTPS}{DOMAIN}/en-gb/catalogue/coders-at-work_207/'
    MAIN_PAGE_LINK = f'{LinkProtocol.HTTP}{DOMAIN}/ru/'

class ProductPageLinks:
    PRODUCT_LINK = f'{LinkProtocol.HTTP}{DOMAIN}/en-gb/catalogue/coders-at-work_207/'