import asyncio
import os
from base64 import b64decode as m

import aiohttp
import httpx
import requests
import wget


class DictToObj:
    def __init__(self, dictionary):
        for key, value in dictionary.items():
            if isinstance(value, dict):
                setattr(self, key, DictToObj(value))
            elif isinstance(value, list):
                setattr(self, key, [DictToObj(item) if isinstance(item, dict) else item for item in value])
            else:
                setattr(self, key, value)

    def __repr__(self):
        return f"{self.__dict__}"

class AkenoPlus:
    def __init__(self, key=..., api_endpoint: str = "https://private-akeno.randydev.my.id"):
        if key is Ellipsis:
            self.key = m("cmFuZGlnaXRodWIzNTY=").decode("utf-8")
        elif not key:
            raise ValueError("API key must be provided!")
        else:
            self.key = key
        self.api_endpoint = api_endpoint
        self.headers = {"x-akeno-key": str(self.key)}

    def set_key(self, new_key: str):
        self.key = new_key

    def show_key(self):
        return f"The API key is: {self.key}"

    async def download_now(self, data):
        return wget.download(data)

    async def clean(self, file_path: str):
        try:
            os.remove(file_path)
        except OSError as e:
            return f"Error removing file {file_path}: {e}"

    async def terabox(self, link=None):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.api_endpoint}/akeno/terabox-v1?link={link}", headers=self.headers) as response:
                return await response.json()

    async def terabox_v2(self, link=None):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.api_endpoint}/akeno/terabox-v2?link={link}", headers=self.headers) as response:
                return await response.json()

    async def chatgpt_old(self, query=None):
        payload = {"query": query}
        async with aiohttp.ClientSession() as session:
            async with session.post(f"{self.api_endpoint}/ryuzaki/chatgpt-old", json=payload) as response:
                return await response.json()

    async def chatgpt_mode_web(self, query=None, **params):
        combined_params = {"query": query}
        combined_params.update(params)
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.api_endpoint}/api/akeno-ai-web", params=combined_params) as response:
                return await response.json()

    async def sites_torrens_all(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.api_endpoint}/akeno/sites_torrens_all") as response:
                return await response.json()

    async def search_for_torrents(self, **params):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.api_endpoint}/akeno/search_for_torrents", params=params) as response:
                return await response.json()

    async def get_torrent_from_url(self, **params):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.api_endpoint}/akeno/get_torrent_from_url", params=params) as response:
                return await response.json()

    async def get_recent(self, **params):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.api_endpoint}/akeno/get_recent", params=params) as response:
                return await response.json()

    async def get_category(self, **params):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.api_endpoint}/akeno/get_category", params=params) as response:
                return await response.json()

    async def paal_see(self, files_open=None, **params):
        async with aiohttp.ClientSession() as session:
            form_data = aiohttp.FormData()
            form_data.add_field(
                'file',
                open(files_open, 'rb'),
                filename=os.path.basename(files_open),
                content_type='application/octet-stream'
            )
            async with session.post(f"{self.api_endpoint}/akeno/paal-see", data=form_data, params=params) as response:
                if response.status != 200:
                    raise Exception(f"Error occurred: {response.status}")
                return await response.json()

    async def paal_text_to_image(self, **params):
        async with aiohttp.ClientSession() as session:
            async with session.post(f"{self.api_endpoint}/akeno/paal-text-to-image", params=params, headers=self.headers) as response:
                return await response.json()

    async def google_video_to_text(self, files_open=None, **params):
        async with aiohttp.ClientSession() as session:
            form_data = aiohttp.FormData()
            form_data.add_field(
                'file',
                open(files_open, 'rb'),
                filename=os.path.basename(files_open),
                content_type='application/octet-stream'
            )
            async with session.post(f"{self.api_endpoint}/api/v2/google/video-to-text", data=form_data, params=params) as response:
                if response.status != 200:
                    raise Exception(f"Error occurred: {response.status}")
                return await response.json()

    async def google_image_to_text(self, files_open=None, **params):
        async with aiohttp.ClientSession() as session:
            form_data = aiohttp.FormData()
            form_data.add_field(
                'file',
                open(files_open, 'rb'),
                filename=os.path.basename(files_open),
                content_type='application/octet-stream'
            )
            async with session.post(f"{self.api_endpoint}/api/v2/google/image-to-text", data=form_data, params=params) as response:
                if response.status != 200:
                    raise Exception(f"Error occurred: {response.status}")
                return await response.json()

    async def google_audio_to_text(self, files_open=None, **params):
        async with aiohttp.ClientSession() as session:
            form_data = aiohttp.FormData()
            form_data.add_field(
                'file',
                open(files_open, 'rb'),
                filename=os.path.basename(files_open),
                content_type='application/octet-stream'
            )
            async with session.post(f"{self.api_endpoint}/api/v2/google/audio-to-text", data=form_data, params=params) as response:
                if response.status != 200:
                    raise Exception(f"Error occurred: {response.status}")
                return await response.json()

    async def blackbox(self, query=None):
        params = {"query": query}
        async with aiohttp.ClientSession() as session:
            async with session.post(f"{self.api_endpoint}/ryuzaki/blackbox", params=params, headers=self.headers) as response:
                return await response.json()

    async def hentai(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.api_endpoint}/akeno/hentai", headers=self.headers) as response:
                return await response.json()

    async def fbdown(self, link=None):
        params = {"link": link}
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.api_endpoint}/akeno/fbdown-v2", params=params, headers=self.headers) as response:
                return await response.json()

    async def fdownloader(self, link=None):
        params = {"link": link}
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.api_endpoint}/akeno/fdownloader", params=params, headers=self.headers) as response:
                return await response.json()

    async def capcut(self, link=None):
        params = {"link": link}
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.api_endpoint}/akeno/capcut-v1", params=params, headers=self.headers) as response:
                return await response.json()

    async def add_ipblock(self, ip=None):
        params = {"ip": ip}
        async with aiohttp.ClientSession() as session:
            async with session.post(f"{self.api_endpoint}/add_to_blacklist_ip/", params=params, headers=self.headers_blacklist) as response:
                return await response.json()

    async def unblock_ip(self, ip=None):
        params = {"ip": ip}
        async with aiohttp.ClientSession() as session:
            async with session.post(f"{self.api_endpoint}/remove_from_blacklist_ip", params=params, headers=self.headers_blacklist) as response:
                return await response.json()

    async def allowed_ip(self, ip=None):
        payload = {"ip": ip}
        async with aiohttp.ClientSession() as session:
            async with session.post(f"{self.api_endpoint}/update_allow_ip", json=payload, headers=self.headers_blacklist) as response:
                return await response.json()

    async def unallowed_ip(self, ip=None):
        params = {"ip": ip}
        async with aiohttp.ClientSession() as session:
            async with session.delete(f"{self.api_endpoint}/remove_allow_ip/", params=params, headers=self.headers_blacklist) as response:
                return await response.json()

    async def get_json(self, response=None):
        return DictToObj(response)
