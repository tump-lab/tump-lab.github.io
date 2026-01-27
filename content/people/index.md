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
      title: Former Students/Researchers
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
        </style>
        <script>
        // 将 Former Students/Researchers 标题字体大小设置成和 Current Students/Researchers (h2) 一样
        (function() {
          function adjustTitleSize() {
            // 获取 Current Students/Researchers 的 h2 元素作为参考
            const h2Ref = document.querySelector('h2.mb-4');
            if (!h2Ref) return;
            
            // 获取计算后的字体大小
            const computedStyle = window.getComputedStyle(h2Ref);
            const fontSize = computedStyle.fontSize;
            const fontWeight = computedStyle.fontWeight;
            
            // 找到 Former Students/Researchers 的 h1 标题
            const headings = document.querySelectorAll('h1.mb-0');
            headings.forEach(function(heading) {
              if (heading.textContent.trim() === 'Former Students/Researchers') {
                heading.style.fontSize = fontSize;
                heading.style.fontWeight = fontWeight;
              }
            });
          }
          
          if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', adjustTitleSize);
          } else {
            adjustTitleSize();
          }
          
          // 使用 MutationObserver 监听动态加载的内容
          const observer = new MutationObserver(adjustTitleSize);
          observer.observe(document.body, { childList: true, subtree: true });
        })();
        </script>
        {{% people-table group="Former Students/Researchers" %}}
  - block: markdown
    content:
      text: |
        {{% people-table group="Former Students/Researchers" %}}
    design:

      columns: '1'
---