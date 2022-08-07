from __future__ import annotations
from dataclasses import dataclass

__VERSION__ = "1.6.0"


@dataclass
class Channels:
    suggestion: int = 982353129913851924
    bug_report: int = 982669110926250004
    errors: int = 986531210283069450
    reddit_faq: int = 985908874362093620
    tickets: int = 1005904969737711760
    logs: int = 977581277010100315
    staff_vote: int = 1005741491861344286

    @classmethod
    def dev(cls):
        cls.suggestion: int = 985554479405490216
        cls.bug_report: int = 985554459948122142
        cls.reddit_faq: int = 985908874362093620
        cls.tickets: int = 1003006753564262452
        cls.logs: int = 988162723890217040
        cls.staff_vote: int = 1002132747441152071
        return cls


@dataclass
class Roles:
    staff: int = 985943266115584010

    @classmethod
    def dev(cls):
        cls.staff: int = 1005904440039047208
        return cls


@dataclass
class Colors:
    invis: int = 0x2F3136
    white: int = 0xFFFFFF


def status(stat):
    statuses = {
        "dnd": "<:dnd:879146778182692934>",
        "online": "<:online:879146898219483176>",
        "offline": "<:offline:879146897951035435>",
        "idle": "<:idle:879146778388205618>",
        "streaming": "<:streaming:879146899809128478>",
    }
    return statuses[stat]


