#!/bin/bash
B=$(ls bin/*-1core-"$1")
for t in 1 2 3; do
  "$B" -warmup_instructions 25000000 -simulation_instructions 25000000 -traces Trace$t.x.y.gz > results/$1_T$t.txt &
done
wait
