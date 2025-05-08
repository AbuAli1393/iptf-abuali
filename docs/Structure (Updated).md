iptf-abuali/
│
├── src/
│   ├── iptf.py                  # Main engine class
│   ├── recon.py                 # Reconnaissance module
│   ├── scan.py                  # Scanning logic
│   ├── exploit.py               # Exploitation logic
│   ├── post_exploit.py          # Post-exploitation logic
│   └── report.py                # Reporting engine
│
├── config/
│   ├── tools.yaml
│   └── settings.json
│
├── web/
│   ├── app.py                   # Flask main application
│   ├── templates/
│   │   ├── index.html           # Home page
│   │   ├── results.html         # Results display
│   │   └── report.html          # Report viewer
│   └── static/
│       ├── style.css            # Basic styling
│       └── script.js            # Optional JS enhancements
│
├── requirements.txt
├── run_iptf.py
├── Dockerfile
├── .gitlab-ci.yml
└── LICENSE