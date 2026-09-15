class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "ą"
        return "ę".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "ą":
            return []
        return s.split("ę")
