import numpy as np
import matplotlib.pyplot as plt

N = 3000
count = 0

for i in range(N):
    x = np.random.rand(i)
    y = np.random.rand(i)
    if x**2 + y**2 < 1:
        count += 1

print(4*count/N)

# -------------------------
# Figure 1
# -------------------------
plt.figure(figsize=(6, 6))

plt.scatter(x[inside], y[inside], s=5, c='red')
plt.scatter(x[~inside], y[~inside], s=5, c='blue')

theta = np.linspace(0, np.pi/2, 200)
plt.plot(np.cos(theta), np.sin(theta), c='green')

plt.xlabel('X')
plt.ylabel('Y')
plt.title(f'n={N}, $\\pi \\approx$ {pi_est:.3f}')
plt.xlim(0, 1)
plt.ylim(0, 1)

plt.savefig('monte_carlo_points.png')
plt.close()


# -------------------------
# Figure 2
# -------------------------
inside_count = np.cumsum(inside)
n_values = np.arange(1, N + 1)
pi_values = 4 * inside_count / n_values

plt.figure()

plt.plot(n_values, pi_values)

plt.xlabel('N')
plt.ylabel('estimated pi')

plt.savefig('estimated_pi.png')
plt.close()
