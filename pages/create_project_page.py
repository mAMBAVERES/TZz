import pyautogui
from locators import coord_create_project_model
from pages.base_page import BasePage
import time


class Create_project_page(BasePage):
    def __init__(self):
        self.cord_model = coord_create_project_model

    def add_model_and_modification(self, image_path_model,
                                   modification,
                                   scroll=False):
        self.click_image(image_path=image_path_model)
        if scroll == True:
            self.move_mouse(1167, 677)
            # Прокручиваем вниз
            pyautogui.scroll(-10)
            pyautogui.scroll(-10)
            time.sleep(1)
        else:
            pass
        self.click_image(modification)
        self.click_image(image_path=self.cord_model.create_button)




