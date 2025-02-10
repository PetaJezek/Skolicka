from manim import *

class SteinitzExchangeLemma(Scene):
    def construct(self):
        # Title
        title = Text("Steinitz Exchange Lemma").to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Introduction
        intro_text = Text(
            "The Steinitz Exchange Lemma states:\n"
            "If you have a spanning set and a linearly independent set,\n"
            "you can exchange vectors while keeping the properties intact.",
            font_size=24
        ).next_to(title, DOWN, buff=0.5)
        self.play(Write(intro_text))
        self.wait(3)
        self.play(FadeOut(intro_text))

        # Basis vectors
        v1 = Arrow(start=ORIGIN, end=2 * RIGHT, color=BLUE, buff=0).set_stroke(width=6)
        v2 = Arrow(start=ORIGIN, end=2 * UP, color=GREEN, buff=0).set_stroke(width=6)
        w = Arrow(start=ORIGIN, end=[1, 1, 0], color=RED, buff=0).set_stroke(width=6)

        # Labels
        v1_label = MathTex("\\vec{v}_1").next_to(v1, DOWN).set_color(BLUE)
        v2_label = MathTex("\\vec{v}_2").next_to(v2, LEFT).set_color(GREEN)
        w_label = MathTex("\\vec{w}").next_to(w, UP).set_color(RED)

        # Display basis and vector w
        self.play(GrowArrow(v1), Write(v1_label))
        self.play(GrowArrow(v2), Write(v2_label))
        self.play(GrowArrow(w), Write(w_label))
        self.wait(2)

        # Span area
        span_area = Polygon(
            ORIGIN, 2 * RIGHT, [2, 2, 0], 2 * UP,
            color=YELLOW, fill_opacity=0.3
        )
        span_text = MathTex(
            "\\text{Span}(\\vec{v}_1, \\vec{v}_2)", font_size=24
        ).set_color(YELLOW).next_to(span_area, RIGHT)
        self.play(FadeIn(span_area), Write(span_text))
        self.wait(2)

        # Project w onto the span
        proj_w = Arrow(start=ORIGIN, end=[1.5, 0.5, 0], color=PURPLE, buff=0).set_stroke(width=6)
        proj_label = MathTex("\\text{Projection of } \\vec{w}").next_to(proj_w, DOWN + RIGHT).set_color(PURPLE)
        self.play(Transform(w, proj_w), FadeIn(proj_label))
        self.wait(2)

        # Replace v1 with w
        new_v1 = proj_w.copy().set_color(ORANGE)
        new_v1_label = MathTex("\\vec{w}").next_to(new_v1, DOWN).set_color(ORANGE)
        replace_text = MathTex("\\text{Replace } \\vec{v}_1 with \\vec{w}", font_size=24).set_color(ORANGE).to_edge(LEFT)

        self.play(FadeOut(v1), FadeOut(v1_label))
        self.play(GrowArrow(new_v1), Write(new_v1_label), Write(replace_text))
        self.wait(2)

        # Proof sketch
        proof_text = MathTex(
            "\\text{Proof Sketch:\n1. } \\vec{w} \\text { is in the span of } \\{\\vec{v}_1, \\vec{v}_2\\}. \n"
            "2. \\text{ Replacing } \\vec{v}_1 \\text{with}  \\vec{w} \\text{still spans the space.} \n"
            "3. \\text{Linear independence of }\\{\\vec{v}_2, \\vec{w}\\} \\text{holds.}",
            font_size=20
        ).to_edge(DOWN)
        self.play(FadeOut(span_area), FadeOut(span_text))
        self.play(Write(proof_text))
        self.wait(5)

        # Outro
        self.play(FadeOut(proof_text))
        outro = Text("AJKA JE KUNDA BROO TO JE JASNY", font_size=36).set_color(BLUE).to_edge(DOWN)
        self.play(Write(outro))
        self.wait(3)
