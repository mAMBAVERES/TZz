import time

from locators import coord_modal_page
from pages.create_project_page import Create_project_page


from pages.base_page import BasePage

class Modal_page(BasePage):
    def __init__(self):
        self.cord = coord_modal_page
        self.create_project = Create_project_page()

    def create_new_project(self, models, scroll, modification):
        self.click_image(image_path=self.cord.new_project)
        self.create_project.add_model_and_modification(image_path_model=models,
                                                       modification=modification,
                                                       scroll=scroll)

    def add_constant(self):
        time.sleep(2)
        self.click_image(image_path=self.cord.constant)

    def start_work(self):
        self.click_image(self.cord.start_button)

    def assert_simulation(self):
        time.sleep(2)
        self.move_mouse(1372, 370)
        work = self.image_exists(self.cord.stop_button)
        assert work















