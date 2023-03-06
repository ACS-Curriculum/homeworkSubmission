f = []
s = []
gr = None


def setup():
    global gr, f, s
    size(800, 600)
    background("#00004f")
    no_stroke()

    gr = Ground()
    fl = Flake(random(800), random(600), random(1, 4), random(0.5, 2))
    sm = Smoke(205, 470, 10)

    for i in range(0, 200):
        f.append(Flake(random(800), random(600), random(1, 4), random(0.5, 2)))

    for i in range(0, 50):
        s.append(Smoke(random(205, 270), random(330, 470), random(10, 15)))


def draw():
    global gr, f, s
    background("#00004f")
    gr.display2()
    gr.window()
    gr.moon()
    for flak in f:
        flak.display()

    for smok in s:
        smok.display()


class Ground(object):
    def __init__(self):
        pass

    def display2(self):
        pass
        stroke(1)
        fill("#ffffff")
        rect(0, 550, 800, 50)
        fill("#4d2600")
        rect(130, 500, 90, 50)
        fill(0)
        triangle(120, 500, 175, 475, 230, 500)
        rect(200, 470, 10, 25)
        rect(185, 515, 20, 20)
        fill("#800000")
        rect(150, 518, 18, 32)
        fill(0)
        ellipse(153, 538, 2, 2)
        fill("#4d2600")
        rect(300, 535, 10, 15)
        rect(380, 535, 10, 15)
        rect(420, 520, 10, 30)
        rect(455, 535, 10, 15)
        rect(550, 535, 10, 15)
        rect(650, 535, 10, 15)
        rect(670, 520, 10, 30)
        rect(605, 535, 10, 15)
        fill("#336600")
        triangle(305, 470, 280, 535, 330, 535)
        triangle(385, 485, 370, 535, 400, 535)
        triangle(425, 435, 395, 520, 455, 520)
        triangle(460, 470, 440, 535, 485, 535)
        triangle(555, 470, 530, 535, 580, 535)
        triangle(385, 485, 370, 535, 400, 535)
        triangle(675, 435, 645, 520, 705, 520)
        triangle(610, 470, 590, 535, 635, 535)
        triangle(655, 470, 630, 535, 680, 535)
        fill("#ff3300")
        ellipse(300, 500, 3, 3)
        ellipse(315, 515, 3, 3)
        ellipse(290, 530, 3, 3)
        ellipse(310, 525, 3, 3)
        fill("#3399ff")
        ellipse(310, 495, 3, 3)
        ellipse(305, 510, 3, 3)
        ellipse(320, 530, 3, 3)
        ellipse(295, 520, 3, 3)
        fill("#ffff00")
        ellipse(307, 485, 3, 3)
        ellipse(313, 508, 3, 3)
        ellipse(301, 530, 3, 3)
        ellipse(297, 513, 3, 3)
        no_stroke()
        fill("#ff0000")
        text_align(CENTER)
        text_size(40)
        text("Happy Holidays!", 400, 590)

    def window(self):
        pass
        stroke(1)
        fill(255, 170, 0, random(100, 200))
        rect(185, 515, 20, 20)
        fill("#4d2600")
        rect(194, 515, 2, 20)
        rect(185, 524, 20, 2)
        no_stroke()

    def moon(self):
        pass
        t = (frame_count / 5000.0) % 1
        x = bezier_point(-50, 200, 600, 850, t)
        y = bezier_point(80, 40, 40, 80, t)
        fill("#fff8e7")
        ellipse_mode(CENTER)
        ellipse(x, y, 80, 80)
        fill("#00004f")
        ellipse(x + 23, y - 18, 80, 80)


class Smoke(object):
    def __init__(self, _x, _y, _siz):
        self.x = _x
        self.y = _y
        self.siz = _siz
        self.increment = 0

    def display(self):
        fill(135, 135, 135, self.increment)
        ellipse(self.x, self.y, self.siz, self.siz)

        if self.y > 340 or self.x < 370:
            self.y -= random(0, 0.3)
            self.x += random(0, 0.3)
            self.siz += random(0, 0.08)
            self.increment -= random(0, 1)

        if self.y < 340 or self.x > 370:
            self.x = 205
            self.y = 470
            self.siz = 10
            self.increment = 255


class Flake(object):
    def __init__(self, _x, _y, _siz, _increment):
        self.x = _x
        self.y = _y
        self.siz = _siz
        self.increment = _increment

    def display(self):
        fill("#ffffff")
        ellipse(self.x, self.y, self.siz, self.siz)
        if self.y < 600:
            self.y = self.y + self.increment
            self.x = self.x + random(0.5, 1.5)
            if self.y >= 600:
                self.y = 0

            if self.x > 800:
                self.x = 0
