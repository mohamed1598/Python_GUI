from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from time import *
import pygame

a = 0
c = 0
t0 = time()
v = 0
angle = 0
y = 0
e = 0
level=1
w = 0
w0=0
w1=0
w2=0
w3=0
w4=0
w5=0
m0=0
lastlevel=0
def test():
    global v
    global a
    global c
    global x
    global e
    global w
    global w0
    global w1
    global w2
    global w3
    global w4
    global w5
    global t0
    global y
    global level
    global lastlevel
    global m0
    lastlevel=level
    level=0
    m0=time()
    if v == 4:
        level=3
    v += 1
    a = 0
    c = 0
    x = 0
    y = 0
    e = 0
    w = 0
    w0 = 0
    w1 = 0
    w2 = 0
    w3 = 0
    w4 = 0
    w5 = 0
    t0 = time()


def Line( x1, z1, x2, z2, x3, z3, x4, z4):
    glLoadIdentity()
    glBegin(GL_POLYGON)
    glColor(1,1,1)
    glVertex(x1, 0, z1)
    glVertex(x2, 0, z2)
    glVertex(x3, 0, z3)
    glVertex(x4, 0, z4)
    glEnd()


def model(a,c):
    glLoadIdentity()
    glColor(0, 0, 0)
    glTranslate(1 + a, 0, 138 + c)
    glutSolidCube(0.7)
    glLoadIdentity()
    glColor(0, 0, 0)
    glTranslate(-1 + a, 0, 138 + c)
    glutSolidCube(0.7)
    glLoadIdentity()
    glColor(0, 0, 0)
    glTranslate(1 + a, 0, 136 + c)
    glutSolidCube(0.7)
    glLoadIdentity()
    glColor(0, 0, 0)
    glTranslate(-1 + a, 0, 136 + c)
    glutSolidCube(0.7)
    glLoadIdentity()
    glColor(0, 0.4, 0.4)
    glTranslate(0 + a, 2, 137 + c)
    glutSolidCube(3)
    glLoadIdentity()
    glColor(1, 1, 0)
    glTranslate(0.9 + a, 4, 136 + c)
    glutSolidCube(0.7)
    glLoadIdentity()
    glColor(1, 1, 0)
    glTranslate(-0.9 + a, 4, 136 + c)
    glutSolidCube(0.7)

def Wall(r,g,b,x,y,z):
    glLoadIdentity()
    glColor(r,g,b)
    glTranslate(x, y, z)
    glScale(8, 40, 1000)
    glutSolidCube(1)


# CAR
def car(x,z,r1,g1,b1,r2,g2,b2):
    # car down
    glLoadIdentity()
    glColor3f(r1, g1, b1)
    glTranslate(x, 3, z)
    glScale(3, 1, 1)
    glutSolidCube(4)
    # car up
    glLoadIdentity()
    glColor3f(r2, g2, b2)
    glTranslate(x, 6, z)
    glScale(1.7, 1, 1)
    glutSolidCube(4)
    # front torus
    glLoadIdentity()
    glColor(r2,g2,b2)
    glTranslate(x + 4 , 1, z +  2)
    glRotate(angle, 0, 0, 1)
    glutSolidTorus(0.5, 1.5, 20, 20)
    # back torus
    glLoadIdentity()
    glColor(r2,g2,b2)
    glTranslate(x - 4, 1, z + 2)
    glRotate(angle, 0, 0, 1)
    glutSolidTorus(0.5, 1.5, 20, 20)


def carCollusion(t, zb, ze):
    global a
    global c
    if a > t - 10 and a < t + 10 and 135 + c > ze and 135 + c < zb:  # t-8 8 is the half of the car down and we add 3
        test()


def road(r, g, b, x, zb, ze):
    glColor(r, g, b)
    glBegin(GL_QUADS)
    glVertex(x, 0, zb)
    glVertex(-x, 0, zb)
    glVertex(-x, 0, ze)
    glVertex(x, 0, ze)
    glEnd()


def wood( t, xb, xe, zb, ze):
    # global a
    glLoadIdentity()
    glColor(0.4,0.3,0)
    glTranslate(t, 0, 0)
    glBegin(GL_QUADS)
    glVertex(xb, .1, zb)
    glVertex(xb, .1, ze)
    glVertex(xe, .1, ze)
    glVertex(xe, .1, zb)
    glEnd()


