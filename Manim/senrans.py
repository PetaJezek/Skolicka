from manim import *
import numpy as np
import random

class ChaoticLSDLikeEffect(Scene):
    def construct(self):
        # Main text $ENRAN$ changing colors
        text = Text("$ENRAN$", font_size=120, weight=BOLD)
        text.scale(1.5)

        # Function to update text color
        def animate_text_colors(mobject, dt):
            colors = [RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE, PINK, TEAL]
            mobject.set_color(random.choice(colors))

        text.add_updater(animate_text_colors)

        # Chaotic shapes randomly appearing and moving
        def random_shape():
            shape_type = random.choice([Circle, Square, Triangle])
            shape = shape_type()
            shape.set_color(random.choice([RED, GREEN, BLUE, YELLOW, PURPLE, PINK, TEAL, ORANGE]))
            shape.set_opacity(random.uniform(0.3, 1.0))
            shape.scale(random.uniform(0.5, 2.0))
            shape.move_to([random.uniform(-7, 7), random.uniform(-4, 4), 0])
            return shape

        def chaotic_shapes(scene):
            for _ in range(random.randint(5, 15)):
                shape = random_shape()
                scene.add(shape)
                shape.animate.shift(
                    [random.uniform(-2, 2), random.uniform(-2, 2), 0]
                ).rotate(random.uniform(0, TAU))
                scene.remove(shape)

        # Background flashing colors
        def background_flash(mobject, dt):
            mobject.set_color(random.choice([RED, BLUE, GREEN, YELLOW, PURPLE, ORANGE, PINK, TEAL]))

        background = FullScreenRectangle()
        background.set_opacity(0.1)
        background.add_updater(background_flash)

        # Add elements to the scene
        self.add(background, text)
        self.play(FadeIn(text, scale=1.2), run_time=2)

        # Continuous chaos for 2 minutes
        for _ in range(240):
            chaotic_shapes(self)
            self.wait(0.1)

        # Clean up
        self.play(FadeOut(text, background))
