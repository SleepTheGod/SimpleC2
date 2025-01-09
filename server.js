const express = require('express');
const multer = require('multer');
const fs = require('fs');
const chalk = require('chalk');
const { exec } = require('child_process');
const pyautogui = require('pyautogui');
const app = express();
const port = 5000;

const upload = multer({ dest: 'uploads/' });

let sessionLogs = [];

// Print banner in red text
function printBanner() {
    const banner = `
███████╗██╗     ███████╗███████╗██████╗     ████████╗ ██████╗  ██████╗ ██╗     ███████╗    
██╔════╝██║     ██╔════╝██╔════╝██╔══██╗    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝    
███████╗██║     █████╗  █████╗  ██████╔╝       ██║   ██║   ██║██║   ██║██║     ███████╗    
╚════██║██║     ██╔══╝  ██╔══╝  ██╔═══╝        ██║   ██║   ██║██║   ██║██║     ╚════██║    
███████║███████╗███████╗███████╗██║            ██║   ╚██████╔╝╚██████╔╝███████╗███████║    
╚══════╝╚══════╝╚══════╝╚══════╝╚═╝            ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝    
                                                                                           
██████╗ ██████╗ ██████╗      ██████╗ ██╗   ██╗███████╗██████╗     ████████╗ ██████╗██████╗ 
██╔══██╗██╔══██╗██╔══██╗    ██╔═══██╗██║   ██║██╔════╝██╔══██╗    ╚══██╔══╝██╔════╝██╔══██╗
██████╔╝██║  ██║██████╔╝    ██║   ██║██║   ██║█████╗  █████╔╝       ██║   ██║     ██████╔╝
██╔══██╗██║  ██║██╔═══╝     ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗       ██║   ██║     ██╔═══╝ 
██║  ██║██████╔╝██║         ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║       ██║   ╚██████╗██║     
╚═╝  ╚═╝╚═════╝ ╚═╝          ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝       ╚═╝    ╚═════╝╚═╝`;
    console.log(chalk.red(banner));
}

printBanner();

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Log session start
app.use((req, res, next) => {
    const sessionStart = new Date().toISOString();
    sessionLogs.push({ ip: req.ip, startTime: sessionStart });
    next();
});

// Endpoint to get server status
app.get('/status', (req, res) => {
    res.json({ status: "Server is running" });
});

// Endpoint to take a screenshot
app.get('/screenshot', (req, res) => {
    const screenshotPath = 'screenshot.png';
    pyautogui.screenshot().save(screenshotPath);
    res.sendFile(screenshotPath, { root: __dirname });
});

// Endpoint to list files
app.get('/files', (req, res) => {
    fs.readdir('.', (err, files) => {
        if (err) {
            res.status(500).json({ error: err.message });
        } else {
            res.json(files);
        }
    });
});

// Endpoint to download a file
app.get('/download/:filename', (req, res) => {
    const filename = req.params.filename;
    if (fs.existsSync(filename)) {
        res.sendFile(filename, { root: __dirname });
    } else {
        res.status(404).json({ error: "File not found" });
    }
});

// Endpoint to upload a file
app.post('/upload', upload.single('file'), (req, res) => {
    const tempPath = req.file.path;
    const targetPath = `uploads/${req.file.originalname}`;

    fs.rename(tempPath, targetPath, err => {
        if (err) return res.status(500).json({ error: err.message });
        res.json({ status: "File uploaded successfully" });
    });
});

// Endpoint to get session logs
app.get('/logs', (req, res) => {
    res.json(sessionLogs);
});

// Log session end
app.use((req, res, next) => {
    const sessionEnd = new Date().toISOString();
    sessionLogs[sessionLogs.length - 1].endTime = sessionEnd;
    next();
});

app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
