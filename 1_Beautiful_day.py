from cs1graphics import *
anis = Canvas(1200,700,bgColor = "sky blue")
#grass
def grass():
    g=Rectangle(1200,100,Point(600,650))
    g.setFillColor("green")
    g.setDepth(80)
    anis.add(g)

#home
def house():
    home=Layer()
    front=Rectangle(250,200,Point(780,500))
    front.setFillColor('red')
    front.setBorderWidth(4)
    home.add(front)

    window=Square(80,Point(710,485))
    window.setFillColor('white')
    window.setBorderWidth(4)
    home.add(window)
    wp1=Path(Point(670,485),Point(750,485))
    wp1.setBorderWidth(4)
    home.add(wp1)

    wp2=Path(Point(710,445),Point(710,525))
    wp2.setBorderWidth(4)
    home.add(wp2)

    door=Rectangle(80,170,Point(832,515))
    door.setFillColor('grey')
    door.setBorderWidth(4)
    home.add(door)

    pus=Rectangle(45,100,Point(710,320))
    pus.setFillColor('gold')
    home.add(pus)

    top=Polygon(Point(635,400),Point(780,250),Point(925,400))
    top.setFillColor('black')
    home.add(top)
    anis.add(home)

#person
def personn():
    person=Layer()
    stomach=Ellipse(30,90,Point(500,490))
    stomach.setFillColor('pink')
    person.add(stomach)

    head=Circle(20,Point(500,426))
    head.setFillColor((255,153,0))
    person.add(head)

    eye_l=Circle(1,Point(490,420))
    person.add(eye_l)

    eye_r=Circle(1,Point(510,420))

    person.add(eye_r)
    mouth=ClosedSpline(Point(495,433),Point(500,436),Point(505,433))
    person.add(mouth)
    leg1=Path(Point(496,535),Point(496,600))
    leg2=Path(Point(504,535),Point(504,600))
    person.add(leg1)
    person.add(leg2)

    hand1=Path(Point(485,470),Point(445,440))
    hand2=Path(Point(515,470),Point(555,440))
    person.add(hand1)
    person.add(hand2)
    person.move(-400,0)
    person.setDepth(45)
    return person

#clouds
def cloud():
    c=Layer()
    c1 = Ellipse(200,100,Point(200,100))
    c1.setFillColor('white')
    c1.setBorderColor('white')
    c.add(c1)
    c2=Ellipse(50,100,Point(250,75))
    c2.setFillColor('white')
    c2.setBorderColor('white')
    c2.rotate(40)
    c.add(c2)
    c3=c2.clone()
    c3.rotate(50)
    c3.move(10,0)
    c.add(c3)
    c4=c2.clone()
    c4.rotate(50)
    c4.move(25,40)
    c.add(c4)
    c5=c4.clone()
    c5.move(-50,10)
    c5.rotate(-40)
    c.add(c5)
    c6=c5.clone()
    c.add(c6)
    c6.move(-90,10)
    c6.rotate(40)
    c7=c6.clone()
    c7.move(-20,-20)
    c.add(c7)
    anis.add(c)

    cc=c.clone()
    cc.scale(0.75)
    cc.rotate(-20)
    cc.move(350,200)
    anis.add(cc)

    ccc=c.clone()
    ccc.move(600,-30)
    anis.add(ccc)

    cccc=cc.clone()
    cccc.move(580,-40)
    anis.add(cccc)  

#trees
def trees():
    tree1=Layer()
    leave=Polygon(Point(10,200),Point(70,100),Point(130,200),Point(90,200),Point(130,260),Point(90,260),Point(130,320),Point(10,320),Point(50,260),Point(10,260),Point(50,200))
    leave.setFillColor('green')
    leave.scale(1.2)
    leave.move(0,50)
    tree1.add(leave)

    stem=Rectangle(70,207,Point(80,497))
    stem.setFillColor('brown')
    tree1.add(stem)
    tree2=tree1.clone()
    tree2.scale(0.8)
    tree2.moveTo(150,120)
    tree3=tree1.clone()
    tree3.scale(0.9)
    tree3.moveTo(260,60)
    tree4=tree2.clone()
    tree4.move(780,0)
    tree5=tree3.clone()
    tree5.move(780,0)
    anis.add(tree1)
    anis.add(tree2)
    anis.add(tree3)
    anis.add(tree4)
    anis.add(tree5)
cloud()
house()
per=personn()
anis.add(per)
grass()
trees()


for i in range(2100):
    per.move(0.2,0)
#comments
comment=Layer()
c1=Ellipse(16,18,Point(468,400))
c2=Ellipse(100,60,Point(410,360))
comment.add(c1)
comment.add(c2)
t=Text('python assignment',9,Point(410,360))
comment.add(t)
comment.move(50,0)
anis.add(comment)
for i in range(2500):
    per.move(0.2,0)


