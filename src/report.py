import json

class ReportGenerator:
    def __init__(self, data):
        self.data = data

    def save(self, filename):
        with open(filename, "w") as f:
            json.dump(self.data, f, indent=4)
        print(f"[+] Report saved to {filename}")