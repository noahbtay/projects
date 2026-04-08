import requests 
import time
from db import log_ip, log_alert
from alerts import send_desktop_alert, send_email_alert


KNOWN_SAFE_IP = None
ALERT_TRIGGERS = False

def get_ip_info():
    try:
        ip = requests.get("https://api.ipify.org", timeout=5).text

        geo_response = requests.get(
            f"https://ipapi.co/{ip}/json/", timeout=5,
            headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 "}
        )
        if geo_response.status_code != 200:
            print("Geo API Error:", geo_response.status_code)
            return {"ip": ip, "city": None, "region": None, "country": None, "org": None        }
        try:
            geo = geo_response.json()
        except:
            print("Invalid JSON response from Geo API")
            return {"ip": ip, "city": None, "region": None, "country": None, "org": None}
        return {
        "ip": ip,
        "city": geo.get("city"),
        "region": geo.get("region"),
        "country": geo.get("country_name"),
        "org": geo.get("org"),
    }
    except Exception as e:
        print("Error getting IP Info:", e)
        return{"ip": None, "city": None, "region": None, "country": None, "org": None}

def detect_leak(current):
    global KNOWN_SAFE_IP, ALERT_TRIGGERED

    if KNOWN_SAFE_IP is None:
        KNOWN_SAFE_IP = current["ip"]
        return "BASELINE"
    
    if current["ip"] != KNOWN_SAFE_IP:
        if not ALERT_TRIGGERED:
            ALERT_TRIGGERED = True
            return "LEAK"
        return "Already Alerted" 
    
    ALERT_TRIGGERED = False
    return "SAFE"

def run_monitor():
    while True:
        data = get_ip_info()
        log_ip(data)

        status = detect_leak(data)
        print(data["ip"], status)

        if status == "LEAK":
            send_desktop_alert(data["ip"])
            send_email_alert(data["ip"])
            log_alert(data["ip"], "IP changed")
        time.sleep(60)  # Check every minute
