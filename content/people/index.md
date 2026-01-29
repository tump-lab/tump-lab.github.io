---
title: People
date: 2022-10-24

type: landing

sections:
  - block: people
    content:
      # title: Meet the Team
      # Choose which groups/teams of users to display.
      #   Edit `user_groups` in each user's profile to add them to one or more of these groups.
      user_groups:
          - Principal Investigators
          - Current Students/Researchers
          - Collaborating Researchers
      sort_by: weight
      sort_ascending: true
    design:
      show_interests: false
      show_role: true
      show_social: true
  - block: markdown
    content:
      text: |
        <style>
        /* organization 样式，与 portrait-subtitle（role）保持一致 */
        .portrait-organization {
          font-size: 0.8rem;
          color: rgba(0,0,0,.54);
          margin-top: 0;
          margin-bottom: 0;
          font-weight: 300;
        }
        /* Former Students/Researchers 标题样式 */
        .former-students-title {
          font-size: 1.5rem;
          font-weight: 600;
          margin-bottom: 1.5rem;
          margin-top: 0.5rem;
          text-align: center;
        }
        </style>
        <h2 class="former-students-title">Former Students/Researchers</h2>
        {{% people-table group="Former Students/Researchers" %}}
---