# MineFake

Simple Minecraft-inspired demo written in Python and Ursina Engine

https://ursinaengine.org/

**What's this project ?**

MineFake is a 3D Game make with Ursina Engine and Python, this is a game of MonKey Indestries

https://monkeyindestries.000webhostapp.com/

## All Python Modules ?

For This Project i have use : 

1. Ursina
2. Perlin Noise
3. Numpy
4. Random

```shell
pip3 install ursina
pip3 install perlin_noise
```

## Map Generating With Perlin Noise : 

For The Map Generating, you do use : 
1. Perlin Noise
2. Numpy (floor)

```python
from numpy import floor
from perlin_noise import PerlinNoise

noise = PerlinNoise(octaves=1, seed=2021)
amp = 10
freq = 12

terrainWidth = 32
for i in range(terrainWidth*terrainWidth):
    budx = floor(i/terrainWidth)
    budz = floor(i%terrainWidth)
    voxel = Voxel(position=(floor(i/terrainWidth),floor((noise([budx/freq,budz/freq]))*amp),floor(i%terrainWidth)))
```

**Hey, What Is Voxel ?**

## How to Run

```shell
git clone https://github.com/Seewers/minefake
python game.py
```

## Voxel Class

```python
class Voxel(Button):
    def __init__(self, position=(0, 0, 0), texture='assets/img/grass_block.png'):
        super().__init__(
            parent=scene,
            position=position,
            model='assets/obj/block',
            origin_y=0.5,
            texture=texture,
            color=color.color(0, 0, random.uniform(0.9, 1.0)),
            scale=0.5
        )

    def input(self, key):
        if self.hovered:
            if key == 'right mouse down':
                if block_id == 0 or block_id == 7 or block_id == 5:
                    print("no")
                else:
                    Voxel(position=self.position + mouse.normal, texture=blocks[block_id])

                if block_id == 5:
                    print("lava")
            elif key == 'left mouse down':
                destroy(self)
```
## Sky Class

```python
class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent = scene,
            model = "sphere",
            texture = sky_skybox_texture,
            scale = 150,
            double_sided = True
        )
```

## Hand Class

```python
class Hand(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            model = "assets/obj/arm",
            texture = blocks[0],
            scale = 0.2,
            rotation = Vec3(150,-10,0),
            position = Vec2(0.4,-0.6)
        )

    def active(self):
        self.position = Vec2(0.3,-0.5)

    def passive(self):
        self.position = Vec2(0.4,-0.6)
```
## Commands

z : Moving Forward
q : Go Left
s : Move Back
d : Go Right
SPACE : Jump
n : Print In The Console The Position Of The Player
