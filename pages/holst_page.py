import time

from pages.modal_page import Modal_page
from pages.base_page import BasePage

class HolstPage(BasePage):
    def __init__(self):
        self.modal_page = Modal_page()

    def rename_const(self, cord, key):
        self.double_click(*cord)
        self.press_key(key=key)
        self.press_enter()

    def add_const_in_holst(self, cord):
        self.modal_page.add_constant()
        self.click(*cord)

    def connection_for_exit(self, exit_q, cord):
        self.click(*cord)
        time.sleep(1)
        self.click(*exit_q)


