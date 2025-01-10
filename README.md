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
