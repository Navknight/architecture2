#!/usr/bin/env python3

import argparse
import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# CONFIGURATION
# ============================================================

TRACES = ["Trace 1", "Trace 2", "Trace 3"]

# IPC values
DEFAULT_IPC  = [0.232204, 0.25113, 0.382061]
CUSTOM_1_IPC = [0.232075, 0.2519, 0.381743]
CUSTOM_2_IPC = [0.231919, 0.256176, 0.38201]

# Data MPKI values
DEFAULT_MPKI_DATA  = [7.34592, 8.53252, 2.8332]
CUSTOM_1_MPKI_DATA = [7.07956, 7.96284, 2.847]
CUSTOM_2_MPKI_DATA = [7.89972, 9.33364, 2.89248]

# Instruction MPKI values
DEFAULT_MPKI_INSTR  = [10.3843, 19.3908, 1.12584]
CUSTOM_1_MPKI_INSTR = [10.536, 18.3329, 1.19624]
CUSTOM_2_MPKI_INSTR = [9.87224, 14.1526, 1.00316]

# Policy labels
DEFAULT_LABEL  = "LRU"
CUSTOM_1_LABEL = "RRIP"
CUSTOM_2_LABEL = "IRRIP"

# Policy colours
# You can use names like "red", "blue", "green"
# or hex values like "#E74C3C"
DEFAULT_COLOR  = "#3498DB"
CUSTOM_1_COLOR = "#E74C3C"
CUSTOM_2_COLOR = "#2ECC71"

# Plot settings
BAR_WIDTH = 0.25
FIGURE_SIZE = (8, 5)
DPI = 300

# ============================================================
# ARGUMENT PARSING
# ============================================================

parser = argparse.ArgumentParser(
    description="Plot IPC and MPKI comparison graphs"
)

parser.add_argument(
    "--file",
    required=True,
    help="Base filename for output PNGs"
)

args = parser.parse_args()

filename = args.file.removesuffix(".png")

# ============================================================
# HELPER FUNCTION
# ============================================================

def plot_comparison(default, custom_1, custom_2,
                    ylabel, title, output,
                    dotted_line_at_one=False):

    x = np.arange(len(TRACES))

    fig, ax = plt.subplots(figsize=FIGURE_SIZE)

    ax.bar(
        x - BAR_WIDTH,
        default,
        BAR_WIDTH,
        label=DEFAULT_LABEL,
        color=DEFAULT_COLOR
    )

    ax.bar(
        x,
        custom_1,
        BAR_WIDTH,
        label=CUSTOM_1_LABEL,
        color=CUSTOM_1_COLOR
    )

    ax.bar(
        x + BAR_WIDTH,
        custom_2,
        BAR_WIDTH,
        label=CUSTOM_2_LABEL,
        color=CUSTOM_2_COLOR
    )

    if dotted_line_at_one:
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
# IPC NORMALIZED (SPEEDUP)
# ============================================================

default_ipc_normalized = np.ones(len(TRACES))
custom_1_ipc_normalized = np.array(CUSTOM_1_IPC) / np.array(DEFAULT_IPC)
custom_2_ipc_normalized = np.array(CUSTOM_2_IPC) / np.array(DEFAULT_IPC)

plot_comparison(
    default_ipc_normalized,
    custom_1_ipc_normalized,
    custom_2_ipc_normalized,
    ylabel="Normalized IPC",
    title="Normalized IPC Comparison",
    output=f"{filename}_IPC_Normalized.png",
    dotted_line_at_one=True
)

# ============================================================
# IPC RAW (NON-NORMALIZED)
# ============================================================

plot_comparison(
    DEFAULT_IPC,
    CUSTOM_1_IPC,
    CUSTOM_2_IPC,
    ylabel="IPC",
    title="Raw IPC Comparison",
    output=f"{filename}_IPC_Raw.png",
    dotted_line_at_one=False
)

# ============================================================
# TOTAL MPKI
# ============================================================

default_mpki_total = np.array(DEFAULT_MPKI_DATA) + np.array(DEFAULT_MPKI_INSTR)
custom_1_mpki_total = np.array(CUSTOM_1_MPKI_DATA) + np.array(CUSTOM_1_MPKI_INSTR)
custom_2_mpki_total = np.array(CUSTOM_2_MPKI_DATA) + np.array(CUSTOM_2_MPKI_INSTR)

plot_comparison(
    default_mpki_total,
    custom_1_mpki_total,
    custom_2_mpki_total,
    ylabel="Total MPKI",
    title="Total MPKI Comparison",
    output=f"{filename}_MPKI.png"
)

# ============================================================
# DATA MPKI
# ============================================================

plot_comparison(
    DEFAULT_MPKI_DATA,
    CUSTOM_1_MPKI_DATA,
    CUSTOM_2_MPKI_DATA,
    ylabel="Data MPKI",
    title="Data MPKI Comparison",
    output=f"{filename}_MPKI_Data.png"
)

# ============================================================
# INSTRUCTION MPKI
# ============================================================

plot_comparison(
    DEFAULT_MPKI_INSTR,
    CUSTOM_1_MPKI_INSTR,
    CUSTOM_2_MPKI_INSTR,
    ylabel="Instruction MPKI",
    title="Instruction MPKI Comparison",
    output=f"{filename}_MPKI_Instruction.png"
)