def seaCollusion(c, xb1, xe1, zb, ze, dir):
    global a
    if 135 + c > ze and 135 + c < zb:
        if not (a > xb1 and a < xe1):
            test()
    if level==1:
        if 135 + c > ze and 135 + c < zb and a < xe1 and a > xb1:
            if dir == 1:
                a = a - .14
            else:
                a = a + .14
            if a <= -48:
                a = -48
            if a >= 48:
                a = 48
    if level==2:
        if 135 + c > ze and 135 + c < zb and a < xe1 and a > xb1:
            if dir == 1:
                if zb == -90:
                    a = a - .14
                if zb == -100:
                    a = a - .16
                if zb == -110:
                    a = a - .18
                if zb == -120:
                    a = a - .2
                if zb == -130:
                    a = a - .22
                if zb == -140:
                    a = a - .24
            else:
                if zb == -90:
                    a = a + .14
                if zb == -100:
                    a = a + .16
                if zb == -110:
                    a = a + .18
                if zb == -120:
                    a = a + .2
                if zb == -130:
                    a = a + .22
                if zb == -140:
                    a = a + .24
            if a <= -48:
                a = -48
            if a >= 48:
                a = 48



def init():
    global a
    global c
    global level
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(100, 1, 1, 150)
    gluLookAt(0, 30, 170 + c,  # eye
              0, 0, -200,  # center
              0, 1, 0)  # up
    # SKY
    if level==1 or level==2:
        glClearColor(0, 0.7, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT)
    if level==0:
        glClearColor(0, 0, 0, 1)
        glClear(GL_COLOR_BUFFER_BIT)


pygame.mixer.init()
jump1 = pygame.mixer.Sound("jump.wav")
jump1.set_volume(0.1)

pygame.mixer.init()
lay= pygame.mixer.Sound("lay.wav")
lay.set_volume(0.2)

pygame.mixer.init()
rgala= pygame.mixer.Sound("rgala.wav")
rgala.set_volume(0.2)


def ARROW_KEYS(key, x, y):
    global a
    global c
    global level
    global m0
    global lastlevel
    if key == GLUT_KEY_LEFT:
        jump1.play()
        a -= 2
        if a <= -48:
            a = -48
    elif key == GLUT_KEY_RIGHT:
        jump1.play()
        a += 2
        if a >= 48:
            a = 48
    elif key == GLUT_KEY_UP:
        jump1.play()
        c -= 10
        if level==1:
            if c <= -138:
                c = -138
                m0=time()
                lastlevel=level
                level=4
        if level==2:
            if c <= -290:
                c = -290
                m0 = time()
                lastlevel = level
                level = 4
    elif key == GLUT_KEY_DOWN:
        jump1.play()
        c += 10
        if c >= 0:
            c = -0


def goOrtho(l=-1, r=1, b=-1, t=1, n=-1, f=1):
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    glOrtho(l, r, b, t, n, f)
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()


def backPrespective():
    glEnable(GL_LIGHTING)
    glMatrixMode(GL_MODELVIEW)
    glPopMatrix()
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glDisable(GL_LIGHTING)


def drawText(string, x, y, scale=0.0005, w=2, r=0, g=0, b=0):
    glLineWidth(w)
    glColor(r, g, b)  # Yellow Color
    glTranslate(x - len(string) / 50, y, 0)
    glScale(scale, scale, 1)
    string = string.encode()  # conversion from Unicode string to byte string
    for c in string:
        glutStrokeCharacter(GLUT_STROKE_ROMAN, c)


forward = 1
x = 0


