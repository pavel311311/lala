import gdsfactory as gf
import matplotlib.pyplot as plt

c =  gf.Component()

wr1 = c << gf.components.straight(length=2)
wr2 = c << gf.components.straight(length=0.5)

wr2.movey(2)
c.add_ports(wr1.ports, prefix="bot_")
c.add_ports(wr2.ports, prefix="top_")



c.pprint_ports

#c.plot()
# plt.show()