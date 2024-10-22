import re
from datetime import datetime

from funcy import group_by

from ..log import LOGGER
from .vars import servers_v


def group(seq, f):
    _tmp = group_by(f, seq)
    return _tmp[True], _tmp[False]


HK_REGEX = re.compile(r"香港|HK|HongKong", re.IGNORECASE)
TW_REGEX = re.compile(r"台湾|TW|Taiwan", re.IGNORECASE)
SG_REGEX = re.compile(r"新加坡|SG|Singapore", re.IGNORECASE)
JP_REGEX = re.compile(r"日本|JP|Japan", re.IGNORECASE)
KR_REGEX = re.compile(r"韩国|KR|KOR|Korea", re.IGNORECASE)
US_REGEX = re.compile(r"USA|US|美国", re.IGNORECASE)
EU_REGEX = re.compile(
    (
        r"UK|GBR|英国|DNK|NLD|Netherlands|POL|"
        r"西班牙|ESP|法国|FRA|德国|DEU|Germany|France"
        r"|Switzerland|Sweden|Austria|Ireland|Hungary"
        r"|Ireland|Ireland"
    ),
    re.IGNORECASE,
)
AUS_RUS_REGEX = re.compile(r"RUS|俄|澳大利亚|AUS|Russia|Australia", re.IGNORECASE)


