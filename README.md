# SequenceWitness

SequenceWitness is a source-bound ordering primitive. It records a prescribed sequence, independently fetches two operational records, and seals only an `IN_ORDER` result. `OUT_OF_ORDER` and `INSUFFICIENT` remain correctable through one owner source replacement. Validators bind the exact verdict and full source digests.
