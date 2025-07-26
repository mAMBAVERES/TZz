import pyautogui
import cv2
import numpy as np
from typing import Tuple, Optional, Union
import time


class BasePage:
    def __init__(self):
        pyautogui.FAILSAFE = True
        pyautogui.PAUSE = 0.1


    def click(self, x: int, y: int):
        pyautogui.click(x, y)
        time.sleep(1)

    def click_image(self, image_path: str, confidence: float = 0.8):
        location = pyautogui.locateOnScreen(image_path, confidence=confidence)
        if location:
            pyautogui.click(pyautogui.center(location))
        else:
            raise Exception(f"Изображение {image_path} не найдено")
        time.sleep(1)

    def double_click(self, x: int, y: int):
        pyautogui.doubleClick(x, y)

    def double_click_image(self, image_path: str, confidence: float = 0.8):
        location = pyautogui.locateOnScreen(image_path, confidence=confidence)
        if location:
            pyautogui.doubleClick(pyautogui.center(location))
        else:
            raise Exception(f"Изображение {image_path} не найдено")

    def move_mouse(self, x: int, y: int, duration: float = 0.5):
        pyautogui.moveTo(x, y, duration=duration)

    def move_mouse_to_image(self, image_path: str, confidence: float = 0.8, duration: float = 0.5):
        location = pyautogui.locateOnScreen(image_path, confidence=confidence)
        if location:
            pyautogui.moveTo(pyautogui.center(location), duration=duration)
        else:
            raise Exception(f"Изображение {image_path} не найдено")

    def drag_mouse(self, start_x: int, start_y: int, end_x: int, end_y: int, duration: float = 1.0):
        pyautogui.drag(end_x - start_x, end_y - start_y, duration=duration, startPoint=(start_x, start_y))

    def drag_mouse_from_image_to_coords(self, image_path: str, end_x: int, end_y: int, confidence: float = 0.8,
                                        duration: float = 1.0):
        location = pyautogui.locateOnScreen(image_path, confidence=confidence)
        if location:
            start_point = pyautogui.center(location)
            pyautogui.drag(end_x - start_point.x, end_y - start_point.y, duration=duration, startPoint=start_point)
        else:
            raise Exception(f"Изображение {image_path} не найдено")

    def drag_mouse_from_image_to_image(self, start_image_path: str, end_image_path: str, confidence: float = 0.8,
                                       duration: float = 1.0):
        start_location = pyautogui.locateOnScreen(start_image_path, confidence=confidence)
        end_location = pyautogui.locateOnScreen(end_image_path, confidence=confidence)

        if start_location and end_location:
            start_point = pyautogui.center(start_location)
            end_point = pyautogui.center(end_location)
            pyautogui.drag(end_point.x - start_point.x, end_point.y - start_point.y, duration=duration,
                           startPoint=start_point)
        else:
            if not start_location:
                raise Exception(f"Начальное изображение {start_image_path} не найдено")
            if not end_location:
                raise Exception(f"Конечное изображение {end_image_path} не найдено")

    def type_text(self, text: str, interval: float = 0.05):
        pyautogui.typewrite(text, interval=interval)

    def type_text_at_coords(self, x: int, y: int, text: str, interval: float = 0.05):
        pyautogui.click(x, y)
        pyautogui.typewrite(text, interval=interval)

    def type_text_at_image(self, image_path: str, text: str, confidence: float = 0.8, interval: float = 0.05):
        location = pyautogui.locateOnScreen(image_path, confidence=confidence)
        if location:
            pyautogui.click(pyautogui.center(location))
            pyautogui.typewrite(text, interval=interval)
        else:
            raise Exception(f"Изображение {image_path} не найдено")

    def press_key(self, key: str):
        pyautogui.press(key)

    def press_keys(self, *keys):
        pyautogui.hotkey(*keys)

    def right_click(self, x: int, y: int):
        pyautogui.rightClick(x, y)

    def right_click_image(self, image_path: str, confidence: float = 0.8):
        location = pyautogui.locateOnScreen(image_path, confidence=confidence)
        if location:
            pyautogui.rightClick(pyautogui.center(location))
        else:
            raise Exception(f"Изображение {image_path} не найдено")

    def scroll(self, x: int, y: int, clicks: int):
        pyautogui.scroll(clicks, x=x, y=y)

    def scroll_at_image(self, image_path: str, clicks: int, confidence: float = 0.8):
        location = pyautogui.locateOnScreen(image_path, confidence=confidence)
        if location:
            center = pyautogui.center(location)
            pyautogui.scroll(clicks, x=center.x, y=center.y)
        else:
            raise Exception(f"Изображение {image_path} не найдено")

    def wait_for_image(self, image_path: str, timeout: int = 10, confidence: float = 0.8):
        start_time = time.time()
        while time.time() - start_time < timeout:
            try:
                location = pyautogui.locateOnScreen(image_path, confidence=confidence)
                if location:
                    return location
            except:
                pass
            time.sleep(0.5)
        raise Exception(f"Изображение {image_path} не найдено в течение {timeout} секунд")

    def image_exists(self, image_path: str, confidence: float = 0.8) -> bool:
        try:
            location = pyautogui.locateOnScreen(image_path, confidence=confidence)
            if location is not None:
                return True
        except:
            return False

    def press_enter(self):
        pyautogui.press('enter')


