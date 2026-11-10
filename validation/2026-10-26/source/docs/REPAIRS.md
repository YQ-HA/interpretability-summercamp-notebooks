# Cell-Level Repair and Completion Record

Original cell numbers below are zero-based. Every original cell remains mapped in the main notebook, including blank cells and comments. `Repair:` explains an edit; `Course completion:` identifies a restored step. Plot export and data-path adjustments are uniform run support.

## Session 01: Attempt 1.ipynb

Course reference: `01_overview.md`.

- **repair**, original cell 8: Convert the integer explicitly before concatenating strings.
- **repair**, original cell 11: The original single-quoted string contained unescaped single quotes (SyntaxError).
- **repair**, original cell 28: Indent the print inside the nested if block.
- **repair**, original cell 37: Import math before its first use; the later import remains in the classroom sequence.
- **reorder**, original cell 56: Define output before inspecting it at original cells 54 and 55.
- **completion**, s01-course-completion-002: Set the seed before the classroom generation example.
- **completion**, s01-course-completion-003: Restore the course comparison of generation settings.

## Session 02: Attempt2.ipynb

Course reference: `02_inputs.md`.

- **repair**, original cell 2: Move the embedding tensor to CPU before NumPy conversion.
- **completion**, s02-course-completion-001: Restore batch tokenization and token identity; encode() is for one text, not a batch.
- **repair**, original cell 9: Seed the PCA projection for repeatable classroom plots.

## Session 03: Attempt 3.ipynb

Course reference: `03_attention.md`.

- **repair**, original cell 4: Seed randomized PCA; illustrative Q/K projections are distinct from learned model projections.
- **repair**, original cell 8: Clarify the original state slice while keeping the classroom note.
- **completion**, s03-course-completion-001: Restore the trajectory-distance comparison in the PCA projection.

## Session 04: Notes on Attention and everything.ipynb

Course reference: `04_outputs.md`.

- **repair**, original cell 21: Convert the raw greedy-decoding cell to executable code.
- **repair**, original cell 26: The top-p example reused top-k and contained an unreachable indented assignment.
- **repair**, original cell 26: Sample from the nucleus-filtered distribution in the top-p example.
- **repair**, original cell 13: Report exponential overflow explicitly and plot its finite values.
- **repair**, original cell 25: A logarithmic histogram requires positive probabilities; filtered-out zeros are not candidates.
- **repair**, original cell 32: Stop the original generation loop on EOS.
- **completion**, s04-course-completion-001: Qualify the determinism note for the greedy example.
- **completion**, s04-course-completion-002: Restore the temperature-distribution comparison.
- **completion**, s04-course-completion-003: Restore the temperature-distribution comparison.
- **completion**, s04-course-completion-004: Restore the temperature-distribution comparison.
- **completion**, s04-course-completion-005: Restore the course EOS stopping comparison.
- **completion**, s04-course-completion-006: Restore the course EOS stopping comparison.
- **completion**, s04-course-completion-007: Restore the course EOS stopping comparison.
- **completion**, s04-course-completion-008: Restore the course EOS stopping comparison.
- **completion**, s04-course-completion-009: Restore distribution statistics inline.
- **completion**, s04-course-completion-010: Restore sampling statistics and perplexity comparisons.
- **completion**, s04-course-completion-011: Restore sampling statistics and perplexity comparisons.
- **completion**, s04-course-completion-012: Restore sampling statistics and perplexity comparisons.
- **completion**, s04-course-completion-013: Restore sampling statistics and perplexity comparisons.
- **completion**, s04-course-completion-014: Restore sampling statistics and perplexity comparisons.
- **completion**, s04-course-completion-015: Restore sampling statistics and perplexity comparisons.
- **completion**, s04-course-completion-016: Restore sampling statistics and perplexity comparisons.
- **completion**, s04-course-completion-017: Restore sampling statistics and perplexity comparisons.
- **completion**, s04-course-completion-018: Restore sampling statistics and perplexity comparisons.

## Session 05: Attempt 4.ipynb

Course reference: `05_text.md`.

