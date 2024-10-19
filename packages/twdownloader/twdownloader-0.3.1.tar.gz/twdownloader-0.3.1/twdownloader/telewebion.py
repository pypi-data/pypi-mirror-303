import json
import os
import urllib.request
import io
import random

import m3u8
import requests


class Request:
    user_agent_list = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
        'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
        'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)',
        'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
        'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'
    ]

    def __init__(self, proxy=None):
        self.proxy = proxy

    def get_request(self, url, params=None, headers=None, proxy=None, timeout=10, **kwargs):
        params, headers, proxy = self._prepare_args(params, headers, proxy)
        session = self.get_session(proxy)
        res = session.get(url, params=params,
                          headers=headers, timeout=timeout, **kwargs)
        return res

    def post_request(self, url, params=None, headers=None, proxy=None, timeout=10, **kwargs):
        params, headers, proxy = self._prepare_args(params, headers, proxy)
        session = self.get_session(proxy)
        res = session.post(url, params=params,
                           headers=headers, timeout=timeout, **kwargs)
        return res

    def get_download(self, url, params=None, headers=None, proxy=None, timeout=10, **kwargs):
        params, headers, proxy = self._prepare_args(params, headers, proxy)
        session = self.get_session(proxy)
        response = session.get(url, params=params,
                               headers=headers, timeout=timeout, **kwargs)
        if response.status_code == 200:
            image_bytes = response.content
            raw_img = io.BytesIO(image_bytes)
            return raw_img
        else:
            return None

    def random_user_agent(self):
        return random.choice(self.user_agent_list)

    def get_session(self, proxy):
        session = requests.session()
        if proxy is None:
            return session
        session.proxies = {}
        proxy_type = proxy['protocol']
        if 'socks5' == proxy_type.lower():
            proxy_type = 'socks5h'
        if 'username' in proxy and proxy['username'] is not None:
            session.proxies['http'] = proxy_type.lower() + '://' + proxy['username'] + ':' + proxy[
                'password'] + '@' + \
                                      proxy['ip'] + ':' + proxy['port']
            session.proxies['https'] = proxy_type.lower() + '://' + proxy['username'] + ':' + proxy[
                'password'] + '@' + \
                                       proxy['ip'] + ':' + proxy['port']
        else:
            session.proxies['http'] = proxy_type.lower() + '://' + proxy['ip'] + ':' + proxy['port']
            session.proxies['https'] = proxy_type.lower() + '://' + proxy['ip'] + ':' + proxy['port']

        return session

    def _prepare_args(self, params, headers, proxy):
        if headers is None:
            headers = {}
        headers['User-Agent'] = self.random_user_agent()
        if params is None:
            params = {}
        if proxy is None:
            proxy = self.proxy
        return params, headers, proxy


def get_episodes(from_date='2022-05-02T00:00:00', to_date='2022-05-02T23:59:59', proxy='tor'):
    payload = {}
    headers = {
        'authority': 'gateway.twdownloader.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9,fa-IR;q=0.8,fa;q=0.7',
        'origin': 'https://telewebion.com',
        'referer': 'https://telewebion.com/',
        'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
    }
    url = (f"https://gateway.telewebion.com/kandoo/channel/getChannelEpisodesByDate/"
           f"?ChannelDescriptor=irinn&IsClip=false&First=50"
           f"&Offset=0&FromDate={from_date}&ToDate={to_date}")
    if proxy == 'tor':
        proxy = {
            'ip': '127.0.0.1',
            'port': '9050',
            'protocol': 'socks5',
        }
    while True:
        try:
            response = Request().get_request(url, headers=headers, proxy=proxy, timeout=200)
            print(response.status_code)
            data = json.loads(response.text)
            break
        except Exception as e:
            print(e)
    if len(data['body']['queryChannel']) > 0 and len(data['body']['queryChannel'][0]['episodes']) > 5:
        for episode in data['body']['queryChannel'][0]['episodes']:
            try:
                response = Request().get_request(url=f"https://cdna-bsht1c83.telewebion.com/irinn/episode/{episode['EpisodeID']}/playlist.m3u8")
                m3u8_playlist = m3u8.loads(response.text)
                m3_response = Request().get_request(url=f"https://cdna-bsht1c84.telewebion.com/irinn/episode/{episode['EpisodeID']}/{m3u8_playlist.data['playlists'][0]['uri']}")
                m3u8_index = m3u8.loads(m3_response.text)
                print(episode['EpisodeID'], 'Downloading ...')
                for segment in m3u8_index.files:
                    content = Request().get_request(url=f"https://cdna-bsht1c84.telewebion.com/irinn/episode/{episode['EpisodeID']}/{m3u8_playlist.data['playlists'][0]['uri'].split('/')[0]}/{segment}")
                    try:
                        os.makedirs('./videos', exist_ok=True)
                    except Exception as e:
                        pass
                    try:
                        with open('./videos' + f"/video-{episode['EpisodeID']}-{from_date}-{to_date}", 'ab+') as f:
                            f.write(content.content)
                    except TypeError:
                        return
                print(episode['EpisodeID'], 'Done')
            except Exception as e:
                print(episode['EpisodeID'],'Failed .....')
                continue

get_episodes(from_date='2024-10-15T00:00:00',to_date='2025-10-15T23:59:00')