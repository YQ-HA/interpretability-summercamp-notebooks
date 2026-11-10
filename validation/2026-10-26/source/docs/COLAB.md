# Fresh Colab Validation

Use the new `Classroom_Colab_Validation.ipynb` and full `interpretability-classroom-notebooks.zip`. Keep the earlier reconstructed-labs files separate.

1. File → Upload notebook: select the new companion. Choose a CPU runtime and connect.
2. Files sidebar → upload the complete new ZIP. Wait for the upload to finish.
3. Run A: Python must be 3.12–3.14; seven data files should be listed.
4. Run B to install requirements in the cloud. If asked to restart the Python session, do so and continue at C.
5. Run C to create log helpers and record actual imported package versions and source hashes.
6. Run D: integrity must pass, then six numerical tests should report OK.
7. Run E (sessions 05–06), F (07), and G (01–04). Every session must print `Saved executed notebook`. Run H at any milestone or error to download all available results.
8. Download CPU results before changing runtimes. Select T4 GPU and connect. On a fresh VM re-upload the new ZIP and repeat A–C; otherwise restore helpers with C.
9. Run I for session 08, then H to download GPU results. Save the executed companion using File → Download → Download .ipynb.
10. Return both result ZIPs and the executed companion for review. After downloads, disconnect and delete the GPU runtime.

Do not re-extract A over an ongoing run or rerun completed sessions after a later failure; use `run_lab(N)` for the failed session and remaining sessions. On an error the runner saves `FAILED-...ipynb` to preserve partial outputs. The command record and the successful executed notebook determine completion, not the existence of a partial figure.

Session 08 checks for CUDA, uses float16 and a 2,048-token generation budget, and records whether reasoning actually completed in `trace_status.json`. A truncated trace can still be analyzed, but is not a completed reasoning answer. Free GPU availability depends on the account's allocation; CPU sessions can be retained while GPU execution is pending.

No local course environment is required. The new run will establish runtime status for these repaired attempts. The numerical tests, model APIs, and all eight notebook executions remain to be confirmed in Colab.
