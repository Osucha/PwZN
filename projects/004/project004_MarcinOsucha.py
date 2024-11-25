import os
import time

def run_and_time(command):
    start_time = time.time()
    exit_code = os.system(command)
    end_time = time.time()
    
    if exit_code != 0:
        print(f"Command failed: {command}")
    else:
        print(f"Command completed successfully: {command}")
    
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time:.2f} seconds\n")
    return execution_time

commands = [
    "python project002Osucha.py --grid_size 50 --J 1 --beta 1000000000 --B 0 --steps 1000 --spin_density 0.5",
    "python ..\\004\\project002OsuchaNumba.py --grid_size 50 --J 1 --beta 1000000000 --B 0 --steps 1000 --spin_density 0.5"
]

for cmd in commands:
    print(f"Running command: {cmd}")
    run_and_time(cmd)

# Output:
# PS C:\Users\mosucha\OneDrive - Exorigo-Upos S.A\Dokumenty\Magisterka\SEMESTR 2\PwZN\PwZN2024_Live\projects\002> & C:/Users/mosucha/AppData/Local/pypoetry/Cache/virtualenvs/pwzn2024-live-ZC7wkB9n-py3.11/Scripts/python.exe "c:/Users/mosucha/OneDrive - Exorigo-Upos S.A/Dokumenty/Magisterka/SEMESTR 2/PwZN/PwZN2024_Live/projects/004/project004_MarcinOsucha.py"
# Running command: python project002Osucha.py --grid_size 50 --J 1 --beta 1000000000 --B 0 --steps 1000 --spin_density 0.5
# Running simulation... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
# Command completed successfully: python project002Osucha.py --grid_size 50 --J 1 --beta 1000000000 --B 0 --steps 1000 --spin_density 0.5
# Execution time: 38.31 seconds

# Running command: python ..\004\project002OsuchaNumba.py --grid_size 50 --J 1 --beta 1000000000 --B 0 --steps 1000 --spin_density 0.5
# Running simulation... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
# Command completed successfully: python ..\004\project002OsuchaNumba.py --grid_size 50 --J 1 --beta 1000000000 --B 0 --steps 1000 --spin_density 0.5
# Execution time: 21.14 seconds