def draw():
    global a
    global c
    global forward
    global x
    global y
    global e
    global w
    global w0
    global w1
    global w2
    global w3
    global w4
    global w5
    global level
    global angle
    global lastlevel
    global m0
    if level==0:
        m1 = time()
        lay.play()
        if m1>m0+10:
            level=lastlevel
        init()
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glClear(GL_COLOR_BUFFER_BIT)
        goOrtho()
        drawText("YOU ARE DEAD.", -.2, 0, 0.001, 6, 1, 0, 0)
        backPrespective()
        glutSwapBuffers()
    if level==1:
        t = int(60 - (time() - t0))
        # print(a,"    " , c)
        # constant
        init()
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glClear(GL_COLOR_BUFFER_BIT)
        #########



        # holes
        glLoadIdentity()
        glColor(0, 0, 0)
        glBegin(GL_QUADS)
        glVertex(50, 0, 130)
        glVertex(50, 0, 0)
        glVertex(50, 18, 0)
        glVertex(50, 18, 130)
        glEnd()
        # begin of the road
        road(0, 0.5, 0, 50, 150, 140)
        road(0, 0.5, 0, 50, 140, 130)
        road(0.45, 0.45, 0.45, 50, 130, 120)
        road(0.45, 0.45, 0.45, 50, 120, 110)
        road(0.45, 0.45, 0.45, 50, 110, 100)
        road(0, 0.5, 0, 50, 100, 90)
        road(0, 0.3, 0.9, 50, 90, 80)
        road(0, 0.5, 0, 50, 80, 70)
        road(0.45, 0.45, 0.45, 50, 70, 60)
        road(0.45, 0.45, 0.45, 50, 60, 50)
        road(0, 0.5, 0, 50, 50, 40)
        road(0, 0.3, 0.9, 50, 40, 30)
        road(0, 0.3, 0.9, 50, 30, 20)
        road(0, 0.5, 0, 50, 20, 10)
        road(0, 0.5, 0, 50, 10, 0)
        # end of the road

        # Road Lines
        Line(-20, 123, -20, 120, -40, 120, -40, 123)
        Line( 10, 123, 10, 120, -10, 120, -10, 123)
        Line( 40, 123, 40, 120, 20, 120, 20, 123)
        Line( -20, 113, -20, 110, -40, 110, -40, 113)
        Line( 10, 113, 10, 110, -10, 110, -10, 113)
        Line( 40, 113, 40, 110, 20, 110, 20, 113)
        Line( -20, 62, -20, 59, -40, 59, -40, 62)
        Line( 10, 62, 10, 59, -10, 59, -10, 62)
        Line( 40, 62, 40, 59, 20, 59, 20, 62)

        # End of Road Lines
