from page_objects.conftest import setup
from page_objects.invoice import Add_Invoice
import pytest
@pytest.mark.usefixtures("setup")
class Test_Invoice:

    def test_add_invoice(self):
        object=Add_Invoice(self.driver)
        object.add_a_invoice()

    def test_edit_invoice(self):
        object=Add_Invoice(self.driver)
        object.edit_invoice()

    def test_collect_deposite(self):
        object=Add_Invoice(self.driver)
        object.check_collect_deposite()

    def test_review_and_send(self):
        object=Add_Invoice(self.driver)
        object.check_review_and_send()

    @pytest.mark.sanity
    def test_collect_signature(self):
        object=Add_Invoice(self.driver)
        object.check_collect_signature()

