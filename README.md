In this demo, we aim to generate structured summaries in terms of three attributes: proposed methods, experimental results and contributions.

# CtrlSum
We test it on papers of Pretrained Language Models (BERT, RoBERTa, ALBERT) and save summaries from abstracts (short documents) in `plm_abstract_summaries.csv`. We save summaries from abstracts and introductions (long documents: 500 - 750 in contrast to 100-150) in `plm_abs_intro_summaries.csv`. 
We find that
* Regardless of keywords, CtrlSum tends to generate summaries about proposed methods even when we give keywords for experimental results and contributions. The goal is that we want distinct features for different attributes described by keywords.
* Analysis: we test two hypotheses: 1) in-domain v.s. out-of-domain articles: when we use in-domain articles, it can kinda "extract" sentences containing provided keywords (e.g., "results"); 2) positions of keywords; 3) it seems to have less distinct summaries for long documents.
* Analysis: Intuitively, CTRLSUM are trained on the abstract as summaries. Almost all the abstracts demonstrate the proposed methods, while only a portion will summarize experimental results and values in the research domain, few will give background. 需要sample文章进一步验证abstract的facets 分布. We apply sectional summarization, which leads to the the same problem.
* Sectional summarization:
  + 大模型Big bird效果要好的多. 
  + Both will generate redundant information, especially methodology summaries, no matter what sections we give to the models.
  + Conclusion: not considered. Even it gives good results, it is not easily to generalize articles without explicit headings.
  


For long documents, we also find
* hallucination: 
* repetition.
* Content Selection for longer documents: extractive and attention-based selection based on LoBART


