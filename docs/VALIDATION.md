# Classroom Notebook Validation — October 26, 2026

**Result: PASS for all eight notebook execution workflows.** Six numerical tests passed. All nonempty code cells executed without notebook error outputs. The supplied source ZIP matched the local delivery at receipt. Its validated source snapshot is now frozen under `validation/2026-10-26/source/`. Every saved result notebook retains the exact source and notes of that snapshot. After validation, the working notebooks received navigation updates and had their `Course completion:` comment lines removed. The audit accounts for those comment removals when comparing the current code against the saved executions.

## Classroom execution and Colab revalidation

During the course, YQ-HA used the hosted Jupyter Notebook server to access the course data, run experiments, and execute the runnable code recorded in these notes, inspecting its outputs during class. The server was shut down after the course ended, so Google Colab was used to revalidate the repaired and completed notebooks during repository preparation.

The saved artifacts below document this later Colab validation on October 26, 2026, including post-course repairs and completions.

## Evidence checked

- Three ZIP archives passed CRC checks.
- All 44 source archive members match local files.
- CPU and GPU runtime source manifests match the supplied source ZIP.
- Each session input SHA-256 matches the corresponding repaired notebook.
- All notebook cells retain their source text, including classroom notes and repair explanations.
- 334 code cells comprise 306 executed nonempty cells and 28 blank cells, which were correctly skipped.
- All 36 PNG figures decoded and were inspected on contact sheets.
- All 19 CSV tables parsed and were nonempty; selected numerical columns were finite, mixture weights summed to one, and probe accuracies lay within [0, 1].
- Session 08 segment spans were contiguous and covered all 2,047 saved score positions.

## Session results

| Session | Notebook | Executed nonempty cells | Blank cells | Time (s) | Status |
|---|---|---:|---:|---:|---|
| 01 | Attempt 1.ipynb | 62 | 2 | 62.9 | Passed |
| 02 | Attempt2.ipynb | 13 | 1 | 36.41 | Passed |
| 03 | Attempt 3.ipynb | 12 | 1 | 64.98 | Passed |
| 04 | Notes on Attention and everything.ipynb | 50 | 3 | 286.25 | Passed |
| 05 | Attempt 4.ipynb | 52 | 2 | 54.74 | Passed |
| 06 | Attempt 5.ipynb | 44 | 5 | 40.38 | Passed |
| 07 | Attempt 6.ipynb | 35 | 1 | 860.28 | Passed |
| 08 | Attempt 7.ipynb | 38 | 13 | 178.26 | Passed |

## Environment and interpretation

Both runtimes used Python 3.13.16, NumPy 2.1.3, pandas 2.2.3, Transformers 4.57.6, and scikit-learn 1.6.1. PyTorch was 2.11.0+cpu in the CPU runtime and 2.11.0+cu130 in the GPU runtime. Session 08 recorded `cuda:0` and `torch.float16`; the runtime recorded a Tesla T4.

**Session 08 reasoning did not complete:** it generated 2,048 tokens and reached the generation budget. The analysis completed on the truncated trace, yielding 63 segments and three clusters. One cluster consists of a newline-only segment. These clusters should not be described as three established reasoning strategies.

Non-fatal messages include Hugging Face authentication notices, optional torchao/Triton notices on CPU, TensorFlow CUDA notices, shutdown callback exceptions, and joblib cleanup warnings. The recorded session commands returned zero, and no notebook error output was found. Dense multi-panel plot labels require viewing full-resolution files.

The outer executed validation companion was not among the uploaded files. The eight executed lesson notebooks, test logs, input hashes, and runtime inventories were present and sufficient for this audit.

The initial review did not modify the repository. The subsequent local integration imported the executions and logs, preserved both raw result ZIPs and a validated source snapshot, and updated status/navigation text. No local environment was installed and no model was rerun. The supplied cloud results are the runtime evidence. The source ZIP checksum and its 44-member inventory are retained without duplicating the large source ZIP. See [the evidence manifest](../validation/2026-10-26/manifest.json), [receipt review](../validation/2026-10-26/review-at-receipt.json), and [current audit](validation-report.json).

Run `python tools/check_validation.py --report docs/validation-report.json` to audit the preserved evidence and its correspondence to current computational cells and notes.
