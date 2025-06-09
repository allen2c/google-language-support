import pytest

from google_language_support import LanguageCodes


class TestLanguageCodes:
    """Test suite for LanguageCodes enum."""

    def test_language_codes_is_str_enum(self):
        """Test that LanguageCodes properly extends StrEnum."""
        # Test that enum values are strings
        assert isinstance(LanguageCodes.ENGLISH, str)
        assert isinstance(LanguageCodes.SPANISH, str)
        assert isinstance(LanguageCodes.FRENCH, str)

        # Test string comparison works
        assert LanguageCodes.ENGLISH == "en"
        assert LanguageCodes.SPANISH == "es"
        assert LanguageCodes.FRENCH == "fr"

    def test_all_language_codes_have_values(self):
        """Test that all language codes have string values."""
        for code in LanguageCodes:
            assert isinstance(code.value, str)
            assert (
                len(code.value) >= 2
            )  # Language codes should be at least 2 characters

    def test_specific_language_code_values(self):
        """Test specific language code values are correct."""
        test_cases = [
            (LanguageCodes.ENGLISH, "en"),
            (LanguageCodes.SPANISH, "es"),
            (LanguageCodes.FRENCH, "fr"),
            (LanguageCodes.GERMAN, "de"),
            (LanguageCodes.CHINESE_SIMPLIFIED, "zh-CN"),
            (LanguageCodes.CHINESE_TRADITIONAL, "zh-TW"),
            (LanguageCodes.PORTUGUESE_BR, "pt-BR"),
            (LanguageCodes.PORTUGUESE_PT, "pt-PT"),
            (LanguageCodes.FRENCH_FR, "fr-FR"),
            (LanguageCodes.FRENCH_CA, "fr-CA"),
            (LanguageCodes.MALAY_JAWI, "ms-Arab"),
            (LanguageCodes.MEITEILON_MANIPURI, "mni-Mtei"),
            (LanguageCodes.PUNJABI_SHAHMUKHI, "pa-Arab"),
        ]

        for code, expected_value in test_cases:
            assert code.value == expected_value

    def test_to_instruction_regular_cases(self):
        """Test to_instruction method for regular language codes."""
        test_cases = [
            (LanguageCodes.ABKHAZ, "Abkhaz"),
            (LanguageCodes.ACEHNESE, "Acehnese"),
            (LanguageCodes.ACHOLI, "Acholi"),
            (LanguageCodes.AFRIKAANS, "Afrikaans"),
            (LanguageCodes.ALBANIAN, "Albanian"),
            (LanguageCodes.ENGLISH, "English"),
            (LanguageCodes.SPANISH, "Spanish"),
            (LanguageCodes.GERMAN, "German"),
            (LanguageCodes.ITALIAN, "Italian"),
            (LanguageCodes.CHICHEWA_NYANJA, "Chichewa Nyanja"),
            (LanguageCodes.BATAK_KARO, "Batak Karo"),
            (LanguageCodes.NORTHERN_SOTHO_SEPEDI, "Northern Sotho Sepedi"),
            (LanguageCodes.NEPALBHASA_NEWARI, "Nepalbhasa Newari"),
        ]

        for code, expected_instruction in test_cases:
            assert code.to_instruction() == expected_instruction

    def test_to_instruction_special_cases(self):
        """Test to_instruction method for special language codes with custom names."""
        special_cases = [
            (LanguageCodes.CHINESE_SIMPLIFIED_2, "Chinese"),  # "zh"
            (LanguageCodes.CHINESE_SIMPLIFIED, "Chinese, Simplified, China"),  # "zh-CN"
            (
                LanguageCodes.CHINESE_TRADITIONAL,
                "Chinese, Traditional, Taiwan",
            ),  # "zh-TW"
            (LanguageCodes.FRENCH, "French"),  # "fr"
            (LanguageCodes.FRENCH_FR, "French, France"),  # "fr-FR"
            (LanguageCodes.FRENCH_CA, "French, Canada"),  # "fr-CA"
            (LanguageCodes.PORTUGUESE, "Portuguese"),  # "pt"
            (LanguageCodes.PORTUGUESE_PT, "Portuguese, Portugal"),  # "pt-PT"
            (LanguageCodes.PORTUGUESE_BR, "Portuguese, Brazil"),  # "pt-BR"
            (LanguageCodes.FILIPINO_TAGALOG, "Filipino (Tagalog)"),  # "fil"
            (LanguageCodes.FILIPINO_TAGALOG_2, "Filipino (Tagalog)"),  # "tl"
            (LanguageCodes.MALAY_JAWI, "Malay, Jawi (Arabic Script)"),  # "ms-Arab"
            (LanguageCodes.MEITEILON_MANIPURI, "Meiteilon (Manipuri)"),  # "mni-Mtei"
            (LanguageCodes.PUNJABI_SHAHMUKHI, "Punjabi (Shahmukhi)"),  # "pa-Arab"
            (LanguageCodes.KURDISH_SORANI, "Kurdish (Sorani)"),  # "ckb"
            (LanguageCodes.KURDISH_KURMANJI, "Kurdish (Kurmanji)"),  # "ku"
            (LanguageCodes.JAVANESE, "Javanese"),  # "jw"
            (LanguageCodes.JAVANESE_2, "Javanese"),  # "jv"
        ]

        for code, expected_instruction in special_cases:
            assert code.to_instruction() == expected_instruction

    def test_duplicate_language_variants(self):
        """Test that duplicate language variants have correct values."""
        # Test Chinese variants
        assert LanguageCodes.CHINESE_SIMPLIFIED_2.value == "zh"
        assert LanguageCodes.CHINESE_SIMPLIFIED.value == "zh-CN"
        assert LanguageCodes.CHINESE_TRADITIONAL.value == "zh-TW"

        # Test Filipino variants
        assert LanguageCodes.FILIPINO_TAGALOG.value == "fil"
        assert LanguageCodes.FILIPINO_TAGALOG_2.value == "tl"

        # Test Hebrew variants
        assert LanguageCodes.HEBREW.value == "iw"
        assert LanguageCodes.HEBREW_2.value == "he"

        # Test Javanese variants
        assert LanguageCodes.JAVANESE.value == "jw"
        assert LanguageCodes.JAVANESE_2.value == "jv"

    def test_language_code_uniqueness(self):
        """Test that enum names are unique."""
        names = [code.name for code in LanguageCodes]
        assert len(names) == len(set(names)), "Enum names should be unique"

    def test_language_code_count(self):
        """Test the total number of language codes."""
        # This ensures we're testing all expected codes and catches if new ones are added
        all_codes = list(LanguageCodes)
        assert (
            len(all_codes) == 198
        ), f"Expected 198 language codes, got {len(all_codes)}"

    def test_enum_iteration(self):
        """Test that enum can be properly iterated."""
        codes = []
        for code in LanguageCodes:
            codes.append(code)
            assert isinstance(code, LanguageCodes)
            assert isinstance(code.value, str)

        assert len(codes) > 0

    def test_enum_membership(self):
        """Test enum membership operations."""
        # Test value membership
        assert "en" in [code.value for code in LanguageCodes]
        assert "es" in [code.value for code in LanguageCodes]
        assert "invalid-code" not in [code.value for code in LanguageCodes]

    def test_to_instruction_returns_string(self):
        """Test that to_instruction always returns a string."""
        for code in LanguageCodes:
            instruction = code.to_instruction()
            assert isinstance(instruction, str)
            assert len(instruction) > 0

    @pytest.mark.parametrize(
        "code_name,expected_value",
        [
            ("ENGLISH", "en"),
            ("SPANISH", "es"),
            ("FRENCH", "fr"),
            ("GERMAN", "de"),
            ("ITALIAN", "it"),
            ("JAPANESE", "ja"),
            ("KOREAN", "ko"),
            ("RUSSIAN", "ru"),
            ("ARABIC", "ar"),
            ("HINDI", "hi"),
        ],
    )
    def test_common_language_codes(self, code_name, expected_value):
        """Test common language codes using parametrize."""
        code = getattr(LanguageCodes, code_name)
        assert code.value == expected_value

    def test_special_characters_in_codes(self):
        """Test language codes with special characters like hyphens."""
        hyphenated_codes = [
            LanguageCodes.CHINESE_SIMPLIFIED,  # "zh-CN"
            LanguageCodes.CHINESE_TRADITIONAL,  # "zh-TW"
            LanguageCodes.FRENCH_FR,  # "fr-FR"
            LanguageCodes.FRENCH_CA,  # "fr-CA"
            LanguageCodes.PORTUGUESE_PT,  # "pt-PT"
            LanguageCodes.PORTUGUESE_BR,  # "pt-BR"
            LanguageCodes.MALAY_JAWI,  # "ms-Arab"
            LanguageCodes.MEITEILON_MANIPURI,  # "mni-Mtei"
            LanguageCodes.PUNJABI_SHAHMUKHI,  # "pa-Arab"
        ]

        for code in hyphenated_codes:
            assert "-" in code.value

    def test_error_cases(self):
        """Test that accessing non-existent codes raises AttributeError."""
        with pytest.raises(AttributeError):
            LanguageCodes.NONEXISTENT_LANGUAGE  # type: ignore

    def test_case_sensitivity(self):
        """Test that enum names are case sensitive."""
        # This should work
        assert LanguageCodes.ENGLISH == "en"

        # This should fail
        with pytest.raises(AttributeError):
            LanguageCodes.english  # type: ignore # lowercase should not work
