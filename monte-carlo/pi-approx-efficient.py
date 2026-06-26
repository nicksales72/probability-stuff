import torch, time

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

start_time = time.perf_counter()
time.sleep(1)

# ------------------------------------------------------
num_points = 10_000_000
points_in_square = torch.empty(num_points, 2, device=device).uniform_(0,1) # (num_points, 2)

# skip sqrt in l2_distance, compare to (0.5)^2 = 0.25 instead
sq_dist = ((points_in_square - 0.5) ** 2).sum(dim=1) # d((x,y), (0.5, 0.5))^2
num_points_circle = (sq_dist <= 0.25).sum().item()

# (num_points_circle) / (num_points) roughly pi / 4
pi_approx = 4 * (num_points_circle / num_points)
print(pi_approx)
# ------------------------------------------------------

end_time = time.perf_counter()
execution_time = end_time - start_time
print(f"total time: {execution_time:.6f}s")
