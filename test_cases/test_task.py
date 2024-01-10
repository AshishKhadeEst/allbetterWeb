from page_objects.conftest import setup
from page_objects.task import Add_Task
import pytest
@pytest.mark.usefixtures("setup")
class Test_Add_Task:
    def test_add_a_task(self):
        object=Add_Task(self.driver)
        object.add_a_task()

    def test_edit_task(self):
        object=Add_Task(self.driver)
        object.edit_task()

    def test_mark_complete(self):
        object=Add_Task(self.driver)
        object.check_mark_completed()

    @pytest.mark.sanity
    def test_back_button(self):
        object=Add_Task(self.driver)
        object.check_back_button()
