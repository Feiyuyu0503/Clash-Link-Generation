import requests
import yaml

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


def main():
    proxys = []

    session = requests.session()

    # 加载模板配置
    with open(INPUT_FILE, encoding='utf-8') as f:
        template = yaml.safe_load(f.read())

    # 加载订阅节点
    for url in URLS:
        print('[+] Load url "%s".' % url)
        # 加载本地文件
        if len(url) >= 7:
            if url[:7] == 'file://':
                with open(url[7:], encoding='utf-8') as f:
                    proxys.append(yaml.safe_load(f.read()))
                continue
        # 剩下都算作订阅链接
        try:
            r = session.get(url)
        except requests.RequestException as e:
            continue
        proxys.append(yaml.safe_load(r.text))
    # 添加节点到Proxy里面
    template['Proxy'] = []
    for proxy in proxys:
        template['Proxy'] += proxy['Proxy']

    # 获取到Proxy Group对象
    proxy_groups = template['Proxy Group']
    proxys_name = []

    # 获取服务器名字列表
    for proxy in template['Proxy']:
        proxys_name.append(proxy['name'])

    # 增加节点
    for proxy_group in proxy_groups:
        if proxy_group['name'] in ADD_GROUPS:
            if not proxy_group['proxies']:
                proxy_group['proxies'] = []
            proxy_group['proxies'] += proxys_name

    # 写出文件
    with open(OUTPUT_FILE, 'w') as f:
        f.write(yaml.safe_dump(template))

    print('[+] Run success.')


if __name__ == '__main__':
    main()
