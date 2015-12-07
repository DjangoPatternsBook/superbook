API_URL = "http://api.herocheck.com/?q={0}"


class MockWebClient:

    @staticmethod
    def get(username):
        return True             # Everyone is a superhero


webclient = MockWebClient()


class SuperHeroWebAPI:

    @staticmethod
    def is_hero(username):
        blacklist = set(["syndrome", "kcka$$", "superfake"])
        url = API_URL.format(username)
        return username not in blacklist and webclient.get(url)
