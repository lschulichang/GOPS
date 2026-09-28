"""Dump the return-vs-iteration curve from a shipped tfevents file."""
import glob
import sys

from tensorboard.backend.event_processing.event_accumulator import EventAccumulator

path = sys.argv[1]
for f in glob.glob(path + "/events.out.tfevents.*"):
    ea = EventAccumulator(f, size_guidance={"scalars": 0})
    ea.Reload()
    tags = ea.Tags()["scalars"]
    print("FILE:", f)
    print("TAGS:", len(tags))
    for t in tags:
        print("   -", t)
    for t in tags:
        if t.startswith("Evaluation/1."):
            evs = ea.Scalars(t)
            print("\n=== %s (%d points) ===" % (t, len(evs)))
            for e in evs:
                print("  iter=%-8d return=%.2f" % (e.step, e.value))