#wood
        #wood(t, xb, xe, zb, ze)
        wood( 2 * w, 10, 50, 90, 80)
        seaCollusion(c, 2 * w + 10, 2 * w + 50, 90, 80, 1)


        wood( 2 * w, 10, 50, 40, 30)
        seaCollusion(c, 2 * w + 10, 2 * w + 50, 40, 30, 1)


        wood( -2 * w, 10, 50, 30, 20)
        seaCollusion(c, 10 - 2 * w, 50 - 2 * w, 30, 20, 0)

        # model
        model(a, c)
        if forward:
            x += 0.05
            y -= .07
            e += .07
            w -= 0.07
            angle += 0.1
            if w < -80:
                w = 50

        # CARS

        j = -600
        while j < 50:
            car(e + j, 55, 0.9, 0.7, 0, 0.4, 0, 0.8)
            carCollusion(e + j, 60, 50)
            j += 50
        i = 600
        while i > -50:
            car(y + i, 65, 1, 0, 0, 0, 0, 0)
            carCollusion(y + i, 70, 60)
            i -= 60
        j = -600
        while j < 50:
            car(e + j, 105, 1, 1, 1, 1, 0, 0)
            carCollusion(e + j, 110, 100)
            j += 50
        i = 600
        while i > -50:
            car(y + i, 115, 0, 0.1, 0.7, 0, 0.9, 0.9)
            carCollusion(y + i, 120, 110)
            i -= 60
        j = -600
        while j < 50:
            car(x + j, 125, 1, 0.9, 0.2, 0, 0, 0.7)
            carCollusion(x + j, 130, 120)
            j += 50

            # wall
            Wall(0.5, 0.5, 0.5, 87, 0, 0)
            Wall(0.5, 0.5, 0.5, -87, 0, 0)


        goOrtho()
        drawText("lives" + " [" + str(4 - v) + "]", - 0.75, .6, 0.0005, 2, 1, 0, 0)
        backPrespective()

        if t == 0:
            test()

        goOrtho()
        drawText(str(t), - 0.75, 0.7, 0.0005, 2, 1, 0, 0)
        backPrespective()

        glutSwapBuffers()
    if level==2:
        t = int(90 - (time() - t0))
        # print(a,"    " , c)
        # constant
        init()
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glClear(GL_COLOR_BUFFER_BIT)

        # begin of the road
        glLoadIdentity()
        road(0, 0.5, 0, 50, 140, 130)
        road(0.45, 0.45, 0.45, 50, 130, 120)
        road(0.45, 0.45, 0.45, 50, 120, 110)
        road(0.45, 0.45, 0.45, 50, 110, 100)
        road(0.45, 0.45, 0.45, 50, 100, 90)
        road(0, 0.5, 0, 50, 90, 80)
        road(0.45, 0.45, 0.45, 50, 80, 70)
        road(0.45, 0.45, 0.45, 50, 70, 60)
        road(0.45, 0.45, 0.45, 50, 60, 50)
        road(0.45, 0.45, 0.45, 50, 50, 40)
        road(0, 0.5, 0, 50, 40, 30)
        road(0, 0.5, 0, 50, 30, 20)
        road(0, 0.5, 0, 50, 20, 10)
        road(0, 0.5, 0, 50, 10, 0)
        road(0, 0.5, 0, 50, 0, -10)
        road(0.45, 0.45, 0.45, 50, -10, -20)
        road(0.45, 0.45, 0.45, 50, -20, -30)
        road(0.45, 0.45, 0.45, 50, -30, -40)
        road(0.45, 0.45, 0.45, 50, -40, -50)
        road(0.45, 0.45, 0.45, 50, -50, -60)
        road(0.45, 0.45, 0.45, 50, -60, -70)
        road(0.45, 0.45, 0.45, 50, -70, -80)
        road(0, 0.5, 0, 50, -80, -90)
        road(0, 0.3, 0.9, 50, -90, -100)
        road(0, 0.3, 0.9, 50, -100, -110)
        road(0, 0.3, 0.9, 50, -110, -120)
        road(0, 0.3, 0.9, 50, -120, -130)
        road(0, 0.3, 0.9, 50, -130, -140)
        road(0, 0.3, 0.9, 50, -140, -150)
        road(0, 0.5, 0, 50, -150, -160)
        # end of the road

        # Road Lines
        Line( -20, 123, -20, 120, -40, 120, -40, 123)
        Line( 10, 123, 10, 120, -10, 120, -10, 123)
        Line(40, 123, 40, 120, 20, 120, 20, 123)
        Line( -20, 113, -20, 110, -40, 110, -40, 113)
        Line( 10, 113, 10, 110, -10, 110, -10, 113)
        Line( 40, 113, 40, 110, 20, 110, 20, 113)
        Line( -20, 103, -20, 100, -40, 100, -40, 103)
        Line( 10, 103, 10, 100, -10, 100, -10, 103)
        Line( 40, 103, 40, 100, 20, 100, 20, 103)
        Line( -20, 62, -20, 59, -40, 59, -40, 62)
        Line( 10, 62, 10, 59, -10, 59, -10, 62)
        Line( 40, 62, 40, 59, 20, 59, 20, 62)
        Line( -20, 72, -20, 69, -40, 69, -40, 72)
        Line( 10, 72, 10, 69, -10, 69, -10, 72)
        Line( 40, 72, 40, 69, 20, 69, 20, 72)
        Line( -20, 52, -20, 49, -40, 49, -40, 52)
        Line(10, 52, 10, 49, -10, 49, -10, 52)
        Line( 40, 52, 40, 49, 20, 49, 20, 52)
        Line( 40, 72, 40, 69, 20, 69, 20, 72)
        Line( -20, -17, -20, -20, -40, -20, -40, -17)
        Line( 10, -17, 10, -20, -10, -20, -10, -17)
        Line( 40, -17, 40, -20, 20, -20, 20, -17)
        Line( -20,  -27, -20, -30, -40, -30, -40, -27)
        Line(10,  -27, 10, -30, -10, -30, -10, -27)
        Line( 40, -27, 40, -30, 20, -30, 20, -27)
        Line(-20, -37, -20, -40, -40, -40, -40, -37)
        Line( 10, -37, 10, -40, -10, -40, -10, -37)
        Line( 40, -37, 40, -40, 20, -40, 20, -37)
        Line( -20, -47, -20, -50, -40, -50, -40, -47)
        Line( 10, -47, 10, -50, -10, -50, -10, -47)
        Line( 40, -47, 40,  -50, 20, -50, 20, -47)
        Line( -20, -57, -20, -60, -40, -60, -40, -57)
        Line( 10, -57, 10, -60, -10, -60, -10, -57)
        Line( 40, -57, 40, -60, 20, -60, 20, -57)
        Line( -20, -67, -20, -70, -40, -70, -40, -67)
        Line( 10, -67, 10, -70, -10, -70, -10,  -67)
        Line( 40, -67, 40, -70, 20, -70, 20, -67)

        # End of Road Lines

        # wood
        #wood( t, xb, xe, zb, ze)
        wood( 2 * w5, 10, 50, -140, -150)
        seaCollusion(c, 2 * w5 + 10, 2 * w5 + 50, -140, -150, 1)

        wood( -2 * w4, 10, 50, -130, -140)
        seaCollusion(c, - 2 * w4 + 10, -2 * w4 + 50, -130, -140, 0)

        wood( +2 * w3, 10, 50, -120, -130)
        seaCollusion(c, 10 + 2 * w3, 50 + 2 * w3, -120, -130, 1)

        wood( -2 * w2, 10, 50, -110, -120)
        seaCollusion(c, -2 * w2 + 10, - 2 * w2 + 50, -110, -120, 0)

        wood( 2 * w1, 10, 50, -100, -110)
        seaCollusion(c, 2 * w1 + 10, 2 * w1 + 50, -100, -110, 1)

        wood( -2 * w0, 10, 50, -90, -100)
        seaCollusion(c, 10 - 2 * w0, 50 - 2 * w0, -90, -100, 0)

        # model
        model(a, c)
        if forward:
            x += 0.07
            y -= .09
            e += .11
            w0 -= 0.07
            w1 -= .08
            w2 -= .09
            w3 -= .1
            w4 -= .11
            w5 -= .12
            angle -= 0.1
            if w0 < -20:
                w0 = 50
            if w1 < -50:
                w1 = 40
            if w2 < -20:
                w2 = 50
            if w3 < -50:
                w3 = 40
            if w4 < -20:
                w4 = 50
            if w5 < -50:
                w5 = 50

        # cars
        # last Cars
        j = -600
        while j < 50:
            car(e + j, -75, 1, 0, 0, 0, 0, 0)
            carCollusion(e + j, -70, -80)
            j += 50
        i = 600
        while i > -50:
            car(y + i, -65, 1, 1, 1, 1, 0, 0)
            carCollusion(y + i, -60, -70)
            i -= 60

        j = -600
        while j < 50:
            car(e + j + 20, -55, 1, 0.9, 0.2, 0, 0, 0.7)
            carCollusion(e + j + 20, -50, -60)
            j += 50
        i = 600
        while i > -50:
            car(y + i + 10, -45, 1, 0.1, 0.7, 0.1, 0.8, 0.1)
            carCollusion(y + i + 10, -40, -50)
            i -= 60
        j = -600
        while j < 50:
            car(e + j, -35, 0.9, 0.7, 0, 0.4, 0, 0.8)
            carCollusion(e + j, -30, -40)
            j += 50
        i = 600

        j = -600
        while j < 50:
            car(e + j + 20, -25, 1, 0, 0, 0, 0, 0)
            carCollusion(e + j + 20, -20, -30)
            j += 50
        i = 600
        while i > -50:
            car(y + i + 50, -15, 1, 1, 1, 1, 0, 0)
            carCollusion(y + i + 50, -10, -20)
            i -= 60
        j = -600

        # second 4 cars
        while j < 50:
            car(e + j + 20, 45, 0, 0.1, 0.7, 0, 0.9, 0.9)
            carCollusion(e + j + 20, 50, 40)
            j += 50
        i = 600
        while i > -50:
            car(y + i + 10, 55, 1, 0.9, 0.2, 0, 0, 0.7)
            carCollusion(y + i + 10, 60, 50)
            i -= 60
        j = -600
        while j < 50:
            car(e + j, 65, 1, 0.1, 0.7, 0.1, 0.8, 0.1)
            carCollusion(e + j, 70, 60)
            j += 50
        i = 600
        while i > -50:
            car(y + i, 75, 0.9, 0.7, 0, 0.4, 0, 0.8)
            carCollusion(y + i, 80, 70)
            i -= 60

        # first 4 Cars
        j = -600
        while j < 50:
            car(e + j + 20, 95, 1, 0, 0, 0, 0, 0)
            carCollusion(e + j + 20, 100, 90)
            j += 50
        i = 600
        while i > -50:
            car(y + i + 10, 105, 1, 1, 1, 1, 0, 0)
            carCollusion(y + i + 10, 110, 100)
            i -= 60
        j = -600
        while j < 50:
            car(e + j, 115, 0, 0.1, 0.7, 0, 0.9, 0.9)
            carCollusion(e + j, 120, 110)
            j += 50
        i = 600
        while i > -50:
            car(y + i, 125, 1, 0.9, 0.2, 0, 0, 0.7)
            carCollusion(y + i, 130, 120)
            i -= 60

        ##################### wall
        Wall(0.5, 0.5, 0.5, -87, 0, 0)
        Wall(0.5, 0.5, 0.5, 87, 0, 0)
        t = int(90 - (time() - t0))
        # print(a,"    " , c)
        # constant
        init()
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glClear(GL_COLOR_BUFFER_BIT)

        # begin of the road
        glLoadIdentity()
        road(0, 0.5, 0, 50, 140, 130)
        road(0.45, 0.45, 0.45, 50, 130, 120)
        road(0.45, 0.45, 0.45, 50, 120, 110)
        road(0.45, 0.45, 0.45, 50, 110, 100)
        road(0.45, 0.45, 0.45, 50, 100, 90)
        road(0, 0.5, 0, 50, 90, 80)
        road(0.45, 0.45, 0.45, 50, 80, 70)
        road(0.45, 0.45, 0.45, 50, 70, 60)
        road(0.45, 0.45, 0.45, 50, 60, 50)
        road(0.45, 0.45, 0.45, 50, 50, 40)
        road(0, 0.5, 0, 50, 40, 30)
        road(0, 0.5, 0, 50, 30, 20)
        road(0, 0.5, 0, 50, 20, 10)
        road(0, 0.5, 0, 50, 10, 0)
        road(0, 0.5, 0, 50, 0, -10)
        road(0.45, 0.45, 0.45, 50, -10, -20)
        road(0.45, 0.45, 0.45, 50, -20, -30)
        road(0.45, 0.45, 0.45, 50, -30, -40)
        road(0.45, 0.45, 0.45, 50, -40, -50)
        road(0.45, 0.45, 0.45, 50, -50, -60)
        road(0.45, 0.45, 0.45, 50, -60, -70)
        road(0.45, 0.45, 0.45, 50, -70, -80)
        road(0, 0.5, 0, 50, -80, -90)
        road(0, 0.3, 0.9, 50, -90, -100)
        road(0, 0.3, 0.9, 50, -100, -110)
        road(0, 0.3, 0.9, 50, -110, -120)
        road(0, 0.3, 0.9, 50, -120, -130)
        road(0, 0.3, 0.9, 50, -130, -140)
        road(0, 0.3, 0.9, 50, -140, -150)
        road(0, 0.5, 0, 50, -150, -160)
        # end of the road

        # Road Lines
        Line(-20, 123, -20,  120, -40, 120, -40,  123)
        Line( 10, 123, 10, 120, -10, 120, -10, 123)
        Line( 40, 123, 40, 120, 20, 120, 20, 123)
        Line(-20, 113, -20, 110, -40, 110, -40, 113)
        Line( 10, 113, 10, 110, -10, 110, -10, 113)
        Line(40, 113, 40, 110, 20, 110, 20, 113)
        Line( -20, 103, -20, 100, -40, 100, -40, 103)
        Line(10, 103, 10, 100, -10, 100, -10, 103)
        Line( 40, 103, 40, 100, 20, 100, 20, 103)
        Line( -20, 62, -20, 59, -40, 59, -40, 62)
        Line(10, 62, 10, 59, -10, 59, -10, 62)
        Line(40, 62, 40, 59, 20, 59, 20, 62)
        Line(-20, 72, -20, 69, -40, 69, -40, 72)
        Line(10, 72, 10, 69, -10, 69, -10, 72)
        Line(40, 72, 40, 69, 20, 69, 20, 72)
        Line( -20, 52, -20, 49, -40, 49, -40, 52)
        Line(10, 52, 10, 49, -10, 49, -10, 52)
        Line( 40, 52, 40, 49, 20, 49, 20, 52)
        Line( 40, 72, 40, 69, 20, 69, 20, 72)
        Line(-20, -17, -20, -20, -40, -20, -40, -17)
        Line(10, -17, 10, -20, -10, -20, -10, -17)
        Line(40, -17, 40, -20, 20, -20, 20, -17)
        Line( -20, -27, -20, -30, -40, -30, -40, -27)
        Line(10, -27, 10, -30, -10, -30, -10, -27)
        Line( 40, -27, 40, -30, 20, -30, 20, -27)
        Line( -20, -37, -20, -40, -40, -40, -40, -37)
        Line(10, -37, 10, -40, -10, -40, -10, -37)
        Line( 40, -37, 40, -40, 20, -40, 20, -37)
        Line( -20, -47, -20, -50, -40, -50, -40, -47)
        Line( 10, -47, 10, -50, -10, -50, -10, -47)
        Line( 40, -47, 40, -50, 20, -50, 20, -47)
        Line( -20, -57, -20, -60, -40, -60, -40, -57)
        Line( 10, -57, 10, -60, -10, -60, -10, -57)
        Line( 40, -57, 40, -60, 20, -60, 20, -57)
        Line( -20, -67, -20, -70, -40, -70, -40, -67)
        Line( 10, -67, 10, -70, -10, -70, -10, -67)
        Line( 40, -67, 40, -70, 20, -70, 20, -67)

        # End of Road Lines

