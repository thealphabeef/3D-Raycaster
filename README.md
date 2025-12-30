# 3D Raycasting Engine (Python)

A **from-scratch 3D raycasting engine** built in Python that renders a pseudo-3D environment from a 2D grid map, inspired by early FPS engines like *Wolfenstein 3D* or *DOOM*. This project focuses on **computer graphics fundamentals** and **linear algebra**.

![til](https://github.com/thealphabeef/3D-Raycaster/blob/main/3D.gif)

---

## 🚀 Features

- Real-time **pseudo-3D rendering** using raycasting
- Player movement
- Configurable 2D tile-based world map
- Adjustable **field of view (FOV)** and render distance
- Distance-based wall shading for depth perception
- Modular engine structure (rendering, input, math, map logic)

![til](https://github.com/thealphabeef/3D-Raycaster/blob/main/2D.gif)

---

## 🧠 How It Works

The engine casts a ray for each vertical slice of the screen:

1. Rays are projected from the player’s position across the FOV
2. Each ray steps through the grid
3. The distance to the first wall hit is calculated
4. Wall slice height is computed
5. Vertical slices are rendered to simulate 3D depth

This approach mimics how early 90s FPS engines achieved 3D visuals without modern GPUs.

---
