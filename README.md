# SimpleC2 Remote Administration Tool
Made By SleepTheGod
```
            ███████╗██╗███╗   ███╗██████╗ ██╗     ███████╗     ██████╗██████╗              
            ██╔════╝██║████╗ ████║██╔══██╗██║     ██╔════╝    ██╔════╝╚════██╗             
            ███████╗██║██╔████╔██║██████╔╝██║     █████╗      ██║      █████╔╝             
            ╚════██║██║██║╚██╔╝██║██╔═══╝ ██║     ██╔══╝      ██║     ██╔═══╝              
            ███████║██║██║ ╚═╝ ██║██║     ███████╗███████╗    ╚██████╗███████╗             
            ╚══════╝╚═╝╚═╝     ╚═╝╚═╝     ╚══════╝╚══════╝     ╚═════╝╚══════╝             
                                                                                           
██████╗ ██████╗ ██████╗      ██████╗ ██╗   ██╗███████╗██████╗     ████████╗ ██████╗██████╗ 
██╔══██╗██╔══██╗██╔══██╗    ██╔═══██╗██║   ██║██╔════╝██╔══██╗    ╚══██╔══╝██╔════╝██╔══██╗
██████╔╝██║  ██║██████╔╝    ██║   ██║██║   ██║█████╗  ██████╔╝       ██║   ██║     ██████╔╝
██╔══██╗██║  ██║██╔═══╝     ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗       ██║   ██║     ██╔═══╝ 
██║  ██║██████╔╝██║         ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║       ██║   ╚██████╗██║     
╚═╝  ╚═╝╚═════╝ ╚═╝          ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝       ╚═╝    ╚═════╝╚═╝     
                                                                                        
```
# Installation
```
sudo apt install git -y && git clone https://github.com/SleepTheGod/SimpleC2/;
mkdir remote-admin-tool
cd remote-admin-tool
npm init -y
npm install express multer fs pyautogui child_process
npm install color --save
npm install chalk --save
pip install flask cryptography pyautogui --break-system-packages
python3 server.py && python3 client_backend.py && npm start server.js;
sudo apt update
sudo apt install -y xvfb
xvfb-run -a python3 ~/SimpleC2/server.py &
xvfb-run -a python3 ~/SimpleC2/client_backend.py &
export DISPLAY=:99
xvfb-run -a python3 ~/SimpleC2/server.py &
python3 ~/SimpleC2/server.py &
python3 ~/SimpleC2/client_backend.py &
ps aux | grep python3
chmod +w server_key.key
python3 ~/SimpleC2/client_backend.py &
```
# Installation 2
```bash
# Install Git and clone the repository
sudo apt install git -y && git clone https://github.com/SleepTheGod/SimpleC2/

# Create and navigate to the project directory
mkdir remote-admin-tool
cd remote-admin-tool

# Initialize a Node.js project and install Node.js dependencies
npm init -y
npm install express multer fs child_process
npm install color chalk --save

# Install Python dependencies
pip install flask cryptography pyautogui --break-system-packages

# Run Python and Node.js components
python3 server.py &
python3 client_backend.py &
npm start
```

# Usage
```bash
debian@vps-a1d18fab:~/SimpleC2/remote-admin-tool$ Accepted TCP connection from ('127.0.0.1', 46222)
Enter command (get <filename>, put <filename>, exit):
```
# Example
```
root         464  0.0  0.2  28736 18992 ?        Ss   Jan09   0:12 /usr/bin/python3 /usr/share/unattended-upgrades/unattended-upgrade-shutdown --wait-for-signal
root       63393  0.0  0.0   7096  4308 pts/0    S    18:07   0:00 sudo xvfb-run -a python3 /home/debian/SimpleC2/server.py
root       63394  0.0  0.0   7096   460 pts/1    Ss+  18:07   0:00 sudo xvfb-run -a python3 /home/debian/SimpleC2/server.py
root       63395  0.0  0.0   2576  1780 pts/1    S    18:07   0:00 /bin/sh /usr/bin/xvfb-run -a python3 /home/debian/SimpleC2/server.py
root       63408  0.0  0.6 137664 48272 pts/1    Sl   18:07   0:00 python3 /home/debian/SimpleC2/server.py
debian     63549  0.0  0.0   2576  1728 pts/0    S    18:14   0:00 /bin/sh /usr/bin/xvfb-run -a python3 /home/debian/SimpleC2/server.py
debian     63550  0.0  0.0   2576   924 pts/0    S    18:14   0:00 /bin/sh /usr/bin/xvfb-run -a python3 /home/debian/SimpleC2/client_backend.py
debian     63551  0.0  0.0  12704  7328 pts/0    R    18:14   0:00 python3 /home/debian/SimpleC2/server.py
debian     63552  100  0.0  12704  7332 pts/0    R    18:14   0:00 python3 /home/debian/SimpleC2/client_backend.py
debian     63558  0.0  0.0   3876  1808 pts/0    S+   18:14   0:00 grep python3
```
