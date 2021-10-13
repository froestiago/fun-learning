import random	

def estimate_pi(n):
	points_in_the_circle = 0
	total_points = 0
	for i in range(n):
		x = random.uniform(0, 1)
		y = random.uniform(0, 1)
		# here I compute how far the point is from the origin
			# if the point is whithin the radius 1, the point
			# is inside the circle and we count it.
		b = (x**2)+(y**2) # to save computation I exluded the
			# sqrt(), this does not influence the result
		if b <= 1:
			points_in_the_circle += 1
		total_points += 1

	pi = 4*(points_in_the_circle/total_points)
	# since the "plot" is a quarter of a circle, multiplying
		# the result by 4 gives us the correct result

	return pi

x = int(input('Number of points: '))
print('Given', x, 'points, π = ', estimate_pi(x))
	