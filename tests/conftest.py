import pytest
from playwright.sync_api import Page
from pages.login import LoginPage
from pages.products import ProductsPage
from pages.cart import CartPage
from pages.checkout_step_one import CheckoutStepOne
from pages.checkout_step_two import CheckoutStepTwo
from pages.checkout_complete import CheckoutComplete
from pages.side_menu import SideMenu


@pytest.fixture
def login_page(page: Page):
    return LoginPage(page)


@pytest.fixture
def products_page(page: Page):
    return ProductsPage(page)


@pytest.fixture
def cart_page(page: Page):
    return CartPage(page)


@pytest.fixture
def checkout_step_one(page: Page):
    return CheckoutStepOne(page)


@pytest.fixture
def checkout_step_two(page: Page):
    return CheckoutStepTwo(page)


@pytest.fixture
def checkout_complete(page: Page):
    return CheckoutComplete(page)


@pytest.fixture
def side_menu(page: Page):
    return SideMenu(page)
