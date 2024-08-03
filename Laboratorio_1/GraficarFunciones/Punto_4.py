import matplotlib.pyplot as plt

x = float(input("Ingrese la coordenada X del vector: "))
y = float(input("Ingrese la coordenada Y del vector: "))
z = float(input("Ingrese la coordenada Z del vector: "))

min_coord = min(0, x, y, z)
max_coord = max(x, y, z)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.quiver(0, 0, 0, 1, 0, 0, color='r', label='X')
ax.quiver(0, 0, 0, 0, 1, 0, color='g', label='Y')
ax.quiver(0, 0, 0, 0, 0, 1, color='b', label='Z')
ax.quiver(0, 0, 0, x, y, z, color='k', label='Vector')

ax.set_xlim([min_coord, max_coord])
ax.set_ylim([min_coord, max_coord])
ax.set_zlim([min_coord, max_coord])

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.legend()
plt.show()