import subprocess

class ReconModule:
    def run(self, target):
        print(f"[+] Running reconnaissance on {target}")
        results = {}

        # Run TheHarvester
        harvester_result = subprocess.run(
            f"theHarvester -d {target} -l 500 -b all", shell=True,
            capture_output=True, text=True
        )
        results["harvester"] = harvester_result.stdout

        # Run Shodan CLI (requires API key setup)
        shodan_result = subprocess.run(
            f"shodan search -- Facet port {target}", shell=True,
            capture_output=True, text=True
        )
        results["shodan"] = shodan_result.stdout

        return results