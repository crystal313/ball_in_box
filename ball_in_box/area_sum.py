import math
import ballinbox as bb
import validate as val
from tkinter import * 

def area_sum(circles):
    area = 0.0
    for circle in circles:
        area += circle[2]**2 * math.pi

    return area

if __name__ == '__main__':
    num_of_circle = 5
    blockers = [(0.5, 0.5)
               ,(0.5, -0.3)]
    
    circles = bb.ball_in_box(num_of_circle, blockers)
    
    if num_of_circle == len(circles) and val.validate(circles, blockers):
        area = area_sum(circles)
        print("Total area: {}".format(area))
    else:
        print("Error: no good circles.")
    
    #画图
    canvas_width = 500
    canvas_height =500
    master = Tk()
    master.title("ball in box")
    w = Canvas(master, width=canvas_width, height=canvas_height)
   
    w.pack()
    w.create_rectangle(50, 50, 450, 450, outline = "black")
    for block in blockers:
        w.create_oval(250+block[0]*200-2,250-block[1]*200-2,250+block[0]*200+2,250-block[1]*200+2,fill='red')
    for circle in circles:
        w.create_oval(250+(circle[0]-circle[2])*200,250-(circle[1]+circle[2])*200,250+(circle[0]+circle[2])*200,250-(circle[1]-circle[2])*200)

    mainloop()




