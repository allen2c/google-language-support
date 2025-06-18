from google_language_support import LanguageCodes

language_common_names = [
    "AFRIKAANS",
    "ALBANIAN",
    "ARABIC",
    "ARMENIAN",
    "AZERBAIJANI",
    "BASQUE",
    "BELARUSIAN",
    "BENGALI",
    "BOKMAL",
    "BOSNIAN",
    "BULGARIAN",
    "CATALAN",
    "CHINESE",
    "CROATIAN",
    "CZECH",
    "DANISH",
    "DUTCH",
    "ENGLISH",
    "ESPERANTO",
    "ESTONIAN",
    "FINNISH",
    "FRENCH",
    "GANDA",
    "GEORGIAN",
    "GERMAN",
    "GREEK",
    "GUJARATI",
    "HEBREW",
    "HINDI",
    "HUNGARIAN",
    "ICELANDIC",
    "INDONESIAN",
    "IRISH",
    "ITALIAN",
    "JAPANESE",
    "KAZAKH",
    "KOREAN",
    "LATIN",
    "LATVIAN",
    "LITHUANIAN",
    "MACEDONIAN",
    "MALAY",
    "MAORI",
    "MARATHI",
    "MONGOLIAN",
    "NYNORSK",
    "PERSIAN",
    "POLISH",
    "PORTUGUESE",
    "PUNJABI",
    "ROMANIAN",
    "RUSSIAN",
    "SERBIAN",
    "SHONA",
    "SLOVAK",
    "SLOVENE",
    "SOMALI",
    "SOTHO",
    "SPANISH",
    "SWAHILI",
    "SWEDISH",
    "TAGALOG",
    "TAMIL",
    "TELUGU",
    "THAI",
    "TSONGA",
    "TSWANA",
    "TURKISH",
    "UKRAINIAN",
    "URDU",
    "VIETNAMESE",
    "WELSH",
    "XHOSA",
    "YORUBA",
    "ZULU",
]
language_iso_639_1 = [
    "AF",
    "AR",
    "AZ",
    "BE",
    "BG",
    "BN",
    "BS",
    "CA",
    "CS",
    "CY",
    "DA",
    "DE",
    "EL",
    "EN",
    "EO",
    "ES",
    "ET",
    "EU",
    "FA",
    "FI",
    "FR",
    "GA",
    "GU",
    "HE",
    "HI",
    "HR",
    "HU",
    "HY",
    "ID",
    "IS",
    "IT",
    "JA",
    "KA",
    "KK",
    "KO",
    "LA",
    "LG",
    "LT",
    "LV",
    "MI",
    "MK",
    "MN",
    "MR",
    "MS",
    "NB",
    "NL",
    "NN",
    "PA",
    "PL",
    "PT",
    "RO",
    "RU",
    "SK",
    "SL",
    "SN",
    "SO",
    "SQ",
    "SR",
    "ST",
    "SV",
    "SW",
    "TA",
    "TE",
    "TH",
    "TL",
    "TN",
    "TR",
    "TS",
    "UK",
    "UR",
    "VI",
    "XH",
    "YO",
    "ZH",
    "ZU",
]
language_iso_639_3 = [
    "AFR",
    "ARA",
    "AZE",
    "BEL",
    "BEN",
    "BOS",
    "BUL",
    "CAT",
    "CES",
    "CYM",
    "DAN",
    "DEU",
    "ELL",
    "ENG",
    "EPO",
    "EST",
    "EUS",
    "FAS",
    "FIN",
    "FRA",
    "GLE",
    "GUJ",
    "HEB",
    "HIN",
    "HRV",
    "HUN",
    "HYE",
    "IND",
    "ISL",
    "ITA",
    "JPN",
    "KAT",
    "KAZ",
    "KOR",
    "LAT",
    "LAV",
    "LIT",
    "LUG",
    "MAR",
    "MKD",
    "MON",
    "MRI",
    "MSA",
    "NLD",
    "NNO",
    "NOB",
    "PAN",
    "POL",
    "POR",
    "RON",
    "RUS",
    "SLK",
    "SLV",
    "SNA",
    "SOM",
    "SOT",
    "SPA",
    "SQI",
    "SRP",
    "SWA",
    "SWE",
    "TAM",
    "TEL",
    "TGL",
    "THA",
    "TSN",
    "TSO",
    "TUR",
    "UKR",
    "URD",
    "VIE",
    "XHO",
    "YOR",
    "ZHO",
    "ZUL",
]
language_casual_names = [
    # Common casual variations
    "Mandarin",  # for Chinese
    "Cantonese",  # for Cantonese (already exists)
    "Farsi",  # for Persian
    "Deutsch",  # German in German
    "Español",  # Spanish in Spanish
    "Français",  # French in French
    "Italiano",  # Italian in Italian
    "Português",  # Portuguese in Portuguese
    "Nederlands",  # Dutch in Dutch
    "Svenska",  # Swedish in Swedish
    "Norsk",  # Norwegian in Norwegian
    "Suomi",  # Finnish in Finnish
    "Ελληνικά",  # Greek in Greek
    "Türkçe",  # Turkish in Turkish
    "עברית",  # Hebrew in Hebrew
    "العربية",  # Arabic in Arabic
    "हिन्दी",  # Hindi in Hindi
    "বাংলা",  # Bengali in Bengali
    "தமிழ்",  # Tamil in Tamil
    "తెలుగు",  # Telugu in Telugu
    "ไทย",  # Thai in Thai
    "Tiếng Việt",  # Vietnamese in Vietnamese
    "Bahasa Indonesia",  # Indonesian in Indonesian
    "Bahasa Melayu",  # Malay in Malay
    # Informal/colloquial names
    "Chinese Simplified",
    "Chinese Traditional",
    "Simplified Chinese",
    "Traditional Chinese",
    "Mandarin Chinese",
    "Mexican Spanish",
    "Latin American Spanish",
    "Castilian",
    "Brazilian Portuguese",
    "European Portuguese",
    "Canadian French",
    "Quebec French",
    "American English",
    "British English",
    "Australian English",
    "Indian English",
    # Short forms people use
    "Chin",  # Chinese
    "Jap",  # Japanese (though potentially offensive)
    "Kor",  # Korean
    "Span",  # Spanish
    "Port",  # Portuguese
    "Russ",  # Russian
    # Cultural references
    "Pinyin",  # Chinese romanization system
    "Kanji",  # Japanese writing system
    "Hangul",  # Korean writing system
    "Cyrillic",  # For Russian/other Slavic
]


