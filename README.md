# Keylogger Project (Educational Use Only)

This Python-based keylogger is made for educational cybersecurity exploration. It records key strokes and clipboard changes to log files.



## Disclaimer
This tool is intended for **educational purposes only**.
Unauthorized use may violate laws
Use only in controlled environments

## Current features

- Logs all key presses into 'log.txt' file
- Logs all clipboard changes into 'clipboard.txt' file
- Special keys are labeled (e.g, '[SPACE]', '[ENTER]')
- Timestamps are included for every key press and clipboard change
- Background thread to allow clipboard logging without interfering with main keylogger
- Captures basic system info into 'sysinfo.txt'

## Future Add-Ons (Ideas)

- Group keystrokes into full words/sentences
- Maybe remove special keys to clean up logs
- Add indicator to log file that shows everytime the program runs (session header??)
- Track what app/window user is typing in
- Detect emails, urls, other important things and dump into a separate log file
- Run as background task
- Send logs to remote server
- Log keyboard layout used
- Capture screenshots
- Inject logger into another app (fake app) 
- Add a requirements.txt to install necessary dependencies
