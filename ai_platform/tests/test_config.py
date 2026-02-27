from packages.core.config import get_settings


def test_settings_load_defaults_or_env():
    s = get_settings()
    assert s.app_name
    assert s.environment in {"development", "staging", "production"}
    assert isinstance(s.max_tokens, int) and s.max_tokens > 0