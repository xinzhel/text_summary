In this demo, we aim to generate structured summaries in terms of three attributes: proposed methods, experimental results and contributions.

# CtrlSum
For papers in the field of Pretrained Language Models:
* We save summaries from abstracts (short documents) in `plm_abstract_summaries.csv`. We find that CtrlSum will have some distinct features for different attributes. Particulary, CtrlSum is sensitive to demonstrate proposed methods even when we give prompts for experimental results and contributions.
* We save summaries from abstracts and introductions (long documents) in `plm_abs_intro_summaries.csv`. Two problems appear for long documents: 1) less distinct summaries; 2) hallucination for the latter generated summaries; 3) repetition.

