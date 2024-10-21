# fetch_web_resource

`fetch_web_resource` 是一个用于抓取网页资源并缓存 HTML 内容的 Python 包。

## 功能

- 抓取网页内容
- 提取网页中的图片和文件链接
- 缓存抓取的 HTML 内容
- 使用随机 User-Agent 模拟请求

## 安装

你可以使用以下命令安装该包：

```sh
pip install .
```

## 使用方法

### 初始化

首先，你需要初始化 `HTMLFetcher` 类：

```python
from web_fetch.web_fetch import HTMLFetcher
import diskcache

cache = diskcache.Cache('./html_cache')
fetcher = HTMLFetcher(cache=cache, max_concurrent_per_domain=5)
```

### 抓取网页内容

你可以使用 `fetch_html_batch` 方法抓取一批网页内容：

```python
results = [
    SearchResult(url="https://example.com/page1"),
    SearchResult(url="https://example.com/page2"),
]

async for result in fetcher.fetch_html_batch(results, timeout=5):
    print(result)
```

### 提取 URL 资源

你可以使用 `_extract_urls` 方法从 HTML 内容中提取图片和文件链接：

```python
html_content = "<html>...</html>"
base_url = "https://example.com"
url_resource = fetcher._extract_urls(html_content, base_url)
print(url_resource)
```

## 环境变量

你需要在项目根目录下创建一个 `.env` 文件，并添加你的 API 密钥：

```
API_KEY=your_api_key_here
```

## 依赖

该项目依赖以下 Python 包：

- requests
- beautifulsoup4
- diskcache
- python-dotenv
- htmldate
- pydantic

## 贡献

欢迎贡献代码！请 fork 本仓库并提交 pull request。

## 许可证

该项目使用 [MIT 许可证](LICENSE)。