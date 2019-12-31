import sdl2
import sdl2.ext
import numpy as np

from threading import Thread


class Window:
    def __init__(self, title='default', size=None, nbox=13):
        if size is None:
            # [width, height]
            size = [640, 640]

        sdl2.ext.init()
        self.window = sdl2.ext.Window(title, size)
        self.renderer = sdl2.ext.Renderer(self.window)
        self.size = size
        self.delay = 100
        self.running = True

        self.n = nbox
        self.boxes = np.zeros([nbox, nbox])

        self._show()

    def _show(self):
        self.window.show()

    def _hide(self):
        self.window.hide()

    def _updatedelay(self, value):
        if 0 < value < 100:
            self.delay = value

    def draw_grid(self):
        size = self.size
        divx = size[0] // self.n
        divy = size[1] // self.n

        for i in range(1, self.n):
            # [x1, y1, x2, y2]
            self.renderer.draw_line([i * divx, 0, i * divx, size[0]], sdl2.ext.Color())
            self.renderer.draw_line([0, i * divy, size[1], i * divy], sdl2.ext.Color())

    def draw_dot(self):
        size = self.size
        divxh = size[0] // self.n
        divyh = size[1] // self.n

        for i in range(self.n + 1):
            for j in range(self.n + 1):
                local = [(divxh // 2) + i * divxh, (divyh // 2) + j * divyh, 3, 3]

                # [x1, y2, w, h]
                self.renderer.fill([local], sdl2.ext.Color())

    def draw_edge(self):
        size = self.size
        divx = size[0] // self.n
        divy = size[1] // self.n

        # TOBE DONE

    def draw_box(self):
        size = self.size
        divx = size[0] // self.n
        divy = size[1] // self.n

        for i in range(self.n + 1):
            for j in range(self.n + 1):

                if i == self.n or j == self.n:
                    rand = self.boxes[i - 1][j - 1]
                else:
                    rand = self.boxes[i][j]

                if rand == 1:
                    # Red
                    color = sdl2.ext.Color(0, 0, 255)
                elif rand == 2:
                    # Blue
                    color = sdl2.ext.Color(255, 0, 0)
                elif rand == 3:
                    # Green
                    color = sdl2.ext.Color(0, 255, 0)
                else:
                    # Black
                    color = sdl2.ext.Color(0, 0, 0)

                self.renderer.fill([i * divx, j * divy, divx, divy], color)

    def _render(self):
        while self.running:
            self.renderer.present()
            self.draw_box()
            self.draw_grid()
            self.draw_dot()
            sdl2.SDL_Delay(self.delay)

    def events(self):
        key_state = sdl2.SDL_GetKeyboardState(None)

        events = sdl2.ext.get_events()
        for event in events:
            if event.type == sdl2.SDL_QUIT:
                self.running = False
                return False
            elif event.type == sdl2.SDL_KEYDOWN:
                if key_state[sdl2.SDL_SCANCODE_UP]:
                    self._updatedelay(self.delay + 10)
                elif key_state[sdl2.SDL_SCANCODE_DOWN]:
                    self._updatedelay(self.delay - 10)
        return True

    def start(self):
        rendert = Thread(target=self._render)
        rendert.start()