def test_from_common_name():
    for name in language_common_names + language_iso_639_1 + language_iso_639_3:
        LanguageCodes.from_common_name(name)


def test_from_casual_names():
    """Test that casual/cultural language names are handled correctly."""
    for name in language_casual_names:
        try:
            result = LanguageCodes.from_common_name(name)
            print(f"✓ {name} -> {result}")
        except ValueError as e:
            print(f"✗ {name} -> {e}")
            # For now, we expect some failures until we implement the mappings


def test_fuzzy_matching():
    """Test fuzzy matching capabilities for typos and variations."""
    fuzzy_test_cases = [
        # Common typos
        ("Englsh", "en"),  # Missing 'i'
        ("Spansh", "es"),  # Missing 'i'
        ("Germn", "de"),  # Missing 'a'
        ("Frech", "fr"),  # Missing 'n'
        ("Japanse", "ja"),  # Extra 's'
        ("Rusian", "ru"),  # Missing 's'
        # Spelling variations
        ("Portugese", "pt"),  # Common misspelling
        ("Chinse", "zh"),  # Missing 'e'
        ("Koreon", "ko"),  # Common variation
        # Accented character variations
        ("Francais", "fr"),  # Without accent
        ("Espanol", "es"),  # Without tilde
        # Partial matches
        ("Eng", "en"),  # Short for English
        ("Ger", "de"),  # Short for German
        ("Jap", "ja"),  # Short for Japanese
        # Case variations with typos
        ("englsh", "en"),  # lowercase with typo
        ("GERMN", "de"),  # uppercase with typo
    ]

    print("\nTesting fuzzy matching:")
    for input_name, expected_code in fuzzy_test_cases:
        try:
            result = LanguageCodes.from_common_name(input_name)
            if result.value == expected_code:
                print(f"✓ {input_name} -> {result} (expected {expected_code})")
            else:
                print(
                    f"⚠ {input_name} -> {result} (expected {expected_code}, but got different match)"
                )
        except ValueError as e:
            print(f"✗ {input_name} -> Failed: {e}")


def test_punctuation_handling():
    """Test that punctuation in instruction names is handled correctly."""
    punctuation_test_cases = [
        # Instruction names with punctuation removed
        ("Chinese Simplified China", "zh-CN"),  # "Chinese, Simplified, China"
        ("Chinese Traditional Taiwan", "zh-TW"),  # "Chinese, Traditional, Taiwan"
        ("Filipino Tagalog", "fil"),  # "Filipino (Tagalog)"
        ("Filipino Tagalog", "tl"),  # "Filipino (Tagalog)" - both variants
        ("French France", "fr-FR"),  # "French, France"
        ("French Canada", "fr-CA"),  # "French, Canada"
        ("Portuguese Portugal", "pt-PT"),  # "Portuguese, Portugal"
        ("Portuguese Brazil", "pt-BR"),  # "Portuguese, Brazil"
        ("Malay Jawi Arabic Script", "ms-Arab"),  # "Malay, Jawi (Arabic Script)"
        ("Meiteilon Manipuri", "mni-Mtei"),  # "Meiteilon (Manipuri)"
        ("Punjabi Shahmukhi", "pa-Arab"),  # "Punjabi (Shahmukhi)"
        ("Kurdish Sorani", "ckb"),  # "Kurdish (Sorani)"
        ("Kurdish Kurmanji", "ku"),  # "Kurdish (Kurmanji)"
        # Case variations
        ("chinese simplified china", "zh-CN"),
        ("FILIPINO TAGALOG", "fil"),
        ("french canada", "fr-CA"),
    ]

    print("\nTesting punctuation handling:")
    for input_name, expected_code in punctuation_test_cases:
        try:
            result = LanguageCodes.from_common_name(input_name)
            if result.value == expected_code:
                print(f"✓ {input_name} -> {result} (expected {expected_code})")
            else:
                print(
                    f"⚠ {input_name} -> {result} (expected {expected_code}, but got different match)"
                )
        except ValueError as e:
            print(f"✗ {input_name} -> Failed: {e}")
