import uvicorn
from fastapi import FastAPI

from core.api_server import ApiServer


def main():
    api_server = ApiServer(fast_api=FastAPI(docs_url="/api"))
    uvicorn.run(api_server.app, host="0.0.0.0", port=8040)


if __name__ == "__main__":
    main()
