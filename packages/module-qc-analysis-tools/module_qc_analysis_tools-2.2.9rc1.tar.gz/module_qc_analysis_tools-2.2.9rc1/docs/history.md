# module-qc-analysis-tools history

---

All notable changes to module-qc-analysis-tools will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to
[Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Unreleased

**_Changed:_**

**_Added:_**

**_Fixed:_**

## [2.2.7](https://gitlab.cern.ch/atlas-itk/pixel/module/module-qc-analysis-tools/-/tags/v2.2.7) - 2024-08-28 ## {: #mqat-v2.2.7 }

**_Changed:_**

- changed QC criteria following up from PRR (!177)

**_Added:_**

- quad bare module metrology (!179)

**_Fixed:_**

- bug in creating per-chip json outputs for ADC calibration
  (b006412b06fb54d09ce075336b0b49e6b9a0292a)

## [2.2.6](https://gitlab.cern.ch/atlas-itk/pixel/module/module-qc-analysis-tools/-/tags/v2.2.6) - 2024-07-12 ## {: #mqat-v2.2.6 }

**_Changed:_**

- SLDO criteria cuts (!169)
- refactored `adc-calibration` to get ready for v3 (!157)

**_Added:_**

- flatness analysis (!160, !162)
- long-term stability dcs analysis (!167)
- This documentation. (!171)

**_Fixed:_**

- Removed `OBSERVATION` field for visual inspection for bare components (!158)
- Bug with TOT mean/rms for minimum health test (!159)
- Bare IV temperatures (!164)

## [2.2.5](https://gitlab.cern.ch/atlas-itk/pixel/module/module-qc-analysis-tools/-/tags/v2.2.5) - 2024-07-12 ## {: #mqat-v2.2.5 }

Note: this version is skipped due to a packaging issue with `module-qc-tools`.
