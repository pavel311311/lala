import gdsfactory as gf
from gdsfactory.simulation.sax import sax_analysis


c = gf.components.awg(arms=10, outputs=3, fpr_spacing=50, arm_spacing=1, cross_section='strip')
c.write_gds("awg.gds")
c.show()

s = sax_analysis(component=c)