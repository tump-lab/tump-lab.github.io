---
title: Adversary Agnostic Robust Deep Reinforcement Learning
authors:
- Xinghua Qu
- Yew Soon Ong
- Abhishek Gupta
- Zhu Sun
date: '2021-01-01'
publishDate: '2025-08-14T14:34:46.801567Z'
publication_types:
- article-journal
publication: '*IEEE Transactions on Neural Networks and Learning Systems (TNNLS)*'
abstract: |
  'Deep reinforcement learning (DRL) policies have been shown to be deceived
  by perturbations (e.g., random noise or intensional adversarial attacks) on state
  observations that appear at test time but are unknown during training. To increase
  the robustness of DRL policies, previous approaches assume that the knowledge of
  adversaries can be added into the training process to achieve the corresponding
  generalization ability on these perturbed observations. However, such an assumption
  not only makes the robustness improvement more expensive but may also leave a model
  less effective to other kinds of attacks in the wild. In contrast, we propose an
  adversary agnostic robust DRL paradigm that does not require learning from adversaries.
  To this end, we first theoretically derive that robustness could indeed be achieved
  independently of the adversaries based on a policy distillation setting. Motivated
  by this finding, we propose a new policy distillation loss with two terms: 1) a
  prescription gap maximization loss aiming at simultaneously maximizing the likelihood
  of the action selected by the teacher policy and the entropy over the remaining
  actions; 2) a corresponding Jacobian regularization loss that minimizes the magnitude
  of the gradient with respect to the input state. The theoretical analysis shows
  that our distillation loss guarantees to increase the prescription gap and the adversarial
  robustness. Furthermore, experiments on five Atari games firmly verify the superiority
  of our approach in terms of boosting adversarial robustness compared to other state-of-the-art
  methods.'
---
