from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*

def MyInit():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60 , 1 , 1 , 30)
    gluLookAt(8,9,10,
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



def draw():
    global angle
    global x
    global forward
    global y



    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glClear(GL_COLOR_BUFFER_BIT)

    # Rood Sides
    glColor3f(0.9, 0.7, 0.3)
    glBegin(GL_POLYGON)
    glVertex(0, 0, 0)
    glVertex(100, 100, 0)
    glVertex(100, -100, 0)
    glVertex(0, -100, 0)
    glEnd()

    glColor3f(0.9, 0.7, 0.3)
    glBegin(GL_POLYGON)
    glVertex(12, -5, 0)
    glVertex(0, -5, 11)
    glVertex(-50, -5, 0)
    glEnd()

    glColor3f(0.9, 0.7, 0.3)
    glBegin(GL_POLYGON)
    glVertex(13, 2, -50)
    glVertex(12, 50, 50)
    glVertex(-50, -50, 50)
    glVertex(-50, 2, -50)
    glEnd()

    # Road
    glBegin(GL_POLYGON)
    glColor3f(0.45, 0.45, 0.45)
    glVertex(15, -1, -3)
    glVertex(15, -1, 3)
    glVertex(-15, -1, 3)
    glVertex(-30, -1, -3)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(1, 1, 1)
    glVertex(2.5, -1, -0.3)
    glVertex(2.5, -1, 0.3)
    glVertex(-2.5, -1, 0.3)
    glVertex(-2.5, -1, -0.3)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(1, 1, 1)
    glVertex(5, -1, -0.3)
    glVertex(5, -1, 0.3)
    glVertex(10, -1, 0.3)
    glVertex(10, -1, -0.3)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(1, 1, 1)
    glVertex(-5, -1, -0.3)
    glVertex(-5, -1, 0.3)
    glVertex(-10, -1, 0.3)
    glVertex(-10, -1, -0.3)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(1, 1, 1)
    glVertex(-15, -1, -0.3)
    glVertex(-15, -1, 0.3)
    glVertex(-25, -1, 0.3)
    glVertex(-25, -1, -0.3)
    glEnd()




    #Car
    glColor3f(1, 1, 1)
    glTranslate(x,0,0)
    glScale(1, 0.25, 0.5)
    glutSolidCube(5)



    glLoadIdentity()
    glColor3f(0,0,0)
    glTranslate(x,5*0.25,0)
    glScale(0.5, 0.25, 0.5)
    glutSolidCube(5)




    glColor3f(0,0,0)
    glLoadIdentity()
    glTranslate(x+1.25,-5*0.25*.5,5*0.5*0.5)
    glRotate(angle,0,0,1)
    glutSolidTorus(0.15,0.5,12,10)

    glColor3f(0, 0, 0)
    glLoadIdentity()
    glTranslate(x+-1.25, -5 * 0.25 * .5, 5 * 0.5 * 0.5)
    glRotate(angle, 0, 0, 1)
    glutSolidTorus(0.15, 0.5, 12, 10)


    #Left Trees
    glLoadIdentity()
    glColor3f(0.7, 0.3, 0)
    glTranslate(4.25,0, -10)
    glScale(0.08, 0.7, 0.08)
    glutSolidCube(5)


    glLoadIdentity()
    glColor3f(0.2, 0.6, 0)
    glTranslate(4.25, 2.8, -10)
    glutSolidSphere(1.5, 10, 10)





    glLoadIdentity()
    glColor3f(0.7, 0.3, 0)
    glTranslate(-1.25,0, -10)
    glScale(0.08, 0.7, 0.08)
    glutSolidCube(5)

    glLoadIdentity()
    glColor3f(0.2, 0.6, 0)
    glTranslate(-1.25, 2.8, -10)
    glutSolidSphere(1.5, 10, 10)

    glLoadIdentity()
    glColor3f(0.7, 0.3, 0)
    glTranslate(-7.25,0, -10)
    glScale(0.08, 0.7, 0.08)
    glutSolidCube(5)

    glLoadIdentity()
    glColor3f(0.2, 0.6, 0)
    glTranslate(-7.25, 2.8, -10)
    glutSolidSphere(1.5, 10, 10)

    glLoadIdentity()
    glColor3f(0.7, 0.3, 0)
    glTranslate(-13.25, 0, -10)
    glScale(0.08, 0.7, 0.08)
    glutSolidCube(5)

    glLoadIdentity()
    glColor3f(0.2, 0.6, 0)
    glTranslate(-13.25, 2.8, -10)
    glutSolidSphere(1.5, 10, 10)



    #Right Trees
    glLoadIdentity()
    glColor3f(0.7, 0.3, 0)
    glTranslate(-1.25,0, 7)
    glScale(0.08, 0.7, 0.08)
    glutSolidCube(5)

    glLoadIdentity()
    glColor3f(0.2, 0.6, 0)
    glTranslate(-1.25, 2.8, 7)
    glutSolidSphere(1.5, 10, 10)

    glLoadIdentity()
    glColor3f(0.2, 0.6, 0)
    glTranslate(5.25, 2.8,7)
    glutSolidSphere(1.5, 10, 10)


    #flash Lights
    glLoadIdentity()
    glColor3f(0,0,0)
    glTranslate(2.5+x,0.25,0.6)
    glutSolidSphere(0.3,10,10)


    glLoadIdentity()
    glColor3f(0,0,0)
    glTranslate(2.5 + x, 0.25,- 0.6)
    glutSolidSphere(0.3, 10, 10)






    glutSwapBuffers()
    glBegin(GL_LINES)



    if forward:
        angle-=0.1
        x+=0.002
        if x>5:
            forward=False
    else:
        angle+=0.1
        x-=0.002
        if x<-5:
            forward=True







    glEnd()

glutInit()

glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(700, 700)
glutCreateWindow(b"Moving Car program")
glutDisplayFunc(draw)
glutIdleFunc(draw)
MyInit()
glutMainLoop()
