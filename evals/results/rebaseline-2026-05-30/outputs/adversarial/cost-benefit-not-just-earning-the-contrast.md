Verdict: keep
Slop tells: "Not just X" is a banned-by-default cadence, so it triggers a first look. The doctrine carves out an exception: keep when it is the exact point. Here it is.
Specificity missing: None. The sentence names the category shift (latency optimization to failure model) and the concrete behavior change that earns it ("the request now completes locally even when the central service is down").
Inflated claim: None. "Changes the failure model" would be inflation if it stood alone, but the because-clause supplies the mechanism: local completion under central-service outage. That is a real availability-category shift, not a latency tweak dressed up.
Flow break: None. The semicolon and the because-clause make the relation explicit (category shift, then cause). This is hypotaxis doing its job — the secondary idea (latency) is subordinated to the primary one (failure model).
Concrete rewrite: No rewrite. Keep as-is. The "not just" earns its place because both sides — the latency framing and the availability framing — are discharged in the same sentence.
Rewrite check: passes self-detectors — no rewrite proposed; the original "not just" passes the editing-pass step 4 exception ("unless it is the exact point").
Remembered line: "the request now completes locally even when the central service is down."
