"""
==============================================================================
Project:     Fuzzy Logic Linguistic Sets & Operations
File:        main.py
Author:      Yevhen Biezhyn
Description: Object-oriented modeling of fuzzy membership functions and
             fundamental fuzzy set operations (Union, Intersection, Complement).
==============================================================================
"""

import argparse
import numpy as np
import matplotlib.pyplot as plt
from typing import Dict


class FuzzySatisfactionModel:
    """Modelliert linguistische Terme für Kundenzufriedenheit auf der Skala [0, 10]."""

    @staticmethod
    def very_dissatisfied(x: np.ndarray) -> np.ndarray:
        return np.maximum(1.0 - x / 3.0, 0.0)

    @staticmethod
    def dissatisfied(x: np.ndarray) -> np.ndarray:
        return np.maximum(np.minimum((x - 2.0) / 2.0, (6.0 - x) / 2.0), 0.0)

    @staticmethod
    def neutral(x: np.ndarray) -> np.ndarray:
        return np.maximum(np.minimum(x - 4.0, 6.0 - x), 0.0)

    @staticmethod
    def satisfied(x: np.ndarray) -> np.ndarray:
        return np.maximum(np.minimum((x - 6.0) / 2.0, (9.0 - x) / 2.0), 0.0)

    @staticmethod
    def very_satisfied(x: np.ndarray) -> np.ndarray:
        return np.maximum((x - 7.0) / 3.0, 0.0)

    # --- Fuzzy Mengenoperationen ---

    @staticmethod
    def union(mu_a: np.ndarray, mu_b: np.ndarray) -> np.ndarray:
        """S-Norm (Maximum) Vereinigung A u B"""
        return np.maximum(mu_a, mu_b)

    @staticmethod
    def intersection(mu_a: np.ndarray, mu_b: np.ndarray) -> np.ndarray:
        """T-Norm (Minimum) Schnittmenge A n B"""
        return np.minimum(mu_a, mu_b)

    @staticmethod
    def complement(mu_a: np.ndarray) -> np.ndarray:
        """Negation / Komplement nicht A = 1 - mu(x)"""
        return 1.0 - mu_a

    def evaluate_scalar(self, val: float) -> Dict[str, float]:
        """Berechnet Zugehörigkeitsgrade für einen konkreten Punktwert."""
        x_val = np.array([val])
        return {
            "Very Dissatisfied": float(self.very_dissatisfied(x_val)[0]),
            "Dissatisfied": float(self.dissatisfied(x_val)[0]),
            "Neutral": float(self.neutral(x_val)[0]),
            "Satisfied": float(self.satisfied(x_val)[0]),
            "Very Satisfied": float(self.very_satisfied(x_val)[0]),
        }


def plot_fuzzy_system(save: bool = False):
    model = FuzzySatisfactionModel()
    x = np.linspace(0, 10, 500)

    vd = model.very_dissatisfied(x)
    d  = model.dissatisfied(x)
    n  = model.neutral(x)
    s  = model.satisfied(x)
    vs = model.very_satisfied(x)

    op_union = model.union(d, n)
    op_inter = model.intersection(s, vs)
    op_neg   = model.complement(vd)

    plt.figure(figsize=(12, 8))

    # Basisterme
    plt.plot(x, vd, label="Sehr unzufrieden (Very Dissatisfied)", color="#d9534f", linewidth=2)
    plt.plot(x, d,  label="Unzufrieden (Dissatisfied)", color="#f0ad4e", linewidth=2)
    plt.plot(x, n,  label="Neutral", color="#5bc0de", linewidth=2)
    plt.plot(x, s,  label="Zufrieden (Satisfied)", color="#0275d8", linewidth=2)
    plt.plot(x, vs, label="Sehr zufrieden (Very Satisfied)", color="#5cb85c", linewidth=2)

    # Mengenoperationen
    plt.plot(x, op_union, 'k--', linewidth=2, label=r"Vereinigung: $D \cup N$ ($\max$)")
    plt.plot(x, op_inter, 'b:',  linewidth=2.5, label=r"Schnittmenge: $S \cap VS$ ($\min$)")
    plt.plot(x, op_neg,   'r-.', linewidth=2, label=r"Negation: $\neg VD$ ($1 - \mu$)")

    plt.xlabel("Zufriedenheitsgrad / Skala $x \in [0, 10]$", fontsize=11)
    plt.ylabel(r"Zugehoerigkeitsgrad $\mu(x)$", fontsize=11)
    plt.title("Fuzzy-Logik: Linguistische Terme und fundamentale Mengenoperationen", fontsize=13)
    plt.ylim(-0.05, 1.05)
    plt.xlim(0, 10)
    plt.legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncol=3, frameon=True)
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.tight_layout()

    if save:
        plt.savefig("fuzzy_logic_visualization.png", dpi=300)
        print("[+] Diagramm gespeichert unter 'fuzzy_logic_visualization.png'")
    else:
        plt.show()


def main():
    parser = argparse.ArgumentParser(description="Fuzzy Logic Set Operations & Membership Evaluator")
    parser.add_argument("--eval", type=float, default=None, help="Konkreten Zufriedenheitswert x auswerten (0.0 bis 10.0)")
    parser.add_argument("--save", action="store_true", help="Diagramm als PNG-Datei speichern")
    args = parser.parse_args()

    model = FuzzySatisfactionModel()

    if args.eval is not None:
        val = max(0.0, min(10.0, args.eval))
        print("=" * 60)
        print(f"  FUZZY MEMBERSHIP EVALUATION FOR x = {val:.2f}")
        print("=" * 60)
        res = model.evaluate_scalar(val)
        for term, deg in res.items():
            print(f"  {term:<20}: mu = {deg:.4f}")
        print("=" * 60)

    plot_fuzzy_system(save=args.save)


if __name__ == "__main__":
    main()
