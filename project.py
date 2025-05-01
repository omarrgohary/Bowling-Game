import pygame as pg
import numpy as np
import time
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from OpenGL.GLUT import GLUT_BITMAP_HELVETICA_18
import math as mm
from pygame import freetype
from PIL import Image
import pygame.mixer
pygame.mixer.init()
freetype.init()
font = freetype.SysFont("Arial", 24)

glutInit()
pg.init()
pg.font.init() 

frame_count = [0, 0]  
player_turn = 1
score_turn1 = 0
score_turn2 = 0
total_pins = 10
show_spare = False
show_score = False
show_strike = False
show_welcome = True
show_message = False
player_1 = False
player_2 = False
game_over = False
total_score_p1 = 0
total_score_p2 = 0
game_start_sound = pygame.mixer.Sound(r"C:\Users\omarr\Downloads\semester 8\graphics\start.mp3")
strike = pygame.mixer.Sound(r"C:\Users\omarr\Downloads\semester 8\graphics\strike.mp3")
ball_radius = 0.25
pin_radius = 0.1

pin_positions1 = [
    (0, 0, -14), 
    (-0.2, 0, -14.3), (0.2, 0, -14.3),  
    (-0.4, 0, -14.6), (0, 0, -14.6), (0.4, 0, -14.6),  
    (-0.6, 0, -14.9), (-0.2, 0, -14.9), (0.2, 0, -14.9), (0.6, 0, -14.9) 
]
pin_positions2 = [                                                                                              
    (-2.4, 0, -14),  
    (-2.2, 0, -14.3), (-2.6, 0, -14.3),  
    (-2.1, 0, -14.6), (-2.4, 0, -14.6), (-2.8, 0, -14.6),  
    (-2.4, 0, -14.9), (-2.1, 0, -14.9), (-2.5, 0, -14.9), (-2.8, 0, -14.9) 
]
pin_positions3 = [
    (2.4, 0, -14),  
    (2.2, 0, -14.3), (2.6, 0, -14.3),  
    (2.1, 0, -14.6), (2.4, 0, -14.6), (2.8, 0, -14.6),  
    (2.4, 0, -14.9), (2.1, 0, -14.9), (2.5, 0, -14.9), (2.8, 0, -14.9)  
]
pin_positions4 = [                                                                                              
    (-6.4, 0, -14),  
    (-6.2, 0, -14.3), (-6.6, 0, -14.3),  
    (-6.1, 0, -14.6), (-6.4, 0, -14.6), (-6.8, 0, -14.6),  
    (-6.4, 0, -14.9), (-6.1, 0, -14.9), (-6.5, 0, -14.9), (-6.8, 0, -14.9)  
]
pin_positions5 = [
    (7.0, 0, -14),  
    (6.8, 0, -14.3), (7.2, 0, -14.3),  
    (6.7, 0, -14.6), (6.9, 0, -14.6), (7.4, 0, -14.6),  
    (6.9, 0, -14.9), (6.7, 0, -14.9), (7.1, 0, -14.9), (7.4, 0, -14.9) 
]


pin_state1 = [True] * len(pin_positions1)
pin_state2 = [True] * len(pin_positions2)
pin_state3 = [True] * len(pin_positions3)
pin_state4 = [True] * len(pin_positions4)
pin_state5 = [True] * len(pin_positions5)

