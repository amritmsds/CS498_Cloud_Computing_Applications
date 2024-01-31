from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
app = FastAPI()

# Initial seed value
seed_value = 0

class SeedModel(BaseModel):
    num :int = 0

@app.get("/")
def get_seed():
    return str(seed_value)

@app.post("/")
def update_seed(seed_input: SeedModel):
    global seed_value
    seed_value = seed_input.num
    return {"message": f"Seed value updated successfully to '{seed_value}'."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8081)
