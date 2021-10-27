from OpenGL.GL import*
from OpenGL.GLUT import*
import numpy as np
from math import *

def Draw_circle(r=0.1,xc=0 ,yc=0):
    glBegin(GL_POLYGON)
    for theta in np.arange(0,2*pi,0.0001):
        x=r*cos(theta)
        y=+r*sin(theta)
        glVertex(x+xc,y+yc)
    glEnd()



def Draw():
    glClearColor(0.9, 1, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT)


    #wheel
    for k in (1, -1):
        glColor3f(0.5, 0.5, 0.5)
        glBegin(GL_QUADS)
        glVertex(k * 0.8, -0.8)
        glVertex(k * 0.5, -0.8)
        glVertex(k * 0.5, -0.3)
        glVertex(k * 0.8, -0.3)
        glEnd()

        glColor(0.1,0.2,0.6)
        glLineWidth(1.5)
        glBegin(GL_LINE_LOOP)
        glVertex(k * 0.8, -0.8)
        glVertex(k * 0.8, -0.3)
        glVertex(k * 0.5, -0.3)
        glVertex(k * 0.5, -0.8)
        glEnd()

        glLineWidth(1)
        glBegin(GL_LINES)
        for j in range(0,8):
            glVertex(k * 0.8, -0.8 + j * (0.8 - 0.3) / 8)
            glVertex(k * 0.5, -0.8 + j * (0.8 - 0.3) / 8)
        glEnd()

        #legs
        glLineWidth(1.58)
        for ((R, G, B), type) in ( ((0.6, 0.7 , 0.7), GL_POLYGON), ((0.1, 0.2, 0.9), GL_LINE_LOOP)):
            glColor3f(R, G, B)

            glBegin(type)
            glVertex(k * 0.5, -0.65)
            glVertex(k * 0.45, -0.65)
            glVertex(k * 0.45, -0.6)
            glVertex(k * 0.5, -0.6)
            glEnd()

            glBegin(type)
            glVertex( k * 0.45, -0.7)
            glVertex( k * 0.34, -0.7)
            glVertex( k * 0.30, -0.63)
            glVertex( k * 0.30, -0.55)
            glVertex( k * 0.45, -0.55)
            glEnd()


            glBegin(type)
            glVertex( k * 0.30, -0.55)
            glVertex( k * 0.45, -0.55)
            glVertex( k * 0.5, -0.5)
            glVertex( k * 0.5, -0.35)
            glVertex( k * 0.30, -0.35)
            glEnd()

            glColor3f(0, 0, 0.9)
            Draw_circle(0.08, k * 0.1, 0.55)
            glColor3f(0.9, 1, 1)
            Draw_circle(0.065, k * 0.1, 0.55)

    for (R, G, B, type) in ((0.5, 0.5, 0.5 , GL_POLYGON), (0.1, 0.2, 0.5, GL_LINE_LOOP)):  #upper
        glColor3f(R, G, B)
        glBegin(type)
        glVertex(-0.45, 0)
        glVertex(-0.45, 0.2)
        glVertex(0.45, 0.2)
        glVertex(0.45, 0)
        glEnd()

    for (R, G, B, type) in ((1, 0.8, 0, GL_POLYGON),(0.1, 0.2, 0.5, GL_LINE_LOOP)):       #lower
        glColor3f(R, G, B)
        glBegin(type)
        glVertex(0.45, -0.5)
        glVertex(-0.45, -0.5)
        glVertex(-0.45, 0)
        glVertex(0.45, 0)
        glEnd()


        #nick
        glBegin(type)
        glVertex(-0.1, 0.2)
        glVertex(0.1, 0.2)
        glVertex(0.1, 0.4)
        glVertex(-0.1, 0.4)
        glEnd()

        glBegin(type)
        glVertex(-0.05, 0.4)
        glVertex(0.05, 0.4)
        glVertex(0.05, 0.5)
        glVertex(-0.05, 0.5)
        glEnd()

        glBegin(type)
        glVertex(-0.05, 0.5)
        glVertex(-0.15, 0.6)
        glVertex(-0.15, 0.8)
        glVertex(0.15, 0.8)
        glVertex(0.15, 0.6)
        glVertex(0.05, 0.5)
        glEnd()

    #Head
    glColor3f(0.1, 0.2, 0.4)
    glLineWidth(1.5)
    glBegin(GL_LINES)
    glVertex(-0.1, 0.267)
    glVertex(0.1, 0.267)
    glVertex(-0.1, 0.33)
    glVertex(0.1, 0.33)
    glVertex(-0.15, 0.7)
    glVertex(0.15, 0.7)
    glVertex(-0.45, 0)
    glVertex(0.45, 0)
    glEnd()

    glLineWidth(1.5)
    glColor3f(0.1, 0.2, 0.4)

    for M in (1, -1):
        glBegin(GL_LINES)
        glVertex(M * 0.2, 0)
        glVertex(M * 0.2, 0.2)
        glVertex(M * 0.45, 0.1)
        glVertex(M * 0.2, 0.1)
        glVertex(M * 0.2, 0.2)
        glEnd()

    glLineWidth(1.5)
    for (R, G, B, type) in ((0.52, 0.8, 1, GL_POLYGON), (0.13, 0.27, 0.45, GL_LINE_LOOP)):
        glColor3f(R, G, B)
        glBegin(type)
        glVertex(-0.05, 0.18)
        glVertex(-0.18, 0.18)
        glVertex(-0.18, 0.1)
        glVertex(-0.05, 0.1)
        glEnd()

    #RED_DOT
    Draw_circle(0.025, -0.145, 0.038)
    glColor3f(0.7, 0.3, 0.2)
    Draw_circle(0.014, -0.143, 0.038)


    #Brown_triangle
    for (R, G, B, type) in ((0.3, 0.3, 0.25, GL_POLYGON), (0.13, 0.27, 0.45, GL_LINE_LOOP)):
        glColor3f(R, G, B)
        glBegin(type)
        glVertex(0.06, 0.12)
        glVertex(0.17, 0.12)
        glVertex(0.17, 0.025)
        glVertex(0.06, 0.025)
        glEnd()



    #left eye frame
    glColor3f(0, 0, 0)
    glLineWidth(2)
    glBegin(GL_LINE_LOOP)
    for theta in np.arange(0, 2 * pi, .0001):
        x = 0.1 * cos(theta)
        y = 0.1 * sin(theta)
        glVertex(x - 0.23, y + 0.75)
    glEnd()

    #left eye

    glColor3f(0.3, 0.4, 0.7)
    glBegin(GL_POLYGON)
    for theta in np.arange(0, 2 * pi, .0001):  # arange for step not integer
        x = 0.1 * cos(theta)
        y = 0.1 * sin(theta)
        glVertex(x - 0.23, y + 0.75)
    glEnd()

    glColor3f(0, 0.2, 0.6)
    glBegin(GL_POLYGON)
    for theta in np.arange(0, 2 * pi, .0001):  # arange for step not integer
        x = .05 * cos(theta)
        y = .05 * sin(theta)
        glVertex(x - 0.23, y + 0.75)
    glEnd()

    #left eye white dot

    glColor3f(0.76, 0.8, 0.84)
    glBegin(GL_POLYGON)
    for theta in np.arange(0, 2 * pi, .0001):  # arange for step not integer
        x = 0.032 * cos(theta)
        y = 0.032 * sin(theta)
        glVertex(x - 0.27, y + 0.79)
    glEnd()

    #small white dot
    glColor3f(0.76, 0.8, 0.84)
    glBegin(GL_POLYGON)
    for theta in np.arange(0, 2 * pi, .0001):  # arange for step not integer
        x = .0245 * cos(theta)
        y = .0245 * sin(theta)
        glVertex(x - 0.2, y + 0.71)
    glEnd()

    #right eye frame
    glColor3f(0, 0, 0)
    glLineWidth(2)
    glBegin(GL_LINE_LOOP)
    for theta in np.arange(0, 2 * pi, .0001):  # arange for step not integer
        x = 0.1 * cos(theta)
        y = 0.1 * sin(theta)
        glVertex(x + 0.23, y + 0.75)
    glEnd()

    #right eye
    glColor3f(0.3, 0.4, 0.7)
    glBegin(GL_POLYGON)
    for theta in np.arange(0, 2 * pi, .0001):  # arange for step not integer
        x = 0.1 * cos(theta)
        y = 0.1 * sin(theta)
        glVertex(x + 0.23, y + 0.75)
    glEnd()

    glColor3f(0, 0.2, 0.6)
    glBegin(GL_POLYGON)
    for theta in np.arange(0, 2 * pi, .0001):  # arange for step not integer
        x = .05 * cos(theta)
        y = .05 * sin(theta)
        glVertex(x + 0.23, y + 0.75)
    glEnd()

    #right eye white dot

    glColor3f(0.76, 0.8, 0.84)
    glBegin(GL_POLYGON)
    for theta in np.arange(0, 2 * pi, .0001):
        x = .032 * cos(theta)
        y = .032 * sin(theta)
        glVertex(x + 0.27, y + 0.79)
    glEnd()

    #small white dot
    glColor3f(0.76, 0.8, 0.84)
    glBegin(GL_POLYGON)
    for theta in np.arange(0, 2 * pi, .0001):
        x = 0.0245 * cos(theta)
        y = 0.0245 * sin(theta)
        glVertex(x + 0.2, y + 0.71)
    glEnd()

    #hand
    glColor3f(1, 1, 1)
    glBegin(GL_LINE_STRIP)
    glVertex(-0.15, 0.15)
    glVertex(-0.45, 0.15)
    glVertex(-0.45, -0.05)
    glVertex(-0.15, -0.05)
    glEnd()
    glBegin(GL_LINE_STRIP)
    glVertex(-0.15, -0.05)
    glVertex(-0.15, 0.02)
    glVertex(-0.2, 0.02)
    glVertex(-0.2, 0.07)
    glVertex(-0.15, 0.07)
    glVertex(-0.15, 0.15)
    glEnd()
    glBegin(GL_LINE_STRIP)
    glVertex(0.15, 0.15)
    glVertex(0.45, 0.15)
    glVertex(0.45, -0.05)
    glVertex(0.15, -0.05)
    glEnd()
    glBegin(GL_LINE_STRIP)
    glVertex(0.15, -0.05)
    glVertex(0.15, 0.02)
    glVertex(0.2, 0.02)
    glVertex(0.2, 0.07)
    glVertex(0.15, 0.07)
    glVertex(0.15, 0.15)
    glEnd()
    glBegin(GL_LINE_STRIP)
    glVertex(0.2, 0.07)
    glVertex(0.35, 0.07)
    glVertex(0.35, 0.02)
    glVertex(0.2, 0.02)
    glEnd()
    glBegin(GL_LINE_STRIP)
    glVertex(-0.2, 0.07)
    glVertex(-0.35, 0.07)
    glVertex(-0.35, 0.02)
    glVertex(-0.2, 0.02)
    glEnd()
    glBegin(GL_LINE_STRIP)
    glVertex(-0.35, 0.07)
    glVertex(-0.35, 0.1)
    glVertex(-0.45, 0.1)
    glVertex(-0.45, 0)
    glVertex(-0.35, 0)
    glVertex(-0.35, 0.07)
    glEnd()
    glBegin(GL_LINE_STRIP)
    glVertex(-0.25, 0.15)
    glVertex(-0.25, 0.07)
    glEnd()
    glBegin(GL_LINE_STRIP)
    glVertex(-0.25, 0.03)
    glVertex(-0.25, -0.05)
    glEnd()
    glBegin(GL_LINE_STRIP)
    glVertex(0.25, 0.15)
    glVertex(0.25, 0.07)
    glEnd()
    glBegin(GL_LINE_STRIP)
    glVertex(0.25, 0.03)
    glVertex(0.25, -0.05)
    glEnd()
    glBegin(GL_LINE_STRIP)
    glVertex(0.35, 0.07)
    glVertex(0.35, 0.1)
    glVertex(0.45, 0.1)
    glVertex(0.45, 0)
    glVertex(0.35, 0)
    glVertex(0.35, 0.07)
    glEnd()
    glColor3f(1, 1, 1)

    glFlush()


glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(800, 800)
glutCreateWindow(b"WALL-E program")
glutDisplayFunc(Draw)

glutMainLoop()