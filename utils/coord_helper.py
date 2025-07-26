from pynput import mouse

def on_move(x, y):
    print(f'Координаты мыши: X={x}, Y={y}')

# Создаем слушатель мыши
with mouse.Listener(on_move=on_move) as listener:
    try:
        listener.join()
    except KeyboardInterrupt:
        print()