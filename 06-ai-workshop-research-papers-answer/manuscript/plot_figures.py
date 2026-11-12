#!/usr/bin/env python3
"""Generate publication-quality manuscript figures strictly from data/tables/*.tsv.
Uses only the Python standard library plus matplotlib.
"""
import csv
import math
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
TABLES = ROOT / "data" / "tables"
FIG_DIR = ROOT / "manuscript" / "figures"
FIG_DIR.mkdir(parents=True, exist_ok=True)

plt.rcParams.update({
    "font.family": "serif",
    "font.size": 9.5,
    "axes.titlesize": 10.5,
    "axes.titleweight": "bold",
    "axes.labelsize": 9.5,
    "xtick.labelsize": 8.5,
    "ytick.labelsize": 8.5,
    "legend.fontsize": 8.5,
    "figure.dpi": 300,
    "savefig.dpi": 300,
    "axes.spines.top": False,
    "axes.spines.right": False,
})


def read_tsv(filename):
    with (TABLES / filename).open("r", encoding="utf-8") as f:
        return list(csv.reader(f, delimiter="\t"))


def make_fig1():
    """Figure 1: (A) Downstream cohort filtering funnel (00_filtering_funnel.tsv)
    and (B) Upstream DADA2 denoising read retention across 41 samples (01_dada2_stats.tsv).
    """
    funnel_rows = read_tsv("00_filtering_funnel.tsv")[1:]
    downstream = [r for r in funnel_rows if r[0] != "upstream_dada2"]
    stage_labels = [
        "0. Raw FigShare\ntable",
        "1. Trial cohort\n(autoFmtGroup)",
        "2. Time window\n(-10 to +70 d)",
        "3. Prevalence\n(>=2 samples)",
        "4. Taxonomy\n(p__, no organellar)",
        "5. Depth >=10,000\nreads/sample",
    ]
    samples = [int(r[2]) for r in downstream]
    asvs = [int(r[3]) for r in downstream]
    reads_m = [int(r[4]) / 1e6 for r in downstream]

    dada_rows = read_tsv("01_dada2_stats.tsv")[2:]  # skip header + #q2:types
    cols = ["input", "filtered", "denoised", "merged", "non-chimeric"]
    col_idx = [1, 2, 4, 5, 7]
    totals = [sum(int(r[i]) for r in dada_rows) for i in col_idx]
    pct_of_input = [t / totals[0] * 100.0 for t in totals]
    per_sample_nonchim_pct = [float(r[8]) for r in dada_rows]

    print("=== Derived Stats for citation-check.md ===")
    print(f"Upstream 41 samples total reads: input={totals[0]:,}, filtered={totals[1]:,} ({pct_of_input[1]:.2f}%), "
          f"denoised={totals[2]:,} ({pct_of_input[2]:.2f}%), merged={totals[3]:,} ({pct_of_input[3]:.2f}%), "
          f"non-chimeric={totals[4]:,} ({pct_of_input[4]:.2f}%)")
    print(f"Per-sample non-chimeric retention: min={min(per_sample_nonchim_pct):.2f}%, "
          f"max={max(per_sample_nonchim_pct):.2f}%, mean={sum(per_sample_nonchim_pct)/len(per_sample_nonchim_pct):.2f}%")

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.5, 4.0), gridspec_kw={"width_ratios": [1.25, 1.0]})

    # Panel A: Downstream filtering funnel (log10 scale or broken/annotated horizontal bars for stages 1-5 + raw inset)
    y_pos = list(range(len(stage_labels)))[::-1]
    bar_h = 0.36
    b1 = ax1.barh([y + bar_h / 2 for y in y_pos], samples, height=bar_h, color="#2b5c8f", label="Samples (n)")
    b2 = ax1.barh([y - bar_h / 2 for y in y_pos], asvs, height=bar_h, color="#d97724", label="ASVs (n)")
    ax1.set_xscale("log")
    ax1.set_yticks(y_pos)
    ax1.set_yticklabels(stage_labels)
    ax1.set_xlabel("Count (log scale)")
    ax1.set_xlim(100, 80000)
    ax1.set_title("A. Downstream Cohort and ASV Filtering Funnel")
    ax1.legend(loc="lower right", frameon=False)
    for y, s, a, rm in zip(y_pos, samples, asvs, reads_m):
        ax1.text(s * 1.12, y + bar_h / 2, f"{s:,} ({rm:.1f}M reads)", va="center", fontsize=7.8, color="#1b3b5c")
        ax1.text(a * 1.12, y - bar_h / 2, f"{a:,} ASVs", va="center", fontsize=7.8, color="#8c460a")

    # Panel B: Upstream DADA2 denoising retention across stages (total % of input + per-sample min-max error bars)
    stage_names = ["Input", "Filtered", "Denoised", "Merged", "Non-chimeric"]
    per_sample_stage_pcts = [
        [100.0 for _ in dada_rows],
        [int(r[2]) / int(r[1]) * 100.0 for r in dada_rows],
        [int(r[4]) / int(r[1]) * 100.0 for r in dada_rows],
        [int(r[5]) / int(r[1]) * 100.0 for r in dada_rows],
        [int(r[7]) / int(r[1]) * 100.0 for r in dada_rows],
    ]
    x = list(range(len(stage_names)))
    bars = ax2.bar(x, pct_of_input, width=0.55, color="#3b7a57", alpha=0.85, label="Pooled read retention (%)")
    # Overlay individual sample trajectories lightly
    for s_idx in range(len(dada_rows)):
        ax2.plot(x, [per_sample_stage_pcts[k][s_idx] for k in range(5)], color="#1f2937", alpha=0.15, linewidth=0.7)
    for xi, pct, tot in zip(x, pct_of_input, totals):
        ax2.text(xi, pct + 1.8, f"{pct:.1f}%\n({tot/1e6:.2f}M)", ha="center", va="bottom", fontsize=7.8)
    ax2.set_xticks(x)
    ax2.set_xticklabels(stage_names, rotation=15)
    ax2.set_ylim(60, 112)
    ax2.set_ylabel("Reads retained (% of input)")
    ax2.set_title("B. Upstream DADA2 Read Retention (n = 41 samples)")

    fig.tight_layout()
    fig.savefig(FIG_DIR / "fig1_filtering_and_qc.pdf", bbox_inches="tight")
    fig.savefig(FIG_DIR / "fig1_filtering_and_qc.png", bbox_inches="tight")
    plt.close(fig)


