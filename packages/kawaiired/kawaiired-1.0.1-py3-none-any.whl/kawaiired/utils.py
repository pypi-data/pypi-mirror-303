from dataclasses import dataclass
from typing import Literal


BASE_URL = "https://kawaii.red/api"

EndpointType = Literal["gif", "image", "text"]

GifType = Literal[
    "alarm",
    "amazing",
    "ask",
    "baka",
    "bite",
    "blush",
    "blyat",
    "boop",
    "clap",
    "coffee",
    "confused",
    "cry",
    "cuddle",
    "cute",
    "dance",
    "destroy",
    "die",
    "disappear",
    "dodge",
    "error",
    "facedesk",
    "facepalm",
    "fbi",
    "fight",
    "happy",
    "hide",
    "highfive",
    "hug",
    "kill",
    "kiss",
    "laugh",
    "lick",
    "lonely",
    "love",
    "mad",
    "money",
    "nom",
    "nosebleed",
    "ok",
    "party",
    "pat",
    "peek",
    "poke",
    "pout",
    "protect",
    "puke",
    "punch",
    "purr",
    "pusheen",
    "run",
    "salute",
    "scared",
    "scream",
    "shame",
    "shocked",
    "shoot",
    "shrug",
    "sip",
    "sit",
    "slap",
    "sleepy",
    "smile",
    "smoke",
    "smug",
    "spin",
    "stare",
    "stomp",
    "tickle",
    "trap",
    "triggered",
    "uwu",
    "wasted",
    "wave",
    "wiggle",
    "wink",
    "yeet",
]


@dataclass
class Stats:
    endpoints: list
    all: int
    failed: int
    history: list
    most_endpoint: dict
    most_endpoints: list
    most_type: dict
    most_types: list
