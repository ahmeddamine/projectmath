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
        # Éléments de base : axes, cercle unité, ligne tangente verticale et repères
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

        x_val = PI / 6  # Angle de base pour toutes les démonstrations

        # Identité 1: tan(-x) = -tan(x)
        eq1 = Tex("La fonction tangente est impaire: $\\tan(-x)=-\\tan(x)$").to_edge(UP)
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

        # Identité 2: tan(π/2 - x) = 1/tan(x)
        eq2 = Tex("Tangente de l'angle complémentaire: $\\tan(\\frac{\\pi}{2}-x)=\\frac{1}{\\tan(x)}$").to_edge(UP)
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

        # Identité 3: tan(π/2 + x) = -1/tan(x)
        eq3 = Tex("Tangente: $\\tan(\\frac{\\pi}{2}+x)=-\\frac{1}{\\tan(x)}$").to_edge(UP)
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

        # Identité 4: tan(π - x) = -tan(x)
        eq4 = Tex("Tangente: $\\tan(\\pi-x)=-\\tan(x)$").to_edge(UP)
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

        # Identité 5: tan(π + x) = tan(x)
        eq5 = Tex("Périodicité de la tangente: $\\tan(\\pi+x)=\\tan(x)$").to_edge(UP)
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

        # Final
        self.play(FadeOut(axes), FadeOut(circle), FadeOut(tangent_line), FadeOut(ticks))
        credit = Tex(r"Réalisé par Sabir Ahmed Amine")
        self.play(Write(credit))
        self.wait(2)

    # Fonctions helper
    def create_full_construction(self, angle, tan_label_text, angle_label_text, color):
        result = {}
        if np.cos(angle) > 0:
            rad_line = Line(ORIGIN, np.array([np.cos(angle), np.sin(angle), 0]), color=color)
        else:
            rad_line = DashedLine(ORIGIN, np.array([1, np.tan(angle), 0]), color=color)
        
        rad_label = MathTex(angle_label_text).next_to(
            rad_line.get_end(), UP if np.sin(angle) >= 0 else DOWN, buff=0.2
        )
        result["radial"] = VGroup(rad_line, rad_label)
        result["radial_angle_label"] = rad_label

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
        ticks = VGroup()
        for y_val, text in [(-1, "-1"), (0, "0"), (1, "1")]:
            tick = Line(np.array([0.95, y_val, 0]), np.array([1.05, y_val, 0]), color=WHITE)
            tick_label = Tex(text).scale(0.5).next_to(tick, LEFT, buff=0.1)
            ticks.add(tick, tick_label)
        return ticks
