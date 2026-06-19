"""
Welfare-loss sensitivity analysis for Visibility Bias v2.

Implements Proposition 3 of the cadre attention model (see 03-analysis/model.md):
    W_i = (1/2) * 1/[a^SO(1-a^SO)] * (a^* - a^SO)^2

Produces:
- Welfare estimates under grid of a^SO and a^* values
- Sensitivity to utility-to-yuan conversion (service-flow rate)
- Sensitivity to utility functional form (log vs CRRA)
- LaTeX table and ggplot-style sensitivity figure

Run from /Users/andy/Desktop/Research/visibility-bias-v2/:
    python 03-analysis/welfare-sensitivity.py

Outputs:
    03-analysis/welfare-sensitivity-results.csv
    04-figures/welfare-sensitivity.pdf
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams.update({
    "font.family": "serif",
    "font.size": 11,
    "axes.titlesize": 12,
    "axes.labelsize": 11,
    "figure.dpi": 110,
    "savefig.bbox": "tight",
})


# ============================================================
# Core welfare function (Proposition 3, log utility)
# ============================================================
def welfare_loss_log(a_star, a_so):
    """Utility-unit welfare loss under U^S = alpha*ln(V) + beta*ln(F)."""
    # Second-order Taylor expansion around a_so
    return 0.5 * (a_star - a_so) ** 2 / (a_so * (1 - a_so))


def welfare_loss_crra(a_star, a_so, sigma=2.0):
    """Welfare loss under CRRA utility with coefficient sigma.
    U(c) = c^(1-sigma) / (1-sigma). Reduces to log as sigma -> 1."""
    # Exact computation using discrete evaluation
    # Normalize B=1 so a is the share
    def U(a, alpha):
        beta = 1 - alpha
        V, F = a, 1 - a
        if sigma == 1.0:
            return alpha * np.log(V) + beta * np.log(F)
        return (alpha * V ** (1 - sigma) + beta * F ** (1 - sigma)) / (1 - sigma)

    # The social planner's alpha = a_so (since optimal a = alpha for CD log case)
    alpha = a_so
    return U(a_so, alpha) - U(a_star, alpha)


# ============================================================
# Parameters
# ============================================================
A_SO_GRID = np.array([0.40, 0.42, 0.44, 0.45, 0.46, 0.48, 0.50, 0.52, 0.55])
A_STAR_POINT = 0.538  # from v1 CIR mean
A_STAR_GRID = np.array([0.50, 0.52, 0.538, 0.55, 0.57, 0.60])
B_ANNUAL_TRILLION = 3.5   # trillion yuan: aggregate municipal construction (MOHURD/NBS)
DEPRECIATION_RATE = 0.08  # 8%/year service-flow factor (Barro 1990)


# ============================================================
# Main sensitivity grid
# ============================================================
rows = []
for a_so in A_SO_GRID:
    for a_star in A_STAR_GRID:
        for sigma in [1.0, 2.0, 4.0]:
            if sigma == 1.0:
                W_unitless = welfare_loss_log(a_star, a_so)
            else:
                W_unitless = welfare_loss_crra(a_star, a_so, sigma=sigma)
            W_yuan_bn = W_unitless * DEPRECIATION_RATE * B_ANNUAL_TRILLION * 1000
            rows.append({
                "a_SO": a_so,
                "a_star": a_star,
                "delta": a_star - a_so,
                "sigma": sigma,
                "W_unitless": W_unitless,
                "W_yuan_billion_per_year": W_yuan_bn,
            })

df = pd.DataFrame(rows)
out_csv = "/Users/andy/Desktop/Research/visibility-bias-v2/03-analysis/welfare-sensitivity-results.csv"
df.to_csv(out_csv, index=False)
print(f"Saved sensitivity grid → {out_csv}")


# ============================================================
# Headline numbers (log, a_star = 0.538)
# ============================================================
headline = df[(df.sigma == 1.0) & (df.a_star == 0.538)].copy()
print("\n=== Headline welfare estimates (log utility, observed a* = 0.538) ===")
print(headline[["a_SO", "delta", "W_unitless", "W_yuan_billion_per_year"]].round(3).to_string(index=False))

central = df[(df.sigma == 1.0) & (df.a_star == 0.538) & (df.a_SO == 0.45)].iloc[0]
print(f"\nCentral estimate (a^SO = 0.45, log utility):")
print(f"  Unitless welfare loss: {central.W_unitless:.4f}")
print(f"  Yuan: ~{central.W_yuan_billion_per_year:.1f} billion per year")
print(f"  Band over a^SO ∈ [0.40, 0.55]: {headline.W_yuan_billion_per_year.min():.0f}"
      f"–{headline.W_yuan_billion_per_year.max():.0f} billion per year")


# ============================================================
# Figure: 2x1 sensitivity panels
# ============================================================
fig, axes = plt.subplots(1, 2, figsize=(11, 4.2))

# Left: welfare vs a_SO, holding a* = 0.538, three utility curvatures
ax = axes[0]
for sigma in [1.0, 2.0, 4.0]:
    sub = df[(df.a_star == 0.538) & (df.sigma == sigma)].sort_values("a_SO")
    label = f"σ = {sigma:g}" + (" (log)" if sigma == 1.0 else "")
    ax.plot(sub.a_SO, sub.W_yuan_billion_per_year, marker="o", label=label, lw=1.5)
ax.axvline(0.45, color="grey", lw=0.8, ls="--")
ax.text(0.452, ax.get_ylim()[1] * 0.85, "preferred\n$a^{SO}$", fontsize=9, color="grey")
ax.set_xlabel("Social-optimum visible share $a^{SO}$")
ax.set_ylabel("Aggregate welfare loss (¥ billion/yr)")
ax.set_title("Sensitivity to $a^{SO}$ (observed $a^* = 0.538$)")
ax.legend(frameon=False)
ax.grid(True, alpha=0.3)

# Right: welfare vs a_star, holding a_SO = 0.45
ax = axes[1]
for sigma in [1.0, 2.0, 4.0]:
    sub = df[(df.a_SO == 0.45) & (df.sigma == sigma)].sort_values("a_star")
    label = f"σ = {sigma:g}" + (" (log)" if sigma == 1.0 else "")
    ax.plot(sub.a_star, sub.W_yuan_billion_per_year, marker="s", label=label, lw=1.5)
ax.axvline(0.538, color="grey", lw=0.8, ls="--")
ax.text(0.540, ax.get_ylim()[1] * 0.85, "observed\n$a^*$", fontsize=9, color="grey")
ax.set_xlabel("Observed visible share $a^*$")
ax.set_ylabel("Aggregate welfare loss (¥ billion/yr)")
ax.set_title("Sensitivity to $a^*$ (social optimum $a^{SO} = 0.45$)")
ax.legend(frameon=False)
ax.grid(True, alpha=0.3)

out_pdf = "/Users/andy/Desktop/Research/visibility-bias-v2/04-figures/welfare-sensitivity.pdf"
out_png = out_pdf.replace(".pdf", ".png")
fig.tight_layout()
fig.savefig(out_pdf)
fig.savefig(out_png, dpi=200)
print(f"\nSaved figure → {out_pdf}")
print(f"Saved figure → {out_png}")
