#!/usr/bin/env python
# -*- coding:utf-8 -*-
from urllib.parse import urlparse

__all__ = []


class UrlMeta:
    """
    url metadata
    """

    def __init__(self, url, method):
        self.__url = urlparse(url)
        self.__host = f"{self.__url.scheme}://{self.__url.netloc}"
        self.__netloc = self.__url.netloc
        self.__protocol = self.__url.scheme
        self.__port = self.__url.port or ""
        self.__path = self.__url.path
        self.__method = method
        self.__count: int = 1

    @property
    def protocol(self):
        return self.__protocol

    @property
    def host(self):
        return self.__host

    @property
    def path(self):
        return self.__path

    @property
    def port(self):
        return self.__port

    @property
    def method(self):
        """
        http method.
        :return:
        """
        return self.__method

    @property
    def count(self) -> int:
        """
        request send count.
        """
        return self.__count

    def __eq__(self, other: 'UrlMeta'):
        result = self.__method == other.__method and self.__protocol == other.__protocol \
                 and self.__netloc == other.__netloc and self.__port == other.__port \
                 and self.__path == other.__path
        if result is True:
            self.__count += 1
        return result

    def __hash__(self):
        return hash(f"{self.__method}:{self.__protocol}{self.__netloc}{self.__port}{self.__path}")

    def __str__(self):
        return str({"method": self.method, "count": self.count, "url": f"{self.host}{self.path}", "path": self.path})

    def __repr__(self):
        return self.__str__()


class StatsUrlHostView:
    """
    url path statistics are performed in the host dimension
    like
    """

    def __init__(self, host):
        self.__host = host
        self.__paths: set[str] = set()
        self.__urls: set[UrlMeta] = set()

    @property
    def paths(self) -> list[str]:
        return list(self.__paths)

    @property
    def urls(self) -> list[UrlMeta]:
        return list(self.__urls)

    @property
    def host(self) -> str:
        return self.__host

    def add(self, *paths: UrlMeta):
        for p in paths:
            if p.host == self.__host:
                self.__paths.add(p.path)
                self.__urls.add(p)

    def path_numbers(self) -> int:
        return len(self.__paths)

    def __str__(self):
        return str({self.__host: {"paths": self.__paths, "urlMeta": self.__urls}})

    def __repr__(self):
        return self.__str__()


class StatsSentUrl:
    """
    statistics the URLs that have been sent.
    get_url_stats return a dict like {'host2': StatsUrlHostView, 'host2': StatsUrlHostView}
    """

    def __init__(self):
        self.__urls_stats: dict[str, StatsUrlHostView] = {}

    def __str__(self):
        return str(self.__urls_stats)

    def __repr__(self):
        return self.__str__()

    def add(self, *reqs: tuple[str, str]):
        for url, method in reqs:
            meta = UrlMeta(url, method)
            if meta.host not in self.__urls_stats:
                self.__urls_stats[meta.host] = StatsUrlHostView(meta.host)
            self.__urls_stats[meta.host].add(meta)

    @property
    def urls_stats(self) -> dict[str, StatsUrlHostView]:
        return self.__urls_stats

    def get_url_stats_by_host(self, host) -> StatsUrlHostView:
        return self.__urls_stats.get(host)


def aggregation(*rests) -> dict[str, StatsUrlHostView]:
    """
    Aggregate all REST request data
    :param rests: Multiple Rest instances.
    """
    stats_sent_urls: dict[str, StatsUrlHostView] = {}

    for rest in rests:
        for k, v in rest.stats_datas.urls_stats.items():
            if k not in stats_sent_urls:
                stats_sent_urls[k] = StatsUrlHostView(k)
            stats_sent_urls[k].add(*v.urls)
    return stats_sent_urls
