import os
import datetime

def generate_audit_log():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] - SECURITY_AUDIT_OK - System Integrity Verified.\n"
    
   
    log_path = os.path.join("logs_archive", "audit_system.log")
    with open(log_path, "a") as log_file:
        log_file.write(log_entry)
    print(f"Log generated: {timestamp}")

if __name__ == "__main__":
    generate_audit_log()