# wood
        #wood( t, xb, xe, zb, ze)

        wood( 2 * w5, 10, 50, -140, -150)
        seaCollusion(c, 2 * w5 + 10, 2 * w5 + 50, -140, -150, 1)

        wood( -2 * w4, 10, 50, -130, -140)
        seaCollusion(c, - 2 * w4 + 10, -2 * w4 + 50, -130, -140, 0)

        wood( +2 * w3, 10, 50, -120, -130)
        seaCollusion(c, 10 + 2 * w3, 50 + 2 * w3, -120, -130, 1)

        wood( -2 * w2, 10, 50, -110, -120)
        seaCollusion(c, -2 * w2 + 10, - 2 * w2 + 50, -110, -120, 0)

        wood( 2 * w1, 10, 50, -100, -110)
        seaCollusion(c, 2 * w1 + 10, 2 * w1 + 50, -100, -110, 1)

        wood( -2 * w0, 10, 50, -90, -100)
        seaCollusion(c, 10 - 2 * w0, 50 - 2 * w0, -90, -100, 0)

        # model
        model(a, c)
        if forward:
            x += 0.07
            y -= .09
            e += .11
            w0 -= 0.07
            w1 -= .08
            w2 -= .09
            w3 -= .1
            w4 -= .11
            w5 -= .12
            angle -= 0.1
            if w0 < -20:
                w0 = 50
            if w1 < -50:
                w1 = 40
            if w2 < -20:
                w2 = 50
            if w3 < -50:
                w3 = 40
            if w4 < -20:
                w4 = 50
            if w5 < -50:
                w5 = 50

        # cars
        # last Cars
        j = -600
        while j < 50:
            car(e + j, -75, 1, 0, 0, 0, 0, 0)
            carCollusion(e + j, -70, -80)
            j += 50
        i = 600
        while i > -50:
            car(y + i, -65, 1, 1, 1, 1, 0, 0)
            carCollusion(y + i, -60, -70)
            i -= 60

        j = -600
        while j < 50:
            car(e + j + 20, -55, 1, 0.9, 0.2,  0, 0, 0.7)
            carCollusion(e + j + 20, -50, -60)
            j += 50
        i = 600
        while i > -50:
            car(y + i + 10, -45, 1, 0.1, 0.7, 0.1, 0.8, 0.1)
            carCollusion(y + i + 10, -40, -50)
            i -= 60
        j = -600
        while j < 50:
            car(e + j, -35, 0.9, 0.7, 0, 0.4, 0, 0.8)
            carCollusion(e + j, -30, -40)
            j += 50
        i = 600

        j = -600
        while j < 50:
            car(e + j + 20, -25, 1, 0, 0, 0, 0, 0)
            carCollusion(e + j + 20, -20, -30)
            j += 50
        i = 600
        while i > -50:
            car(y + i + 50, -15, 1, 1, 1, 1, 0, 0)
            carCollusion(y + i + 50, -10, -20)
            i -= 60
        j = -600

        # second 4 cars
        while j < 50:
            car(e + j + 20, 45, 0, 0.1, 0.7, 0, 0.9, 0.9)
            carCollusion(e + j + 20, 50, 40)
            j += 50
        i = 600
        while i > -50:
            car(y + i + 10, 55, 1, 0.9, 0.2, 0, 0, 0.7)
            carCollusion(y + i + 10, 60, 50)
            i -= 60
        j = -600
        while j < 50:
            car(e + j, 65, 1, 0.1, 0.7, 0.1, 0.8, 0.1)
            carCollusion(e + j, 70, 60)
            j += 50
        i = 600
        while i > -50:
            car(y + i, 75, 0.9, 0.7, 0, 0.4, 0, 0.8)
            carCollusion(y + i, 80, 70)
            i -= 60

        # first 4 Cars
        j = -600
        while j < 50:
            car(e + j + 20, 95, 1, 0, 0, 0, 0, 0)
            carCollusion(e + j + 20, 100, 90)
            j += 50
        i = 600
        while i > -50:
            car(y + i + 10, 105, 1, 1, 1, 1, 0, 0)
            carCollusion(y + i + 10, 110, 100)
            i -= 60
        j = -600
        while j < 50:
            car(e + j, 115, 0, 0.1, 0.7, 0, 0.9, 0.9)
            carCollusion(e + j, 120, 110)
            j += 50
        i = 600
        while i > -50:
            car(y + i, 125, 1, 0.9, 0.2, 0, 0, 0.7)
            carCollusion(y + i, 130, 120)
            i -= 60

