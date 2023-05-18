In this demo, we aim to generate structured summaries in terms of different facets: background, methods, results and values.

# facet summarization: 
(1) Pr(corresponding faceted summary | the annotated section): sectional summarization; (2) Pr(corresponding faceted summary | article, controlled signal): Constrained summarization.

## Sectional summarization: 
* Datasets with Faceted Summaries
  + manually generate faceted summaries from the perspectives of purpose/background, methods, experimental results: require many experts with domain knowledge for annotation. To the best of our knowledge, there does not exist such work.
  + extract faceted, structured summaries from abstract: Hence, due to the complication of scientific articles, abstracts from the original authors are argubly in the best summaries. The three problems are 1) Not all abstracts contain all the facets. However, this is also the motivation why we need a faceted summarization model rather than a simple clasifier to extract sentences from abstract for different facets; 2) how to extract different facets from abstracts. 3) not all articles are explicitly organized by the predefined structured.  most of articles (more than 2/3) have no explicit headings. We search for articles with section names matching predefined keywords.
    + publications that explicitly require authors to summarize their work from specified persepctives, e.g., Emerald. For example, [this paper](https://arxiv.org/pdf/2106.00130.pdf) generates faceted summaries from Emerald since Emerald publications require authors to summarize their work from the perspectives of purpose, method, findings and values.
    However, they do not publish the dataset. 
    + [This paper](https://arxiv.org/pdf/1905.07695.pdf) anotates article and abstract sections into the categories: introduction, background, methods, results, discussion and conclusion
  + For structured summarization from multiple documents, [this paper](https://arxiv.org/abs/2302.04580) generates "the target summaries from more than seven thousand survey papers and utilizes their 430 thousand reference papers’ abstracts as input documents".

*  For testing, we manually retrieve two articles whose sections are organized with the structure. Wen then generate summaries using unconstrained CtrlSumm and BigBird on the sections for background, methods, results and values. 
  + Although BigBird generates more coherent summaries, both models will generate redundant information, especially for methods, no matter what sections we give to the models. We hypothesize two underlying reasons: (1) As shown in the figure below, methodology spreads over all the sections in the whole articles. Results are shown in `ctrlsum_abs_intro_summaries.csv` and `ctrlsum_abstract_summaries.csv`;  (2) Both models are trained on datasets with abstracts as summaries, which always emphasize the proposed methods.
  ![image](https://user-images.githubusercontent.com/43598514/228387539-aa9f352a-368b-451d-9091-69a4dc383d2a.png)

## Constrained summarization
We test [CtrlSum](https://arxiv.org/abs/2012.04281) on three papers related to Pretrained Language Models (BERT, RoBERTa, ALBERT) and save summaries from abstracts (short documents) in `plm_abstract_summaries.csv`. We save summaries according to abstracts and introductions (long documents: 500 - 750 in contrast to 100-150) in `plm_abs_intro_summaries.csv`. 
We find that
* We cannot generalize controlled signals into those facets we care about.
* Regardless of keywords, CtrlSum tends to generate summaries about proposed methods even when we give keywords for experimental results and contributions. The goal is that we want distinct features for different attributes described by keywords.
* Analysis: we test two hypotheses: 
  1. in-domain v.s. out-of-domain articles: when we use in-domain articles, it can kinda "extract" sentences containing provided keywords (e.g., "results"); 
  2. positions of keywords; 
  3. it seems to have less distinct summaries for long documents.
* Analysis: Intuitively, CTRLSUM are trained on the abstract as summaries. Almost all the abstracts demonstrate the proposed methods, while only a portion will summarize experimental results and values in the research domain, few will give background. 需要sample文章进一步验证abstract的facets 分布. We apply sectional summarization, which leads to the the same problem.


For long documents, we also find
* hallucination: 
* repetition.
* Content Selection for longer documents: extractive and attention-based selection based on LoBART

## Development 
* Develop datasets with faceted summaries for background, methods, results and values. So far, we plan to perform zero/few-shot prompts on ChatGPT. For support documents, we will only use I-C (Intro and conclusion). Previous work shows that, instead of the whole article as input, Introduction and conclusion seem to be enough, especially for purposes and values. Also, it avoids inefficiency and incapability of transformer models to deal with long documents and the problems we identified in the experiment.
  ![image](https://user-images.githubusercontent.com/43598514/228387015-22195c77-d13b-4b47-88eb-9335cab6dbc1.png)
* Develop a classifier to categorize sentences of abstracts into categories 
* Develop a summarization model. For this part, the current plan is to construct a CTRLSUM-like model, which can take categories as controllable signals.

# Dataset
[`arxiv-metadata-oai-snapshot.json`](https://www.kaggle.com/datasets/Cornell-University/arxiv)