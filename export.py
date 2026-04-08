import sqlite3
import pandas as pd

conn = sqlite3.connect('vpnAudit.db')

df_logs = pd.read_sql_query("SELECT * FROM ip_logs", conn)
df_logs.to_csv('ip_logs.csv', index=False)

df_alerts = pd.read_sql_query("SELECT * FROM alerts", conn)
df_alerts.to_csv('alerts.csv', index=False)

conn.close()

print("Export Complete.")
