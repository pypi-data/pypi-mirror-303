<p align="center">
    <b>Sosial Media Downloader API for Python</b>
    <br>
    <a href="https://github.com/AyiinXd/sosmed">
        Homepage
    </a>
    •
    <a href="https://github.com/AyiinXd/sosmed/releases">
        Releases
    </a>
    •
    <a href="https://t.me/AyiinChannel">
        News
    </a>
</p>

## Sosmed

> Multiple Site Provider and Asynchronous API in Python

``` python
from sosmed import Sosmed


sosmed = Sosmed(
    apiToken="YOUR_API_TOKEN",
    secret="YOUR_SECRET_TOKEN"
)

async def instagramDl():
    url = 'https://www.instagram.com/reel/DA2qTBspJPh/?igsh=ZjM4M2ZydWFjYzRt';
    res = await sosmed.instagram(url=url)
    path = await res.download()
    print(res.videoUrl)
    print(path)

async def tiktokDl():
    url = 'https://vt.tiktok.com/ZS2oQvs1s/';
    res = await sosmed.tiktok(url=url)
    path = await res.download()
    print(res.parse())
    print(path)

async def twitterDl():
    url = 'https://x.com/HumansNoContext/status/1848152497476493332?t=wncNBDv7iRegV_lXgvcl3Q&s=19';
    res = await sosmed.twitter(url=url)
    path = await res.download()
    print(res.mediaExtended[0].parse())
    print(path)

```


### Installation

``` bash
pip3 install sosmed
```


### License

[MIT License](https://github.com/AyiinXd/pyPorn/blob/master/LICENSE)
