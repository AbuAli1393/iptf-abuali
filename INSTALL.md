## Installation

```bash
git clone https://github.com/AbuAli1393/iptf-abuali.git
cd iptf-abuali
pip install -r requirements.txt

in Docker

Build it:

bash
docker build -t iptf-abuali .

Run it:

bash
docker run -it iptf-abuali --target example.com --mode full

# Usage
bash
python run_iptf.py --target example.com --mode full


Available modes:
recon – Reconnaissance only
scan – Vulnerability scanning
exploit – Exploitation mode
full – Complete penetration test cycle



