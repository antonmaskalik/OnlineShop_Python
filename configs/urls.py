from units.config import Config


class Urls:
    LOGIN_PAGE: str = Config().BASE_URL
    PRODUCTS_PAGE: str = f"{LOGIN_PAGE}inventory.html"
    CART_PAGE: str = f"{LOGIN_PAGE}cart.html"
    YOUR_INFORMATION_PAGE: str = f"{LOGIN_PAGE}checkout-step-one.html"
    OVERVIEW_PAGE: str = f"{LOGIN_PAGE}checkout-step-two.html"
    COMPLETE_PAGE: str = f"{LOGIN_PAGE}checkout-complete.html"
