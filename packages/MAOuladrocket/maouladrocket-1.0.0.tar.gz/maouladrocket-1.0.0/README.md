# Rocket

`Rocket` est une bibliothèque Python pour simuler des fusées et des navettes dans un jeu ou une simulation physique. Elle fournit des fonctionnalités pour déplacer les fusées, calculer des distances et modéliser des fusées sous différentes formes, y compris des fusées circulaires.

## Installation

Utilisez le gestionnaire de paquets [pip](https://pip.pypa.io/en/stable/) pour installer `rocket`.

```bash
pip install rocket

## Usage

```python
import rocket

# Create a new rocket at position (0,0)
rocket1 = rocket.Rocket()

# Move the rocket by 5 units along the x-axis and 3 units along the y-axis
rocket1.move_rocket(5, 3)

# Create another rocket and calculate the distance to rocket1
rocket2 = rocket.Rocket(10, 10)
distance = rocket1.get_distance(rocket2)
print(f"Distance between rocket1 and rocket2: {distance}")

# Create a circular rocket with radius 5
circle_rocket = rocket.CircleRocket(0, 0, 5)

# Get the area of the circular rocket
area = circle_rocket.get_area()
print(f"Area of the circular rocket: {area}")

# Get the circumference of the circular rocket
circumference = circle_rocket.get_circumference()
print(f"Circumference of the circular rocket: {circumference}")
```

## License
[MIT](https://choosealicense.com/licenses/mit/)