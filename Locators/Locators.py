from selenium.webdriver.common.by import By


class RegisterLocators(object):
    REG_BTN = (By.XPATH, "//header/nav[1]/div[2]/div[5]/a[1]")
    SET_EMAIL = (By.XPATH, "//input[@id='username']")
    CONTINUE_EMAIL = (By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[3]/button[1]")
    NEW_PASSWORD = (By.XPATH, "//input[@id='new_password']")
    CONFIRM_PASSWORD = (By.XPATH, "//input[@id='confirmed_password']")
    CREATE_ACCOUNT = (By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/button[1]")
    FB_BTN = (By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[4]/div[2]/a[1]")
    GOOGLE_BTN = (By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[4]/div[2]/a[2]")
    MORE_WAYS_BTN = (By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[4]/div[3]")
    APPLE_BTN = (By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[4]/div[3]/a[1]")


class SigninLocators(object):
    SIGNIN_BTN = (By.XPATH, "//header/nav[1]/div[2]/div[6]/a[1]")
    INPUT_EMAIL = (By.XPATH, "//input[@id='username']")
    CONTINUE_EMAIL = (By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[3]/button[1]")
    ENTER_PASSWORD = (By.XPATH, "//*[@id='password']")
    CLICK_SIGNIN = (By.XPATH, "//*[@id='root']/div/div/div[2]/div[1]/div/div/div/div/div/div/form/button")


class StaysLocators(object):
    STAYS_BTN = (By.XPATH, "//body[1]/header[1]/nav[2]/ul[1]/li[1]/a[1]")
    PLACE_INPUT = (By.XPATH, "//input[@id='ss']")
    DATE_INPUT = (By.XPATH, "//body/div[1]/div[2]/div[1]/form[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/span[1]")
    PICK_CHECKIN_DATE = (By.XPATH,
                         "//body[1]/div[1]/div[2]/div[1]/form[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[3]/div[1]/table[1]/tbody[1]/tr[4]/td[6]")
    PICK_CHECKOUT_DATE = (By.XPATH,
                          "//body[1]/div[1]/div[2]/div[1]/form[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[3]/div[2]/table[1]/tbody[1]/tr[1]/td[5]")
    CLICK_DROPDOWN = (By.XPATH, "//label[@id='xp__guests__toggle']")
    CLICK_ADULT_POS = (
    By.XPATH, "//body/div[1]/div[2]/div[1]/form[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/button[2]")
    CLICK_ADULT_NEG = (
    By.XPATH, "//body/div[1]/div[2]/div[1]/form[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/button[1]")
    CLICK_CHILD_POS = (
    By.XPATH, "//body/div[1]/div[2]/div[1]/form[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/button[2]")
    CLICK_CHILD_NEG = (
    By.XPATH, "//body/div[1]/div[2]/div[1]/form[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/button[1]")
    CLICK_ROOMS_POS = (
    By.XPATH, "//body/div[1]/div[2]/div[1]/form[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[4]/div[1]/div[2]/button[2]")
    CLICK_ROOMS_NEG = (
    By.XPATH, "//body/div[1]/div[2]/div[1]/form[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[4]/div[1]/div[2]/button[1]")


class FlightLocators(object):
    FLIGHTS_BTN = (By.XPATH, "//header/nav[2]/ul[1]/li[2]/a[1]")
    CLICK_TRIP = (By.XPATH, "//div[@data-value='roundtrip']")
    CLICK_ONEWAY = (By.XPATH, '//li[@data-title="One-way"]')
    CLICK_PASSENGER = (By.XPATH, "//body/div[@id='piXF']/div[@id='Ej3F']/main[@id='Ej3F-pageContent']/div[@id='piXF-fd']/div[@id='c1sl9']/div[@id='NEJw']/div[1]/div[1]/div[2]/section[2]/div[2]/div[1]/div[1]/div[2]/div[1]/button[1]/div[1]")
    CLICK_CLASS = (By.XPATH, "//div[@id='dP3I-cabinType-widget-display']")
    CLICK_FROM = (By.XPATH, "//div[@id='AywG-origin-airport-display']")
    SET_FROM = (By.XPATH, '//*[@id="z0kM-origin-airport-display"]')


class CarRentalLocators(object):
    CAR_BTN = (By.XPATH, "//header/nav[2]/ul[1]/li[3]/a[1]")
    RET_SM_LOC = (By.XPATH, "//*[@id='frm']/div[1]/div[1]/label")
    RET_DF_LOC = (By.XPATH, "//label[contains(text(),'Return to different location')]")
    PICKUP_LOC = (By.XPATH, "//input[@id='ss_origin']")
    DROPUP_LOC = (By.XPATH, "//input[@id='ss']")
    CLICK_DATE = (By.XPATH, "//body/div[@id='bodyconstraint']/div[@id='bodyconstraint-inner']/div[3]/div[1]/div[1]/div[1]/div[1]/form[1]/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]")
    DATE_SET_FROM = (By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div/form/div[2]/div[3]/div/div[3]/div/div[2]/div/div[2]/div[2]/div[3]/div/div/div[1]/table/tbody/tr[2]/td[6]/span")
    DATE_SET_TO = (By.XPATH, "//body[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/form[1]/div[2]/div[3]/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[2]/div[3]/div[1]/div[1]/div[2]/table[1]/tbody[1]/tr[2]/td[2]/span[1]")


class AttractionsLocators(object):
    ATTR_BTN = (By.XPATH, "//header/nav[2]/ul[1]/li[4]/a[1]")
    SET_SEARCH = (By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/div/div[2]/div/div[3]/div/div[1]/form/div/input')


class AirportTaxisLocators(object):
    AIRTAXI_BTN = (By.XPATH, "//header/nav[2]/ul[1]/li[5]/a[1]")
