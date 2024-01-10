from page_objects.conftest import setup
import pytest
from page_objects.jobs import Add_job

@pytest.mark.usefixtures("setup")
class Test_add_job:

    def test_create_job(self):
        object=Add_job(self.driver)
        object.create_job()

    def test_edit_job(self):
        object=Add_job(self.driver)
        object.edit_job()

    def test_collect_signature(self):
        object=Add_job(self.driver)
        object.collect_the_signature()

    def test_complete_job(self):
        object=Add_job(self.driver)
        object.complete_job()

    @pytest.mark.sanity
    def test_back_button(self):
        object=Add_job(self.driver)
        object.check_back_button()




