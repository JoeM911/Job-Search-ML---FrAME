import time
import csv
from datetime import datetime
import win32gui
import win32process
import psutil

LOG_FILE = "app_usage_log.csv"
POLL_INTERVAL = 5  # seconds


def get_active_window():
    try:
        hwnd = win32gui.GetForegroundWindow()
        title = win32gui.GetWindowText(hwnd)

        _, pid = win32process.GetWindowThreadProcessId(hwnd)
        process = psutil.Process(pid)
        app = process.name()

        return app, title
    except:
        return "Unknown", "Unknown"


# Initialize CSV (only if it doesn't exist)
try:
    open(LOG_FILE, "x").write("timestamp,app,title\n")
except FileExistsError:
    pass


print("🟢 Tracking started (Ctrl+C to stop)...")

last_state = None

try:
    while True:
        app, title = get_active_window()
        timestamp = datetime.now().isoformat()

        state = (app, title)
        if state != last_state:
            with open(LOG_FILE, "a", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow([timestamp, app, title])
            print(f"{timestamp} → {app} | {title}")
            last_state = state

        time.sleep(POLL_INTERVAL)

except KeyboardInterrupt:
    print("\n🛑 Tracking stopped.")