IGNORE_EXCEPTIONS = ["UserBlacklisted"]
morse = {
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-",
}
TICKET_PERMS = {
    "send_messages": True,
    "read_messages": True,
    "add_reactions": True,
    "embed_links": True,
    "attach_files": True,
    "read_message_history": True,
    "external_emojis": True,
}
tag_help = {
    "public": {
        "tag get (or /t)": "Gives you the tags value",
        "tag create": "Creates a tag",
        "tag help": "Gives you this help",
        "tag info": "Gives you the tags info (views, owner, etc)",
        "tag list": "Gives you a lists of tags (use the arrows to navigate)",
        "tag claim": "Claims a tag (can only be used if the previous owner is no longer in the server)",
    },
    "owner_only": {
        "tag rename": "Renames a tag",
        "tag edit": "Edits a tag",
        "tag transfer": "Transfers a tag to another user",
        "tag delete": "Deletes a tag",
        "tag alias add": "Adds an alias to a tag",
        "tag alias remove": "Removes an alias from a tag",
    },
}
# noinspection SpellCheckingInspection
COUNTRIES = {
    "🇦🇫": "Afghanistan",
    "🇦🇱": "Albania",
    "🇩🇿": "Algeria",
    "🇦🇩": "Andorra",
    "🇦🇴": "Angola",
    "🇦🇮": "Anguilla",
    "🇦🇬": "Antigua and Barbuda",
    "🇦🇷": "Argentina",
    "🇦🇲": "Armenia",
    "🇦🇺": "Australia",
    "🇦🇹": "Austria",
    "🇦🇿": "Azerbaijan",
    "🇧🇸": "Bahamas",
    "🇧🇭": "Bahrain",
    "🇧🇩": "Bangladesh",
    "🇧🇧": "Barbados",
    "🇧🇾": "Belarus",
    "🇧🇪": "Belgium",
    "🇧🇿": "Belize",
    "🇧🇯": "Benin",
    "🇧🇲": "Bermuda",
    "🇧🇹": "Bhutan",
    "🇧🇴": "Bolivia",
    "🇧🇦": "Bosnia and Herzegovina",
    "🇧🇼": "Botswana",
    "🇧🇷": "Brazil",
    "🇧🇳": "Brunei",
    "🇧🇬": "Bulgaria",
    "🇧🇫": "Burkina Faso",
    "🇧🇮": "Burundi",
    "🇰🇭": "Cambodia",
    "🇨🇲": "Cameroon",
    "🇨🇦": "Canada",
    "🇨🇻": "Cape Verde",
    "🇰🇾": "Cayman Islands",
    "🇨🇫": "Central African Republic",
    "🇹🇩": "Chad",
    "🇨🇱": "Chile",
    "🇨🇳": "China",
    "🇨🇴": "Colombia",
    "🇨🇬": "Republic of the Congo",
    "🇨🇩": "DR Congo",
    "🇨🇷": "Costa Rica",
    "🇨🇮": "Ivory Coast",
    "🇭🇷": "Croatia",
    "🇨🇺": "Cuba",
    "🇨🇾": "Cyprus",
    "🇨🇿": "Czechia",
    "🇩🇰": "Denmark",
    "🇩🇯": "Djibouti",
    "🇩🇲": "Dominica",
    "🇩🇴": "Dominican Republic",
    "🇪🇨": "Ecuador",
    "🇪🇬": "Egypt",
    "🇸🇻": "El Salvador",
    "🇬🇶": "Equatorial Guinea",
    "🇪🇷": "Eritrea",
    "🇪🇪": "Estonia",
    "🇸🇿": "Eswatini",
    "🇪🇹": "Ethiopia",
    "🇫🇯": "Fiji",
    "🇫🇮": "Finland",
    "🇫🇷": "France",
    "🇬🇦": "Gabon",
    "🇬🇲": "Gambia",
    "🇬🇪": "Georgia",
    "🇩🇪": "Germany",
    "🇬🇭": "Ghana",
    "🇬🇷": "Greece",
    "🇬🇩": "Grenada",
    "🇬🇺": "Guam",
    "🇬🇹": "Guatemala",
    "🇬🇳": "Guinea",
    "🇬🇼": "Guinea-Bissau",
    "🇬🇾": "Guyana",
    "🇭🇹": "Haiti",
    "🇭🇳": "Honduras",
    "🇭🇺": "Hungary",
    "🇮🇸": "Iceland",
    "🇮🇳": "India",
    "🇮🇩": "Indonesia",
    "🇮🇷": "Iran",
    "🇮🇶": "Iraq",
    "🇮🇪": "Ireland",
    "🇮🇱": "Israel",
    "🇮🇹": "Italy",
    "🇯🇲": "Jamaica",
    "🇯🇵": "Japan",
    "🇯🇴": "Jordan",
    "🇰🇿": "Kazakhstan",
    "🇰🇪": "Kenya",
    "🇰🇮": "Kiribati",
    "🇰🇵": "North Korea",
    "🇰🇷": "South Korea",
    "🇽🇰": "Kosovo",
    "🇰🇼": "Kuwait",
    "🇰🇬": "Kyrgyzstan",
    "🇱🇦": "Laos",
    "🇱🇻": "Latvia",
    "🇱🇧": "Lebanon",
    "🇱🇸": "Lesotho",
    "🇱🇷": "Liberia",
    "🇱🇾": "Libya",
    "🇱🇮": "Liechtenstein",
    "🇱🇹": "Lithuania",
    "🇱🇺": "Luxembourg",
    "🇲🇬": "Madagascar",
    "🇲🇼": "Malawi",
    "🇲🇾": "Malaysia",
    "🇲🇻": "Maldives",
    "🇲🇱": "Mali",
    "🇲🇹": "Malta",
    "🇲🇷": "Mauritania",
    "🇲🇺": "Mauritius",
    "🇲🇽": "Mexico",
    "🇫🇲": "Micronesia",
    "🇲🇩": "Moldova",
    "🇲🇨": "Monaco",
    "🇲🇳": "Mongolia",
    "🇲🇪": "Montenegro",
    "🇲🇦": "Morocco",
    "🇲🇿": "Mozambique",
    "🇲🇲": "Myanmar",
    "🇳🇦": "Namibia",
    "🇳🇷": "Nauru",
    "🇳🇵": "Nepal",
    "🇳🇱": "Netherlands",
    "🇳🇿": "New Zealand",
    "🇳🇮": "Nicaragua",
    "🇳🇪": "Niger",
    "🇳🇬": "Nigeria",
    "🇳🇺": "Niue",
    "🇲🇰": "North Macedonia",
    "🇳🇴": "Norway",
    "🇴🇲": "Oman",
    "🇵🇰": "Pakistan",
    "🇵🇼": "Palau",
    "🇵🇦": "Panama",
    "🇵🇬": "Papua New Guinea",
    "🇵🇾": "Paraguay",
    "🇵🇪": "Peru",
    "🇵🇭": "Philippines",
    "🇵🇱": "Poland",
    "🇵🇹": "Portugal",
    "🇶🇦": "Qatar",
    "🇷🇴": "Romania",
    "🇷🇺": "Russia",
    "🇷🇼": "Rwanda",
    "🇰🇳": "Saint Kitts and Nevis",
    "🇱🇨": "Saint Lucia",
    "🇲🇫": "Saint Martin",
    "🇻🇨": "Saint Vincent and the Grenadines",
    "🇼🇸": "Samoa",
    "🇸🇲": "San Marino",
    "🇸🇹": "São Tomé and Príncipe",
    "🇸🇦": "Saudi Arabia",
    "🇸🇳": "Senegal",
    "🇷🇸": "Serbia",
    "🇸🇨": "Seychelles",
    "🇸🇱": "Sierra Leone",
    "🇸🇬": "Singapore",
    "🇸🇰": "Slovakia",
    "🇸🇮": "Slovenia",
    "🇸🇧": "Solomon Islands",
    "🇸🇴": "Somalia",
    "🇿🇦": "South Africa",
    "🇪🇸": "Spain",
    "🇱🇰": "Sri Lanka",
    "🇸🇩": "Sudan",
    "🇸🇷": "Suriname",
    "🇸🇪": "Sweden",
    "🇨🇭": "Switzerland",
    "🇸🇾": "Syria",
    "🇹🇼": "Taiwan",
    "🇹🇯": "Tajikistan",
    "🇹🇿": "Tanzania",
    "🇹🇭": "Thailand",
    "🇹🇱": "Timor-Leste",
    "🇹🇬": "Togo",
    "🇹🇴": "Tonga",
    "🇹🇹": "Trinidad and Tobago",
    "🇹🇳": "Tunisia",
    "🇹🇷": "Turkey",
    "🇹🇲": "Turkmenistan",
    "🇹🇻": "Tuvalu",
    "🇺🇬": "Uganda",
    "🇺🇦": "Ukraine",
    "🇦🇪": "United Arab Emirates",
    "🇬🇧": "United Kingdom",
    "🇺🇸": "United States",
    "🇺🇾": "Uruguay",
    "🇺🇿": "Uzbekistan",
    "🇻🇺": "Vanuatu",
    "🇻🇦": "Vatican City",
    "🇻🇪": "Venezuela",
    "🇻🇳": "Vietnam",
    "🇾🇪": "Yemen",
    "🇿🇲": "Zambia",
    "🇿🇼": "Zimbabwe",
}

