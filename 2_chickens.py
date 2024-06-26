from cs1graphics import *
anis=Canvas(800,600,'skyblue')
grass=Rectangle(800,200,Point(400,500))
grass.setFillColor('green')
anis.add(grass)

#sun
def sun():
    sun=Circle(30,Point(40,50))
    sun.setFillColor('yellow')
    return sun
#hens
def hen():
    hens=Layer()
    body=Ellipse(55,120,Point(610,400))
    body.setFillColor("white")
    body.setBorderColor("white")
    hens.add(body)
    leg=Circle(25,Point(618,435))
    leg.setFillColor("white")
    leg.setBorderColor("white")
    hens.add(leg)
    upper=Square(7,Point(608,336))
    upper.setFillColor("red")
    upper.setBorderColor("red")
    hens.add(upper)
    aye=Rectangle(2,6,Point(595,380))
    aye.setFillColor("black")
    hens.add(aye)
    mouse=Polygon(Point(576,400),Point(582,406),Point(582,394))
    mouse.setFillColor("yellow")
    mouse.setBorderColor("Yellow")
    hens.add(mouse)
    return hens
#chicken
def chickens():
        chicken=Layer()
        body=Ellipse(28,75,Point(690,422))
        body.setFillColor("yellow")
        body.setBorderColor("yellow")
        chicken.add(body)
        leg=Circle(15,Point(698,445))
        leg.setFillColor("yellow")
        leg.setBorderColor("yellow")
        chicken.add(leg)
        mouse=Polygon(Point(670,422),Point(675,417),Point(675,428))
        mouse.setFillColor("red")
        mouse.setBorderColor("Yellow")
        chicken.add(mouse)
        aye=Rectangle(2,4,Point(685,402))
        aye.setFillColor("red")
        chicken.add(aye)
        aye.setDepth(45)
        chicken2=chicken.clone()
        chicken2.move(70,0)
        chicken.add(chicken2)
        return chicken
chicken=chickens()
anis.add(chicken)
henn=hen()
anis.add(henn)
sunn=sun()
anis.add(sunn)
for i in range(3000):
    chicken.move(-0.19,0)
    henn.move(-0.19,0)
    sunn.move(0.21,0)



