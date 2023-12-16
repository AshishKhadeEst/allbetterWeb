import pytest
from page_objects.conftest import setup
from page_objects.request import Add_request
@pytest.mark.usefixtures("setup")
class Test_add_request:

    def test_add_a_request(self):
        object=Add_request(self.driver)
        object.add_request()
