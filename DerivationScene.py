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

class DerivationScene(Scene):
    def construct(self):
        # -------------------------------------------
        # Partie 1 : cos²(x) = 1/(1+tan²(x))
        title1 = Tex("Démonstration de $\\cos^2(x) = \\frac{1}{1+\\tan^2(x)}$").to_edge(UP)
        self.play(Write(title1))
        self.wait(0.5)
        
        # Étape 1 : Définition de la tangente
        step1 = MathTex(r"\tan(x) = \frac{\sin(x)}{\cos(x)}")
        self.play(Write(step1))
        self.wait(1)
        
        # Étape 2 : Mise au carré
        step2 = MathTex(r"\tan^2(x) = \left(\frac{\sin(x)}{\cos(x)}\right)^2")
        self.play(ReplacementTransform(step1, step2))
        self.wait(1)
        
        # Étape 3 : Simplification
        step3 = MathTex(r"\tan^2(x) = \frac{\sin^2(x)}{\cos^2(x)}")
        self.play(ReplacementTransform(step2, step3))
        self.wait(1)
        
        # Étape 4 : Ajout de 1
        step4 = MathTex(r"1 + \tan^2(x) = 1 + \frac{\sin^2(x)}{\cos^2(x)}")
        self.play(ReplacementTransform(step3, step4))
        self.wait(1)
        
        # Étape 5 : Common denominator
        step5 = MathTex(r"1 + \tan^2(x) = \frac{\sin^2(x) + \cos^2(x)}{\cos^2(x)}")
        self.play(ReplacementTransform(step4, step5))
        self.wait(1)
        
        # Étape 6 : Identité trigonométrique
        step6 = MathTex(r"1 + \tan^2(x) = \frac{1}{\cos^2(x)}")
        self.play(ReplacementTransform(step5, step6))
        self.wait(1)
        
        # Étape 7 : Conclusion
        step7 = MathTex(r"\cos^2(x) = \frac{1}{1 + \tan^2(x)}")
        self.play(ReplacementTransform(step6, step7))
        self.wait(2)
        
        self.play(FadeOut(VGroup(title1, step7)))
        self.wait(1)

        # -------------------------------------------
        # Partie 2 : sin²(x) = tan²(x)/(1+tan²(x))
        title2 = Tex("Démonstration de $\\sin^2(x) = \\frac{\\tan^2(x)}{1+\\tan^2(x)}$").to_edge(UP)
        self.play(Write(title2))
        self.wait(0.5)
        
        # Étape A : Identité de base
        stepA = MathTex(r"\sin^2(x) + \cos^2(x) = 1")
        self.play(Write(stepA))
        self.wait(1)
        
        # Étape B : Substitution avec cos²
        stepB = MathTex(r"\sin^2(x) + \frac{1}{1+\tan^2(x)} = 1")
        self.play(ReplacementTransform(stepA, stepB))
        self.wait(1)
        
        # Étape C : Isolation de sin²
        stepC = MathTex(r"\sin^2(x) = 1 - \frac{1}{1+\tan^2(x)}")
        self.play(ReplacementTransform(stepB, stepC))
        self.wait(1)
        
        # Étape D : Combinaison des termes
        stepD = MathTex(r"\sin^2(x) = \frac{(1+\tan^2(x)) - 1}{1+\tan^2(x)}")
        self.play(ReplacementTransform(stepC, stepD))
        self.wait(1)
        
        # Étape E : Simplification finale
        stepE = MathTex(r"\sin^2(x) = \frac{\tan^2(x)}{1+\tan^2(x)}")
        self.play(ReplacementTransform(stepD, stepE))
        self.wait(2)
        
        self.play(FadeOut(VGroup(title2, stepE)))
        self.wait(1)