# noinspection SpellCheckingInspection
VALID_CODE_LANGUAGES = [
    "abap",
    "aes",
    "apex",
    "awk",
    "azcli",
    "bat",
    "bicep",
    "c",
    "cameligo",
    "cjam",
    "clojure",
    "cobol",
    "coffeescript",
    "cow",
    "cpp",
    "crystal",
    "csharp",
    "csp",
    "css",
    "d",
    "dart",
    "dash",
    "dockerfile",
    "dragon",
    "ecl",
    "elixir",
    "emacs",
    "erlang",
    "fortran",
    "fsharp",
    "go",
    "golfscript",
    "graphql",
    "groovy",
    "handlebars",
    "haskell",
    "hcl",
    "html",
    "ini",
    "java",
    "javascript",
    "jelly",
    "json",
    "julia",
    "kotlin",
    "less",
    "lexon",
    "liquid",
    "lisp",
    "lua",
    "lolcode",
    "m3",
    "markdown",
    "mips",
    "msdax",
    "mysql",
    "sql",
    "objective-c",
    "nasm",
    "nasm64",
    "nim",
    "ocaml",
    "octave",
    "osabie",
    "paradoc",
    "pascal",
    "pascaligo",
    "perl",
    "pgsql",
    "php",
    "plaintext",
    "ponylang",
    "postiats",
    "powerquery",
    "powershell",
    "prolog",
    "pure",
    "pug",
    "py",
    "pyth",
    "python",
    "python2",
    "qsharp",
    "r",
    "raku",
    "razor",
    "redis",
    "redshift",
    "restructuredtext",
    "rockstar",
    "ruby",
    "rust",
    "sb",
    "scala",
    "scheme",
    "scss",
    "shell",
    "sol",
    "sparql",
    "st",
    "swift",
    "systemverilog",
    "tcl",
    "twig",
    "typescript",
    "vb",
    "verilog",
    "vlang",
    "xml",
    "yaml",
    "yeethon",
    "zig",
]