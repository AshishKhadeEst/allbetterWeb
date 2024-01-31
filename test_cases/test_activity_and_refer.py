from page_objects.activity_log_and_refer import Action_Log_Refer
from page_objects.conftest import setup
import pytest


@pytest.mark.usefixtures("setup")
class Test_Refer_And_Activity:

    def test_activity(self):
        object=Action_Log_Refer(self.driver)
        object.check_activity()

    @pytest.mark.sanity
    def test_referral(self):
        object=Action_Log_Refer(self.driver)
        object.check_referral()





