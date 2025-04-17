from units.config import Config


class Urls:
    LOGIN_PAGE = Config().BASE_URL
    PRODUCTS_PAGE = f"{LOGIN_PAGE}inventory.html"
    CART_PAGE = f"{LOGIN_PAGE}cart.html"
