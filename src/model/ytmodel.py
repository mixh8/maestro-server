from typing import List


class YtResult:
    def __init__(self, title, url, channel, thumbnail_url):
        self.title = title
        self.url = url
        self.thumbnail_url = thumbnail_url
        self.channel = channel

    def serialize(self):
        return {
            "title": self.title,
            "url": self.url,
            "thumbnail_url": self.thumbnail_url,
            "channel": self.channel
        }

class YtResponse:
    def __init__(self, results: List[YtResult]):
        self.results = results

    def serialize(self):
        return [result.serialize() for result in self.results]
    
class Response:
    def __init__(self, data, status_code):
        self.data = data
        self.status_code = status_code

    def serialize(self):
        return {
            "data": self.data,
            "status_code": self.status_code
        }