from page_objects.conftest import setup
import pytest
from page_objects.profile_page import Edit_Profile


@pytest.mark.usefixtures("setup")
class Test_Edit_Profile:

    def test_edit_company(self):
        object=Edit_Profile(self.driver)
        object.edit_company()

    def test_edit_profile(self):
        object=Edit_Profile(self.driver)
        object.edit_user_profile()

    @pytest.mark.sanity
    def test_add_new_card(self):
        object=Edit_Profile(self.driver)
        object.add_new_payment_card()


