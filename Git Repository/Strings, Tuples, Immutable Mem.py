#extract & Verify Attacker IPs from Logs

#Raw Server Log String
raw_log = "ALERT | 2026-10-19 | 192.168.4.11 | SQL_Injection_Attempt"

#Seperate with .split() 
#Use comma (",") or this | thingy ("|")
#In Brackets [] indexing? starts at 0 so in raw_log, the IP Address is 3rd section, after 2nd | divider
ip = raw_log.split("|")[2]
banned_ips = ("10.0.0.1","192.168.161","192.168.4.11", "129.255.0.0")

alert = print(f"REPEAT OFFENDER!\nBlocked traffic from known threat:{ip}")

if ip in banned_ips:
    print(alert)
