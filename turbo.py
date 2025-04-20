import os
import subprocess
from datetime import datetime, timedelta

# Retomamos desde donde estábamos
start_date = datetime(2025, 11, 6)
total_days = 162
commits_per_day = 78

print(">>> ACTIVANDO TURBO: Inyeccion por lotes...")

for day in range(total_days + 1):
    current_date = start_date + timedelta(days=day)
    date_str = current_date.strftime('%Y-%m-%dT12:00:00')
    
    # Configuramos la fecha una sola vez por dia
    os.environ['GIT_AUTHOR_DATE'] = date_str
    os.environ['GIT_COMMITTER_DATE'] = date_str
    
    # Creamos un archivo de comandos (batch) para que Windows lo ejecute de una
    with open("batch_commit.bat", "w") as f:
        for j in range(1, commits_per_day + 1):
            f.write(f'git commit -m "Security Audit {j} - {date_str}" --allow-empty --quiet\n')
    
    # Ejecutamos todo el dia de una sola vez
    subprocess.run("batch_commit.bat", shell=True, env=os.environ)
    
    print(f">>> OK: {date_str}")

if os.path.exists("batch_commit.bat"):
    os.remove("batch_commit.bat")

print(">>> PROCESO FINALIZADO.")
