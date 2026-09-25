---
title: Amoebanator
colorFrom: blue
colorTo: blue
sdk: docker
app_port: 8501
tags:
- streamlit
pinned: false
short_description: Calibrated, abstention-aware PAM triage (synthetic data)
license: mit
---

# Amoebanator

Research codebase for a calibrated, abstention-aware triage signal for primary amoebic
meningoencephalitis (PAM), the rare and near-uniformly fatal CNS infection caused by
*Naegleria fowleri*. The classifier is small by design, with calibration,
split conformal prediction and an out-of-distribution gate, and it abstains instead of
predicting when either one flags the input. Out-of-distribution detection is
dual-gated: Mahalanobis distance in feature space and an energy score on the
temperature-scaled logits. The conformal step abstains when the prediction set is
empty or holds both classes. A literature-anchored registry of meningoencephalitis
vignettes provides the differential-diagnosis context.

> **For research and educational use.** Not a cleared medical device, not a substitute
> for clinical judgment, and not validated for unsupervised use.

## Scope and status

Amoebanator is a clinical-ML infrastructure project for CNS-infection triage, using
primary amoebic meningoencephalitis (Naegleria fowleri) as a high-risk must-not-miss
example. This release demonstrates the engineering stack: conformal prediction,
calibrated selective abstention, OOD detection, and reproducible training and
evaluation. The classifier is trained and evaluated on a small synthetic cohort and is
an infrastructure demonstration, not a clinically validated diagnostic tool. Validation
on real clinical data is not part of this release. Not for clinical use.

## License and disclaimer

The code and documentation in this repository are released under the MIT
License (see `LICENSE`). They are provided for research and education only;
nothing here should be used to make clinical decisions.
