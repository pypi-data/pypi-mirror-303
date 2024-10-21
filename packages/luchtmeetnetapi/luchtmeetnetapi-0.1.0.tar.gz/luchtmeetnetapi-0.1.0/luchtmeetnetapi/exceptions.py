"""LuchtmeetNet exceptions."""


class LuchtmeetNetError(Exception):
    """Generic exception."""


class LuchtmeetNetConnectionError(LuchtmeetNetError):
    """LuchtmeetNet connection exception."""
