import argparse
from src.iptf import IPTFEngine

def main():
    parser = argparse.ArgumentParser(description="IPTF_AbuAli - Integrated Penetration Testing Framework")
    parser.add_argument("--target", required=True, help="Target URL or IP address")
    parser.add_argument("--mode", choices=["recon", "scan", "exploit", "post", "full"], default="full",
                        help="Test mode to run")
    parser.add_argument("--output", default="report.json", help="Output report file")

    args = parser.parse_args()

    engine = IPTFEngine(args.target, args.mode)
    engine.run()
    engine.generate_report(args.output)

if __name__ == "__main__":
    main()