def make_fig2():
    """Figure 2: (A) Pairwise Kruskal-Wallis H-statistics on observed ASVs across metadata variables
    (02_kruskal_*.tsv) and (B) Beta-diversity PCoA variance explained (05_pcoa_proportion_explained.tsv).
    """
    kw_items = []
    # 1. Time relative to HCT
    for r in read_tsv("02_kruskal_categorical-time-relative-to-hct.tsv")[1:]:
        kw_items.append((f"HCT time: {r[0]} vs {r[1]}", float(r[2]), float(r[3]), float(r[4]), "Time (HCT)"))
    # 2. Time relative to FMT
    for r in read_tsv("02_kruskal_categorical-time-relative-to-fmt.tsv")[1:]:
        kw_items.append((f"FMT time: {r[0]} vs {r[1]}", float(r[2]), float(r[3]), float(r[4]), "Time (FMT)"))
    # 3. Treatment group
    for r in read_tsv("02_kruskal_autoFmtGroup.tsv")[1:]:
        kw_items.append((f"Group: {r[0]} vs {r[1]}", float(r[2]), float(r[3]), float(r[4]), "Intervention"))
    # 4. Stool consistency
    for r in read_tsv("02_kruskal_Consistency.tsv")[1:]:
        kw_items.append((f"Stool: {r[0]} vs {r[1]}", float(r[2]), float(r[3]), float(r[4]), "Clinical"))
    # 5. HCT Source (top 3 significant + non-sig summary or all)
    for r in read_tsv("02_kruskal_HCTSource.tsv")[1:]:
        g1 = r[0].replace("_unmodified", "")
        g2 = r[1].replace("_unmodified", "")
        kw_items.append((f"Graft: {g1} vs {g2}", float(r[2]), float(r[3]), float(r[4]), "Clinical"))

    # Sort by H statistic ascending for horizontal bar chart
    kw_items.sort(key=lambda x: x[1])

    pcoa_rows = read_tsv("05_pcoa_proportion_explained.tsv")[1:]
    metric_labels = {
        "weighted_unifrac": "Weighted UniFrac",
        "unweighted_unifrac": "Unweighted UniFrac",
        "bray_curtis": "Bray-Curtis",
        "jaccard": "Jaccard",
    }

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.0, 4.6), gridspec_kw={"width_ratios": [1.35, 1.0]})

    # Panel A: Horizontal bar plot of Kruskal-Wallis H statistics
    y_pos = list(range(len(kw_items)))
    colors = []
    for _, _, _, q, cat in kw_items:
        if cat == "Intervention":
            colors.append("#dc2626")
        elif q < 0.05:
            colors.append("#2b5c8f")
        else:
            colors.append("#9ca3af")
    hs = [x[1] for x in kw_items]
    ax1.barh(y_pos, hs, color=colors, height=0.68)
    ax1.set_yticks(y_pos)
    ax1.set_yticklabels([x[0] for x in kw_items], fontsize=7.8)
    ax1.set_xlabel("Kruskal-Wallis H statistic (observed ASVs)")
    ax1.set_xlim(0, 88)
    ax1.set_title("A. Cross-Sectional Richness Comparisons (n = 356 samples)")
    for y, (_, h, p, q, _) in enumerate(kw_items):
        q_str = f"q = {q:.1e}" if q < 0.001 else f"q = {q:.3f}"
        ax1.text(h + 1.0, y, f"H = {h:.2f} ({q_str})", va="center", fontsize=7.3)

    # Panel B: PCoA proportion explained (PC1, PC2, PC3 stacked/grouped)
    m_names = [metric_labels[r[0]] for r in pcoa_rows]
    pc1 = [float(r[1].rstrip("%")) for r in pcoa_rows]
    pc2 = [float(r[2].rstrip("%")) for r in pcoa_rows]
    pc3 = [float(r[3].rstrip("%")) for r in pcoa_rows]
    x = list(range(len(m_names)))
    w = 0.26
    ax2.bar([i - w for i in x], pc1, width=0.23, color="#1d4ed8", label="PC1")
    ax2.bar(x, pc2, width=0.23, color="#3b82f6", label="PC2")
    ax2.bar([i + w for i in x], pc3, width=0.23, color="#93c5fd", label="PC3")
    for i, (p1, p2, p3) in enumerate(zip(pc1, pc2, pc3)):
        tot = p1 + p2 + p3
        ax2.text(i - w, p1 + 0.5, f"{p1:.1f}%", ha="center", va="bottom", fontsize=6.6)
        ax2.text(i, p2 + (1.6 if abs(p2 - p3) < 1.5 else 0.5), f"{p2:.1f}%", ha="center", va="bottom", fontsize=6.6)
        ax2.text(i + w, p3 + 0.5, f"{p3:.1f}%", ha="center", va="bottom", fontsize=6.6)
        ax2.text(i, max(p1, p2, p3) + 3.8, f"Sum: {tot:.1f}%", ha="center", va="bottom",
                 fontsize=7.6, fontweight="bold", color="#1e3a8a")
    ax2.set_xticks(x)
    ax2.set_xticklabels(m_names, rotation=15)
    ax2.set_ylim(0, 39)
    ax2.set_ylabel("Variance explained (%)")
    ax2.set_title("B. Beta-Diversity PCoA Variance Explained")
    ax2.legend(loc="upper right", frameon=False)

    fig.tight_layout()
    fig.savefig(FIG_DIR / "fig2_diversity_and_pcoa.pdf", bbox_inches="tight")
    fig.savefig(FIG_DIR / "fig2_diversity_and_pcoa.png", bbox_inches="tight")
    plt.close(fig)