def get():
    servers = servers_v.get()
    # rules = rules_v.get()
    proxy_names = [server["name"] for server in servers]
    proxy_names.sort()
    LOGGER.info("共 %d 个服务器信息", len(proxy_names))
    HK, remain = group(proxy_names, lambda name: bool(re.findall(HK_REGEX, name)))
    TW, remain = group(remain, lambda name: bool(re.findall(TW_REGEX, name)))
    SG, remain = group(remain, lambda name: bool(re.findall(SG_REGEX, name)))
    RUS_AUS, remain = group(remain, lambda name: bool(re.findall(AUS_RUS_REGEX, name)))
    US, remain = group(remain, lambda name: bool(re.findall(US_REGEX, name)))
    JP, remain = group(remain, lambda name: bool(re.findall(JP_REGEX, name)))
    KR, remain = group(remain, lambda name: bool(re.findall(KR_REGEX, name)))
    EU, remain = group(remain, lambda name: bool(re.findall(EU_REGEX, name)))
    remain.extend(RUS_AUS)
    Others = remain
    now = datetime.now().strftime("%m%d%Y-%H:%M:%S")
    others_name = f"👀Others@{now}"
    all_groups = [
        "🇭🇰HK",
        "🇭🇰HK_S",
        "🇭🇰HK-hash",
        "🇭🇰HK-round",
        "🇹🇼TW",
        "🇹🇼TW_S",
        "🇸🇬SG",
        "🇸🇬SG_S",
        "🇸🇬SG-hash",
        "🇸🇬SG-round",
        "🇺🇸US",
        "🇺🇸US_S",
        "🇯🇵JP-hash",
        "🇯🇵JP-round",
        "🇯🇵JP_S",
        "🇯🇵JP",
        "🇰🇷KR",
        "🇪🇺EU",
        "🇪🇺EU_S",
        others_name,
    ]
    proxy_groups = [
        {
            "name": "PROXY",
            "type": "select",
            "proxies": all_groups,
        },
        #        {
        #            "name": "HOME",
        #            "type": "select",
        #            "proxies": all_groups,
        #        },
        {
            "name": "学术网站",
            "type": "select",
            "proxies": [
                "DIRECT",
                "PROXY",
            ]
            + all_groups,
        },
        {
            "name": "🐳DOCKER",
            "type": "select",
            "proxies": [
                "PROXY",
                "DIRECT",
            ]
            + all_groups,
        },
        {
            "name": "Apple",
            "type": "select",
            "proxies": [
                "DIRECT",
                "PROXY",
            ]
            + all_groups,
        },
        {
            "name": "Apple Domestic",
            "type": "select",
            "proxies": [
                "DIRECT",
                "PROXY",
            ]
            + all_groups,
        },
        {
            "name": "Apple Music",
            "type": "select",
            "proxies": [
                "DIRECT",
                "PROXY",
            ]
            + all_groups,
        },
        {
            "name": "Apple OutSide",
            "type": "select",
            "proxies": [
                "PROXY",
                "DIRECT",
            ]
            + all_groups,
        },
        {
            "name": "BiliBili",
            "type": "select",
            "proxies": [
                "DIRECT",
                "PROXY",
            ]
            + all_groups,
        },
        {
            "name": "DisneyPlus",
            "type": "select",
            "proxies": [
                "🇹🇼TW",
                "🇹🇼TW_S",
                "🇸🇬SG_S",
                "🇭🇰HK_S",
                "PROXY",
            ],
        },
        {
            "name": "Google",
            "type": "select",
            "proxies": [
                "PROXY",
                "DIRECT",
            ]
            + all_groups,
        },
        {
            "name": "Google Domestic",
            "type": "select",
            "proxies": [
                "DIRECT",
                "PROXY",
            ]
            + all_groups,
        },
        {
            "name": "Microsoft",
            "type": "select",
            "proxies": [
                "DIRECT",
                "PROXY",
            ]
            + all_groups,
        },
        {
            "name": "Microsoft Domestic",
            "type": "select",
            "proxies": [
                "DIRECT",
                "PROXY",
            ]
            + all_groups,
        },
        {
            "name": "Netflix",
            "type": "select",
            "proxies": [
                "🇹🇼TW",
                "🇹🇼TW_S",
                "🇸🇬SG_S",
                "🇭🇰HK_S",
                "PROXY",
            ],
        },
        {
            "name": "OpenAI",
            "type": "select",
            "proxies": [
                "🇺🇸US_S",
                "🇺🇸US",
                "PROXY",
                others_name,
            ],
        },
        {
            "name": "Sony",
            "type": "select",
            "proxies": [
                "DIRECT",
                "PROXY",
            ]
            + all_groups,
        },
        {
            "name": "Steam",
            "type": "select",
            "proxies": [
                "DIRECT",
                "PROXY",
            ]
            + all_groups,
        },
        {
            "name": "Telegram",
            "type": "select",
            "proxies": [
                "PROXY",
                "DIRECT",
            ]
            + all_groups,
        },
        {
            "name": "YouTube",
            "type": "select",
            "proxies": [
                "🇹🇼TW",
                "🇹🇼TW_S",
                "🇸🇬SG_S",
                "🇭🇰HK_S",
                "PROXY",
            ],
        },
        {
            "name": "直连",
            "type": "select",
            "proxies": [
                "DIRECT",
                "PROXY",
            ]
            + all_groups,
        },
        {
            "name": "禁连",
            "type": "select",
            "proxies": ["REJECT", "DIRECT"],
        },
        #    {
        #    "name": "HYMAC",
        #    "type": "select",
        #    "tolerance": 100,
        #    "lazy": False,
        #    "url": 'http://wifi.vivo.com.cn/generate_204',
        #    "interval": 300,
        #    "disable-udp": True,
        #    "proxies": ["HY", "PASS"]
        # },
        {
            "name": "🇭🇰HK",
            "type": "url-test",
            "tolerance": 100,
            "lazy": True,
            "url": "https://i.ytimg.com/generate_204",
            "interval": 300,
            "strategy": "consistent-hashing",
            "disable-udp": False,
            "proxies": HK,
        },
        {"name": "🇭🇰HK_S", "type": "select", "proxies": HK},
        {
            "name": "🇭🇰HK-hash",
            "type": "load-balance",
            "strategy": "consistent-hashing",
            "tolerance": 100,
            "lazy": True,
            "url": "https://i.ytimg.com/generate_204",
            "interval": 900,
            "disable-udp": False,
            "proxies": HK,
        },
        {
            "name": "🇭🇰HK-round",
            "type": "load-balance",
            "strategy": "round-robin",
            "tolerance": 100,
            "lazy": True,
            "url": "https://i.ytimg.com/generate_204",
            "interval": 900,
            "disable-udp": False,
            "proxies": HK,
        },
        {
            "name": "🇹🇼TW",
            "type": "url-test",
            "tolerance": 100,
            "lazy": True,
            "url": "https://i.ytimg.com/generate_204",
            "interval": 300,
            "disable-udp": False,
            "proxies": TW,
        },
        {"name": "🇹🇼TW_S", "type": "select", "proxies": TW},
        {
            "name": "🇸🇬SG",
            "type": "url-test",
            "tolerance": 100,
            "lazy": True,
            "url": "https://i.ytimg.com/generate_204",
            "interval": 900,
            "disable-udp": False,
            "proxies": SG,
        },
        {"name": "🇸🇬SG_S", "type": "select", "proxies": SG},
        {
            "name": "🇸🇬SG-hash",
            "type": "load-balance",
            "strategy": "consistent-hashing",
            "tolerance": 100,
            "lazy": True,
            "url": "https://i.ytimg.com/generate_204",
            "interval": 900,
            "disable-udp": False,
            "proxies": SG,
        },
        {
            "name": "🇸🇬SG-round",
            "type": "load-balance",
            "strategy": "round-robin",
            "tolerance": 100,
            "lazy": True,
            "url": "https://i.ytimg.com/generate_204",
            "interval": 900,
            "disable-udp": False,
            "proxies": SG,
        },
        {
            "name": "🇺🇸US",
            "type": "url-test",
            "tolerance": 100,
            "lazy": True,
            "url": "https://i.ytimg.com/generate_204",
            "interval": 900,
            "disable-udp": False,
            "proxies": US,
        },
        {"name": "🇺🇸US_S", "type": "select", "proxies": US},
        {
            "name": "🇯🇵JP-hash",
            "type": "load-balance",
            "strategy": "consistent-hashing",
            "tolerance": 100,
            "lazy": True,
            "url": "https://i.ytimg.com/generate_204",
            "interval": 900,
            "disable-udp": False,
            # "proxies": [name for name in JP if name.find("JPN") > -1],
            "proxies": JP,
        },
        {
            "name": "🇯🇵JP-round",
            "type": "load-balance",
            "strategy": "round-robin",
            "tolerance": 100,
            "lazy": True,
            "url": "https://i.ytimg.com/generate_204",
            "interval": 900,
            "disable-udp": False,
            # "proxies": [name for name in JP if name.find("JPN") > -1],
            "proxies": JP,
        },
        {"name": "🇯🇵JP_S", "type": "select", "proxies": JP},
        {
            "name": "🇯🇵JP",
            "type": "url-test",
            "tolerance": 100,
            "lazy": True,
            "url": "https://i.ytimg.com/generate_204",
            "interval": 900,
            "disable-udp": False,
            "proxies": JP,
        },
        {
            "name": "🇰🇷KR",
            "type": "url-test",
            "tolerance": 100,
            "lazy": True,
            "url": "https://i.ytimg.com/generate_204",
            "interval": 900,
            "disable-udp": False,
            "proxies": KR,
        },
        {
            "name": "🇪🇺EU",
            "type": "url-test",
            "tolerance": 100,
            "lazy": True,
            "url": "https://www.google.co.uk/generate_204",
            "interval": 900,
            "disable-udp": True,
            "proxies": EU,
        },
        {"name": "🇪🇺EU_S", "type": "select", "proxies": EU},
        {"name": others_name, "type": "select", "proxies": Others},
    ]
    return proxy_groups
