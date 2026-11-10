# Static Checks — October 22, 2026

Result: PASS. Eight repaired classroom notebooks contain 334 code cells. All 10 archived input files and seven data files match their recorded SHA-256 hashes. The main notebooks retain 233 original full-line comments, including all four `##`/`###` note lines; original cell lineage is retained, with the generation cell moved before its first use in Attempt 1.

Checks cover Python syntax, sequential top-level names, function global references, clear execution outputs, original-cell IDs, preserved comments, file hashes, the clean validation companion, and local document links. Six numerical tests are provided but have not been run locally. No local scientific dependencies were installed, and no model or repaired notebook was executed.

```text
python tools/check_integrity.py --require-data --report docs/static-report.json
```

The previous repository's cloud runs are separate historical evidence. This repository awaits fresh Colab execution. See [the Colab guide](COLAB.md), [coverage](COURSE_MAP.md), and [authorship](AUTHORSHIP.md).
