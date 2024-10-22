from pydantic_settings import BaseSettings, SettingsConfigDict


class TheCvesSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="THE_CVES_CLI_", case_sensitive=False)
    confluence_user: str
    confluence_token: str
    confluence_domain: str
    api_key: str
    host: str
    username: str
    github_token: str = None
    github_repo_url: str = None
