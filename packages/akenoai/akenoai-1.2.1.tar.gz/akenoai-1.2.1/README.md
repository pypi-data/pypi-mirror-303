# akenoai-lib
- install : `pip3 install akenoai[porno]`

### Google-Dev
> performance high speed API
> `google_video_to_text`
> `google_audio_to_text`

> params string optional: `prompt`, `mime_type`

### Example this
```python
import akenoai as dev

file_path = "example.jpg"

api = dev.AkenoPlus(key=...)

response = await api.google_image_to_text(files_open=file_path)

print(response)
```

### Paal AI Dev
> method `paal_see`

> params string optional: `lang="en"` and `is_trans="True"`

### Example this
```python
import akenoai as dev

file_path = "example.jpg"
api = dev.AkenoPlus(key=...)
response = await api.paal_see(files_open=file_path)
print(response)

response_2 = await api.paal_text_to_image(prompt="cat beautiful")
print(response_2)
```

# Attribute
```python
# Use await
import akenoai as ak
_ = ak.AkenoPlus(key=...)
_.download_now(data)
_.clean(file_path)
_.terabox(link)
_.terabox_v2(link)
_.chatgpt_old(query)
_.chatgpt_mode_web(query)
_.sites_torrens_all()
_.search_for_torrents(params)
_.get_torrent_from_url(params)
_.get_recent(params)
_.get_category(params)
_.paal_see(files_open, params)
_.google_video_to_text(files_open, params)
_.google_image_to_text(files_open, params)
_.google_audio_to_text(files_open, params)
_.blackbox(query)
_.fbdown(link)
_.fdownloader(link)
_.capcut(link)

# Pornohub
# Use await
import akenoai as ak
_ = ak.Pornohub(key=...)
_.x_search(query)
_.x_download(query)
_.x_download(url, is_stream=True)
```

# License
[![License](https://www.gnu.org/graphics/agplv3-155x51.png)](LICENSE)
TeamKillerX is licensed under [GNU Affero General Public License](https://www.gnu.org/licenses/agpl-3.0.en.html) v3 or later.

<h4 align="center">Copyright (C) 2019 - 2024 The AkenoAI <a href="https://github.com/TeamKillerX">TeamKillerX</a>
<a href="https://t.me/xtdevs">@xtdevs</a>
</h4>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Project [RyuzakiLib](https://github.com/TeamKillerX/) is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
