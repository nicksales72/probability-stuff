import torch 

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

num_points = 10_000_000
points_in_square = torch.empty(num_points, 2, device=device).uniform_(0,1) # (num_points, 2)

# skip sqrt in l2_distance, compare to (0.5)^2 = 0.25 instead
sq_dist = ((points_in_square - 0.5) ** 2).sum(dim=1) # d((x,y), (0.5, 0.5))^2
num_points_circle = (sq_dist <= 0.25).sum().item()

# (num_points_circle) / (num_points) roughly pi / 4
pi_approx = 4 * (num_points_circle / num_points)
print(pi_approx)