def draw_lane1():
    glEnable(GL_DEPTH_TEST)

    lane_length = 17  
    z_start = -15
    z_end = 2
    num_z_steps = 50
    step = (z_end - z_start) / num_z_steps

   
    stripe_count = 12
    lane_width = 1.6
    stripe_width = lane_width / stripe_count
    x_start = -0.8

    tone1 = (0.82, 0.62, 0.42)
    tone2 = (0.92, 0.78, 0.55)

    for i in range(stripe_count):
        color = tone1 if i % 2 == 0 else tone2
        glColor3f(*color)
        x1 = x_start + i * stripe_width
        x2 = x_start + (i + 1) * stripe_width

        glBegin(GL_QUADS)
        glVertex3f(x1, 0, z_start)
        glVertex3f(x2, 0, z_start)
        glVertex3f(x2, 0, z_end)
        glVertex3f(x1, 0, z_end)
        glEnd()

   
    glColor3f(0.3, 0.3, 0.3)  
    for i in range(num_z_steps):
        z1 = z_start + i * step
        z2 = z_start + (i + 1) * step

        glBegin(GL_QUAD_STRIP)
        for j in range(5):
            x = -1.2 - 0.1 * j
            y = -0.01 * (j ** 2)  
            glVertex3f(x, y, z1)
            glVertex3f(x, y, z2)
        glEnd()

   
    for i in range(num_z_steps):
        z1 = z_start + i * step
        z2 = z_start + (i + 1) * step

        glBegin(GL_QUAD_STRIP)
        for j in range(5):
            x = 1.2 + 0.1 * j
            y = -0.01 * (j ** 2)
            glVertex3f(x, y, z1)
            glVertex3f(x, y, z2)
        glEnd()

def draw_lane2():
    glEnable(GL_DEPTH_TEST)

    lane_length = 17 
    z_start = -15
    z_end = 2
    num_z_steps = 50
    step = (z_end - z_start) / num_z_steps

   
    stripe_count = 12
    lane_width = 1.6
    stripe_width = lane_width / stripe_count
    x_start = -3.2

    tone1 = (0.82, 0.62, 0.42)
    tone2 = (0.92, 0.78, 0.55)

    for i in range(stripe_count):
        color = tone1 if i % 2 == 0 else tone2
        glColor3f(*color)
        x1 = x_start + i * stripe_width
        x2 = x_start + (i + 1) * stripe_width

        glBegin(GL_QUADS)
        glVertex3f(x1, 0, z_start)
        glVertex3f(x2, 0, z_start)
        glVertex3f(x2, 0, z_end)
        glVertex3f(x1, 0, z_end)
        glEnd()


    glColor3f(0.3, 0.3, 0.3)  
    for i in range(num_z_steps):
        z1 = z_start + i * step
        z2 = z_start + (i + 1) * step

        glBegin(GL_QUAD_STRIP)
        for j in range(5):
            x = -4.5 + 0.1 * j
            y = -0.01 * (j ** 2)
            glVertex3f(x, y, z1)
            glVertex3f(x, y, z2)
        glEnd()

def draw_lane3():
    glEnable(GL_DEPTH_TEST)

    lane_length = 17  
    z_start = -15
    z_end = 2
    num_z_steps = 50
    step = (z_end - z_start) / num_z_steps

   
    stripe_count = 12
    lane_width = 1.6
    stripe_width = lane_width / stripe_count
    x_start = 1.7

    tone1 = (0.82, 0.62, 0.42)
    tone2 = (0.92, 0.78, 0.55)

    for i in range(stripe_count):
        color = tone1 if i % 2 == 0 else tone2
        glColor3f(*color)
        x1 = x_start + i * stripe_width
        x2 = x_start + (i + 1) * stripe_width

        glBegin(GL_QUADS)
        glVertex3f(x1, 0, z_start)
        glVertex3f(x2, 0, z_start)
        glVertex3f(x2, 0, z_end)
        glVertex3f(x1, 0, z_end)
        glEnd()

  
    glColor3f(0.3, 0.3, 0.3)  
    for i in range(num_z_steps):
        z1 = z_start + i * step
        z2 = z_start + (i + 1) * step

        glBegin(GL_QUAD_STRIP)
        for j in range(5):
            x = 9.0 - 0.1 * j
            y = -0.01 * (j ** 2)  
            glVertex3f(x, y, z1)
            glVertex3f(x, y, z2)
        glEnd()

    
    for i in range(num_z_steps):
        z1 = z_start + i * step
        z2 = z_start + (i + 1) * step

        glBegin(GL_QUAD_STRIP)
        for j in range(5):
            x = 5.0 - 0.1 * j
            y = -0.01 * (j ** 2)
            glVertex3f(x, y, z1)
            glVertex3f(x, y, z2)
        glEnd()
        
