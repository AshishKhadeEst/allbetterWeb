import pytest
from page_objects.conftest import setup
from page_objects.employees import Add_Employees


@pytest.mark.usefixtures("setup")
class Test_Add_Employees:

    def test_add_employees(self):
        object=Add_Employees(self.driver)
        object.add_employee("Ashish","Khade","9893000000","ashu123@yahoo.com","123456","123456")

    def test_edit_employee(self):
        object=Add_Employees(self.driver)
        object.edit_employee("Ashish","khade","ashu123@gmail.com")

    @pytest.mark.sanity
    def test_change_status(self):
        object=Add_Employees(self.driver)
        object.change_status()

