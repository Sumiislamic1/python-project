from cs1graphics import *
anis=Canvas(600,500,'skyblue')
hang=Layer()
hr=Polygon(Point(100,450),Point(100,455),Point(500,455),Point(500,450),Point(300,420))
hr.setFillColor('yellow')
hang.add(hr)
hf=Polygon(Point(100,450),Point(300,437),Point(500,450),Point(300,380))
hf.setFillColor('brown')
hang.add(hf)
#person
face=Circle(8,Point(300,400))
face.setFillColor('white')
hang.add(face)
body=Path(Point(300,407),Point(300,445))
body.setBorderWidth(3)
hang.add(body)
hand=Path(Point(280,410),Point(320,410))
hand.setBorderWidth(3)
hang.add(hand)
lleg=Path(Point(300,445),Point(290,465))
lleg.setBorderWidth(3)
hang.add(lleg)
rleg=Path(Point(300,445),Point(310,465))
rleg.setBorderWidth(3)
hang.add(rleg)


#message

mes=Ellipse(50,100,Point(380,360))
mes.rotate(90)
hang.add(mes)
mes_text=Text('Wheee!',20,Point(380,360))
hang.add(mes_text)

l=Path(Point(342,378),Point(326,392),Point(360,384))
hang.add(l)
anis.add(hang)

hang.setDepth(48)
#cloud
cool=Layer()
c=Circle(40,Point(150,80))
c.setFillColor('white')
c.setBorderColor('white')
cool.add(c)
cc=Ellipse(50,100,Point(180,80))
cc.setFillColor('white')
cc.setBorderColor('white')
cc.rotate(45)
cool.add(cc)
c2=c.clone()
c2.move(20,20)
cool.add(c2)
c3=c.clone()
c3.move(-30,30)
cool.add(c3)
c4=c3.clone()
c4.move(-50,-2)
cool.add(c4)
c5=c4.clone()
c5.move(-50,-6)
cool.add(c5)
c6=c.clone()
c6.move(-50,-20)
cool.add(c6)
anis.add(cool)
cooll=cool.clone()
cooll.move(360,100)
anis.add(cooll)
coolll=cool.clone()
coolll.scale(0.8)
coolll.move(-20,230)
coolll.rotate(-20)
anis.add(coolll)
cool.setDepth(47)
coolll.setDepth(45)
ci=Circle(20,Point(180,300))
ci.setFillColor('white')
ci.setBorderColor('white')
anis.add(ci)
ci.setDepth(45)
#Birds
bird=Path(Point(385,435),Point(395,428),Point(400,440),Point(405,428),Point(415,435))
anis.add(bird)
bird2=bird.clone()
bird.move(50,-30)
anis.add(bird2)
bird3=bird.clone()
bird3.move(-100,10)
anis.add(bird3)

for i in range(1600):
    hang.move(0,-0.2)












