"""Time per-iteration cost of the default (unshortened) FHADP idpendulum config.

Patches start_tensorboard to a no-op so the benchmark does not kill port 6006
or spawn a detached cmd window.
"""
import runpy
import sys

sys.path.insert(0, r"E:\GOPS")

import gops.utils.tensorboard_setup as tbs

tbs.start_tensorboard = lambda *a, **k: None

EXAMPLE = r"E:\GOPS\example_train\fhadp\fhadp_mlp_idpendulum_serial.py"
SAVE = r"E:\GOPS\results\timing_bench"

sys.argv = [
    "bench",
    "--enable_cuda", "True",
    "--max_iteration", "5",
    "--log_save_interval", "1",
    "--save_folder", SAVE,
    "--eval_interval", "100000",        # skip eval for the probe
    "--apprfunc_save_interval", "100000",
]

runpy.run_path(EXAMPLE, run_name="__main__")