- **repair**, original cell 16: fit is a method of the classifier instance, not a standalone function.
- **repair**, original cell 18: Correct DataFrame capitalization and use parentheses for predict_proba.
- **repair**, original cell 14: Display a small slice while retaining the full sparse X for fitting.
- **completion**, s05-course-completion-001: Restore classifier evaluation with vocabulary fitted inside each cross-validation fold.
- **completion**, s05-course-completion-002: Restore classifier evaluation with vocabulary fitted inside each cross-validation fold.
- **completion**, s05-course-completion-003: Restore classifier evaluation with vocabulary fitted inside each cross-validation fold.
- **completion**, s05-course-completion-004: Restore the course token-distribution, weighted PMI, KL mixture, and residual steps.
- **completion**, s05-course-completion-005: Restore the course token-distribution, weighted PMI, KL mixture, and residual steps.
- **completion**, s05-course-completion-006: Restore the course token-distribution, weighted PMI, KL mixture, and residual steps.
- **completion**, s05-course-completion-007: Restore the course token-distribution, weighted PMI, KL mixture, and residual steps.
- **completion**, s05-course-completion-008: Restore the course token-distribution, weighted PMI, KL mixture, and residual steps.
- **completion**, s05-course-completion-009: Restore the course token-distribution, weighted PMI, KL mixture, and residual steps.
- **completion**, s05-course-completion-010: Restore the course token-distribution, weighted PMI, KL mixture, and residual steps.
- **completion**, s05-course-completion-011: Restore the course token-distribution, weighted PMI, KL mixture, and residual steps.
- **completion**, s05-course-completion-012: Restore the course token-distribution, weighted PMI, KL mixture, and residual steps.
- **completion**, s05-course-completion-013: Restore the course token-distribution, weighted PMI, KL mixture, and residual steps.
- **completion**, s05-course-completion-014: Restore the course token-distribution, weighted PMI, KL mixture, and residual steps.
- **completion**, s05-course-completion-015: Restore the course token-distribution, weighted PMI, KL mixture, and residual steps.
- **completion**, s05-course-completion-016: Restore the course token-distribution, weighted PMI, KL mixture, and residual steps.
- **completion**, s05-course-completion-017: Restore the course token-distribution, weighted PMI, KL mixture, and residual steps.
- **completion**, s05-course-completion-018: Restore the course token-distribution, weighted PMI, KL mixture, and residual steps.
- **completion**, s05-course-completion-019: Restore the course token-distribution, weighted PMI, KL mixture, and residual steps.
- **completion**, s05-course-completion-020: Restore the course token-distribution, weighted PMI, KL mixture, and residual steps.
- **completion**, s05-course-completion-021: Restore the course token-distribution, weighted PMI, KL mixture, and residual steps.
- **completion**, s05-course-completion-022: Restore the course token-distribution, weighted PMI, KL mixture, and residual steps.
- **completion**, s05-course-completion-023: Restore the course token-distribution, weighted PMI, KL mixture, and residual steps.
- **completion**, s05-course-completion-024: Restore the course token-distribution, weighted PMI, KL mixture, and residual steps.
- **completion**, s05-course-completion-025: Restore the course token-distribution, weighted PMI, KL mixture, and residual steps.
- **completion**, s05-course-completion-026: Restore the course token-distribution, weighted PMI, KL mixture, and residual steps.
- **completion**, s05-course-completion-027: Restore the course token-distribution, weighted PMI, KL mixture, and residual steps.
- **completion**, s05-course-completion-028: Restore the course token-distribution, weighted PMI, KL mixture, and residual steps.
- **completion**, s05-course-completion-029: Restore the course token-distribution, weighted PMI, KL mixture, and residual steps.
- **completion**, s05-course-completion-030: Restore the course token-distribution, weighted PMI, KL mixture, and residual steps.
- **completion**, s05-course-completion-031: Restore the course token-distribution, weighted PMI, KL mixture, and residual steps.
- **completion**, s05-course-completion-032: Restore the course token-distribution, weighted PMI, KL mixture, and residual steps.

## Session 06: Attempt 5.ipynb

Course reference: `06_attribution.md`.

- **completion**, s06-course-completion-001: Restore plotting constants before the first facet plot.
- **repair**, original cell 21: Use the LETTERS constant already defined in this cell.
- **repair**, original cell 15: Exclude words with no leave-one-genre-out comparison.
- **completion**, s06-course-completion-002: Restore layer-wise letter distribution, bias, and prediction-stability analysis.
- **completion**, s06-course-completion-003: Restore layer-wise letter distribution, bias, and prediction-stability analysis.
- **completion**, s06-course-completion-004: Restore layer-wise letter distribution, bias, and prediction-stability analysis.
- **completion**, s06-course-completion-005: Restore layer-wise letter distribution, bias, and prediction-stability analysis.
- **completion**, s06-course-completion-006: Restore layer-wise letter distribution, bias, and prediction-stability analysis.
- **completion**, s06-course-completion-007: Restore layer-wise letter distribution, bias, and prediction-stability analysis.
- **completion**, s06-course-completion-008: Restore layer-wise letter distribution, bias, and prediction-stability analysis.

