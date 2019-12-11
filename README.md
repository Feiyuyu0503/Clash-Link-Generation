# Clash-Link-Generation
clash_link_generation
Modify the following:
```python
# 订阅链接，支持本地自有节点
URLS = [
    'file://other.yaml',
    'https://xxx.com/clash',
]
# 需要添加节点的节点组
ADD_GROUPS = ['UrlTest', 'PROXY', 'GlobalMedia', 'HKMTMedia']
# 输入文件
INPUT_FILE = 'template.yaml'
# 输出文件
OUTPUT_FILE = 'output.yaml'
```

Then use the following command to generate
```bash
python gen.py
```
