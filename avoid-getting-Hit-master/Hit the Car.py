from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*


def MyInit():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60 , 1 , 1 , 30)
    gluLookAt(7,9,10,
              0,0,0,
    0,1,0)

    glClearColor(1,1,1,1)
    glClear(GL_COLOR_BUFFER_BIT)

def rectangle(x0, y0, z0, x1, y1, z1, x2, y2, z2, x3, y3, z3):
    global k

    glVertex(x0, y0, z0)
    glVertex(x1, y1, z1)
    glVertex(x2, y2, z2)
    glVertex(x3, y3, z3)
    glEnd()



x=0
angle=0
forward=0
K=0
F=90
Y=0

def ARROW_KEYS(key,x,y):
    global K

    if key== GLUT_KEY_LEFT:
       K-=0.75


    elif key == GLUT_KEY_RIGHT:
       K+=0.75


    draw()

def draw():
    global angle
    global x
    global forward
    global F
    global Y


    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glRotate(F,0,1,0)
    glClear(GL_COLOR_BUFFER_BIT)


    # Rood Sides
    glClearColor(0.9, 0.7, 0.3,0)

# **********************************************************************

    # Road
    glBegin(GL_POLYGON)
    glColor3f(0.45, 0.45, 0.45)
    glVertex(50, 9, -2)
    glVertex(70, 9, 5)
    glVertex(-100, -1, 5)
    glVertex(50, -1, -2)
    glEnd()

# **********************************************************************

    #Road Signs
    glBegin(GL_POLYGON)
    glColor3f(1, 1, 1)
    glVertex(2.5, 2, -0.3)
    glVertex(2.5, 2, 0.3)
    glVertex(-2.5, 1.9, 0.3)
    glVertex(-2.5,1.9, -0.3)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(1, 1, 1)
    glVertex(5, 1.9, -0.3)
    glVertex(5, 1.9, 0.3)
    glVertex(10,2, 0.3)
    glVertex(10,2, -0.3)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(1, 1, 1)
    glVertex(-5,2, -0.3)
    glVertex(-5,2, 0.3)
    glVertex(-10,1.9, 0.3)
    glVertex(-10,1.9, -0.3)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(1, 1, 1)
    glVertex(12.5 , 1.9 , -0.3)
    glVertex(12.5 , 1.9 , 0.3)
    glVertex(19 , 2 , 0.3)
    glVertex(19 , 2 , -0.3)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(1, 1, 1)
    glVertex(21.5 , 1.9 , -0.3)
    glVertex(21.5 , 1.9 , 0.3)
    glVertex(1000 , 2.9 , 0.3)
    glVertex(1000, 2.9 , -0.3)
    glEnd()

# **********************************************************************

    # Left Trees
    glLoadIdentity()
    glColor3f(0.7, 0.3, 0)
    glRotate(F,0,1,0)
    glTranslate(4.25, 2, -10)
    glScale(0.08, 0.7, 0.08)
    glutSolidCube(5)

    glLoadIdentity()
    glColor3f(0.2, 0.6, 0)
    glRotate(F,0,1,0)
    glTranslate(4.25, 4.8, -10)
    glutSolidSphere(1.5, 100, 100)

    glLoadIdentity()
    glColor3f(0.7, 0.3, 0)
    glRotate(F,0,1,0)
    glTranslate(-1.25, 2, -10)
    glScale(0.08, 0.7, 0.08)
    glutSolidCube(5)

    glLoadIdentity()
    glColor3f(0.2, 0.6, 0)
    glRotate(F,0,1,0)
    glTranslate(-1.25, 4.8, -10)
    glutSolidSphere(1.5, 100, 100)

# **********************************************************************

    #Car
    glLoadIdentity()
    glColor3f(1, 1, 1)
    glRotate(F,0,1,0)
    glTranslate(x,0,0+K)
    glScale(1, 0.25, 0.5)
    glutSolidCube(5)

    glLoadIdentity()
    glColor3f(0,0,0)
    glRotate(F,0,1,0)
    glTranslate(x,5*0.25,0+K)
    glScale(0.5, 0.25, 0.5)
    glutSolidCube(5)

    glColor3f(0,0,0)
    glLoadIdentity()
    glRotate(F,0,1,0)
    glTranslate(x+1.25,-5*0.25*.5,5*0.5*0.5+K)
    glRotate(angle,0,0,1)
    glutSolidTorus(0.15,0.5,12,10)

    glColor3f(0, 0, 0)
    glLoadIdentity()
    glRotate(F,0,1,0)
    glTranslate(x+-1.25, -5 * 0.25 * .5, 5 * 0.5 * 0.5+K)
    glRotate(angle, 0, 0, 1)
    glutSolidTorus(0.15, 0.5, 12, 10)

# **********************************************************************
    #flash Lights
    glLoadIdentity()
    glColor3f(0,0,0)
    glRotate(F, 0, 1, 0)
    glTranslate(-2.5+x,0.15,0.6+K)
    glutSolidSphere(0.3,100,100)


    glLoadIdentity()
    glColor3f(0,0,0)
    glRotate(F, 0, 1, 0)
    glTranslate(-2.5 + x, 0.15,- 0.6+K)
    glutSolidSphere(0.3, 100, 100)

# **********************************************************************

    #Moving Sphere
    glColor3f(0.8, 0, 0.1)
    glRotate(0, -0.2, 1, -0.1)
    glTranslate(Y+2,3,0-K)
    glutSolidSphere(0.5,100,100)

# **********************************************************************

    #Right Trees
    glLoadIdentity()
    glColor3f(0.7, 0.3, 0)
    glRotate(F, 0, 1, 0)
    glTranslate(-1.25,0, 6)
    glScale(0.08, 0.7, 0.08)
    glutSolidCube(5)

    glLoadIdentity()
    glColor3f(0.2, 0.6, 0)
    glRotate(F, 0, 1, 0)
    glTranslate(-1.25, 2.8, 6)
    glutSolidSphere(1.5, 100, 100)

    glLoadIdentity()
    glColor3f(0.7, 0.3, 0)
    glRotate(F, 0, 1, 0)
    glTranslate(5.25, 2.8,6)
    glScale(0.08, 0.7, 0.08)
    glutSolidCube(5)

    glLoadIdentity()
    glColor3f(0.2, 0.6, 0)
    glRotate(F, 0, 1, 0)
    glTranslate(5.25, 2.8,6)
    glutSolidSphere(1.5, 100, 100)




    glutSwapBuffers()
    glBegin(GL_LINES)




    if forward:
        angle-=0.1
        x+=0.009
        Y+=0.025

        if x>12 :
            forward=False
    else:
        angle+=0.1
        x-=0.009
        Y -= 0.025

        if x<-3 :
            forward=True







    glEnd()

glutInit()

glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(700, 700)
glutCreateWindow(b"Moving Car program")
glutDisplayFunc(draw)
glutIdleFunc(draw)
glutSpecialFunc(ARROW_KEYS)
MyInit()
glutMainLoop()