---
title: 'LightKG: Efficient Knowledge-Aware Recommendations with Simplified GNN Architecture'
authors:
- Yanhui Li
- Dongxia Wang
- Zhu Sun
- Haonan Zhang
- Huizhong Guo
date: '2025-01-01'
publishDate: '2025-08-14T14:34:46.774798Z'
publication_types:
- paper-conference
publication: '*The 31st SIGKDD Conference on Knowledge Discovery and Data Mining (KDD)*'
abstract: 'Recently, Graph Neural Networks (GNNs) have become the dominant approach
  for Knowledge Graph-aware Recommender Systems (KGRSs) due to their proven effectiveness.
  Building upon GNN-based KGRSs, Self-Supervised Learning (SSL) has been incorporated
  to address the sparsity issue, leading to longer training time. However, through
  extensive experiments, we reveal that: (1) compared to other KGRSs, the existing
  GNN-based KGRSs fail to keep their superior performance under sparse interactions
  even with SSL; (2) more complex models tend to perform worse in sparse interaction
  scenarios and complex mechanisms, like attention mechanisms, can be detrimental
  as they often increase learning difficulty. Inspired by these findings, we propose
  LightKG, a simple yet powerful GNN-based KGRS to address sparsity issues. LightKG
  includes a simplified GNN layer that encodes directed relations as scalar pairs
  rather than dense embeddings and employs a linear aggregation framework, greatly
  reducing the complexity of GNNs. Additionally, LightKG incorporates an efficient
  contrastive layer to implement SSL. It directly minimizes the node similarity in
  the original graph, avoiding the time-consuming subgraph generation and comparison
  required in previous SSL methods. Experiments on four benchmark datasets show that
  LightKG outperforms 12 competitive KGRSs in both sparse and dense scenarios while
  significantly reducing training time. Specifically, it surpasses the best baselines
  by an average of 5.8% in recommendation accuracy and saves 84.3% of training time
  compared to KGRSs with SSL.'
---
