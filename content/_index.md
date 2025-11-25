---
# Leave the homepage title empty to use the site title
title:
date: 2022-10-24
type: landing

sections:
  - block: hero
    content:
      title: |
        Trustworthy User Modelling and Personalization
        (TUMP)
      text: |
        <p style="text-align: left; margin-left: 130px; margin-right: auto; max-width: 900px;">The TUMP Lab advances trustworthy user modeling and personalization through cutting-edge AI techniques, human-centric LLM-based user simulation, and rigorous benchmarking via open-source frameworks.</p>
        
        **Research Focus:**
        
        - Designing trustworthy recommendation algorithms—robust, diverse, fair, explainable, and privacy-preserving—by applying cutting-edge techniques e.g., deep learning and large language models across various domains including e-commerce, multimedia, location-based social networks, and healthcare.
        - Developing LLM-based user simulators for human-centric evaluation and optimization of recommender systems.
        - Benchmarking recommender systems through rigorous evaluation and fair comparison by advancing open-source libraries such as [DaisyRec](https://github.com/yudi-mars/daisyRec) and [DaisyRec-v2.0](https://github.com/recsys-benchmark/DaisyRec-v2.0).
    design:
      background:
        color: 'white'
      spacing:
        padding: ['40px', '0', '40px', '0']
      css_style: |
        text-align: center;
        max-width: 1200px;
        margin: 0 auto;
      css_class: 'hero-centered'
  
  - block: markdown
    content:
      title: Latest News
      text: |
        {{% news-list %}}
  
  # - block: collection
  #   content:
  #     title: Latest Preprints
  #     text: ""
  #     count: 5
  #     filters:
  #       folders:
  #         - publication
  #       publication_type: 'article'
  #   design:
  #     view: citation
  #     columns: '1'

  - block: markdown
    content:
      title:
      subtitle:
      text: |
        <style>
        /* 主页 Hero 区块文本居中和间距调整 */
        .hero-centered .hero-title {
          margin-bottom: 2.5rem !important;
          text-align: center;
        }
        .hero-centered .hero-lead,
        .hero-centered p:not([style*="text-align: left"]) {
          text-align: center !important;
          max-width: 900px;
          margin-left: auto !important;
          margin-right: auto !important;
        }
        .hero-centered .hero-lead {
          margin-top: 2rem !important;
        }
        
        /* Research Focus 段落左对齐 */
        .hero-centered p[style*="text-align: left"] {
          text-align: left !important;
          max-width: 900px;
          margin-right: auto !important;
        }
        
        /* Research Focus 列表左对齐 - 强制覆盖所有样式 */
        .hero-centered ul {
          text-align: left !important;
          margin-left: 130px !important;
          margin-right: auto !important;
          padding-left: 1.2rem !important;
          max-width: 900px !important;
        }
        .hero-centered ul li {
          text-align: left !important;
          list-style-position: outside !important;
          margin-left: 0 !important;
          padding-left: 0 !important;
          line-height: 1.6 !important;
        }
        
        /* 隐藏 Latest News 部分的图片 */
        section:has(h1:contains("Latest News")) img,
        section:has(h2:contains("Latest News")) img,
        section:has(h1:contains("Latest News")) .article-image,
        section:has(h2:contains("Latest News")) .article-image,
        section:has(h1:contains("Latest News")) .article-banner,
        section:has(h2:contains("Latest News")) .article-banner,
        section:has(h1:contains("Latest News")) .featured-image,
        section:has(h2:contains("Latest News")) .featured-image,
        section:has(h1:contains("Latest News")) .card-image,
        section:has(h2:contains("Latest News")) .card-image {
          display: none !important;
        }
        </style>
        <script>
        // 隐藏 Latest News 部分的图片
        (function() {
          function hideNewsImages() {
            // 查找包含 "Latest News" 标题的 section
            const headings = document.querySelectorAll('h1, h2');
            headings.forEach(function(heading) {
              if (heading.textContent.trim() === 'Latest News') {
                // 找到包含该标题的 section
                let section = heading.closest('section');
                if (!section) {
                  // 如果找不到 section，向上查找父容器
                  let parent = heading.parentElement;
                  while (parent && parent.tagName !== 'SECTION') {
                    parent = parent.parentElement;
                  }
                  section = parent;
                }
                if (section) {
                  // 隐藏该 section 中的所有图片
                  const images = section.querySelectorAll('img, .article-image, .article-banner, .featured-image, .card-image, [class*="image"]');
                  images.forEach(function(img) {
                    img.style.display = 'none';
                  });
                  // 也隐藏包含图片的容器
                  const imageContainers = section.querySelectorAll('.article-image-wrapper, .card-img, [class*="img"]');
                  imageContainers.forEach(function(container) {
                    container.style.display = 'none';
                  });
                }
              }
            });
          }
          if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', hideNewsImages);
          } else {
            hideNewsImages();
          }
          const observer = new MutationObserver(hideNewsImages);
          observer.observe(document.body, { childList: true, subtree: true });
        })();
        
        // Research Focus 段落和列表左对齐
        (function() {
          function alignResearchFocusLeft() {
            const paragraphs = document.querySelectorAll('.hero-centered p');
            let foundResearchFocus = false;
            paragraphs.forEach(function(p) {
              if (p.textContent.includes('Research Focus:')) {
                foundResearchFocus = true;
                p.style.textAlign = 'left';
                p.style.marginLeft = '130px';
                p.style.marginRight = 'auto';
              } else if (foundResearchFocus && (p.textContent.includes('1、') || p.textContent.includes('2、') || p.textContent.includes('3、'))) {
                p.style.textAlign = 'left';
                p.style.marginLeft = '130px';
                p.style.marginRight = 'auto';
              }
            });
            
            // 对齐Research Focus部分的列表
            const lists = document.querySelectorAll('.hero-centered ul');
            lists.forEach(function(ul) {
              ul.style.textAlign = 'left';
              ul.style.marginLeft = '130px';
              ul.style.marginRight = 'auto';
              ul.style.paddingLeft = '1.2rem';
              ul.style.maxWidth = '900px';
              
              const listItems = ul.querySelectorAll('li');
              listItems.forEach(function(li) {
                li.style.textAlign = 'left';
                li.style.listStylePosition = 'outside';
                li.style.paddingLeft = '0';
                li.style.marginLeft = '0';
                li.style.lineHeight = '1.6';
              });
            });
          }
          if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', alignResearchFocusLeft);
          } else {
            alignResearchFocusLeft();
          }
          setTimeout(alignResearchFocusLeft, 100);
          setTimeout(alignResearchFocusLeft, 500);
        })();
        </script>
        {{% cta cta_link="./people/" cta_text="Meet the team →" %}}
    design:
      columns: '1'
---