def draw_lane4():
    glEnable(GL_DEPTH_TEST)

    lane_length = 17  
    z_start = -15
    z_end = 2
    num_z_steps = 50
    step = (z_end - z_start) / num_z_steps

  
    stripe_count = 12
    lane_width = 1.6
    stripe_width = lane_width / stripe_count
    x_start = -7

    tone1 = (0.82, 0.62, 0.42)
    tone2 = (0.92, 0.78, 0.55)

    for i in range(stripe_count):
        color = tone1 if i % 2 == 0 else tone2
        glColor3f(*color)
        x1 = x_start + i * stripe_width
        x2 = x_start + (i + 1) * stripe_width

        glBegin(GL_QUADS)
        glVertex3f(x1, 0, z_start)
        glVertex3f(x2, 0, z_start)
        glVertex3f(x2, 0, z_end)
        glVertex3f(x1, 0, z_end)
        glEnd()

    
    glColor3f(0.3, 0.3, 0.3)  
    for i in range(num_z_steps):
        z1 = z_start + i * step
        z2 = z_start + (i + 1) * step

        glBegin(GL_QUAD_STRIP)
        for j in range(5):
            x = -1.2 - 0.1 * j
            y = -0.01 * (j ** 2)  
            glVertex3f(x, y, z1)
            glVertex3f(x, y, z2)
        glEnd()

    for i in range(num_z_steps):
        z1 = z_start + i * step
        z2 = z_start + (i + 1) * step

        glBegin(GL_QUAD_STRIP)
        for j in range(5):
            x = -9 + 0.1 * j
            y = -0.01 * (j ** 2)
            glVertex3f(x, y, z1)
            glVertex3f(x, y, z2)
        glEnd()
 
def draw_lane5():
    glEnable(GL_DEPTH_TEST)

    lane_length = 17  
    z_start = -15
    z_end = 2
    num_z_steps = 50
    step = (z_end - z_start) / num_z_steps

    stripe_count = 12
    lane_width = 1.6
    stripe_width = lane_width / stripe_count
    x_start = 6

    tone1 = (0.82, 0.62, 0.42)
    tone2 = (0.92, 0.78, 0.55)

    for i in range(stripe_count):
        color = tone1 if i % 2 == 0 else tone2
        glColor3f(*color)
        x1 = x_start + i * stripe_width
        x2 = x_start + (i + 1) * stripe_width

        glBegin(GL_QUADS)
        glVertex3f(x1, 0, z_start)
        glVertex3f(x2, 0, z_start)
        glVertex3f(x2, 0, z_end)
        glVertex3f(x1, 0, z_end)
        glEnd()

def draw_lane6():
    glEnable(GL_DEPTH_TEST)

    lane_length = 17  
    z_start = -15
    z_end = 2
    num_z_steps = 50
    step = (z_end - z_start) / num_z_steps

   
    stripe_count = 12
    lane_width = 1.6
    stripe_width = lane_width / stripe_count
    x_start = -11.5

    tone1 = (0.82, 0.62, 0.42)
    tone2 = (0.92, 0.78, 0.55)

    for i in range(stripe_count):
        color = tone1 if i % 2 == 0 else tone2
        glColor3f(*color)
        x1 = x_start + i * stripe_width
        x2 = x_start + (i + 1) * stripe_width

        glBegin(GL_QUADS)
        glVertex3f(x1, 0, z_start)
        glVertex3f(x2, 0, z_start)
        glVertex3f(x2, 0, z_end)
        glVertex3f(x1, 0, z_end)
        glEnd()  
        
    for i in range(num_z_steps):
        z1 = z_start + i * step
        z2 = z_start + (i + 1) * step

        glBegin(GL_QUAD_STRIP)
        for j in range(5):
            x = 9.0 + 0.1 * j
            y = -0.01 * (j ** 2)
            glVertex3f(x, y, z1)
            glVertex3f(x, y, z2)
        glEnd()

