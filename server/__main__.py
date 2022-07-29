from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    """Main page of our server, this is not a web-based applications, so should just show some information on usage"""
    return {"message": "This is a server for picphone app (Python Discord Summer Code Jam 2022)"}
