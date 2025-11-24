---
title: Adaptive Intention Learning for Session-based Recommendation
authors:
- Qingbo Zhang
- Xiaochun Yang
- Hao Chen
- Bing Wang
- Zhu Sun
- Xiangmin Zhou
date: '2024-01-01'
publishDate: '2025-08-14T14:34:46.959909Z'
publication_types:
- article-journal
publication: '*ACM Transactions on Intelligent Systems and Technology (TIST)*'
abstract: |
  In recent years, session-based recommender systems (SRSs) have emerged as
  a significant research focus within the recommendation field. Capturing user intentions
  to infer user interest accordingly has proven to be effective in enhancing the accuracy
  of SRSs. However, existing techniques assume that all sessions have the same number
  of intentions or that the items in one category belonging to the same session reflect
  the same intention. In real applications, such as e-commerce, sessions may have
  different numbers of intentions, and the same type of items in a session may correspond
  to different intentions. As a result, existing techniques cannot guarantee high-quality
  user interest prediction. In this article, we propose a novel Adaptive Intention
  Learning Network (AILN) to capture an adaptive number of intentions for each session,
  thereby enhancing the accuracy of user interest inference. Specifically, we design
  an intention evaluation network (IEN) to evaluate whether a subsequence of a session
  corresponds to a valid intention, and an intention generation network (IGN) to learn
  the representation of a valid intention. By checking each subsequence of a session,
  IEN and IGN enable the incremental learning of a session-specific intention hierarchy
  (IH) to store valid intentions of the session. To reduce the cost of building the
  IH, we propose a pruning strategy that exploits the intention validity to avoid
  unnecessary evaluation. The representative intentions are selected from IH and input
  into a designed interest predictor to infer the user interest. Experimental results
  on two real-world datasets demonstrate the superiority of our proposed AILN.
---
