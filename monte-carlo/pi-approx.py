import random, math

def sample_points_square(num_points):
    points = []
    for i in range(num_points):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        points.append((x,y))
    return points

def total_in_circle(points):
    total_in_circle = 0
    for (x,y) in points: 
        # d((x, y), (0.5, 0.5)) = sqrt{(x - 0.5)^2 + (y - 0.5)^2} <= 0.5
        l2_distance = math.sqrt((x - 0.5)**2 + (y - 0.5)**2)
        if l2_distance <= 0.5: total_in_circle += 1
    return total_in_circle

num_points = 10_000_000
points_in_square = sample_points_square(num_points)
num_points_circle = total_in_circle(points_in_square)

# (num_points_circle) / (num_points) roughly pi / 4
pi_approx = 4 * (num_points_circle / num_points)
print(pi_approx)

