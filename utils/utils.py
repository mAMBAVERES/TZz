

class Utils:
    def calculate_exit_coords(self, cons_1, cons_2):
        # Разницы из примера
        delta_x = 35
        delta_y1 = -7  # для cons1_exit
        delta_y2 = 4    # для cons2_exit

        # Вычисляем новые координаты
        cons1_exit = (cons_1[0] + delta_x, cons_1[1] + delta_y1)
        cons2_exit = (cons_2[0] + delta_x, cons_2[1] + delta_y2)

        return cons1_exit, cons2_exit