def draw_lane7():
    glEnable(GL_DEPTH_TEST)

    lane_length = 17  
    z_start = -15
    z_end = 2
    num_z_steps = 50
    step = (z_end - z_start) / num_z_steps

   
    stripe_count = 12
    lane_width = 1.6
    stripe_width = lane_width / stripe_count
    x_start = 10.0

    tone1 = (0.82, 0.62, 0.42)
    tone2 = (0.92, 0.78, 0.55)

    for i in range(stripe_count):
        color = tone1 if i % 2 == 0 else tone2
        glColor3f(*color)
        x1 = x_start + i * stripe_width
        x2 = x_start + (i + 1) * stripe_width

        glBegin(GL_QUADS)
        glVertex3f(x1, 0, z_start)
        glVertex3f(x2, 0, z_start)
        glVertex3f(x2, 0, z_end)
        glVertex3f(x1, 0, z_end)
        glEnd()  
        

    for i in range(num_z_steps):
        z1 = z_start + i * step
        z2 = z_start + (i + 1) * step

        glBegin(GL_QUAD_STRIP)
        for j in range(5):
            x = 9.0 + 0.1 * j
            y = -0.01 * (j ** 2)
            glVertex3f(x, y, z1)
            glVertex3f(x, y, z2)
        glEnd()
   
def Triangle(x1, y1, z1, x2, y2, z2, x3, y3, z3):
    glColor3f(0,0,0) 
    glBegin(GL_TRIANGLES)
    glVertex3f(x1, y1, z1)  
    glVertex3f(x2, y2, z2)  
    glVertex3f(x3, y3, z3)  
    glEnd()

def draw_line(x1, y1, z1, x2, y2, z2):
    glLineWidth(4.0)
    glColor3f(0.65, 0.37, 0.17)  
    glBegin(GL_LINES)
    glVertex3f(x1, y1, z1)
    glVertex3f(x2, y2, z2)
    glEnd()

def draw_sphere(current , radius=0.15, slices=32, stacks=16):
    if current == 0:
        glColor3f(0, 0, 1)  
    else :
        glColor3f(0, 1, 0)  
    
    for i in range(stacks):
        lat0 = mm.pi * (-0.5 + float(i) / stacks)
        z0 = radius * mm.sin(lat0)
        zr0 = radius * mm.cos(lat0)

        lat1 = mm.pi * (-0.5 + float(i + 1) / stacks)
        z1 = radius * mm.sin(lat1)
        zr1 = radius * mm.cos(lat1)

        glBegin(GL_QUAD_STRIP)
        for j in range(slices + 1):
            lng = 2 * mm.pi * float(j) / slices
            x = mm.cos(lng)
            y = mm.sin(lng)

            glVertex3f(x * zr0, y * zr0, z0)
            glVertex3f(x * zr1, y * zr1, z1)
        glEnd()

def draw_ball(ball_x, ball_z, current_player):
    glPushMatrix()
    if ball_x < -0.9 or ball_x > 0.9:
        y_pos = 0.05
    else:
        y_pos = 0.15
    glTranslatef(ball_x, y_pos, ball_z)

    draw_sphere(current_player)  
    glPopMatrix()

def check_collision(ball_pos, pin_pos):
    distance = mm.sqrt((ball_pos[0] - pin_pos[0]) ** 2 +
                       (ball_pos[1] - pin_pos[1]) ** 2 +
                       (ball_pos[2] - pin_pos[2]) ** 2)
    return distance < (ball_radius + pin_radius)

def draw_pins_lane1():
    global pin_state1
    for i, (x, y, z) in enumerate(pin_positions1):
        if pin_state1[i]:  
            draw_pin(x, y, z)
                       
def draw_pins_lane2():
    global pin_state2
    for i, (x, y, z) in enumerate(pin_positions2):
        if pin_state2[i]:  
            draw_pin(x, y, z)
                     
def draw_pins_lane3():
    global pin_state3
    for i, (x, y, z) in enumerate(pin_positions3):
        if pin_state3[i]:  
            draw_pin(x, y, z)

def draw_pins_lane4():
    global pin_state4
    for i, (x, y, z) in enumerate(pin_positions4):
        if pin_state4[i]:  
            draw_pin(x, y, z)

def draw_pins_lane5():
    global pin_state5
    for i, (x, y, z) in enumerate(pin_positions5):
        if pin_state5[i]:  
            draw_pin(x, y, z)

