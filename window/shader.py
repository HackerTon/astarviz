import pyglet
from pyshader import mat4, python2shader, vec3, vec4

# @python2shader
# def vertex_shader(
#     vertex_pos=("input", 0, vec3),
#     transform=("uniform", (0, 0), mat4),
#     out_pos=("output", "Position", vec4),
# ):
#     out_pos = transform * vec4(vertex_pos, 1.0)


# @python2shader
# def fragment_shader_flat(
#     color=("uniform", (0, 1), vec3),
#     out_color=("output", 0, vec4),
# ):
#     out_color = vec4(color, 1.0)  # noqa


window = pyglet.window.Window()

label = pyglet.text.Label(
    "Hello world",
    font_name="Times New Roman",
    font_size=36,
    x=window.width // 2,
    y=window.height // 2,
    anchor_x="center",
    anchor_y="center",
)

pyglet.graphics.draw(
    2, pyglet.gl.GL_POINTS, ("v3f", (10.0, 15.0, 0.0, 30.0, 35.0, 0.0))
)


@window.event
def on_draw():
    window.clear()

    pyglet.graphics.draw_indexed(
        4,
        pyglet.gl.GL_TRIANGLES,
        [0, 1, 2, 0, 2, 3],
        ("v2i", (100, 100, 150, 100, 150, 150, 100, 150)),
    )


pyglet.app.run()
