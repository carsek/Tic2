'''DIBUIXANT ELEMENTS
La llibreria arcade disposa d'unes primitives (funcions de dibuix) que ens permeten dibuixar:'''
import arcade

def arbre (px,py):
    arcade.draw_lrtb_rectangle_filled(px, 40+px, 120+py, py, arcade.csscolor.SIENNA)
    arcade.draw_circle_filled(20+px, 140+py, 60, arcade.csscolor.DARK_GREEN)

def arbre2 (px,py):
    arcade.draw_lrtb_rectangle_filled(px, 40+px, 120+py, py, arcade.csscolor.SIENNA)
    arcade.draw_circle_filled(20+px, 140+py, 60, arcade.csscolor.DARK_GREEN)

def sol (px,py):
    arcade.draw_circle_filled(20+px, 10+py, 40, arcade.csscolor.YELLOW)

def nuvol (px,py):
    arcade.draw_circle_filled(220, 480, 30, arcade.csscolor.ALICE_BLUE)

arcade.open_window(600, 600, "Drawing Example")

# Set the background color
arcade.set_background_color(arcade.csscolor.SKY_BLUE)

# Get ready to draw
arcade.start_render()

#Rectangles:
arcade.draw_lrtb_rectangle_filled(0, 599, 300, 0, arcade.csscolor.OLIVE_DRAB)


arbre(100,200)
arbre2(300,250)
sol(500, 510)

# Finish drawing
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()