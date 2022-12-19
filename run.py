from ursina import *
from ursina import camera, mouse
from ursina.prefabs.first_person_controller import FirstPersonController
from perlin import *

app = Ursina()

sky_texture = load_texture('assets/skybox.png')
arm_texture = load_texture('assets/arm_texture.png')

window.fps_counter.enabled = True
window.exit_button.visible = True


def update():
    if held_keys['left mouse'] or held_keys['right mouse']:
        hand.active()
    else:
        hand.passive()


class Voxel(Button):
    def __init__(self, position=(1, 0, 1)):
        super().__init__(
            parent=scene,
            position=position,
            model='assets/block',
            origin_y=0.5,
            texture='white_cube',
            color=color.color(random.uniform(1, 1), 1, random.uniform(0.9, 1)),
            scale=0.5)


    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                voxel = Voxel(position=self.position + mouse.normal)

            if key == 'right mouse down':
                destroy(self)


class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent=scene,
            model='sphere',
            texture=sky_texture,
            scale=150,
            double_sided=True)


class Hand(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui,
            model='assets/arm',
            texture=arm_texture,
            scale=0.2,
            rotation=Vec3(150, -10, 0),
            position=Vec2(0.4, -0.6))

    def active(self):
        self.position = Vec2(0.3, -0.5)

    def passive(self):
        self.position = Vec2(0.4, -0.6)


for z in range(width):
    for x in range(length):
        voxel = Voxel(position=(x, 0, z))
        height = int(elevation[x][z] // .3)
        for i in range(height):
            voxel = Voxel(position=(x, i, z))

player = FirstPersonController()
sky = Sky()
hand = Hand()

app.run()
