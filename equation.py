from manim import *
import numpy as np

class TanPeriodicite(Scene):
    def construct(self):
        # Setup axes, unit circle, tangent line, and ticks
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            axis_config={"include_numbers": False}
        ).set_opacity(0.5)
        circle = Circle(radius=1, color=BLUE)
        tangent_line = Line(np.array([1, -3, 0]), np.array([1, 3, 0]), color=YELLOW)
        ticks = self.create_tangent_ticks()
        self.play(Create(axes), Create(circle), Create(tangent_line), Create(ticks))
        self.wait(1)

        # Title for the periodicity identity
        eq = Tex(r"$\tan(x) = \tan(\alpha) \Rightarrow x = \alpha + k\pi$").to_edge(UP)
        self.play(Write(eq))
        self.wait(1)

        # Initial angle α (π/6)
        alpha = PI / 6
        cons = self.create_full_construction(alpha, r"\tan(\alpha)", r"\alpha", RED)
        self.play(FadeIn(cons["group"]))
        self.wait(1)

        # Rotate to α + π (k=1)
        new_angle1 = alpha + PI
        radial_group = cons["radial"]
        self.play(
            Rotate(radial_group, angle=PI, about_point=ORIGIN, run_time=2)
        )
        # Update angle label
        old_angle_label = cons["radial_angle_label"]
        new_angle_label1 = MathTex(r"\alpha + \pi").next_to(
            radial_group[0].get_end(), UP if np.sin(new_angle1) >= 0 else DOWN, buff=0.2
        )
        self.play(Transform(old_angle_label, new_angle_label1))
        # Update extension line (same tan value)
        new_cons1 = self.create_full_construction(new_angle1, r"\tan(\alpha)", r"\alpha + \pi", RED)
        self.play(ReplacementTransform(cons["extension"], new_cons1["extension"]))
        self.wait(1)

        # Rotate to α + 2π (k=2)
        new_angle2 = alpha + 2 * PI
        self.play(
            Rotate(radial_group, angle=PI, about_point=ORIGIN, run_time=2)
        )
        new_angle_label2 = MathTex(r"\alpha + 2\pi").next_to(
            radial_group[0].get_end(), UP if np.sin(new_angle2) >= 0 else DOWN, buff=0.2
        )
        self.play(Transform(old_angle_label, new_angle_label2))
        new_cons2 = self.create_full_construction(new_angle2, r"\tan(\alpha)", r"\alpha + 2\pi", RED)
        self.play(ReplacementTransform(new_cons1["extension"], new_cons2["extension"]))
        self.wait(1)

        # Rotate back to α - π (k=-1)
        new_angle3 = alpha - PI
        self.play(
            Rotate(radial_group, angle=-3 * PI, about_point=ORIGIN, run_time=2)  # Total rotation from α + 2π to α - π is -3π
        )
        new_angle_label3 = MathTex(r"\alpha - \pi").next_to(
            radial_group[0].get_end(), UP if np.sin(new_angle3) >= 0 else DOWN, buff=0.2
        )
        self.play(Transform(old_angle_label, new_angle_label3))
        new_cons3 = self.create_full_construction(new_angle3, r"\tan(\alpha)", r"\alpha - \pi", RED)
        self.play(ReplacementTransform(new_cons2["extension"], new_cons3["extension"]))
        self.wait(2)

        # Fade out elements and show credit
        self.play(FadeOut(VGroup(axes, circle, tangent_line, ticks, cons["group"], new_cons3["extension"], eq)))
        credit = Tex(r"Réalisé par Sabir Ahmed Amine")
        self.play(Write(credit))
        self.wait(2)

    def create_full_construction(self, angle, tan_label_text, angle_label_text, color):
        """Helper function to create the radial line, angle label, and tangent extension."""
        result = {}
        # Radial line and angle label
        if np.cos(angle) > 0:
            rad_line = Line(ORIGIN, np.array([np.cos(angle), np.sin(angle), 0]), color=color)
        else:
            rad_line = DashedLine(ORIGIN, np.array([1, np.tan(angle), 0]), color=color)
        rad_label = MathTex(angle_label_text).next_to(
            rad_line.get_end(), UP if np.sin(angle) >= 0 else DOWN, buff=0.2
        )
        result["radial"] = VGroup(rad_line, rad_label)
        result["radial_angle_label"] = rad_label

        # Extension line to tangent
        if np.cos(angle) > 0:
            circle_pt = np.array([np.cos(angle), np.sin(angle), 0])
            ext_line = DashedLine(circle_pt, np.array([1, np.tan(angle), 0]), color=color)
        else:
            ext_line = DashedLine(ORIGIN, np.array([1, np.tan(angle), 0]), color=color)
        dot = Dot(np.array([1, np.tan(angle), 0]), color=color)
        tan_label = MathTex(tan_label_text).next_to(dot, RIGHT, buff=0.1)
        result["extension"] = VGroup(ext_line, dot, tan_label)

        result["group"] = VGroup(result["radial"], result["extension"])
        return result

    def create_tangent_ticks(self):
        """Creates tick marks on the vertical tangent line at x=1."""
        ticks = VGroup()
        for y_val, text in [(-1, "-1"), (0, "0"), (1, "1")]:
            tick = Line(np.array([0.95, y_val, 0]), np.array([1.05, y_val, 0]), color=WHITE)
            tick_label = Tex(text).scale(0.5).next_to(tick, LEFT, buff=0.1)
            ticks.add(tick, tick_label)
        return ticks
