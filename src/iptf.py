import subprocess
import json
from .recon import ReconModule
from .scan import ScanModule
from .exploit import ExploitModule
from .post_exploit import PostExploitModule
from .report import ReportGenerator

class IPTFEngine:
    def __init__(self, target, mode):
        self.target = target
        self.mode = mode
        self.results = {}

    def run(self):
        if self.mode in ["recon", "full"]:
            self.results["recon"] = ReconModule().run(self.target)

        if self.mode in ["scan", "full"]:
            self.results["scan"] = ScanModule().run(self.target)

        if self.mode in ["exploit", "full"]:
            self.results["exploit"] = ExploitModule().run(self.target)

        if self.mode in ["post", "full"]:
            self.results["post"] = PostExploitModule().run(self.target)

    def generate_report(self, filename):
        ReportGenerator(self.results).save(filename)
