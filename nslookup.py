import subprocess
import os
import pip

try:
    from tqdm import tqdm
except ModuleNotFoundError:
    pip.main(["install", "tqdm"])
    from tqdm import tqdm

powershell = "C:\Windows\System32\WindowsPowerShell\\v1.0\powershell.exe"

print("Podaj adres sieci: np. 172.16.196.0")
netw = input()
data = open("data.txt", "w")
print("Sprawdzanie adresów: ")
for i in tqdm(range(1, 255)):
    nslookup = subprocess.check_output(
        powershell
        + " nslookup -type=PTR "
        + netw[:-2]
        + "."
        + str(i)
        + " | Select-String name",
        stderr=subprocess.DEVNULL,
        text=True,
        shell=False,
    )
    if not nslookup.startswith("***"):
        data.write(nslookup)
data.close()

data = open("data.txt", "r")
resadd = open("resolved addresses - " + netw + ".txt", "w")
for line in data:
    if not line.strip():
        continue
    resadd.write(line)
data.close()
resadd.close()
os.remove("data.txt")
print('Zapisano do pliku "resolved addresses - ' + netw + '.txt"')
