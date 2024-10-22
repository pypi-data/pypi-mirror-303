from .utilities import decompose_dict, factor_check

class masterppl:
    """
    Based on maseter ppl file made by Tim Burgess,
    SyringePumpPro https://SyringePumpPro.com
    timb@syringepumppro.com
    Find example file by Tim on SyringPumpPro manual
    All code is original, by me
    """
    def __init__(self, file, adrs=[]):
        self.file = file
        self.adrs = adrs

    def add(self, adr: int, ppl):
        self.adrs.append(adr)
        self.file.write(f"Set adr={adr}\n")
        self.file.write(f"call {ppl.file.name}\n")

    def clearall(self):
        for adr in self.adrs:
            self.file.write(f"{adr}cldinf\n{adr}cldwdr\n{adr}dis\n")

    def beepall(self):
        for adr in self.adrs:
            self.file.write(f"{adr}buz13\n")
    
    def quickset(self, all: dict):
        for tuples in all.items():
            self.add(*tuples)
        self.clearall()
        self.beepall()