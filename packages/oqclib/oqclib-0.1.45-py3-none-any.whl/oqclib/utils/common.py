import os

def has_gui():
    # Check if DISPLAY environment variable is set (common in Unix-like systems)
    if os.name == 'posix' and 'DISPLAY' not in os.environ:
        return False
    # Windows and macOS are generally running under a GUI
    elif os.name == 'nt' or sys.platform == 'darwin':
        return True
    return False