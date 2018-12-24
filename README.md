[![spaCy](https://img.shields.io/badge/built%20with-spaCy-09a3d5.svg)](https://spacy.io)
# medaCy
:hospital: Clinical Notes Model for medaCy :hospital:

This repository contains a versioned, medaCy compatible Model for information extraction from clinical notes.

![alt text](https://nlp.cs.vcu.edu/images/Edit_NanomedicineDatabase.png "Nanoinformatics")

# Description
This is the light-weight version (no metamap) of medaCy's model for extracting 9 unique entities from clinical notes:

`Drug, Strength, Duration, Route, Form, ADE, Dosage, Reason, Frequency`

# Results
Model generalization ability is evaluated over 202 patient clinical note files not seen during training. *Strict* indicates exact matches of spans, *Lenient* indicates a fuzzy matching of spans (model predictions are off by single characters).

| Entities | Strict | Lenient |
| :-------: | :----------------: |:-------------:|
|Drug| | |  |
|Strength|  |  |
|Duration | |  |
|Route | |  |
|Form | |  |
|ADE | |  |
|Dosage | |  |
|Reason | |  |
|Frequency | |  |
|**System** | |  |

# Training Data
N2C2 2018 Shared Task
The data used to induce this model is protected by HIPAA privacy regulations and thus cannot be published.

Authors
=======
Andriy Mulyar and Bridget McInnes

Acknowledgments
===============
- [VCU Natural Language Processing Lab](https://nlp.cs.vcu.edu/)     ![alt text](https://nlp.cs.vcu.edu/images/vcu_head_logo "VCU")
- [Nanoinformatics Vertically Integrated Projects](https://rampages.us/nanoinformatics/)
