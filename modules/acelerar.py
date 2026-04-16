import os
import subprocess
from datetime import datetime, timedelta


start_date = datetime(2025, 11, 6) 
total_days = 161 
commits_per_day = 78

print(f">>> ACELERANDO: Procesando {total_days} dias restantes...")

for day in range(total_days + 1):
    current_date = start_date + timedelta(days=day)
    date_str = current_date.strftime('%Y-%m-%dT12:00:00')
    
    os.environ['GIT_AUTHOR_DATE'] = date_str
    os.environ['GIT_COMMITTER_DATE'] = date_str
    
    --allow-empty --quiet' for j in range(1, commits_per_day + 1)]
    full_cmd = " && ".join(cmd_parts)
    
    subprocess.run(f'cmd /c "{full_cmd}"', shell=True, env=os.environ)
    
    print(f">>> Dia completado: {date_str}")

print(">>> PROCESO FINALIZADO CON EXITO.")
