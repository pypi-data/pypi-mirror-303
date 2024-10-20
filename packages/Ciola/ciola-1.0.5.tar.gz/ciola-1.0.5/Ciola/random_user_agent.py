import random

class UserAgentGen:
    def __init__(self):
        self.browsers = {
            "Chrome": {
                "user_agent": "Mozilla/5.0 ({os}; {arch}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{version} Safari/537.36",
                "versions": [
                    "113.0.5672.63", "114.0.5735.90", "115.0.5790.98", "116.0.5845.97",
                    "117.0.5938.92", "118.0.6040.20", "119.0.6136.21"
                ]
            },
            "Firefox": {
                "user_agent": "Mozilla/5.0 ({os}; {arch}) Gecko/20100101 Firefox/{version}",
                "versions": [
                    "114.0", "115.0", "116.0", "117.0", "118.0"
                ]
            },
            "Edge": {
                "user_agent": "Mozilla/5.0 ({os}; {arch}) AppleWebKit/537.36 (KHTML, like Gecko) Edg/{version}",
                "versions": [
                    "113.0.1998.58", "114.0.1823.67", "115.0.1920.77", "116.0.2053.23"
                ]
            },
            "Safari": {
                "user_agent": "Mozilla/5.0 ({os}; {arch}) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/{version} Safari/605.1.15",
                "versions": [
                    "15.6.1", "16.0", "16.1", "16.2", "16.3"
                ]
            },
            "Opera": {
                "user_agent": "Mozilla/5.0 ({os}; {arch}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version} Safari/537.36 OPR/{version}",
                "versions": [
                    "99.0.4788.77", "100.0.4815.27", "101.0.4951.64", "102.0.5071.40"
                ]
            },
            "Internet Explorer": {
                "user_agent": "Mozilla/5.0 ({os}; {arch}) Trident/{trident_version} like Gecko IE/{version}",
                "versions": [
                    "11.0", "10.0", "9.0", "8.0", "7.0"
                ]
            },
        }

        self.operating_systems = {
            "Windows": [
                "Windows NT 10.0; Win64; x64", "Windows NT 10.0; Win32", "Windows NT 11.0; Win64; x64",
                "Windows NT 10.0; ARM", "Windows NT 10.0; WOW64"
            ],
            "Macintosh": [
                "Macintosh; Intel Mac OS X 10_15_7", "Macintosh; Intel Mac OS X 11_0", "Macintosh; Apple Mac OS X 12_3",
                "Macintosh; Apple Mac OS X 13_0"
            ],
            "Linux": [
                "X11; Ubuntu; Linux x86_64", "X11; Debian; Linux x86_64", "X11; Fedora; Linux x86_64",
                "X11; Arch Linux; Linux x86_64", "X11; openSUSE; Linux x86_64"
            ],
            "Android": [
                "Android 10; Mobile", "Android 11; Mobile", "Android 12; Mobile", "Android 13; Mobile",
                "Android 14; Mobile"
            ],
            "iOS": [
                "iPhone; CPU iPhone OS 15_0 like Mac OS X", "iPhone; CPU iPhone OS 16_0 like Mac OS X",
                "iPad; CPU OS 15_0 like Mac OS X", "iPad; CPU OS 16_0 like Mac OS X"
            ]
        }

        self.architectures = {
            "Windows": ["Win64; x64", "Win32", "WOW64", "ARM"],
            "Macintosh": ["Intel Mac OS X", "Apple Mac OS X"],
            "Linux": ["x86_64", "x86"],
            "Android": ["Mobile"],
            "iOS": ["iPhone", "iPad"]
        }

        self.trident_versions = ["7.0"]

    def random_os_and_arch(self):
        os_name = random.choice(list(self.operating_systems.keys()))
        architecture = random.choice(self.architectures[os_name])
        return os_name, architecture

    def generate_user_agent(self, browser):
        os_name, architecture = self.random_os_and_arch()
        version = random.choice(self.browsers[browser]["versions"])
        if browser == "Opera":
            chrome_version = version
            user_agent = self.browsers[browser]["user_agent"].format(
                os=os_name,
                arch=architecture,
                version=version,
                chrome_version=chrome_version
            )
        elif browser == "Internet Explorer":
            trident_version = random.choice(self.trident_versions)
            user_agent = self.browsers[browser]["user_agent"].format(
                os=os_name,
                arch=architecture,
                version=version,
                trident_version=trident_version
            )
        else:
            user_agent = self.browsers[browser]["user_agent"].format(
                os=os_name,
                arch=architecture,
                version=version
            )
        return user_agent

    def chrome(self):
        """Return a random, but realistc user-agent for Chrome"""
        return self.generate_user_agent("Chrome")

    def firefox(self):
        """Return a random, but realistc user-agent for Firefox"""
        return self.generate_user_agent("Firefox")

    def edge(self):
        """Return a random, but realistc user-agent for Microsoft Edge"""
        return self.generate_user_agent("Edge")

    def safari(self):
        """Return a random, but realistc user-agent for Safari"""
        return self.generate_user_agent("Safari")

    def opera(self):
        """Return a random, but realistc user-agent for Opera"""
        return self.generate_user_agent("Opera")

    def internet_explorer(self):
        """Return a random, but realistc user-agent for Internet Explorer"""
        return self.generate_user_agent("Internet Explorer")
