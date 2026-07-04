import tkinter as tk
from tkinter import messagebox
import time
import pyautogui
import pyperclip
import win32gui


def find_kakao_window(title):
    """카카오톡 채팅방 윈도우를 찾는 함수"""
    hwnd = win32gui.FindWindow(None, title)
    if hwnd == 0:
        print(f"'{title}' 채팅방을 찾을 수 없습니다.")
        return None
    return hwnd


def send_message(chat_room, message, count, interval):
    hwnd = find_kakao_window(chat_room)
    if not hwnd:
        messagebox.showerror("오류", f"'{chat_room}' 채팅방을 찾을 수 없습니다.")
        return
    
    win32gui.SetForegroundWindow(hwnd)
    time.sleep(0.5)  # 윈도우가 활성화될 때까지 대기
    
    pyperclip.copy(message)
    
    for _ in range(count):
        time.sleep(0.5)  # 창이 준비될 때까지 대기
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
        time.sleep(interval)
    
    print(f"채팅방: {chat_room}, 메시지: {message}, 횟수: {count}, 간격: {interval}")
    # 실제 메시지 전송 로직은 여기에 추가


def create_gui():
    root = tk.Tk()
    root.title("카카오톡 자동 메시지 전송기")
    root.geometry("400x350")
    
    tk.Label(root, text="채팅방 이름").pack(pady=5)
    chat_room_entry = tk.Entry(root, width=30)
    chat_room_entry.pack(pady=5)
    
    tk.Label(root, text="메시지 내용").pack(pady=5)
    message_entry = tk.Entry(root, width=30)
    message_entry.pack(pady=5)
    
    tk.Label(root, text="반복 횟수").pack(pady=5)
    count_entry = tk.Entry(root, width=10)
    count_entry.insert(0, "1")
    count_entry.pack(pady=5)
    
    tk.Label(root, text="간격 (초)").pack(pady=5)
    interval_entry = tk.Entry(root, width=10)
    interval_entry.insert(0, "1")
    interval_entry.pack(pady=5)
    
    status_label = tk.Label(root, text="", fg="blue")
    status_label.pack(pady=5)
    
    def on_send():
        chat_room = chat_room_entry.get()
        message = message_entry.get()
        count = int(count_entry.get())
        interval = float(interval_entry.get())
        
        status_label.config(text="3초 후에 메시지를 전송합니다.")
        root.after(3000, lambda: send_message(chat_room, message, count, interval))
    
    send_button = tk.Button(root, text="메시지 전송", command=on_send)
    send_button.pack(pady=20)
    
    root.mainloop()

if __name__ == "__main__":
    create_gui() 