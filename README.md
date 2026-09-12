# SequenceWitness

> **CONTROL ROOM / ORDER VERIFICATION** · The order is the evidence.

SequenceWitness is a source-bound ordering primitive. It records a prescribed sequence, independently fetches two operational records, and seals only an `IN_ORDER` result. `OUT_OF_ORDER` and `INSUFFICIENT` remain correctable through one owner source replacement. Validators bind the exact verdict and full source digests.

## Console sequence

`register_sequence` freezes ordered steps plus two distinct public records. `verify_sequence` asks validators whether the records support the exact ordering. Only `IN_ORDER` seals the sequence. `OUT_OF_ORDER` and `INSUFFICIENT` expose the failed evidence indexes and open a one-time owner correction path rather than silently overwriting the record.

This fits operational runbooks, release sequencing, and compliance handoffs where the order itself matters. It is not a general evidence classifier: its stored decision is specifically whether the prescribed sequence was respected.

## Console interlocks

The contract rejects duplicate IDs, same-host sources, malformed records, replayed correction, and leader results with altered verdicts or digests. Call `get_sequence(id)` to inspect the original steps, result, and evidence attribution.

StudioNet: [`0x50CA0f6831d9b9f15740e7cA922E6b09ef6b5896`](https://explorer-studio.genlayer.com/address/0x50CA0f6831d9b9f15740e7cA922E6b09ef6b5896)
