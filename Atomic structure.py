from vpython import*
from tkinter import*

root = Tk()
root. geometry("550x550")
root.title("Atomic Structure")
def Hydrogen():
    scene.autoscale = False

    nucleus = sphere(pos = vec(0,0,0), radius = 1.0, color = color.red )

    electron = sphere(pos = vec(10,0,0), radius = .7, color = color.blue)

    R = 10 #radius
    m = 1 #mass 
    omega = 100 # omega 2pi/T wala 
 
    axis = vec(0,1,0)
    dt = 0.01

    electron.pos = vector(R,0,0)

    trail = curve(color = color.green, radius = 0.05, interval=5, trail_type = "points")

    while True:

       force = m *  omega**2 * R
       force_vec = force * axis

       # electron_velocity = (force_vec / m)* dt
       electron_velocity = omega * cross(axis, electron.pos) * dt #cross product ker rhe hai 

       # by v = x/t == x = vt 
       electron.pos += electron_velocity * dt

       electron.rotate(angle=omega*dt, axis=axis) 
       trail.append(pos=electron.pos)

       rate(100)
       trail.retain = 630

intro = Label(
    root,
    text = "Hello!!!, In this program you can see the animation of structures of atom \n To see the animation type the atom name in caps",
    font = ("Helvetica", 16),
)
intro.place(x = 20 , y = 30)

#btn = Spinbox(
#    root,
#    text = "Start",
    
#)
#btn.place(x = 30 , y = 30)

e = Entry(root, width = 30)
e.place(x = 30 , y = 80)

def play():
  if e.get() == "HYDROGEN":
       Hydrogen()
  else:
       v = Label(
           root, 
           text = e.get() + " is under devlopment", 
        )
       v.place(x = 20 , y=110)     

btn1  = Button(
    root,
    text = "play ",
    font = ("Helvetica", 16),
    command = play 
)
btn1.place( x = 320 , y = 75)

def first():
    back.destroy()
    b.destroy()
    intro = Label(
    root,
    text = "Hello!!!, In this program you can see the animation of structures of atom \n To see the animation type the atom name in caps",
    font = ("Helvetica", 16),
    )
    intro.place(x = 20 , y = 30)

    e = Entry(root, width = 30)
    e.place(x = 30 , y = 80)

    def play():
      if e.get() == "HYDROGEN":
          Hydrogen()
      else:
          v = Label(
              root, 
              text = e.get() + " is under devlopment", 
            )
          v.place(x = 20 , y=110) 

    btn  = Button(
      root,
      text = "play ",
      font = ("Helvetica", 16),
      command = play 
    )
    btn.place( x = 320 , y = 75)

    see_other_animation = Button(
        root,
        text = "click here to see available animations",
        command = see
    )
    see_other_animation.place(x = 20 ,y = 150)
          


btn  = Button(
    root,
    text = "play ",
    font = ("Helvetica", 16),
    command = play 
)
btn.place( x = 320 , y = 75)



def see():
    btn.destroy()
    see_other_animation.destroy()
    e.destroy()
    intro.destroy()
    btn1.destroy()
    global back
    global b

    b = Label(
        root,
        text = "1) Hydrogen",
    )
    b.place(x = 100, y = 100)

    back = Button(
      root , 
      text = "Back",
      command = first
    )
    back.place(x = 2, y = 2)

see_other_animation = Button(
    root,
    text = "click here to see available animations",
    command = see
)
see_other_animation.place(x = 20 ,y = 150)

root.mainloop()
