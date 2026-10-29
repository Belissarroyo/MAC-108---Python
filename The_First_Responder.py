# Define the immutable Tuple
# RAW SOC SYSTEM LOGS
# Format:[SEVERITY] | IP_ADDRESS | USERNAME | PORT | EVENT_STATUS

#First need to create a list to define IP addresses

threat_levels = ("[warning]", "[alert]", "[critical]")
malicious_IP = []
watch_list = []

raw_forensic_logs = [
    "  [critical] | 192.168.1.105 | Admin_User | 22 | failed_login  ",
    "[WARNING] | 10.0.0.50 | root | 443 | MALWARE_SIGNATURE_DETECTED",
    "  [CRITICAL] | 172.16.254.1 | unknown_user | 80 | SQL_INJECTION_ATTEMPT  ",
    " [alert] | 192.168.1.200 | SYS_ADMIN | 3389 | UNAUTHORIZED_ACCESS ",
    "  [warning] | 10.0.0.12 | test_acc | 8080 | brute_force_suspected  "
]

#Change to lowercase for 
nocap_raw_logs = [raw_forensic_logs.lower() for raw_forensic_logs in raw_forensic_logs]
print(nocap_raw_logs)

#Strip to eliminate blank spaces
clean_raw_logs = [nocap_raw_logs.strip() for nocap_raw_logs in nocap_raw_logs]
print(clean_raw_logs)

#Split into categories - in this case: Threat levels, Seperate logs, IP Addresses, Malicious IPs, 
sep_raw_logs = [clean_raw_logs.split(",") for clean_raw_logs in clean_raw_logs]
print(sep_raw_logs)

ip = [clean_raw_logs.split("|")[1] for clean_raw_logs in clean_raw_logs]

#Can combine .strip and .lower in one line
#clean_raw_logs = [raw_forensic_logs.strip().lower() for raw_forensic_logs in raw_forensic_logs]


#malicious_IP = 

clean_raw_logs.append(malicious_IP)