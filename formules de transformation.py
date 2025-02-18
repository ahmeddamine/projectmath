# === CRÉDITS ===
# Animation des identités trigonométriques par Sabir Ahmed Amine
# Développé avec ManimCE - https://www.manim.community
# Date de création : [17.02.2025]
"""
=== CREDITS ===
Project: Trigonometric Identities Visualization with Manim
Author: Sabir Ahmed Amine
Purpose: Educational video for trigonometry
Developed with Manim Community Edition
"""

from manim import *
import numpy as np

class TrigonometryEqualitiesPresentation(Scene):
    def construct(self):
        # Basic elements: axes, unit circle, vertical tangent line at x=1, and tick marks.
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

        # Base angle x = PI/6 for all demonstrations.
        x_val = PI / 6

        ###########################################################
        # Identity 1: tan(-x) = -tan(x)
        eq1 = Tex("La fonction tangente est negative: $\\tan(-x)=-\\tan(x)$").to_edge(UP)
        self.play(Write(eq1))
        self.wait(0.5)
        cons = self.create_full_construction(x_val, r"\tan(x)", "x", RED)
        self.play(FadeIn(cons["group"]), run_time=1.5)
        self.wait(1)
        new_angle = -x_val
        radial_group = cons["radial"]
        self.play(
            Rotate(radial_group, angle=new_angle - x_val, about_point=ORIGIN, run_time=1.5)
        )
        # Use the actual line to determine the new label position.
        radial_line = radial_group[0]
        old_angle_label = cons["radial_angle_label"]
        new_angle_label = MathTex("-x").next_to(
            radial_line.get_end(), UP if np.sin(new_angle) >= 0 else DOWN, buff=0.2
        )
        self.play(Transform(old_angle_label, new_angle_label), run_time=0.8)
        new_cons = self.create_full_construction(new_angle, r"-\tan(x)", "-x", RED)
        self.play(ReplacementTransform(cons["extension"], new_cons["extension"]), run_time=1)
        self.wait(2)
        self.play(FadeOut(VGroup(cons["group"], eq1)))
        self.wait(0.5)

        ###########################################################
        # Identity 2: tan(π/2 - x) = 1/tan(x)
        eq2 = Tex("Tangente de l'angle: $\\tan(\\frac{\\pi}{2}-x)=\\frac{1}{\\tan(x)}$").to_edge(UP)
        self.play(Write(eq2))
        self.wait(0.5)
        cons = self.create_full_construction(x_val, r"\tan(x)", "x", GREEN)
        self.play(FadeIn(cons["group"]), run_time=1.5)
        self.wait(0.5)
        new_angle = PI/2 - x_val
        radial_group = cons["radial"]
        self.play(
            Rotate(radial_group, angle=new_angle - x_val, about_point=ORIGIN, run_time=1.5)
        )
        radial_line = radial_group[0]
        old_angle_label = cons["radial_angle_label"]
        new_angle_label = MathTex(r"\frac{\pi}{2}-x").next_to(
            radial_line.get_end(), UP if np.sin(new_angle) >= 0 else DOWN, buff=0.2
        )
        self.play(Transform(old_angle_label, new_angle_label), run_time=0.8)
        new_cons = self.create_full_construction(new_angle, r"\frac{1}{\tan(x)}", r"\frac{\pi}{2}-x", GREEN)
        self.play(ReplacementTransform(cons["extension"], new_cons["extension"]), run_time=1)
        self.wait(2)
        self.play(FadeOut(VGroup(cons["group"], eq2)))
        self.wait(0.5)

        ###########################################################
        # Identity 3: tan(π/2 + x) = -1/tan(x)
        eq3 = Tex("Tangente de l'angle: $\\tan(\\frac{\\pi}{2}+x)=-\\frac{1}{\\tan(x)}$").to_edge(UP)
        self.play(Write(eq3))
        self.wait(0.5)
        cons = self.create_full_construction(x_val, r"\tan(x)", "x", ORANGE)
        self.play(FadeIn(cons["group"]), run_time=1.5)
        self.wait(0.5)
        new_angle = PI/2 + x_val
        radial_group = cons["radial"]
        self.play(
            Rotate(radial_group, angle=new_angle - x_val, about_point=ORIGIN, run_time=1.5)
        )
        radial_line = radial_group[0]
        old_angle_label = cons["radial_angle_label"]
        new_angle_label = MathTex(r"\frac{\pi}{2}+x").next_to(
            radial_line.get_end(), UP if np.sin(new_angle) >= 0 else DOWN, buff=0.2
        )
        self.play(Transform(old_angle_label, new_angle_label), run_time=0.8)
        new_cons = self.create_full_construction(new_angle, r"-\frac{1}{\tan(x)}", r"\frac{\pi}{2}+x", ORANGE)
        self.play(ReplacementTransform(cons["extension"], new_cons["extension"]), run_time=1)
        self.wait(2)
        self.play(FadeOut(VGroup(cons["group"], eq3)))
        self.wait(0.5)

        ###########################################################
        # Identity 4: tan(π - x) = -tan(x)
        eq4 = Tex("Tangente de l'angle: $\\tan(\\pi-x)=-\\tan(x)$").to_edge(UP)
        self.play(Write(eq4))
        self.wait(0.5)
        cons = self.create_full_construction(x_val, r"\tan(x)", "x", PURPLE)
        self.play(FadeIn(cons["group"]), run_time=1.5)
        self.wait(0.5)
        new_angle = PI - x_val
        radial_group = cons["radial"]
        self.play(
            Rotate(radial_group, angle=new_angle - x_val, about_point=ORIGIN, run_time=1.5)
        )
        radial_line = radial_group[0]
        old_angle_label = cons["radial_angle_label"]
        new_angle_label = MathTex(r"\pi-x").next_to(
            radial_line.get_end(), UP if np.sin(new_angle) >= 0 else DOWN, buff=0.2
        )
        self.play(Transform(old_angle_label, new_angle_label), run_time=0.8)
        new_cons = self.create_full_construction(new_angle, r"-\tan(x)", r"\pi-x", PURPLE)
        self.play(ReplacementTransform(cons["extension"], new_cons["extension"]), run_time=1)
        self.wait(2)
        self.play(FadeOut(VGroup(cons["group"], eq4)))
        self.wait(0.5)

        ###########################################################
        # Identity 5: tan(π + x) = tan(x)
        eq5 = Tex("Tangente de l'angle: $\\tan(\\pi+x)=\\tan(x)$").to_edge(UP)
        self.play(Write(eq5))
        self.wait(0.5)
        cons = self.create_full_construction(x_val, r"\tan(x)", "x", TEAL)
        self.play(FadeIn(cons["group"]), run_time=1.5)
        self.wait(0.5)
        new_angle = PI + x_val
        radial_group = cons["radial"]
        self.play(
            Rotate(radial_group, angle=new_angle - x_val, about_point=ORIGIN, run_time=1.5)
        )
        radial_line = radial_group[0]
        old_angle_label = cons["radial_angle_label"]
        new_angle_label = MathTex(r"\pi+x").next_to(
            radial_line.get_end(), UP if np.sin(new_angle) >= 0 else DOWN, buff=0.2
        )
        self.play(Transform(old_angle_label, new_angle_label), run_time=0.8)
        new_cons = self.create_full_construction(new_angle, r"\tan(x)", r"\pi+x", TEAL)
        self.play(ReplacementTransform(cons["extension"], new_cons["extension"]), run_time=1)
        self.wait(2)
        self.play(FadeOut(VGroup(cons["group"], eq5)))
        self.wait(0.5)

        ###########################################################
        # Identity 6: Périodicité générale: tan(x)=tan(α) avec x=α+kπ
        eq6 = Tex("Périodicité: $\\tan(x)=\\tan\\alpha$ avec $x=\\alpha+k\\pi$").to_edge(UP)
        self.play(Write(eq6))
        self.wait(0.5)
        cons = self.create_full_construction(x_val, r"\tan(x)", r"\alpha", RED)
        self.play(FadeIn(cons["group"]), run_time=1.5)
        self.wait(0.5)
        new_angle = x_val + PI
        radial_group = cons["radial"]
        self.play(
            Rotate(radial_group, angle=new_angle - x_val, about_point=ORIGIN, run_time=1.5)
        )
        radial_line = radial_group[0]
        old_angle_label = cons["radial_angle_label"]
        new_angle_label = MathTex(r"\alpha+\pi").next_to(
            radial_line.get_end(), UP if np.sin(new_angle) >= 0 else DOWN, buff=0.2
        )
        self.play(Transform(old_angle_label, new_angle_label), run_time=0.8)
        new_cons = self.create_full_construction(new_angle, r"\tan(x)", r"\alpha+\pi", RED)
        self.play(ReplacementTransform(cons["extension"], new_cons["extension"]), run_time=1)
        self.wait(1)
        # Further rotate to α+2π.
        new_angle2 = x_val + 2 * PI
        self.play(
            Rotate(radial_group, angle=new_angle2 - new_angle, about_point=ORIGIN, run_time=1.5)
        )
        radial_line = radial_group[0]
        new_angle_label2 = MathTex(r"\alpha+2\pi").next_to(
            radial_line.get_end(), UP if np.sin(new_angle2) >= 0 else DOWN, buff=0.2
        )
        self.play(Transform(old_angle_label, new_angle_label2), run_time=0.8)
        new_cons2 = self.create_full_construction(new_angle2, r"\tan(x)", r"\alpha+2\pi", RED)
        self.play(ReplacementTransform(new_cons["extension"], new_cons2["extension"]), run_time=1)
        self.wait(2)
        self.play(FadeOut(VGroup(radial_group, new_cons2["extension"], old_angle_label, eq6)))
        self.wait(0.5)

        ###########################################################
        # Clear the circle demo.
        self.play(FadeOut(axes), FadeOut(circle), FadeOut(tangent_line), FadeOut(ticks))
        self.wait(1)

        # Add centered credit
        credit = Tex("Réalisé par Sabir Ahmed Amine").scale(1.5).move_to(ORIGIN)
        self.play(Write(credit))
        self.wait(3)
        return
        ###########################################################
        # Derivation of:
        #   cos²x = 1/(1+tan²x)   and   sin²x = tan²x/(1+tan²x)
        deriv_title = Tex("Dérivation:").to_edge(UP)
        self.play(Write(deriv_title))
        self.wait(0.5)
        # Step 1: tan(x)=sin(x)/cos(x)
        eq_a = MathTex(r"\tan(x)=\frac{\sin(x)}{\cos(x)}").next_to(deriv_title, DOWN)
        self.play(Write(eq_a), run_time=1)
        self.wait(1)
        # Step 2: Square both sides.
        eq_b = MathTex(r"\tan^2(x)=\frac{\sin^2(x)}{\cos^2(x)}").next_to(deriv_title, DOWN)
        self.play(TransformMatchingTex(eq_a, eq_b), run_time=1.5)
        self.wait(1)
        self.play(FadeOut(eq_b))
        # Step 3: Pythagorean identity.
        eq_c = MathTex(r"\sin^2(x)+\cos^2(x)=1").next_to(deriv_title, DOWN)
        self.play(Write(eq_c), run_time=1)
        self.wait(1)
        self.play(FadeOut(eq_c))
        # Step 4: Divide by cos²(x): 1/cos²(x)=1+tan²(x)
        eq_d = MathTex(r"\frac{1}{\cos^2(x)}=1+\tan^2(x)").next_to(deriv_title, DOWN)
        self.play(Write(eq_d), run_time=1.5)
        self.wait(1)
        # Step 5: Invert to get cos²(x).
        eq_e = MathTex(r"\cos^2(x)=\frac{1}{1+\tan^2(x)}").next_to(deriv_title, DOWN)
        self.play(TransformMatchingTex(eq_d, eq_e), run_time=1.5)
        self.wait(1)
        self.play(FadeOut(eq_e))
        # Step 6: Then, sin²(x)=1-cos²(x)=tan²(x)/(1+tan²(x))
        eq_f = MathTex(r"\sin^2(x)=\frac{\tan^2(x)}{1+\tan^2(x)}").next_to(deriv_title, DOWN)
        self.play(Write(eq_f), run_time=1.5)
        self.wait(2)
        self.play(FadeOut(VGroup(deriv_title, eq_f)))
        self.wait(1)

    ###########################################################
    # Helper functions
    def create_full_construction(self, angle, tan_label_text, angle_label_text, color):
        """
        Returns a dictionary with:
          - "radial": a VGroup containing the radial line (from the origin to the circle, or dashed if needed)
            and its attached angle label.
          - "extension": a VGroup with a dashed line from the circle (or origin) to the intersection
             on the vertical tangent (x=1), plus a dot and a tangent label.
          - "group": the combined VGroup.
          - "radial_angle_label": a reference to the angle label.
        """
        result = {}
        # Radial part.
        if np.cos(angle) > 0:
            rad_line = Line(ORIGIN, np.array([np.cos(angle), np.sin(angle), 0]), color=color)
        else:
            rad_line = DashedLine(ORIGIN, np.array([1, np.tan(angle), 0]), color=color)
        rad_label = MathTex(angle_label_text).next_to(
            rad_line.get_end(), UP if np.sin(angle) >= 0 else DOWN, buff=0.2
        )
        result["radial"] = VGroup(rad_line, rad_label)
        result["radial_angle_label"] = rad_label

        # Extension part.
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
        """Creates tick marks on the vertical tangent (x=1) for -1, 0, and 1."""
        ticks = VGroup()
        for y_val, text in [(-1, "-1"), (0, "0"), (1, "1")]:
            tick = Line(np.array([0.95, y_val, 0]), np.array([1.05, y_val, 0]), color=WHITE)
            tick_label = Tex(text).scale(0.5).next_to(tick, LEFT, buff=0.1)
            ticks.add(tick, tick_label)
        return ticks

        for y_val, text in [(-1, "-1"), (0, "0"), (1, "1")]:
            tick = Line(np.array([0.95, y_val, 0]), np.array([1.05, y_val, 0]), color=WHITE)
            tick_label = Tex(text).scale(0.5).next_to(tick, LEFT, buff=0.1)
            ticks.add(tick, tick_label)
        return ticks
