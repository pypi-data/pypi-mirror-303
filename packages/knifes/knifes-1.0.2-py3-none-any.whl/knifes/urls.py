import mimetypes
import os
from urllib import parse
from urllib.parse import urlparse

from knifes.media import MediaType, extension_to_media_type_dict


def get_url_from_text(text):
    if not text:
        return text
    start_index = text.rfind("http://")
    if start_index == -1:
        start_index = text.rfind("https://")
    if start_index == -1:
        return None
    text = text[start_index:]
    # 去掉空格后内容
    end_index = text.find(" ")
    if end_index != -1:
        text = text[0:end_index]
    return text


# m.oasis.weibo.cn => weibo.cn
def get_base_domain_with_suffix_from_url(url) -> str:
    """get base domain with suffix from url, like 'm.oasis.weibo.cn' => 'weibo.cn'"""
    if not url:
        return url
    u = parse.urlparse(url)
    if not u.hostname:
        return ""
    host_list = u.hostname.split(".")
    if len(host_list) < 2:
        return ""
    return host_list[-2].lower() + "." + host_list[-1].lower()


# m.oasis.weibo.cn => weibo
def get_base_domain_from_url(url) -> str:
    """get base domain from url, like 'm.oasis.weibo.cn' => 'weibo'"""
    if not url:
        return url
    u = parse.urlparse(url)
    if not u.hostname:
        return ""
    host_list = u.hostname.split(".")
    if len(host_list) < 2:
        return ""
    return host_list[-2].lower()


# m.oasis.weibo.cn => oasis.weibo
def get_sub_domain_from_url(url) -> str:
    """get sub domain from url, like 'm.oasis.weibo.cn' => 'oasis.weibo'"""
    if not url:
        return url
    u = parse.urlparse(url)
    if not u.hostname:
        return ""
    host_list = u.hostname.split(".")
    if len(host_list) < 3:
        return ""
    return host_list[-3].lower() + "." + host_list[-2].lower()


# 目前支持video、audio、image类型，其他返回None
# fixed bug for 'http://v.example.com/o0/000bH9u0lx07TQ0OHwmA01041200Onth0E010.mp4?label=mp4_hd&template=852x480.28.0&ori=0&ps=1CwnkDw1GXwCQx&Expires=1645114865&ssig=8QbZXUCE85&KID=unistore,video'
def guess_media_type(url) -> MediaType | None:
    url_without_query = url.split("?", maxsplit=1)[0]
    mimetype, _ = mimetypes.guess_type(url_without_query)
    if not mimetype:
        try:
            return extension_to_media_type_dict.get(get_extension(url_without_query.lower()))
        except:  # noqa: E722
            return None
    if mimetype in ("application/x-mpegurl", "application/vnd.apple.mpegurl"):  # .m3u8
        return MediaType.VIDEO
    try:
        return MediaType(mimetype.split("/")[0])
    except:  # noqa: E722
        return None


def parse_url(url) -> tuple[str, list, dict]:
    """return (hostname、path_list, query_dict)
    the difference between hostname and netloc is that hostname does not include the port number
    """
    parsed = parse.urlparse(url)
    return (
        parsed.hostname,
        parsed.path.strip("/").split("/"),
        dict(parse.parse_qsl(parsed.query)),
    )


def parse_path(url) -> list[str]:
    """return path list, like ['a', 'b', 'c']"""
    return parse.urlparse(url).path.strip("/").split("/")


def parse_query(url) -> dict[str, str]:
    """return query dict, like {'a': '1', 'b': '2'}"""
    return dict(parse.parse_qsl(parse.urlparse(url).query))


def get_query_value(url, parameter) -> str | None:
    """return query value by parameter, like 'http://example.com?a=1&b=2' => get_query_value(url, 'b') => '2'"""
    return parse_query(url).get(parameter)


def sanitize_url(url, scheme="http"):
    """Prepend protocol-less URLs with `http:` scheme in order to mitigate
    the number of unwanted failures due to missing protocol
    """
    if not url:
        return url
    if url.startswith("//"):
        return f"{scheme}:{url}"
    return url


def get_extension(url):
    return os.path.splitext(parse.urlparse(url).path)[1]


def is_http_url(url):
    result = urlparse(url)
    return all([result.scheme, result.netloc]) and result.scheme in {"http", "https"}
