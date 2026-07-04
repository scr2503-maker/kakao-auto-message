import time
import pyautogui
import win32gui
import pyperclip

def find_kakao_window(title):
    """카카오톡 채팅방 윈도우를 찾는 함수"""
    hwnd = win32gui.FindWindow(None, title)
    if hwnd == 0:
        hwnd = win32gui.FindWindow(None, title + ' - 카카오톡')
    if hwnd == 0:
        hwnd = win32gui.FindWindowEx(None, None, None, title)
    if hwnd == 0:
        print(f"'{title}' 채팅방을 찾을 수 없습니다.")
        return None
    return hwnd

def send_messages(chat_room, message, count, interval):
    pyperclip.copy(message)
    
    for _ in range(count):
        hwnd = find_kakao_window(chat_room)
        if hwnd:
            win32gui.ShowWindow(hwnd, 5)  # 윈도우를 복원
            win32gui.SetForegroundWindow(hwnd)
            start_time = time.time()
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.press('enter')
            elapsed_time = time.time() - start_time
            time.sleep(max(0, interval - elapsed_time))
        else:
            print("채팅방을 찾을 수 없습니다.") 