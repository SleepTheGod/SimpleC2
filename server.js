const express = require('express');
const multer = require('multer');
const fs = require('fs');
const chalk = require('chalk');
const { exec } = require('child_process');
const pyautogui = require('pyautogui');
const path = require('path');
const app = express();
const port = process.env.PORT || 5000; // Allow port to be set by environment variables

// Setup automatic upload path creation
const uploadDir = path.join(__dirname, 'uploads');
if (!fs.existsSync(uploadDir)) {
    fs.mkdirSync(uploadDir, { recursive: true });
}

const upload = multer({ dest: uploadDir });

// Session log storage
let sessionLogs = [];

// Function to automatically create banner
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

// Automatically configure Express to handle JSON and URL-encoded data
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Log session start automatically
app.use((req, res, next) => {
    const sessionStart = new Date().toISOString();
    sessionLogs.push({ ip: req.ip, startTime: sessionStart });
    next();
});

// Endpoint to get server status
app.get('/status', (req, res) => {
    res.json({ status: "Server is running", port: port });
});

// Endpoint to take a screenshot
app.get('/screenshot', (req, res) => {
    const screenshotPath = path.join(__dirname, 'screenshot.png');
    pyautogui.screenshot().save(screenshotPath);
    res.sendFile(screenshotPath);
});

// Endpoint to list files in the current directory
app.get('/files', (req, res) => {
    fs.readdir(__dirname, (err, files) => {
        if (err) {
            return res.status(500).json({ error: err.message });
        }
        res.json(files);
    });
});

// Endpoint to download a file from the server
app.get('/download/:filename', (req, res) => {
    const filename = req.params.filename;
    const filePath = path.join(__dirname, filename);
    if (fs.existsSync(filePath)) {
        res.sendFile(filePath);
    } else {
        res.status(404).json({ error: "File not found" });
    }
});

// Endpoint to upload files
app.post('/upload', upload.single('file'), (req, res) => {
    const targetPath = path.join(uploadDir, req.file.originalname);
    fs.rename(req.file.path, targetPath, err => {
        if (err) {
            return res.status(500).json({ error: err.message });
        }
        res.json({ status: "File uploaded successfully", filename: req.file.originalname });
    });
});

// Endpoint to view session logs
app.get('/logs', (req, res) => {
    res.json(sessionLogs);
});

// Log session end automatically
app.use((req, res, next) => {
    const sessionEnd = new Date().toISOString();
    if (sessionLogs.length > 0) {
        sessionLogs[sessionLogs.length - 1].endTime = sessionEnd;
    }
    next();
});

// Automatically start the server
app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