## Session 07: Attempt 6.ipynb

Course reference: `07_metamodeling.md`.

- **repair**, original cell 22: Interpret classifier columns in the saved class order.
- **repair**, original cell 22: Align the head test examples by story ID rather than the last-token cache row order.
- **repair**, original cell 25: Match the capitalization of the dataset genre labels.
- **completion**, s07-course-completion-001: Restore sorted word-rank comparisons on the shared saved vocabulary.
- **completion**, s07-course-completion-002: Restore sorted word-rank comparisons on the shared saved vocabulary.
- **completion**, s07-course-completion-003: Restore sorted word-rank comparisons on the shared saved vocabulary.
- **completion**, s07-course-completion-004: Restore sorted word-rank comparisons on the shared saved vocabulary.
- **completion**, s07-course-completion-005: Restore sorted word-rank comparisons on the shared saved vocabulary.
- **completion**, s07-course-completion-006: Restore sorted word-rank comparisons on the shared saved vocabulary.
- **completion**, s07-course-completion-007: Restore sorted word-rank comparisons on the shared saved vocabulary.

## Session 08: Attempt 7.ipynb

Course reference: `08_reasoning.md`.

- **repair**, original cell 1: Use T4-compatible precision; the saved original run did not leave a usable model.
- **completion**, s08-course-completion-001: Restore generation, trace extraction, and predictive-state alignment before the coherence notes.
- **completion**, s08-course-completion-002: Restore generation, trace extraction, and predictive-state alignment before the coherence notes.
- **completion**, s08-course-completion-003: Restore generation, trace extraction, and predictive-state alignment before the coherence notes.
- **completion**, s08-course-completion-004: Restore generation, trace extraction, and predictive-state alignment before the coherence notes.
- **completion**, s08-course-completion-005: Restore generation, trace extraction, and predictive-state alignment before the coherence notes.
- **completion**, s08-course-completion-006: Restore generation, trace extraction, and predictive-state alignment before the coherence notes.
- **completion**, s08-course-completion-007: Restore generation, trace extraction, and predictive-state alignment before the coherence notes.
- **completion**, s08-course-completion-008: Restore generation, trace extraction, and predictive-state alignment before the coherence notes.
- **completion**, s08-course-completion-009: Restore generation, trace extraction, and predictive-state alignment before the coherence notes.
- **completion**, s08-course-completion-010: Restore generation, trace extraction, and predictive-state alignment before the coherence notes.
- **completion**, s08-course-completion-011: Restore generation, trace extraction, and predictive-state alignment before the coherence notes.
- **completion**, s08-course-completion-012: Restore generation, trace extraction, and predictive-state alignment before the coherence notes.
- **completion**, s08-course-completion-013: Restore the coherence-length implementation inline.
- **completion**, s08-course-completion-014: Restore coherence-window estimation and its plot.
- **completion**, s08-course-completion-015: Restore coherence-window estimation and its plot.
- **completion**, s08-course-completion-016: Restore scoring functions after the original scoring note.
- **completion**, s08-course-completion-017: Restore boundary detection and trace segmentation.
- **completion**, s08-course-completion-018: Restore boundary detection and trace segmentation.
- **completion**, s08-course-completion-019: Restore boundary detection and trace segmentation.
- **completion**, s08-course-completion-020: Restore boundary detection and trace segmentation.
- **completion**, s08-course-completion-021: Restore boundary detection and trace segmentation.
- **completion**, s08-course-completion-022: Restore boundary detection and trace segmentation.
- **completion**, s08-course-completion-023: Restore mean-pooling for each segment inline.
- **completion**, s08-course-completion-024: Restore segment clustering and inspection.
- **completion**, s08-course-completion-025: Restore segment clustering and inspection.
- **completion**, s08-course-completion-026: Restore segment clustering and inspection.
- **completion**, s08-course-completion-027: Restore segment clustering and inspection.
- **completion**, s08-course-completion-028: Restore segment clustering and inspection.
- **completion**, s08-course-completion-029: Restore segment clustering and inspection.
- **completion**, s08-course-completion-030: Restore segment clustering and inspection.
- **completion**, s08-course-completion-031: Save trace completion, model device, and precision with the analysis.