def make_fig3():
    """Figure 3: Longitudinal Linear Mixed-Effects (LME) Model Results (03_lme_model_results.tsv & 03_lme_model_summary.tsv).
    (A) Predicted linear trajectories of observed_features across day-relative-to-fmt for Control vs Auto-FMT.
    (B) Fixed-effect slope coefficients and 95% confidence intervals.
    """
    lme_rows = read_tsv("03_lme_model_results.tsv")[1:]
    # Rows: Intercept, autoFmtGroup[T.treatment], Q('day-relative-to-fmt'), Q('day-relative-to-fmt'):autoFmtGroup[T.treatment], Group Var
    b0 = float(lme_rows[0][1])          # 65.687
    b_grp = float(lme_rows[1][1])       # 2.962
    b_day = float(lme_rows[2][1])       # -0.859
    b_int = float(lme_rows[3][1])       # 0.560

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.5, 4.0), gridspec_kw={"width_ratios": [1.2, 1.0]})

    # Panel A: Model-implied linear trajectories across day-relative-to-fmt (-25 to +55 days)
    days = [d for d in range(-25, 56, 5)]
    y_ctrl = [b0 + b_day * d for d in days]
    y_treat = [(b0 + b_grp) + (b_day + b_int) * d for d in days]

    ax1.axvline(0, color="#6b7280", linestyle=":", linewidth=1.0, label="Day of auto-FMT (day 0)")
    ax1.plot(days, y_ctrl, color="#2563eb", linestyle="--", linewidth=2.2,
             label=f"Control: slope = {b_day:.3f} ASVs/d (p < 0.001)")
    ax1.plot(days, y_treat, color="#d97706", linestyle="-", linewidth=2.2,
             label=f"Auto-FMT: net slope = {b_day + b_int:.3f} ASVs/d\n(interaction +{b_int:.3f} ASVs/d, p = 0.016)")
    ax1.set_xlabel("Day relative to FMT")
    ax1.set_ylabel("Model-predicted observed ASVs")
    ax1.set_title("A. LME Predicted Trajectories (24 patients, 356 samples)")
    ax1.set_ylim(10, 105)
    ax1.legend(loc="upper right", frameon=False, fontsize=8.0)
    ax1.text(-23, 16, "Note: REML optimizer reported Converged = No\n(Random intercept variance = 197.005; Scale = 1757.408)",
             fontsize=7.5, color="#4b5563", bbox=dict(boxstyle="round,pad=0.3", facecolor="#f3f4f6", edgecolor="#d1d5db"))

    # Panel B: Forest plot of daily slope parameters (95% CI)
    terms = [
        ("Control slope\n(day-relative-to-fmt)", float(lme_rows[2][1]), float(lme_rows[2][5]), float(lme_rows[2][6]), "p < 0.001", "#2563eb"),
        ("Interaction\n(day × treatment)", float(lme_rows[3][1]), float(lme_rows[3][5]), float(lme_rows[3][6]), "p = 0.016", "#d97706"),
    ]
    ax2.axvline(0, color="#6b7280", linestyle="--", linewidth=1.0)
    y_pos = [1, 0]
    for y, (label, est, ci_low, ci_high, p_txt, col) in zip(y_pos, terms):
        ax2.errorbar(est, y, xerr=[[est - ci_low], [ci_high - est]], fmt="o", color=col,
                     ecolor=col, elinewidth=2.2, capsize=5, markersize=7)
        ax2.text(est, y + 0.18, f"{est:+.3f} [{ci_low:+.3f}, {ci_high:+.3f}]\n({p_txt})",
                 ha="center", va="bottom", fontsize=8.2, color=col, fontweight="bold")
    ax2.set_yticks(y_pos)
    ax2.set_yticklabels([t[0] for t in terms])
    ax2.set_ylim(-0.5, 1.65)
    ax2.set_xlim(-1.45, 1.35)
    ax2.set_xlabel("Rate of change in observed ASVs per day (95% CI)")
    ax2.set_title("B. Fixed-Effect Slope Estimates and 95% CIs")

    fig.tight_layout()
    fig.savefig(FIG_DIR / "fig3_lme_trajectories.pdf", bbox_inches="tight")
    fig.savefig(FIG_DIR / "fig3_lme_trajectories.png", bbox_inches="tight")
    plt.close(fig)


