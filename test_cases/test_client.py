import pytest
from page_objects.conftest import setup
from page_objects.client import Add_client
@pytest.mark.usefixtures("setup")
class Test_client:

    def test_add_a_client(self):
        object=Add_client(self.driver)
        object.add_a_client()

    def test_edit_client(self):
        object=Add_client(self.driver)
        object.edit_client()

    def test_check_button(self):
        object=Add_client(self.driver)
        object.check_back_button()

    @pytest.mark.sanity
    def test_search_box(self):
        object=Add_client(self.driver)
        object.client_search_box("Ash")















