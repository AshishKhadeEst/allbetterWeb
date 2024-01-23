from page_objects.Services_and_products import Product_And_Services
import pytest
from page_objects.conftest import setup


@pytest.mark.usefixtures("setup")
class Test_Services_And_Products:

    @pytest.mark.sanity
    def test_add_service(self):
        object=Product_And_Services(self.driver)
        object.add_service()

    def test_add_product(self):
        object=Product_And_Services(self.driver)
        object.add_products()

    def test_edit_product(self):
        object=Product_And_Services(self.driver)
        object.edit_product()
