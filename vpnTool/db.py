import sqlite3
from datetime import datetime

def init_db():
    print("Initializing database...")
    conn = sqlite3.connect('vpnAudit.db')
    c = conn.cursor()

    c.execute('''
        CREATE TABLE IF NOT EXISTS ip_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
              timestamp TEXT,
              ip TEXT,
                city TEXT,
                region TEXT,
                country TEXT,
                org TEXT
        )
    ''')

    c.execute('''
        CREATE TABLE IF NOT EXISTS alerts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT,
                ip TEXT,
                reason TEXT
        )
    ''')

    conn.commit()
    conn.close()

def log_ip(data):
    conn = sqlite3.connect('vpnAudit.db')
    c = conn.cursor()

    c.execute('''
    INSERT INTO ip_logs (timestamp, ip, city, region, country, org)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (
        datetime.now().isoformat(),
          data["ip"],
          data["city"],
          data["region"],
          data["country"],
          data["org"]
          
    ))
    
    conn.commit()
    conn.close()

def log_alert(ip, reason):
    conn = sqlite3.connect('vpnAudit.db')
    c = conn.cursor()

    c.execute('''
        INSERT INTO alerts (timestamp, ip, reason)
        VALUES (?, ?, ?)
    ''', (datetime.now().isoformat(), ip, reason))
    
    conn.commit()
    conn.close()