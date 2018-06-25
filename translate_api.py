# coding=utf-8

import re
import urllib2

AGENT = """ Mozilla/4.0 (
             compatible;
             MSIE 6.0;
             Windows NT 5.1;
             SV1;
             .NET CLR 1.1.4322;
             .NET CLR 2.0.50727;
             .NET CLR 3.0.04506.30
             )"""


def translate(content, from_lang='auto', to_lang='zh-CN'):
    content = urllib2.quote(content.encode('utf-8'))
    url = "http://translate.google.cn/m?hl=%s&sl=%s&q=%s" % (to_lang, from_lang, content)
    request = urllib2.Request(url, headers={'User-Agent': AGENT})
    data = urllib2.urlopen(request).read().decode("utf-8")
    expr = r'class="t0">(.*?)<'
    result = re.findall(expr, data)[0]
    return result


if __name__ == '__main__':
    print(translate(u'あなたは最高です'))
