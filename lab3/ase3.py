from matplotlib import pyplot as plt


def calculate_probability():

    chance_to_be_a = 0
    chance_to_be_b = 0
    radius = 0.1
    circle = None

    while chance_to_be_a == 0 and chance_to_be_b == 0:

        circle = plt.Circle(new_point, radius, color='r', fill=False)

        a_in_circle = []
        b_in_circle = []

        for i in range(0, size_a):
            if circle.contains_point((xA[i], yA[i]), 0.0):
                a_in_circle.append([xA[i], yA[i]])

        for i in range(0, size_b):
            if circle.contains_point((xB[i], yB[i]), 0.0):
                b_in_circle.append([xB[i], yB[i]])

        chance_to_be_a = len(a_in_circle) / size_a
        chance_to_be_b = len(b_in_circle) / size_b

        radius += 0.1

    return chance_to_be_a, chance_to_be_b, circle


xA = [0.5, 0.6, 0.45, 0.66, 0.54, 0.87, 0.99, 0.11]
yA = [2, 2.3, 2.5, 3.5, 3.4, 3.7, 3.6, 3.8]

xB = [1.25, 1.3, 1.45, 1.55, 1.45, 1.6, 1.8, 1.9, 2.1]
yB = [4, 3, 6, 4, 5, 3, 4, 3, 5]

size_a = len(xA)
size_b = len(xB)

new_point = [0, 5]

probability_a, probability_b, final_circle = calculate_probability()

if probability_a > probability_b:
    xA.append(new_point[0])
    yA.append(new_point[1])
else:
    xB.append(new_point[0])
    yB.append(new_point[1])

fig, ax = plt.subplots(1, 2, figsize=(12, 6))

ax[0].plot(xA, yA, '.')
ax[0].plot(xB, yB, '.')
ax[0].plot(new_point[0], new_point[1], 'o')
ax[0].add_artist(final_circle)
ax[0].axis([0, 4, 1.5, 5.5])
ax[0].axis("equal")

ax[1].plot(xA, yA, '.')
ax[1].plot(xB, yB, '.')
ax[1].axis([0, 4, 1.5, 5.5])
ax[1].axis("equal")

plt.show()
