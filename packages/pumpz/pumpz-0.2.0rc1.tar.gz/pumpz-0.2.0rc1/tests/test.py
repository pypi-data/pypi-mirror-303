import pumpz as pz
import math

f_aq = open("aq.ppl", "w")
f_org = open("org.ppl", "w")
f_master = open("master.ppl", "w")

aq = pz.pump(f_aq, 26.59, "mm", "mL")
org = pz.pump(f_org, 26.59, "mm", "mL")

master = pz.masterppl(f_master)
master.quickset({0: org, 1: aq})

pz.pump.init(aq, org)
aq.rate(22, 20, "wdr")
org.rate(22, 20, "wdr")

aq.rate(10, 20, "inf")
aq.pause(5 * 60)
pz.pump.sync(aq, org)

org.rate(10, 20, "inf")
t0 = math.ceil(org.time)
org.pause(60)
pz.pump.sync(aq, org)

aq.rate(22, 50, "wdr")
org.rate(22, 50, "wdr")
t1 = math.ceil(org.time)
pause_length = t0 + 500 - t1
if pause_length < 0:
    print("Error: timing is incompatible")
org.pause(pause_length)
pz.pump.sync(aq, org)

aq.loopstart(2)
org.loopstart(2)

aq.rate(22, 50, "inf")
org.rate(22, 50, "inf")
aq.rate(22, 50, "wdr")
org.rate(22, 50, "wdr")

aq.loopend()
org.loopend()

aq.rate(22, 50, "inf")
org.rate(22, 50, "inf")
