from page_objects.conftest import setup
from page_objects.notes import Add_Notes
import pytest


@pytest.mark.usefixtures("setup")
class Test_Add_Notes:

    def test_add_notes(self):
        object=Add_Notes(self.driver)
        object.add_notes()

    @pytest.mark.sanity
    def test_edit_notes(self):
        object=Add_Notes(self.driver)
        object.edit_notes()

