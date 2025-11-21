// 自定义作者链接重定向
// 当作者页面有 external_link 时，自动重定向

document.addEventListener('DOMContentLoaded', function() {
  // 获取页面中的 external_link 数据（通过 data 属性或 meta 标签）
  const metaLink = document.querySelector('meta[name="author-external-link"]');
  if (metaLink && metaLink.content) {
    window.location.href = metaLink.content;
    return;
  }
  
  // 或者通过检查 URL 参数
  const urlParams = new URLSearchParams(window.location.search);
  const externalLink = urlParams.get('external_link');
  if (externalLink) {
    window.location.href = externalLink;
  }
});

