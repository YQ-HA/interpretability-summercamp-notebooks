# Executed Classroom Notebooks

YQ-HA ran these repaired attempts in Google Colab on October 26, 2026. Every nonempty code cell completed without notebook error outputs. Files were imported without changing their contents.

| Session | Executed notebook | Executed nonempty cells | Blank cells | Command time (s) |
|---|---|---:|---:|---:|
| 01 | [Attempt 1.ipynb](<session-01/Attempt 1.ipynb>) | 62 | 2 | 62.9 |
| 02 | [Attempt2.ipynb](<session-02/Attempt2.ipynb>) | 13 | 1 | 36.41 |
| 03 | [Attempt 3.ipynb](<session-03/Attempt 3.ipynb>) | 12 | 1 | 64.98 |
| 04 | [Notes on Attention and everything.ipynb](<session-04/Notes on Attention and everything.ipynb>) | 50 | 3 | 286.25 |
| 05 | [Attempt 4.ipynb](<session-05/Attempt 4.ipynb>) | 52 | 2 | 54.74 |
| 06 | [Attempt 5.ipynb](<session-06/Attempt 5.ipynb>) | 44 | 5 | 40.38 |
| 07 | [Attempt 6.ipynb](<session-07/Attempt 6.ipynb>) | 35 | 1 | 860.28 |
| 08 | [Attempt 7.ipynb](<session-08/Attempt 7.ipynb>) | 38 | 13 | 178.26 |

The run contains 36 PNG figures and 19 CSV tables. Sessions 01–07 used CPU; session 08 used Tesla T4, `cuda:0`, and float16. The latter generated 2,048 tokens, then analyzed its truncated reasoning trace. It did not finish reasoning.

CPU and GPU logs are kept separately under `validation/cpu/` and `validation/gpu/`. Each session includes the input source hash and imported-library versions. The original result archives and validated source snapshot are retained under `../validation/2026-10-26/`. Timings include startup/download work and are not benchmarks.

See [the validation report](../docs/VALIDATION.md). Re-running a notebook overwrites its session outputs; the archived ZIPs preserve this reference run.
