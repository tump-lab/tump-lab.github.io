---
title: Enhancing New-item Fairness in Dynamic Recommender Systems
authors:
- Huizhong Guo
- Zhu Sun
- Dongxia Wang
- Tianjun Wei
- Jinfeng Li
- Jie Zhang
date: '2025-01-01'
publishDate: '2025-08-14T14:34:46.759693Z'
publication_types:
- paper-conference
publication: '*The 48th International ACM SIGIR Conference on Research and Development
  in Information Retrieval (SIGIR)*'
abstract: "New-items play a crucial role in recommender systems (RSs) for delivering
  fresh and engaging user experiences. However, traditional methods struggle to effectively
  recommend new-items due to their short exposure time and limited interaction records,
  especially in dynamic recommender systems (DRSs) where new-items get continuously
  introduced and users' preferences evolve over time. This leads to significant unfairness
  towards new-items, which could accumulate over the successive model updates, ultimately
  compromising the stability of the entire system. Therefore, we propose FairAgent,
  a reinforcement learning (RL)-based new-item fairness enhancement framework specifically
  designed for DRSs. It leverages knowledge distillation to extract collaborative
  signals from traditional models, retaining strong recommendation capabilities for
  old-items. In addition, FairAgent introduces a novel reward mechanism for recommendation
  tailored to the characteristics of DRSs, which consists of three components: 1)
  a new-item exploration reward to promote the exposure of dynamically introduced
  new-items, 2) a fairness reward to adapt to users' personalized fairness requirements
  for new-items, and 3) an accuracy reward which leverages users' dynamic feedback
  to enhance recommendation accuracy. Extensive experiments on three public datasets
  and backbone models demonstrate the superior performance of FairAgent."
---
