"""
PDG & Developers & Sound Disigner == Mazine Fertal

Co-PDG & Disigner & The Best Guys This Society == Antoine Donarelle-Pont
"""
from ursina import *
from numpy import floor
from perlin_noise import PerlinNoise
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import camera_grayscale_shader
camera.shader = camera_grayscale_shader

app = Ursina()

sky_skybox_texture = load_texture("assets/img/sky.jpg")
punch_sound = Audio("assets/sound/punch_sound.wav", autoplay=False, loop=False)

noise = PerlinNoise(octaves=1, seed=2021)
amp = 10
freq = 12

blocks = [
    load_texture("assets/img/arm_texture.png"),
    load_texture('assets/img/grass_block.png'),
    load_texture('assets/img/stone_block.png'),
    load_texture('assets/img/bug_block.png'),
    load_texture('assets/img/gold.png'),
    load_texture('assets/img/lava.png'),
    load_texture('assets/img/ametique_block.png'),
    load_texture('assets/img/water.png'),
]

block_id = 1

def input(key):
    global block_id, hand
    if key.isdigit():
        block_id = int(key)
        if block_id >= len(blocks):
            block_id = len(blocks) - 1
        hand.texture = blocks[block_id]
        hand.model = "assets/obj/block"
        if block_id == 0:
            hand.model = "assets/obj/arm"

    if key == "n":
        print(player.position)

class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent = scene,
            model = "sphere",
            texture = sky_skybox_texture,
            scale = 150,
            double_sided = True
        )

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

def update():
    if held_keys['left mouse'] or held_keys['right mouse']:
        punch_sound.play()
        hand.position = Vec2(0.4, -0.5)
    else:
        hand.position = Vec2(0.6, -0.6)

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

terrainWidth = 32
for i in range(terrainWidth*terrainWidth):
    budx = floor(i/terrainWidth)
    budz = floor(i%terrainWidth)
    voxel = Voxel(position=(floor(i/terrainWidth),floor((noise([budx/freq,budz/freq]))*amp),floor(i%terrainWidth)))

player = FirstPersonController()

sky = Sky()
hand = Hand()

app.run()