# GC-II Status Delta — Audit 024

- Reachable-label future signature as complete whole-envelope invariant: **FALSIFIED**.
- Counterexample: two same-labelled states have identical reachable-label sets at every horizon but different enabled action identities and therefore different prescribed operational capabilities.
- Endpoint-only reversibility insufficiency: remains **PROVED finite falsification**, but the existing `future_label_signature` helper is now explicitly only a weak diagnostic, not a whole-envelope equivalence test.
- Trace/future-capability reversibility invariant: **OPEN**; must preserve relevant action-labelled, cost/budget and task-scale-error semantics.
- Breakthrough status: **NONE YET**.
- Evidence: `FUTURE_LABEL_SIGNATURE_INCOMPLETENESS_AUDIT_024.md` and `tests/test_gc2_future_signature_incompleteness.py`.
