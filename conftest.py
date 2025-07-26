import os
import pytest
import time
from models.Application import Application

@pytest.fixture
def app():
    DIRAPP = r"E:\Owen_Logic\ProgramRelayFBD.exe"
    try:
        os.startfile(DIRAPP)
        print(f"Приложение запущено по пути: {DIRAPP}")
        time.sleep(5.0)
    except Exception as e:
        print(f"Ошибка при открытии приложения: {e}")

    time.sleep(3)


    yield Application()

    os.system("taskkill /IM ProgramRelayFBD.exe /F")
    print("Приложение закрыто через завершение процесса")
    time.sleep(2.0)

