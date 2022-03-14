from fastapi import FastAPI
import pendulum

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World3dfdsfsdfsdf"}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("api:app", port=8780, debug=True, reload=True)