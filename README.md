# honeyslop - code canaries to quickly triage hallucinated ("slop") vulnerability reports

honeyslop is code canaries, or decoys, for open-source projects  
drowning in AI-hallucinated ("slop") and unverified vulnerability  
reports. A slop scanner ingests the canary, then generates  
a vulnerability "report" based on it. The report self-identifies  
as slop. Close it in one grep.

This is a quick PoC, vibe-coded as a joke (not production-grade),  
because we recieved a slop report to raptor, ourselves.  
Should be fun!

Code canaries extend familiar triage signals (i.e. detections in test
files, example secrets, non-existent paths) into deliberate markers,
or decoys.

In tests, these canaries work well enough to pinpoint slop, but they  
can be further improved (embedded in real code, function/file/directory  
names less indicative, regularly regenerated as new code, etc.).

Written by: Gadi Evron (@gadievron)
Named by: Michal Kamensky (@kamenskymic).

## Use at your own risk

If you paste this into production, that's a you problem.

**See DISCLAIMER below.**

## Triage rules to automatically disqualify slop reports

For each incoming report, in order:

1. grep canary UUID in the report → close.
2. grep canary-only function names (`zqx_slopsig_quarnish`,
  `_validate_pep_440_plus`, `handle_*_request`) → close.
3. grep `CVE-2025-99919` (fake) → close.
4. Cited file path under `canaries/` → close.
5. Cited function doesn't exist in the tree → "does not exist."
6. For memcpy/bounds claims on B/D: ask the reporter to walk through how
   their PoC defeats the specific guard on the cited line. AI follow-ups
   cannot answer; humans can.

## Canary types

| Type               | What it does                                                                          | Stages           |
| ------------------ | ------------------------------------------------------------------------------------- | ---------------- |
| **SCANNER-FLAG**   | Trips scanners so slop reports pile up on canary                                        | A, B, C, D, E    |
| **RESOURCE-WASTE** | Potentially runs agentic LLM scanners through their full iteration budget at max cost | F + G (together) |


## Stages

| Stage   | File(s)                                       | Shape that fools                                                                                                                                                  | Defense against execution                                                                                                                                                 |
| ------- | --------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **A**   | `ready/python/slop_canary.py`                 | 15 textbook CWE sinks (eval/exec/shell/SQL/pickle/yaml/verify=False/md5/XXE/JWT none/etc.) + fake AWS/GH/Slack/Stripe secrets + shibboleth `zqx_slopsig_quarnish` | 5 layers (see below)                                                                                                                                                      |
| **B**   | `ready/c/slop_canary.c`                       | 4 memcpy/memmove shapes scanners flag as CWE-120/121/787/170                                                                                                      | Shapes bounded by construction (Static_assert, clamps, truncation, memmove semantics); file never linked                                                                  |
| **C**   | merged into A                                 | Extended CWE yield                                                                                                                                                | Same as A                                                                                                                                                                 |
| **D**   | `ready/c/canary_heartbeat.c` + `canary_sat.h` | Heartbleed silhouette: `uint16_t payload_len` → `malloc(1+2+payload_len+16)` → `memcpy`                                                                           | Distributed `sat_sub` bounds, cached frame fields (closes TOCTOU + signal-handler UB), NULL checks, `SIZE_MAX - 19 >= UINT16_MAX` assert, `payload_len > 0` short-circuit |
| **E**   | `ready/python/regex_validator.py`             | Catastrophic-backtrack regex `^(([a-z]+)+)+@example\.com$` + fake **CVE-2025-99919**                                                                              | 5 layers + regex stored as string literal only (no module-level `re.compile`)                                                                                             |
| **F+G** | `private/fractal_dag/` (12 nodes)             | Cross-referenced DAG of `handle_*_request(req)` entry points with Stage-1 `vulnerable`-shaped sinks                                                               | 5 layers per node + cross-refs only in docstrings, never `from .node_XX import`                                                                                           |


## Watch out for...

**Bucket 1 - your own tools trip.** Your scanners, linters, IDE, and  
secret-scanning will fire on the canary. This is the intended behaviour for  
*incoming* scans but means **your own pipelines** need to skip these paths.
Required: exclude `canaries/`** from every SAST config (CodeQL
`paths-ignore`, `.semgrepignore`, `bandit -x canaries`, Ruff
`--extend-exclude`, `.clang-format-ignore`, editor LSP), exclude from
published artefacts (`MANIFEST.in prune`, `.dockerignore`, wheel
excludes), allowlist the fake secrets (`AKIAIOSFODNN7EXAMPLE`, fake
`ghp_`/`xoxb-`/`sk_live_`) in your secret scanner. Warn contributors not
to "clean up" the honeypot. Watch for linter removal of the `if False:`
as a tripwire, and insertion of `# noqa`/`# nosec`.

**Bucket 2 - effectiveness erosion.** Public canaries enter LLM training  
corpora over 6–18 months and scanner vendors add skip-heuristics. Rotate  
UUIDs / banner / shibboleth / fake-CVE annually (see `ROTATE_UUID.md`);
vary wording across adopters; keep F+G private. It won't stop the models
from learning the code, but might buy you some time.

**Bucket 3 - post-compromise.** If an attacker already has access they can  
do whatever they want, and don't need honeyslop. However, flipping  
`if False:` → `if True:`, inserting Unicode/BIDI tricks, or adding  
prompt-injection text in docstrings turns canary live, where you may not  
expect it to be, would certainly be interesting to watch for, if unlikely.

## How to try

1. **Pick stages.** C/C++ parser surface → D (+ B). Python OSS maintainer
  → A + E. Under sustained agentic scanner spam → add F + G privately.
2. **Rotate every UUID.** Distinct per adopter, not prefix variants of
  one base. See `ROTATE_UUID.md`.
3. **Exclude from build artefacts.** Python: `MANIFEST.in prune canaries`
  or `pyproject.toml tool.setuptools.exclude-package-data`. C: omit from
   `CMakeLists.txt` / `Makefile` / sdist. Docker: `.dockerignore`.
4. **Exclude from CI static analysis.** Otherwise your own CI produces
  findings on the canary. CodeQL `paths-ignore: [canaries/**]`,
   `.semgrepignore` add `canaries/`, `bandit -x canaries`, Ruff
   `--extend-exclude canaries/`**.
5. **Consider adding the triage rule to `SECURITY.md`** —
  see `SECURITY.md.template`. This could alert slop scanners to the
   canary. (maybe a good thing?)
6. **Protect from contributor cleanup.** `CODEOWNERS` on the canary
  files; a pre-commit hook that fails if the canary UUID count decreases
   or if `if False:` tripwires go missing.
7. **Remove obvious "tells".** Replace code comments, directory, file,
and function names with "canary", "canaries", "honeypot", "decoy", "fake",
or "slop".

We've added some examples as to how we might do it, but feel free to share the ones that worked for you. 

## DISCLAIMER

This project is provided "as is", without warranty of any kind, express or
implied, including but not limited to the warranties of merchantability,
fitness for a particular purpose, and noninfringement. In no event shall the
authors or contributors be liable for any claim, damages, or other liability,
whether in an action of contract, tort, or otherwise, arising from, out of, or
in connection with the software or the use or other dealings in the software.

**Warning:** This project contains code that appears vulnerable, and should be
assumed to be so. That is its function. Some of it works by being costly to
analyze - assume this code will consume significant computing resources when
executed or inspected, depending on the canary. Do not run, deploy, or adapt
any of it in a real environment.

## License

Licensed under MIT. See LICENSE.
