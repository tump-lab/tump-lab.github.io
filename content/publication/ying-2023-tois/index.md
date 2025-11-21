---
title: Understanding Diversity in Session-based Recommendation
authors:
- Qin Ying
- Hui Fang
- Zhu Sun
- Yew Soon Ong
date: '2023-01-01'
publishDate: '2025-08-14T14:34:46.931156Z'
publication_types:
- article-journal
publication: '*ACM Transactions on Information Systems (TOIS)*'
abstract: Current session-based recommender systems (SBRSs) mainly focus on maximizing
  recommendation accuracy, while few studies have been devoted to improve diversity
  beyond accuracy. Meanwhile, it is unclear how the accuracy-oriented SBRSs perform
  in terms of diversity. In addition, the asserted “tradeoff” relationship between
  accuracy and diversity has been increasingly questioned in the literature. Toward
  the aforementioned issues, we conduct a holistic study to particularly examine the
  recommendation performance of representative SBRSs w.r.t. both accuracy and diversity,
  striving for better understanding of the diversity-related issues for SBRSs and
  providing guidance on designing diversified SBRSs. Particularly, for a fair and
  thorough comparison, we deliberately select state-of-the-art non-neural, deep neural,
  and diversified SBRSs by covering more scenarios with appropriate experimental setups,
  e.g., representative datasets, evaluation metrics, and hyper-parameter optimization
  technique. The source code can be obtained via github.com/qyin863/Understanding-Diversity-in-SBRSs
  . Our empirical results unveil that (1) non-diversified methods can also obtain
  satisfying performance on diversity, which can even surpass diversified ones, and
  (2) the relationship between accuracy and diversity is quite complex. Besides the
  “tradeoff” relationship, they can be positively correlated with each other, that
  is, having a same-trend (win–win or lose–lose) relationship, which varies across
  different methods and datasets. Additionally, we further identify three possible
  influential factors on diversity in SBRSs (i.e., granularity of item categorization,
  session diversity of datasets, and length of recommendation lists) and offer an
  intuitive guideline and a potential solution regarding learned item embeddings for
  more effective session-based recommendation.
---
