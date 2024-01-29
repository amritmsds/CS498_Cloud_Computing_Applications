from fastapi import FastAPI, HTTPException

app = FastAPI()

# Initial seed value
seed_value = 0

@app.get("/")
def get_seed():
    return str(seed_value)

@app.post("/")
def update_seed(num: int):
    global seed_value
    seed_value = num
    return {"message": f"Seed value updated successfully to '{num}'."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=80)