def draw_pin(x, y, z):
    slices     = 32      
    stacks     = 40      
    base_r     = 0.07   
    top_r      = 0.05   
    h          = 0.35   
    band_h     = h * 0.7 
    band_half  = 0.01    

    glPushMatrix()
    glTranslatef(x, y, z)
    glEnable(GL_DEPTH_TEST)

    glColor3f(1, 1, 1)
    glBegin(GL_QUAD_STRIP)
    for i in range(slices + 1):
        theta = 2 * mm.pi * i / slices
        cx, cz = mm.cos(theta), mm.sin(theta)
        glVertex3f(cx * base_r,    0.0,    cz * base_r)
        glVertex3f(cx * top_r,     h,      cz * top_r)
    glEnd()

   
    for stack in range(stacks):
        phi0 = (stack    / stacks) * (mm.pi / 2)
        phi1 = ((stack+1)/ stacks) * (mm.pi / 2)
        r0   = top_r * mm.sin(phi0)
        y0   = h     + top_r * mm.cos(phi0)
        r1   = top_r * mm.sin(phi1)
        y1   = h     + top_r * mm.cos(phi1)

        glBegin(GL_QUAD_STRIP)
        for i in range(slices + 1):
            theta = 2 * mm.pi * i / slices
            cx0, cz0 = r0 * mm.cos(theta), r0 * mm.sin(theta)
            cx1, cz1 = r1 * mm.cos(theta), r1 * mm.sin(theta)
            glVertex3f(cx0, y0, cz0)
            glVertex3f(cx1, y1, cz1)
        glEnd()

    band_r = base_r + (top_r - base_r) * (band_h / h)
    glColor3f(1, 0, 0)
    glBegin(GL_QUAD_STRIP)
    for i in range(slices + 1):
        theta = 2 * mm.pi * i / slices
        cx, cz = mm.cos(theta) * (band_r + 0.001), mm.sin(theta) * (band_r + 0.001)
        glVertex3f(cx, band_h - band_half, cz)
        glVertex3f(cx, band_h + band_half, cz)
    glEnd()

    glColor3f(1, 1, 1)
    glBegin(GL_POLYGON)
    for i in range(slices):
        theta = 2 * mm.pi * i / slices
        glVertex3f(mm.cos(theta) * base_r,
                   0.0,
                   mm.sin(theta) * base_r)
    glEnd()
    glPopMatrix()

def cascade_knockdown(pin_index, pin_positions, pin_states):
    knocked_pos = pin_positions[pin_index]
    for i, pos in enumerate(pin_positions):
        if pin_states[i] and i != pin_index:
            dx = pos[0] - knocked_pos[0]
            dz = pos[2] - knocked_pos[2]
            dist = mm.sqrt(dx**2 + dz**2)
            
          
            in_front = dz < 0  
            close_enough = dist < 0.37
            aligned = abs(dx) < 0.35  
            
            if in_front and close_enough and aligned:
                pin_states[i] = False
                cascade_knockdown(i, pin_positions, pin_states)

def load_texture(image_path):
    img = Image.open(image_path)  
    img = img.convert('RGBA')  
    img_data = np.array(img, dtype=np.uint8)
    img_data = np.flipud(img_data)

    width, height = img.size  
    texture = glGenTextures(1) 
    glBindTexture(GL_TEXTURE_2D, texture)  
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, img_data)
    glGenerateMipmap(GL_TEXTURE_2D) 
    return texture

def draw_pin_overlay(x, z,texture):
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texture)

    glPushMatrix()
    glTranslatef(x,5.0, z) 
    glScalef(25.0, 7.0, 1)    

    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex3f(-0.5, -0.5, 0)
    glTexCoord2f(1, 0); glVertex3f(0.5, -0.5, 0)
    glTexCoord2f(1, 1); glVertex3f(0.5, 0.5, 0)
    glTexCoord2f(0, 1); glVertex3f(-0.5, 0.5, 0)
    glEnd()

    glPopMatrix()
    glDisable(GL_TEXTURE_2D)

