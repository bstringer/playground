
import os

print("my first one \n\n");

with open('/home/bs/Documents/linux_commands/lin_commands.txt', 'r') as f:
    data = f.read();
print("mydata is: \n", data);

entries = os.scandir("/home/bs")

for entry in entries:
    print("scan Drive: \n", entry);