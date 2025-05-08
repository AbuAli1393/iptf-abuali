iptf-abuali/
│
├── src/
│   ├── iptf.py                  # Main framework entry point
│   ├── recon.py                 # Reconnaissance & intelligence gathering
│   ├── scan.py                  # Vulnerability scanning engine
│   ├── exploit.py               # Exploitation logic
│   ├── post_exploit.py          # Post-exploitation simulation
│   └── report.py                # Reporting engine
│
├── config/
│   ├── tools.yaml               # Tool configuration file
│   └── settings.json            # Global settings
│
├── docs/
│   ├── README.md
│   └── INSTALL.md
│
├── requirements.txt             # Python dependencies
├── run_iptf.py                  # CLI runner script
├── Dockerfile                   # For containerized deployment
├── .gitlab-ci.yml               # CI/CD integration example
└── LICENSE                      # MIT License