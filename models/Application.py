from pages.base_page import BasePage
from  pages.modal_page import Modal_page
from  pages.holst_page import HolstPage
from  utils.utils import Utils


class Application(object):

    def __init__(self):
        self.base_page = BasePage()
        self.modal_page = Modal_page()
        self.holst_page = HolstPage()
        self.utils = Utils()



