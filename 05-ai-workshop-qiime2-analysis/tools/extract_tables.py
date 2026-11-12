"""Extract the key statistics from the QIIME 2 outputs into plain TSV tables (results/tables/).

QIIME 2 .qza / .qzv files are zip archives; the numbers live in <uuid>/data/*.tsv|csv inside them.

usage: python tools/extract_tables.py QIIME2_RUN_DIR
  QIIME2_RUN_DIR = the full run folder (with Upstream/ and Downstream/), e.g. the unpacked QIIME2.tar.gz
Writes results/tables/*.tsv next to this script's parent folder.
"""
import csv, io, os, sys, zipfile

run = sys.argv[1]
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results", "tables")
os.makedirs(out, exist_ok=True)


def member(path, name):
    """Return the text of <uuid>/data/<name> inside a QIIME 2 archive."""
    with zipfile.ZipFile(os.path.join(run, path)) as z:
        for m in z.namelist():
            if m.split("/", 1)[-1] == f"data/{name}":
                return z.read(m).decode("utf-8")
    raise FileNotFoundError(f"{name} in {path}")


def save(fname, text, delim="\t"):
    rows = list(csv.reader(io.StringIO(text), delimiter=delim))
    with open(os.path.join(out, fname), "w", newline="", encoding="utf-8") as f:
        csv.writer(f, delimiter="\t", lineterminator="\n").writerows(rows)
    print(f"{fname}: {len(rows) - 1} rows")


# 1 Upstream: DADA2 denoising statistics (41 demo samples)
save("01_dada2_stats.tsv", member("Upstream/dada2-stats.qza", "stats.tsv"))
save("01_demux_per_sample_counts.tsv", member("Upstream/demultiplexed-sequences-summ.qzv", "per-sample-fastq-counts.tsv"))

# 2 Downstream: alpha diversity (observed features) Kruskal–Wallis
for col in ["autoFmtGroup", "categorical-time-relative-to-hct", "categorical-time-relative-to-fmt", "HCTSource", "Consistency"]:
    save(f"02_kruskal_{col}.tsv", member("Downstream/alpha-group-sig-obs-feats.qzv", f"kruskal-wallis-pairwise-{col}.csv"), ",")

# 3 Longitudinal: linear mixed-effects model
save("03_lme_model_results.tsv", member("Downstream/lme-obs-features-treatmentVScontrol.qzv", "model_results.tsv"))
save("03_lme_model_summary.tsv", member("Downstream/lme-obs-features-treatmentVScontrol.qzv", "model_summary.tsv"))

# 4 Random forest (feature volatility): accuracy + importance
save("04_rf_accuracy.tsv", member("Downstream/longitudinal-feature-volatility/accuracy_results.qzv", "predictive_accuracy.tsv"))
save("04_rf_feature_importance.tsv", member("Downstream/longitudinal-feature-volatility/feature_importance.qza", "importance.tsv"))

# 5 Beta diversity: proportion explained by PC1–PC3
rows = [["metric", "PC1", "PC2", "PC3"]]
for m in ["unweighted_unifrac", "weighted_unifrac", "bray_curtis", "jaccard"]:
    txt = member(f"Downstream/diversity-core-metrics-phylogenetic/{m}_pcoa_results.qza", "ordination.txt").splitlines()
    i = next(k for k, l in enumerate(txt) if l.startswith("Proportion explained"))
    vals = txt[i + 1].split("\t")[:3]
    rows.append([m] + [f"{float(v) * 100:.2f}%" for v in vals])
with open(os.path.join(out, "05_pcoa_proportion_explained.tsv"), "w", encoding="utf-8") as f:
    f.write("\n".join("\t".join(r) for r in rows) + "\n")
print("05_pcoa_proportion_explained.tsv:", rows[1:])

# 0 Filtering funnel: samples / ASVs / reads at every stage (needs h5py: the tables are BIOM v2.1 = HDF5)
try:
    import h5py

    def biom_stats(path):
        with zipfile.ZipFile(os.path.join(run, path)) as z:
            m = next(n for n in z.namelist() if n.endswith("data/feature-table.biom"))
            with h5py.File(io.BytesIO(z.read(m)), "r") as f:
                return f["sample/ids"].shape[0], f["observation/ids"].shape[0], int(round(f["sample/matrix/data"][:].sum()))

    stages = [
        ("upstream_dada2", "41 示範檢體 DADA2 去噪後（與下游不承接）", "Upstream/feature-table-0.qza"),
        ("0_raw", "FigShare 全部檢體（下游起點）", "Input_Data/feature-table.qza"),
        ("1_trial_cohort", "autoFmtGroup IS NOT NULL（納入隨機分組）", "Downstream/autofmt-table.qza"),
        ("2_time_window", "DayRelativeToNearestHCT BETWEEN -10 AND 70", "Downstream/filtered-table-1.qza"),
        ("3_prevalence", "--p-min-samples 2（剔除只出現在 1 個檢體的 ASV）", "Downstream/filtered-table-2.qza"),
        ("4_taxonomy", "保留 p__；排除 Chloroplast、Mitochondria", "Downstream/filtered-table-3.qza"),
        ("5_depth", "--p-min-frequency 10000（讀數不足的檢體剔除）", "Downstream/filtered-table-4.qza"),
    ]
    with open(os.path.join(out, "00_filtering_funnel.tsv"), "w", encoding="utf-8") as f:
        f.write("stage\tfilter\tsamples\tASVs\ttotal_reads\tsource\n")
        for st, desc, p in stages:
            s, o, t = biom_stats(p)
            f.write(f"{st}\t{desc}\t{s}\t{o}\t{t}\t{p}\n")
    print("00_filtering_funnel.tsv: 7 rows")
except ImportError:
    print("h5py not installed: skipped 00_filtering_funnel.tsv (pip install h5py)")
