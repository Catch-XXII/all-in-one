from pydantic import BaseModel, HttpUrl


class AnalyzeRequestSchema(BaseModel):
    url: HttpUrl
