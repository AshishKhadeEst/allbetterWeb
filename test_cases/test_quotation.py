import pytest
from page_objects.conftest import setup
from page_objects.quotation import Add_quotation


@pytest.mark.usefixtures("setup")
class Test_add_quote:


    def test_add_quotation(self):
        object=Add_quotation(self.driver)
        object.add_quotation()

    @pytest.mark.sanity
    def test_edit_quotation(self):
        object=Add_quotation(self.driver)
        object.edit_quote()

    def test_approve_quote(self):
        object=Add_quotation(self.driver)
        object.approve_quotation()

    def test_review_and_send(self):
        object=Add_quotation(self.driver)
        object.review_and_send_check("testashu123@mailinator.com")

    def test_convert_to_job(self):
        object=Add_quotation(self.driver)
        object.convert_to_job()