def make_fig4():
    """Figure 4: Random Forest Feature Volatility Importance (04_rf_feature_importance.tsv & 04_rf_accuracy.tsv)."""
    rf_rows = read_tsv("04_rf_feature_importance.tsv")[1:]
    acc_row = read_tsv("04_rf_accuracy.tsv")[1]
    mse = float(acc_row[1])
    r_val = float(acc_row[2])
    r2_val = float(acc_row[3])
    p_val = float(acc_row[4])
    slope = float(acc_row[6])
    intercept = float(acc_row[7])

    def clean_taxon(raw):
        parts = [p.strip() for p in raw.split(";")]
        phylum = parts[1].replace("p__", "") if len(parts) > 1 else ""
        fam = parts[4].replace("f__", "") if len(parts) > 4 else ""
        gen = parts[5].replace("g__", "") if len(parts) > 5 else ""
        cls = parts[2].replace("c__", "") if len(parts) > 2 else ""
        if gen and gen != "__":
            label = f"{fam}; g__{gen}" if gen == "Incertae_Sedis" else f"g__{gen} ({fam})"
        elif fam and fam != "__":
            label = f"f__{fam} (unclassified genus)"
        else:
            label = f"c__{cls} (unclassified)"
        return label, phylum

    parsed = []
    for r in rf_rows:
        lbl, phy = clean_taxon(r[0])
        parsed.append((lbl, phy, float(r[1])))
    parsed.reverse()  # ascending for horizontal bar chart

    phylum_colors = {
        "Bacillota": "#2b5c8f",
        "Actinomycetota": "#d97724",
        "Verrucomicrobiota": "#16a34a",
        "Pseudomonadota": "#dc2626",
    }

    fig, ax = plt.subplots(figsize=(8.8, 5.2))
    y_pos = list(range(len(parsed)))
    vals = [x[2] for x in parsed]
    cols = [phylum_colors.get(x[1], "#6b7280") for x in parsed]
    ax.barh(y_pos, vals, color=cols, height=0.7)
    ax.set_yticks(y_pos)
    ax.set_yticklabels([x[0] for x in parsed], fontsize=8.2)
    ax.set_xlabel("Random forest feature importance (predicting week-relative-to-hct)")
    ax.set_xlim(0, 0.148)
    ax.set_title("Temporal Indicator Taxa Ranked by Random Forest Regression Importance")

    for y, v in zip(y_pos, vals):
        ax.text(v + 0.0018, y, f"{v:.3f}", va="center", fontsize=7.8)

    # Legend for phylum colors + model performance box
    handles = [plt.Rectangle((0, 0), 1, 1, color=c, label=p) for p, c in phylum_colors.items()]
    ax.legend(handles=handles, title="Phylum", loc="lower right", frameon=True)

    perf_text = (
        f"Model performance (week-relative-to-hct):\n"
        f"R² = {r2_val:.3f}, Pearson r = {r_val:.3f}\n"
        f"P = {p_val:.2e}, MSE = {mse:.3f}\n"
        f"Fit: y = {slope:.3f}x + {intercept:.3f}"
    )
    ax.text(0.078, 4.2, perf_text, fontsize=8.2,
            bbox=dict(boxstyle="round,pad=0.4", facecolor="#f8fafc", edgecolor="#cbd5e1"))

    fig.tight_layout()
    fig.savefig(FIG_DIR / "fig4_rf_feature_importance.pdf", bbox_inches="tight")
    fig.savefig(FIG_DIR / "fig4_rf_feature_importance.png", bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    make_fig1()
    make_fig2()
    make_fig3()
    make_fig4()
    print("Successfully generated all 4 figures in manuscript/figures/.")
