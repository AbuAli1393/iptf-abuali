import subprocess

class ScanModule:
    def run(self, target):
        print(f"[+] Scanning vulnerabilities on {target}")
        results = {}

        # Run Nuclei scans
        nuclei_result = subprocess.run(
            f"nuclei -u https://{target} -t cves.yaml -o nuclei_results.txt", shell=True,
            capture_output=True, text=True
        )
        results["nuclei"] = open("nuclei_results.txt").read() if not nuclei_result.returncode else ""

        # Run OpenVAS scan
        openvas_result = subprocess.run(
            f"omp -u admin -w password --xml='<create_task><name>Scan {target}</name></create_task>'",
            shell=True, capture_output=True, text=True
        )
        results["openvas"] = openvas_result.stdout

        return results