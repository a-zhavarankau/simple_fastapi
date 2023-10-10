from fastapi import FastAPI
import uvicorn


app = FastAPI(title="simple_fastapi", debug=True)

@app.get("/")
def index():
    return f"Hello from \'simple_fastapi\'"


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
