import pytest
from page_objects.conftest import setup
from page_objects.request import Add_request
@pytest.mark.usefixtures("setup")
class Test_add_request:

    def test_add_a_request(self):
        object=Add_request(self.driver)
        object.add_request()

    def test_edit_request(self):
        object=Add_request(self.driver)
        object.edit_request()

    def test_search(self):
        object=Add_request(self.driver)
        object.check_search("Ashish")

    def test_filter(self):
        object=Add_request(self.driver)
        object.check_filter()

    def test_convert_to_quote(self):
        object =Add_request(self.driver)
        object.check_convert_to_quote()

    def test_convert_to_job(self):
        object=Add_request(self.driver)
        object.check_convert_to_job()

    @pytest.mark.sanity
    def test_archieve(self):
        object = Add_request(self.driver)
        object.check_archieve()

    def test_job_completed(self):
        object = Add_request(self.driver)
        object.check_request_completed()


