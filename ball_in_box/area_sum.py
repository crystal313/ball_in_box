import math
import ballinbox as bb
import validate as val
# import matplotlib.pyplot as plt
# from matplotlib.patches import Ellipse,Circle

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
	# x1 = [-1,1]
	# x2 = [-1,-1]
	# x3 = [1,1]
	# y1 = [-1,1]
	# y2 = [-1,-1]
	# y3 = [1,1]
	# fig = plt.figure()
	# ax = fig.add_subplot(111)
	# for blocker in blockers:
	# 	plt.scatter(blocker[0],blocker[1],c = 36,marker = '*')
	# for circle in circles:
	# 	cir = Circle(xy = (circle[0],circle[1]),radius = circle[2],alpha = 0.8)
	# 	ax.add_patch(cir)
	# plt.plot(x1,y2)
	# plt.plot(x1,y3)
	# plt.plot(x2,y1)
	# plt.plot(x3,y1)
	# plt.show()