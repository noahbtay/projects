from db import init_db
from monitor import run_monitor

if __name__ == "__main__":
    print("Starting VPN Audit Tool...")
    init_db()
    run_monitor()