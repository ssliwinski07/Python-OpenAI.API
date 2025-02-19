from fastapi import APIRouter, HTTPException
import os


class OpenAITokenAPI:
    def __init__(self, router: APIRouter):
        self.router = router
        self.routes_setup()

    def routes_setup(self):
        @self.router.post("/", tags=["API keys"])
        def get_api_key():
            api_key = os.getenv("API_KEY")
            if not api_key:
                raise HTTPException(status_code=404, detail="API key not found")
            return api_key
