import gdsfactory as gf
import trace
import model_pd

def outline(size=(1500,4500),w=50) -> gf.Component:
    c =  gf.Component()
    c1 = c << gf.components.rectangle(size=size)
    c2 = c << gf.components.rectangle(size=(size[0]-w*2,size[1]-w*2))
    c2.movex(w)
    c2.movey(w)
    cc = gf.boolean(A=c1, B=c2, operation='not')
    return cc

#####################
c =  gf.Component()

pd_array = c << model_pd.pd_array()
pd_trace = c << trace.trace_array()
outline = c << outline(size=(1500,4500),w=40)

outline.move((-100,-4000))
pd_array.move((800,131.25))

c.write_gds("./interposer/interposer.gds")