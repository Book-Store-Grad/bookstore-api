from server.application import app


@app.get("/")
async def root():
    return {"message": "Hello World"}
