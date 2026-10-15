#!/usr/bin/env python3

import argparse
import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# CONFIGURATION
# ============================================================

TRACES = ["Trace 1", "Trace 2", "Trace 3"]

# Original LRU baseline (normalization only)
BASELINE_IPC = [0.232204, 0.25113, 0.382061]

# Policy labels
POLICY_LABELS = [
    "128 Eq",
    "144 Eq",
    "144 Uneq",
    "160 Eq",
    "160 Uneq"
]

# Policy colours (named colours or HEX)
POLICY_COLORS = [
    "#3498DB",
    "#E74C3C",
    "#2ECC71",
    "#9B59B6",
    "#F39C12"
]

# ============================================================
# IPC VALUES
# Each row represents one policy.
# Each column represents Trace 1, Trace 2, Trace 3.
# ============================================================

IPC = np.array([
    [0.232017, 0.254853, 0.381977],  # 128 Eq
    [0.232017, 0.255009, 0.381977],  # 144 Eq
    [0.232022, 0.254961, 0.381952],  # 144 Uneq
    [0.232017, 0.255138, 0.381977],  # 160 Eq
    [0.232022, 0.254923, 0.381952],  # 160 Uneq
])

# ============================================================
# L2 TOTAL MPKI
# Extracted directly from "L2C TOTAL ... MPKI"
# ============================================================

L2_MPKI = np.array([
    [25.02890, 31.44240, 6.38592],  # 128 Eq
    [25.02890, 31.38440, 6.38592],  # 144 Eq
    [25.02890, 31.50170, 6.38328],  # 144 Uneq
    [25.02890, 31.37220, 6.38592],  # 160 Eq
    [25.02890, 31.50690, 6.38328],  # 160 Uneq
])

# ============================================================
# L2 DATA LOAD MPKI
# ============================================================

L2_MPKI_DATA = np.array([
    [7.72744, 8.68876, 2.88812],  # 128 Eq
    [7.72744, 8.71804, 2.88812],  # 144 Eq
    [7.72288, 8.77312, 2.88864],  # 144 Uneq
    [7.72744, 8.75168, 2.88812],  # 160 Eq
    [7.72288, 8.76404, 2.88864],  # 160 Uneq
])

# ============================================================
# L2 INSTRUCTION LOAD MPKI
# ============================================================

L2_MPKI_INSTR = np.array([
    [9.99344, 15.76220, 1.05296],  # 128 Eq
    [9.99344, 15.62630, 1.05296],  # 144 Eq
    [9.99448, 15.60270, 1.05424],  # 144 Uneq
    [9.99344, 15.53580, 1.05296],  # 160 Eq
    [9.99448, 15.63120, 1.05424],  # 160 Uneq
])

# ============================================================
# PLOT SETTINGS
# ============================================================

BAR_WIDTH = 0.15
FIGURE_SIZE = (10, 5)
DPI = 300

# ============================================================
# ARGUMENT PARSING
# ============================================================

parser = argparse.ArgumentParser(
    description="Generate DRRIP IPC and L2 MPKI graphs"
)

parser.add_argument(
    "--file",
    required=True,
    help="Base filename for output PNGs"
)

args = parser.parse_args()

filename = args.file.removesuffix(".png")

# ============================================================
# PLOTTING FUNCTION
# ============================================================

def plot_comparison(data, ylabel, title, output, normalized=False):

    x = np.arange(len(TRACES))

    fig, ax = plt.subplots(figsize=FIGURE_SIZE)

    num_policies = len(POLICY_LABELS)
    center = (num_policies - 1) / 2

    for i in range(num_policies):

        offset = (i - center) * BAR_WIDTH

        ax.bar(
            x + offset,
            data[i],
            BAR_WIDTH,
            label=POLICY_LABELS[i],
            color=POLICY_COLORS[i]
        )

    # Reference line for normalized IPC
    if normalized:
        ax.axhline(
            y=1.0,
            color="black",
            linestyle=":",
            linewidth=1.5
        )

    ax.set_xlabel("Traces")
    ax.set_ylabel(ylabel)
    ax.set_title(title)

    ax.set_xticks(x)
    ax.set_xticklabels(TRACES)

    ax.legend()
    ax.grid(axis="y", linestyle="--", alpha=0.3)
    ax.set_axisbelow(True)
    ax.set_ylim(bottom=0)

    plt.tight_layout()
    plt.savefig(output, dpi=DPI)
    plt.close()

    print(f"Saved: {output}")

# ============================================================
# NORMALIZE IPC
# ============================================================

IPC_NORMALIZED = IPC / np.array(BASELINE_IPC)

# ============================================================
# GENERATE RAW IPC
# ============================================================

plot_comparison(
    IPC,
    ylabel="IPC",
    title="IPC Comparison",
    output=f"{filename}_IPC.png"
)

# ============================================================
# GENERATE NORMALIZED IPC
# ============================================================

plot_comparison(
    IPC_NORMALIZED,
    ylabel="Normalized IPC",
    title="Normalized IPC Comparison",
    output=f"{filename}_IPC_Normalized.png",
    normalized=True
)

# ============================================================
# GENERATE TOTAL L2 MPKI
# ============================================================

plot_comparison(
    L2_MPKI,
    ylabel="L2 MPKI",
    title="L2 MPKI Comparison",
    output=f"{filename}_L2_MPKI.png"
)

# ============================================================
# GENERATE L2 DATA MPKI
# ============================================================

plot_comparison(
    L2_MPKI_DATA,
    ylabel="L2 Data MPKI",
    title="L2 Data MPKI Comparison",
    output=f"{filename}_L2_MPKI_Data.png"
)

# ============================================================
# GENERATE L2 INSTRUCTION MPKI
# ============================================================

plot_comparison(
    L2_MPKI_INSTR,
    ylabel="L2 Instruction MPKI",
    title="L2 Instruction MPKI Comparison",
    output=f"{filename}_L2_MPKI_Instruction.png"
)
