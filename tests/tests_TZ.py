import pytest
from locators.coord_create_project_model import *
from locators.coord_holst_page import *
from locators.coord_modal_page import constant


class Test_tz:


    def test_tech_work(self, app):
        # Иницируем данные теста
        models = PR_200
        modification = twenty_for_two_for
        constant_1 = 1372, 370
        constant_2 = 1372, 380
        new_name_cord = "1"

        cons1_exit, cons2_exit = app.utils.calculate_exit_coords(cons_1=constant_1, cons_2=constant_2)


        # создаем новый проект
        app.modal_page.create_new_project(models=models, scroll=True, modification=modification)

        # выстраиваем константы
        app.holst_page.add_const_in_holst(cord=constant_1)
        app.holst_page.add_const_in_holst(cord=constant_2)

        # переименовываем данные в конс 1
        app.holst_page.rename_const(cord=constant_1, key=new_name_cord)

        # Соединяем константы
        app.holst_page.connection_for_exit(cord=cons1_exit, exit_q=exit_q1)
        app.holst_page.connection_for_exit(cord=cons2_exit, exit_q=exit_q2)

        # запуск
        app.modal_page.start_work()

        # проверяем что симуляция запущена
        app.modal_page.assert_simulation()