# wall
        Wall(0.5, 0.5, 0.5, -87, 0, 0)
        Wall(0.5, 0.5, 0.5, 87, 0, 0)

        goOrtho()
        drawText("lives" + " [" + str(4 - v) + "]", - 0.75, .6, 0.0005, 2, 1, 0, 0)
        backPrespective()

        if t == 0:
            test()

        goOrtho()
        drawText(str(t), - 0.75, 0.7, 0.0005, 2, 1, 0, 0)
        backPrespective()

        glutSwapBuffers()
    if level==3:
        lay.play()
        m1 = time()
        if m1 > m0 + 10:
            sys.exit(0)
        init()
        c=0
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glClear(GL_COLOR_BUFFER_BIT)
        goOrtho()
        drawText("GAME OVER.", -.2, 0, 0.001, 6, 1, 0, 0)
        backPrespective()
        glutSwapBuffers()
    if level==4:
        rgala.play()
        m1 = time()
        if m1 > m0 + 6:
            level=lastlevel+1
        init()
        c=0
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glClear(GL_COLOR_BUFFER_BIT)
        goOrtho()
        drawText("LEVEL COMPLETED.", -.2, 0, 0.001, 6, 1, 0, 0)
        backPrespective()
        glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE)
glutInitWindowPosition(10, 10)
glutInitWindowSize(1000, 1000)
glutCreateWindow(b"practice for frog")
glutDisplayFunc(draw)
glutIdleFunc(draw)
glutSpecialFunc(ARROW_KEYS)
init()
glutMainLoop()
