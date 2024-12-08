import gdsfactory as gf

pp = (1,2)

c = gf.Component()

cc = c << gf.components.rectangle(size=(5,5))

cc.move(pp)