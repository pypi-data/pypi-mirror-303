import re


class TextPostprocessor:
    def primary_text(s: str) -> str:
        # "Glean.ai | Accounts Payable Spend Intelligence"
        # > Accounts Payable Spend Intelligence
        parts = re.split(r"\s+[|—]\s+", s)
        parts = list(sorted(parts, key=lambda x: len(x), reverse=True))
        return parts[0].strip()
