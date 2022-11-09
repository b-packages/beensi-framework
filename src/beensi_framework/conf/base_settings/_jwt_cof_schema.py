from pydantic import BaseModel as BModel


class _JWTConf(BModel):
    SECRET_KEY: str = '********'
    ALGORITHM: str = 'HS256'
    # minute - access token life
    EXPIRATION_DATE: int = 5
    # minute - authentication life
    TIME_TO_BE_ALIVE: int = 60 * 24
