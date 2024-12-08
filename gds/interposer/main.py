import gdsfactory as gf
import matplotlib.pyplot as plt
import model


#####################
c =  gf.Component()

pd_array = c << model.pd_array()
pd_trace = c << model.trace_array()
outline = c << model.outline(size=(1500,4500),w=40)

outline.move((-100,-4000))
pd_array.move((800,131.25))

c.write_gds("./gds/interposer/interposer_800G_Rx.gds")

c.plot()
plt.show()
