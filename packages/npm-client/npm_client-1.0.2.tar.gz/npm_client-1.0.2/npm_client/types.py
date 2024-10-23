from pydantic import BaseModel, Field, field_validator

class HeaderModel(BaseModel):
    token: str = Field(None, alias="Authorization")

    @field_validator("token", mode="before")
    def add_cookie_prefix(cls, value):
        if value and not value.startswith("Bearer"):
            return f"Bearer {value}"
        return value

    class Config:
        populate_by_name = True

class Certificate(BaseModel):
    id:int
    created_on:str
    modified_on:str
    owner_user_id:int
    provider:str
    nice_name:str
    domain_names:list[str] | None = None
    expires_on:str
    meta:dict

class ProxyHost(BaseModel):
    id: int
    created_on: str
    modified_on: str
    owner_user_id: int
    domain_names: list[str] | None = None
    forward_host: str
    forward_port: int
    access_list_id: int
    certificate_id: int
    ssl_forced: int
    caching_enabled: int
    block_exploits: int
    advanced_config: str
    meta: dict | None = None
    allow_websocket_upgrade: int
    http2_support: int
    forward_scheme: str
    enabled: int
    locations: list
    hsts_enabled: int
    hsts_subdomains: int
    certificate: Certificate | None = None