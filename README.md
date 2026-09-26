---
title: Amoebanator
colorFrom: blue
colorTo: blue
sdk: docker
app_port: 8501
tags:
- streamlit
pinned: false
short_description: Abstention-aware PAM triage demo (synthetic data)
license: mit
---

# Amoebanator

Amoebanator is a research codebase for a triage signal for primary amoebic
meningoencephalitis (PAM), a rare CNS infection caused by *Naegleria fowleri* that
is almost always fatal. It is a small PyTorch classifier trained on 30 synthetic rows
(24 for training, 6 for validation), served as a Streamlit demo.

- **Abstention.** The model returns High, Low or ABSTAIN. It abstains when either of
  two out-of-distribution gates flags the input, or when the split conformal
  prediction set is empty or holds both classes.
- **Out-of-distribution gates.** A Mahalanobis distance on the seven non-symptom
  inputs, and an energy score on the temperature-scaled logits.
- **Temperature scaling.** The raw logits already separate the six validation rows
  perfectly, so the temperature is not identifiable. The fit leaves T at essentially
  1.0, and the probabilities shown are the model's own softmax outputs.
- **Vignette registry.** A registry of 138 meningoencephalitis vignettes (60 PAM, 78
  across five other diagnostic classes), each anchored to published literature, is
  kept under `data/vignettes/`. Neither the classifier nor the app reads it. Its
  adjudication fields (adjudicator IDs, Cohen's kappa, inclusion decision) are
  placeholders set by the generator script; no physician adjudication is recorded
  (`ml/schemas/SCHEMA_README.md` Section 1).

> **For research and educational use.** Not a cleared medical device, not a substitute
> for clinical judgment, and not clinically validated.

## Limitations

The most important limitation of this demo as a must-not-miss triage tool:
run through the full pipeline, 18 of the 30 bundled rows abstain, including 8
of the 11 High rows (6 at the logit-energy gate, 2 at the Mahalanobis gate).
Only 3 High rows get a High label, and none gets a Low label. These are the
rows the model was built from (24 of them are its training rows), so the
abstention stack declines on most of the cases it exists to catch
(`outputs/metrics/bundled_outcomes.json`; `docs/model_card.md`, top and
Section 9).

## Scope and status

Amoebanator is a clinical-ML infrastructure project for CNS-infection triage, using
primary amoebic meningoencephalitis (Naegleria fowleri) as a high-risk must-not-miss
example. This release, V1.1, demonstrates the engineering stack: temperature scaling,
split conformal prediction with selective abstention, OOD detection, and reproducible
training and evaluation. The classifier is trained and evaluated on a small synthetic
cohort (30 rows: 24 for training, 6 for validation) and is an infrastructure
demonstration, not a clinically validated diagnostic tool. Metrics on six validation
rows are not meaningful, and on the repository's synthetic covariate-shift benchmark
neither OOD gate separates the shifted rows from the bundled ones (AUC 0.56 for
Mahalanobis, 0.57 for logit energy). Validation on real clinical data is not part of
this release. Not for clinical use.

Amoebanator is the methodological prototype for the abstention architecture carried
into a national multicenter network in Peru on opportunistic CNS infection in people
living with HIV, where a new abstention-aware model is to be trained from scratch on
the network's own data. That work is separate from this repository.

## License and disclaimer

The code and documentation in this repository are released under the MIT
License (see `LICENSE`). They are provided for research and education only;
nothing here should be used to make clinical decisions.
