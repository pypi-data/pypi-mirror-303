# Rocket Package

This package provides classes for simulating rockets, shuttles, and circular rockets. It can be used for games or physics simulations.

## Installation

You can install the package via pip:

```bash
pip install rocket
```
## Usage
from rocket import Rocket, Shuttle, CircleRocket

### Create a rocket instance
rocket = Rocket(0, 0)

### Move the rocket
rocket.move_rocket(3, 4)

### Create a circular rocket and calculate its area
circle_rocket = CircleRocket(0, 0, radius=5)
area = circle_rocket.get_area()

