import gdsfactory as gf
import matplotlib.pyplot as plt

@gf.cell
def trace_single() ->gf.Component:
    #Pad_left
    s0 = gf.Section(width=100, offset=0, layer=(2, 0), name="core", port_names=("o1", "o2"))
    s1 = gf.Section(width=150, offset=-155, layer=(2, 0), name="etch")
    s2 = gf.Section(width=150, offset=155, layer=(2, 0), name="wg2")
    X1 = gf.CrossSection(sections=[s0, s1, s2])
    
    P1 = gf.path.straight(length=150)
    wg1 = gf.path.extrude(P1, X1)
    
    #Pad_right
    s0 = gf.Section(width=65, offset=0, layer=(2, 0), name="core", port_names=("o1", "o2"))
    s1 = gf.Section(width=77, offset=-131.25, layer=(2, 0), name="etch")
    s2 = gf.Section(width=77, offset=131.25, layer=(2, 0), name="wg2")
    X2 = gf.CrossSection(sections=[s0, s1, s2])
    
    P2 = gf.path.straight(length=100)
    wg2 = gf.path.extrude(P2, X2)
    
    
    # trace rf
    # Create the transitional CrossSection
    Xtrans = gf.path.transition(cross_section1=X1, cross_section2=X2, width_type="linear")
    # Create a Path for the transitional CrossSection to follow
    P3 = gf.path.straight(length=500, npoints=100)
    # Use the transitional CrossSection to create a Component
    straight_transition = gf.path.extrude_transition(P3, Xtrans)
    
    
    # Place both cross-section Components and quickplot them
    c = gf.Component()
    wg1ref = c << wg1
    wg2ref = c << wg2
    wgtref = c << straight_transition
    
    wgtref.connect("o1", wg1ref.ports["o2"])
    wg2ref.connect("o1", wgtref.ports["o2"])

    return c
    
def trace_array() -> gf.Component:
    c = gf.Component()
    pitch = 500
    for n in range(8):
        c.add_ref(trace_single()).movey(pitch*n*-1)
    return c

#c = trace_array()
#c.plot()
#plt.show()