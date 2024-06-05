import pyautogui, time

position =pyautogui.position()
pesan = "bebebbbbbbbb"
for a in range(1000):
    pyautogui.click(position.x,position.y)
    pyautogui.typewrite(pesan)
    print(pesan)
    time.sleep(0.1)
    pyautogui.typewrite(["enter"])