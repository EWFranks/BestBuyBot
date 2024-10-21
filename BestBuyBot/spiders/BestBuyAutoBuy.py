from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import info


driver = webdriver.Chrome()

LINK = "https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440"
#LINK = "https://www.bestbuy.com/site/dynex-6-hdmi-cable-black/6405508.p?skuId=6405508"
#LINK = "https://www.bestbuy.com/site/lg-65-class-up8000-series-led-4k-uhd-smart-webos-tv/6452988.p?skuId=6452988"
driver.get(LINK)

isComplete = False

while not isComplete:
    # find add to cart button
    try:
        atcBtn = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".add-to-cart-button"))
        )
    except:
        driver.refresh()
        continue

    print("Add to cart button found")
    try:
        # add to cart
        atcBtn.click()

        # go to cart and begin checkout as guest
        driver.get("https://www.bestbuy.com/cart")

        checkoutBtn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@class='btn btn-lg btn-block btn-primary']"))
        )
        checkoutBtn.click()
        print("Successfully added to cart - beginning check out")

        # fill in email and password
        emailField = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "fld-e"))
        )
        emailField.send_keys(info.email)

        pwField = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "fld-p1"))
        )
        pwField.send_keys(info.password)

        # click sign in button

        signInBtn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[1]/div/section/main/div[2]/div[1]/div/div/div/div/form/div[3]/button"))

        )
        signInBtn.click()
        print("Signing in")

        shipping = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[2]/div/div/button"))

        )
        shipping.click()

        # fill in card cvv
        cvvField = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "credit-card-cvv"))
         )
        cvvField.send_keys(info.cvv)
        print("Attempting to place order")

        # place order
        placeOrderBtn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[3]/div/section/div[4]/div[2]/button"))
        )
        placeOrderBtn.click()

        isComplete = True
    except:
        print("Error - restarting bot")
        continue

print("Order successfully placed")
