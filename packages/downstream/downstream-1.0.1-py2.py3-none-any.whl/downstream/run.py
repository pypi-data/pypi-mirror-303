from itertools import repeat
import json
import multiprocessing as mp
import subprocess


def run_external_script_batch(args):
    batch, executable = args
    cmd = [executable, "--batch"] + [
        item for s, t in batch for item in ["-S", str(s), "-T", str(t)]
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise ValueError(result.stderr)
    if not result.stdout:
        raise ValueError("No output from script")
    return json.loads(result.stdout)


def run_external_script_parallel(test_cases, executable, batch_size=500):
    batches = [
        test_cases[i : i + batch_size]
        for i in range(0, len(test_cases), batch_size)
    ]
    with mp.Pool(processes=mp.cpu_count()) as pool:
        results = pool.map(
            run_external_script_batch, zip(batches, repeat(executable))
        )
    return {k: v for d in results for k, v in d.items()}