def draw_pin_overlay1(x, z,texture):
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texture)

    glPushMatrix()
    glTranslatef(x, 1.0, z)  # Increase Y to move the image higher
    glScalef(2.5, 1.0, 1)    # Scale image size

    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex3f(-0.5, -0.5, 0)
    glTexCoord2f(1, 0); glVertex3f(0.5, -0.5, 0)
    glTexCoord2f(1, 1); glVertex3f(0.5, 0.5, 0)
    glTexCoord2f(0, 1); glVertex3f(-0.5, 0.5, 0)
    glEnd()

    glPopMatrix()
    glDisable(GL_TEXTURE_2D)
    
def hit_ball():
    strike.play()
    
def start_game():
    game_start_sound.play()  
        
def count_knocked_pins():
   
    knocked_pins = sum(1 for state in pin_state1 if not state)
    return knocked_pins

def update_score(pins_hit):
    global player_turn, score_turn1, score_turn2, show_spare, show_score, show_strike, reset_scheduled, reset_time, game_over, player_1, player_2

    if player_turn == 1:
        score_turn1 = pins_hit
        player_turn += 1  
        
        
    elif player_turn == 2:
        score_turn2 = pins_hit - score_turn1
        show_score = True
        reset_scheduled = True
        reset_time = time.time() + 2  
        
    if score_turn1 == total_pins :
        show_strike = True
        show_score = True
        reset_scheduled = True
        reset_time = time.time() + 2  

    elif score_turn1 + score_turn2 == total_pins:
        show_spare = True
        show_score = True
        reset_scheduled = True
        reset_time = time.time() + 2  
        
def draw_text(x, y, text):
    glColor3f(1, 1, 1)
    glRasterPos2f(x, y)
    for ch in text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(ch))

def reset_game():
    global player_turn, score_turn1, score_turn2, show_spare, show_score, show_strike
    player_turn = 1
    score_turn1 = 0
    score_turn2 = 0
    show_spare = False
    show_score = False
    show_strike = False
    
def dis(w) :
    global final_score, total_score_p2, total_score_p1, reset_time, show_welcome, total_score_p1, total_score_p2
    
    current_time = pg.time.get_ticks()
    if show_welcome and current_time - w < 2000:
        draw_text(-0.2, 1.0, "Welcome!")
    else:
        show_welcome = False
    
    if show_message :
        draw_text(-0.5, 1.2, "Do you want to play again? Y/n")
    
    if show_spare:
        draw_text(-0.2, 1.0, "Spare!")

    if show_strike :
        draw_text(-0.2, 1.0, "Strike!")

    if show_score:
        final_score = score_turn1 + score_turn2
        draw_text(-0.2, 0.9, f"Score: {final_score}")
        
    if player_1 and player_2 and game_over:
        draw_text(-0.2, 1.1, "Game Over!")
        draw_text(-0.2, 1.0, f"P1 Score: {total_score_p1}")
        draw_text(-0.2, 0.9  , f"P2 Score: {total_score_p2}")

