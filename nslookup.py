import subprocess
process = subprocess.Popen(["nslookup", "10.8.15.191"], stdout=subprocess.PIPE)
output = str(process.communicate()[0]).split('\\r\\n')

print(output[3])