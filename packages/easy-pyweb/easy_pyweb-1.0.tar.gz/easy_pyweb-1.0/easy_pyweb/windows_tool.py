# pip install pywin32
import win32con
import win32gui


def hide_chrome_windows():
    def cb(handle):
        classname = win32gui.GetClassName(handle)
        title = win32gui.GetWindowText(handle)
        if 'chrome' in classname.lower() and 'google chrome' in title.lower():
            h_list.append(handle)

    h_list = []
    win32gui.EnumWindows(cb, h_list)
    for handel in h_list:
        win32gui.ShowWindow(handel, win32con.SW_SHOWMINIMIZED)
