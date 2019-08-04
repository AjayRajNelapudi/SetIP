import cv2
import pyautogui
from gui_automation import GuiAuto

class Navigate:
    def __init__(self, images_path=""):
        self.path = images_path

    def click_widget(self, widgetImagePath):
        widgetImage = cv2.imread(self.path + widgetImagePath)
        GuiAuto(widgetImage, 0.7).detect_and_click()

    def click_and_hold_widget(self, widgetImagePath):
        widget_image = cv2.imread(self.path + widgetImagePath)
        GuiAuto(widget_image, 0.8).detect_and_hold(0.1)

    def open_network_preferences(self):
        pyautogui.moveTo(x=800, y=0, pause=0.5)
        self.click_widget("wifi.png")
        pyautogui.press("up")
        pyautogui.press("enter")

    def open_advanced_panel(self):
        self.click_widget("advanced.png")

    def goto_tcp_ip(self):
        self.click_widget("tcpip.png")

    def set_college_ip(self):
        self.click_and_hold_widget("dhcp.png")

        pyautogui.press("d")
        pyautogui.press("enter")

        pyautogui.press("tab")
        pyautogui.typewrite("10.0.67.195")

        pyautogui.press("tab")
        pyautogui.typewrite("255.255.252.0")

        pyautogui.press("tab")
        pyautogui.typewrite("10.0.64.1")

        self.click_and_hold_widget("ok.png")

    def set_home_ip(self):
        self.click_and_hold_widget("manually.png")
        pyautogui.press("u")
        pyautogui.press("enter")

        self.click_and_hold_widget("ok.png")

    def apply_and_close(self):
        self.click_and_hold_widget("apply.png")
        pyautogui.hotkey("command", "q")

if __name__ == "__main__":
    nav = Navigate(images_path="/Users/ajayraj/Documents/SetIP/")

    nav.open_network_preferences()
    pyautogui.sleep(0.5)

    nav.open_advanced_panel()
    nav.goto_tcp_ip()
    nav.set_home_ip()
    pyautogui.sleep(0.2)

    nav.apply_and_close()