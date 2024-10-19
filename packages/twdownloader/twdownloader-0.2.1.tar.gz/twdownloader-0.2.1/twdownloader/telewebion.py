from components.my_requests import Request
import json
import urllib.request

request = Request()


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
            response = request.get_request(url, headers=headers, proxy=proxy, timeout=200)
            print(response.status_code)
            data = json.loads(response.text)
            break
        except Exception as e:
            print(e)
    if len(data['body']['queryChannel']) > 0 and len(data['body']['queryChannel'][0]['episodes']) > 5:
        for episode in data['body']['queryChannel'][0]['episodes']:
            try:
                print(episode['EpisodeID'], 'Downloading ...')
                urllib.request.urlretrieve(
                    f"https://dl.telewebion.com/dc51a6c1-f185-4d67-b409-16269d2c963b/{episode['EpisodeID']}/480p/",
                    f'./video-{episode['EpisodeID']}-{from_date}-{to_date}.mp4')
                print(episode['EpisodeID'], 'Done')
            except Exception as e:
                continue
