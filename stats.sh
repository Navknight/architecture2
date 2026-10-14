#!/bin/bash
for n in "$@"; do for f in results/${n}_T*.txt; do
  ipc=$(grep -m1 "CPU 0 cumulative IPC" "$f" | awk '{print $5}')
  lm=$(grep -m1 "^L1D LOAD" "$f" | awk '{print $8}')
  mpki=$(grep -m1 "^L1D LOAD" "$f" | awk '{print $8/25000}')
  pf=$(grep -m1 "^L1D PREFETCH  REQUESTED" "$f")
  echo "$f IPC=$ipc L1D_load_miss=$lm MPKI=$mpki | $pf"
done; done