def main():
    global reset_scheduled, reset_time, frame_count, game_over, player_1, player_2, total_score_p2, total_score_p1, show_message
    display = (1000, 700)
    pg.display.set_mode(display, DOUBLEBUF | OPENGL)
    start_game() 
        
    pin_overlay_texture = load_texture(r"C:\Users\omarr\Downloads\semester 8\graphics\a1.jpg")
    pin_overlay_texture1 = load_texture(r"C:\Users\omarr\Downloads\semester 8\graphics\stop.jpg")

    # Set up 3D perspective
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)

    c=0
    ball_z = 1.2  
    ball_x = 0  
    ball_has_hit_pins = False
    ball_y=0.15
    ball_returned = False
    throw_count =0
    throw_counted = False
    reset_scheduled = False
    reset_time = 0  
    welcome_start_time = pg.time.get_ticks()
    show_game_over = False  
    game_over_time = 0  
    game_over_display_time = 3
    game_over_timer = 0
    play_again_prompt_time = 0
    timers_initialized = False
    restart_game = False
    
    clock = pg.time.Clock()
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        keys = pg.key.get_pressed()
       
       
        if not ball_has_hit_pins:
            if keys[pg.K_LEFT]:
                ball_x -= 0.05  
            elif keys[pg.K_RIGHT]:
                ball_x += 0.05 
            
            if ball_x < -1:
                ball_x = -1
            elif ball_x > 1:  
                ball_x = 1

            if keys[pg.K_SPACE] and not ball_has_hit_pins : 
                ball_z -= 0.7  
            if c == 0:
                if ball_z <= -15:  
                        pins_hit_count = count_knocked_pins()
                        update_score(pins_hit_count)
                        hit_ball()  # Play strike sound    
                        ball_y = 0.15
                        ball_z = 1.2
                        ball_x = 0
                        ball_has_hit_pins = False
                        if throw_count == 0 and pins_hit_count == total_pins:
                            pin_state1[:] = [True for _ in pin_state1] 
                            throw_count = 0  
                            throw_counted = True  
                            total_score_p1 += pins_hit_count
                            frame_count[0] += 1
                            c=1
                        else:
                            ball_returned = True
                            throw_counted = False  
                        
                if ball_returned and not throw_counted:
                    throw_count += 1
                    throw_counted = True  
                                                
                    if throw_count == 2:
                        pin_state1[:] = [True for _ in pin_state1]  
                        throw_count = 0
                        total_score_p1 += score_turn1 + score_turn2
                        frame_count[0] += 1
                        c=1 
                        
            elif c == 1:
                if ball_z <= -15:  
                        pins_hit_count = count_knocked_pins()
                        update_score(pins_hit_count)
                        hit_ball()     
                        ball_y = 0.15
                        ball_z = 1.2
                        ball_x = 0
                        ball_has_hit_pins = False
                        if throw_count == 0 and pins_hit_count == total_pins:
                            pin_state1[:] = [True for _ in pin_state1]  
                            throw_count = 0 
                            throw_counted = True 
                            total_score_p2 += pins_hit_count
                            frame_count[1] += 1
                            c=0
                            show_game_over = True  
                            game_over_time = time.time() + 2 
                        else:
                            ball_returned = True
                            throw_counted = False  
                        
                if ball_returned and not throw_counted:
                    throw_count += 1
                    throw_counted = True  
                                     
                    if throw_count == 2:
                        pin_state1[:] = [True for _ in pin_state1]  
                        throw_count = 0
                        total_score_p2 += score_turn1 + score_turn2
                        frame_count[1] += 1
                        c=0
                        
            if frame_count[0] == 2  and frame_count[1] == 2:
                if show_game_over and time.time() >= game_over_time:
                    if not timers_initialized:
                        game_over_timer = time.time() + game_over_display_time
                        play_again_prompt_time = game_over_timer + 1
                        timers_initialized = True

                    game_over = True
                    player_1 = True
                    player_2 = True

            if game_over_timer != 0 and time.time() >= game_over_timer:
                game_over = False
                player_1 = False
                player_2 = False
                show_message = True

            if play_again_prompt_time != 0 and time.time() >= play_again_prompt_time:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_y]:
                    restart_game = True
                    show_message = False
                elif keys[pygame.K_n]:
                    pygame.quit()
                    exit()

            if restart_game:
                frame_count = [0, 0]
                total_score_p1 = 0
                total_score_p2 = 0
                game_over = False
                player_1 = False
                player_2 = False
                game_over_timer = 0
                play_again_prompt_time = 0
                timers_initialized = False
                restart_game = False
            
            
        if -0.9 <= ball_x <= 0.9:
            ball_pos = (ball_x,ball_y , ball_z)
            for i, p in enumerate(pin_positions1):
                if pin_state1[i] and check_collision(ball_pos, p):
                    pin_state1[i] = False
                    x, _, z = p
                    cascade_knockdown(i, pin_positions1, pin_state1)  
    

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        gluLookAt(0, 1.0, 4.2,   
                  0.0, 0.8, ball_z, 
                  0, 1, 0)  
        
        glEnable(GL_DEPTH_TEST)

        # Drawing Lanes 
        draw_lane1()
        draw_lane2()
        draw_lane3()
        draw_lane4()
        draw_lane5()
        draw_lane6()
        draw_lane7()
        
        #Drawing Pins on each lane
        draw_pins_lane1()
        draw_pins_lane2()
        draw_pins_lane3()
        draw_pins_lane4()
        draw_pins_lane5()
        
        draw_ball(ball_x,ball_z,c)  
        
        # Triangular Pins for Center Lane1
        Triangle(0.0, 0.01, -3.0, 0.02, 0.0, -2.8, -0.02, 0.0, -2.8) 
        Triangle(0.09, 0.01, -2.8, 0.07, 0.0, -2.6, 0.11, 0.0, -2.6)  
        Triangle(-0.09, 0.01, -2.8, -0.07, 0.0, -2.6, -0.11, 0.0, -2.6)  
        Triangle(0.18, 0.01, -2.6, 0.2, 0.0, -2.4, 0.16, 0.0, -2.4)  
        Triangle(-0.18, 0.01, -2.6, -0.2, 0.0, -2.4, -0.16, 0.0, -2.4) 
        Triangle(0.27, 0.01, -2.4, 0.29, 0.0, -2.2, 0.25, 0.0, -2.2) 
        Triangle(-0.27, 0.01, -2.4, -0.29, 0.0, -2.2, -0.25, 0.0, -2.2) 
        # Triangular Pins for Center Lane2
        Triangle(-2.4, 0.01, -3.0, -2.38, 0.0, -2.8, -2.42, 0.0, -2.8) 
        Triangle(-2.31, 0.01, -2.8, -2.29, 0.0, -2.6, -2.33, 0.0, -2.6) 
        Triangle(-2.49, 0.01, -2.8, -2.47, 0.0, -2.6, -2.51, 0.0, -2.6) 
        Triangle(-2.22, 0.01, -2.6, -2.2, 0.0, -2.4, -2.24, 0.0, -2.4) 
        Triangle(-2.58, 0.01, -2.6, -2.56, 0.0, -2.4, -2.6, 0.0, -2.4)
        Triangle(-2.11, 0.01, -2.4, -2.09, 0.0, -2.2, -2.13, 0.0, -2.2) 
        Triangle(-2.67, 0.01, -2.4, -2.65, 0.0, -2.2, -2.69, 0.0, -2.2) 
        # Triangular Pins for Center Lane3
        Triangle(2.4, 0.01, -3.0, 2.38, 0.0, -2.8, 2.42, 0.0, -2.8) 
        Triangle(2.31, 0.01, -2.8, 2.29, 0.0, -2.6, 2.33, 0.0, -2.6) 
        Triangle(2.49, 0.01, -2.8, 2.47, 0.0, -2.6, 2.51, 0.0, -2.6) 
        Triangle(2.22, 0.01, -2.6, 2.2, 0.0, -2.4, 2.24, 0.0, -2.4) 
        Triangle(2.58, 0.01, -2.6, 2.56, 0.0, -2.4, 2.6, 0.0, -2.4)
        Triangle(2.11, 0.01, -2.4, 2.09, 0.0, -2.2, 2.13, 0.0, -2.2) 
        Triangle(2.67, 0.01, -2.4, 2.65, 0.0, -2.2, 2.69, 0.0, -2.2) 
        
        
        # Start Line for Lane 1
        draw_line(-0.8, 0.01, -0.12, 0.8, 0.01, -0.12)
        # Start Line for Lane 2
        draw_line(-3.2, 0.01, -0.12, -1.6, 0.01, -0.12)
        # Start Line for Lane 3
        draw_line(1.7, 0.01, -0.12, 3.3, 0.01, -0.12)
        
        
        #Draw Images
        draw_pin_overlay(0, -15, pin_overlay_texture)  
        draw_pin_overlay1(-2.25, -15, pin_overlay_texture1)        
        draw_pin_overlay1(2.5, -15, pin_overlay_texture1)
        draw_pin_overlay1(-6.0, -15, pin_overlay_texture1)
        draw_pin_overlay1(6.25, -15, pin_overlay_texture1)
        draw_pin_overlay1(-10, -15, pin_overlay_texture1)
        draw_pin_overlay1(10.0, -15, pin_overlay_texture1)

        dis(welcome_start_time)
        if reset_scheduled and time.time() >= reset_time:
            reset_game()
            reset_scheduled = False

        pg.display.flip()
        clock.tick(60)
    pg.quit()
if __name__ == "__main__":
    main()



