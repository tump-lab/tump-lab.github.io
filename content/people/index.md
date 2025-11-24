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
        <script>
        (function() {
          // 作者外部链接映射表（手动维护，或通过 Hugo 生成）
          const authorExternalLinks = {
            "lingfeng-huang": "https://scholar.google.com/citations?hl=zh-CN&user=tdEFQ3cAAAAJ",
            "kaidong-feng": "https://scholar.google.com/citations?hl=zh-CN&user=QCSiF_sAAAAJ",
            "hongyang-liu": "https://researchers.mq.edu.au/en/persons/hongyang-liu/",
            "huizhong-guo": "https://scholar.google.com/citations?hl=en&user=KLk57IEAAAAJ",
            "jiajie-zhu": "https://scholar.google.com/citations?hl=en&user=mlkEyZUAAAAJ",
            "jinze-wang": "https://scholar.google.com/citations?user=FBnolecAAAAJ&hl=en",
            "joshua-dodanduwa": "https://scholar.google.com/citations?hl=en&user=mlkEyZUAAAAJ",
            "li-zhou": "https://csfzswz.swu.edu.cn/info/1030/1651.htm",
            "yu-lei": "https://scholar.google.com/citations?user=DEUmArsAAAAJ&hl=en&oi=ao",
            "zhuoxuan-huang": "https://scholar.google.com/citations?user=yzI95WIAAAAJ&hl=en&oi=ao",
            "samal-mukhtar": "https://ieeexplore.ieee.org/author/455078308513416",
            "lee-yueh-ern-shannon": "https://scholar.google.com/citations?user=i-nrDQcAAAAJ&hl=en",
            // 添加更多作者的外部链接：
            // "author-slug": "external-url",
          }; 

          // 修改所有作者链接
          function updateAuthorLinks() {
            // 查找所有指向作者页面的链接
            const authorLinks = document.querySelectorAll('a[href*="/author/"]');
            
            authorLinks.forEach(function(link) {
              const href = link.getAttribute('href');
              if (!href) return;
              
              // 匹配 /author/xxx/ 格式
              const match = href.match(/\/author\/([^\/]+)/);
              if (!match) return;
              
              const authorSlug = match[1];
              
              // 检查是否有外部链接
              if (authorExternalLinks[authorSlug]) {
                // 有外部链接：更新链接指向外部URL
                link.href = authorExternalLinks[authorSlug];
                link.target = '_blank';
                link.rel = 'noopener noreferrer';
              } else {
                // 没有外部链接：禁用链接但保留元素
                link.removeAttribute('href');
                link.style.cursor = 'default';
                link.style.textDecoration = 'none';
                link.onclick = function(e) { e.preventDefault(); return false; };
              }
            });
          }

          // 页面加载完成后执行
          if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', updateAuthorLinks);
          } else {
            updateAuthorLinks();
          }

          // 使用 MutationObserver 监听动态加载的内容
          const observer = new MutationObserver(function(mutations) {
            updateAuthorLinks();
          });

          observer.observe(document.body, {
            childList: true,
            subtree: true
          });
        })();
        </script>
    design:
      columns: '1'
---