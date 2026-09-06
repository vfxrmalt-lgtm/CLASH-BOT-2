const { app, BrowserWindow } = require('electron');
const path = require('path');
const { spawn } = require('child_process');

let mainWindow;
let pyProcess = null;

function startBackend() {
  const binaryPath = app.isPackaged
    ? path.join(process.resourcesPath, 'bot-engine.exe')
    : path.join(__dirname, 'bot-engine.exe');

  pyProcess = spawn(binaryPath, [], {
    windowsHide: true,
    stdio: 'ignore'
  });
}

function createWindow() {
  mainWindow = new BrowserWindow({
    width: 440,
    height: 740,
    resizable: false,
    autoHideMenuBar: true,
    backgroundColor: '#020617',
    webPreferences: {
      nodeIntegration: false,
      contextIsolation: true,
    },
  });

  mainWindow.loadFile(path.join(__dirname, 'dist', 'index.html'));
}

app.whenReady().then(() => {
  startBackend();
  setTimeout(createWindow, 2000);
});

app.on('window-all-closed', () => {
  if (pyProcess) pyProcess.kill();
  if (process.platform !== 'darwin') app.quit();
});
