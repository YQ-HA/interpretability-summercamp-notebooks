# Interpretability Classroom Notebooks

**Student implementer and maintainer: YQ-HA.** These are my instructor-led classroom notebooks for Tyler Shoemaker's [Introduction to Interpretability for Language Models](https://digitaltheorylab.github.io/2026_interpretability-reader/) at Digital Theory Lab, followed by post-course completions and maintenance. During class I typed, ran, and adapted code while following the instructor. Missing or erroneous cells reflect an incomplete live record of those sessions.

The original classroom work used the course's hosted Jupyter Notebook server for data access and experiments. During class, I executed the runnable code recorded in these notes and inspected its outputs there. The Jupyter server was shut down after the course ended, so I used Google Colab to validate the repaired and completed notebooks while preparing this repository.

The main files below repair those same attempts, retaining original cells, comments, and `##` notes. Methods remain implemented inline. Course designs and reference implementations are credited to the instructor. OpenAI Codex assisted with locating and explaining errors, restoring omitted code, and checking course coverage and runnability. See [authorship](docs/AUTHORSHIP.md) and the [cell-level repair record](docs/REPAIRS.md).

**Validated in Google Colab on October 26, 2026:** all eight repaired classroom notebooks completed, and all six numerical tests passed. The 334 code cells comprise 306 executed nonempty cells and 28 blank cells. The saved run contains 36 figures and 19 CSV tables. See [executed results](results/README.md), the [validation report](docs/VALIDATION.md), and the [preserved evidence](validation/2026-10-26/manifest.json).

Session 08 ran on Tesla T4 with float16. Its analysis completed on a reasoning trace truncated at the 2,048-token generation limit. The working notebooks retain the validated code and original classroom notes. Later edits updated the navigation text and removed labels from restored code.

| Session | Main classroom notebook | Topic |
|---|---|---|
| 01 | [Attempt 1.ipynb](<notebooks/Attempt 1.ipynb>) | Python and Text Generation |
| 02 | [Attempt2.ipynb](<notebooks/Attempt2.ipynb>) | Tokenization and Embeddings |
| 03 | [Attempt 3.ipynb](<notebooks/Attempt 3.ipynb>) | Attention and Hidden States |
| 04 | [Notes on Attention and everything.ipynb](<notebooks/Notes on Attention and everything.ipynb>) | Sampling and Generation |
| 05 | [Attempt 4.ipynb](<notebooks/Attempt 4.ipynb>) | Generated Text as Data |
| 06 | [Attempt 5.ipynb](<notebooks/Attempt 5.ipynb>) | Attribution and Logit Lens |
| 07 | [Attempt 6.ipynb](<notebooks/Attempt 6.ipynb>) | Linear Probes and Metamodeling |
| 08 | [Attempt 7.ipynb](<notebooks/Attempt 7.ipynb>) | Reasoning Trajectories |

## Run in Colab

Upload [Classroom_Colab_Validation.ipynb](validation/Classroom_Colab_Validation.ipynb) as a notebook, then upload the full `interpretability-classroom-notebooks.zip` through the Files sidebar. Run A–E on CPU, then F and G, and download H. Switch to T4 GPU, repeat setup A–C if needed, execute I for session 08, and download H again. Detailed [steps and checkpoints](docs/COLAB.md) are included.

## Run in an installed environment

Use Python 3.12–3.14. From the repository root:

```text
python -m pip install -r requirements.txt
python -m ipykernel install --user --name python3 --display-name "Classroom Attempts"
python tools/check_integrity.py --require-data
python tools/check_validation.py
python -m unittest discover -s tests -v
python tools/run_notebook.py --session 5
```

Use `--session 1` through `8` for the other rows. The runner starts a fresh kernel in `notebooks/`; all methods are visible there. Completed and failed executed notebooks, figures, tables, runtime versions, and input hashes go to `results/session-XX/`. To open one directly in JupyterLab, start its kernel in the `notebooks` directory.

## Records and data

The nine original notebooks and classroom workspace README remain unchanged under `archive/classroom-raw/`. Both identical Attention notes copies are preserved there; the main sequence uses the copy without `(1)`. The seven course data files are included in the local ZIP and described by `data/manifest.json`; Git tracks that manifest rather than the binaries. Supplied gradients, states, and classifier artifacts remain course data. No large-model data reconstruction is required.

The standard-library checker verifies archive/data hashes, comment preservation, original-cell mapping, syntax, names, and document links. Six numerical checks extract actual function definitions from these notebooks without loading a language model; all six passed in the saved Colab run. The repair manifest records restored blocks and edits rather than claiming every completed cell was present during class.

See also [course coverage](docs/COURSE_MAP.md) and [static inspection](docs/STATIC_CHECKS.md).
