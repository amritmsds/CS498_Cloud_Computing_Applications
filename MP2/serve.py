from fastapi import FastAPI, HTTPException
import subprocess
import socket

app = FastAPI()

@app.post("/")
async def stress_cpu():
    # Run "stress_cpu.py" in a separate process
    subprocess.Popen(["python", "stress_cpu.py"])
    return {"message": "Stressing CPU in a separate process"}

@app.get("/")
async def get_private_ip():
    # Get the private IP address using socket
    private_ip = socket.gethostbyname(socket.gethostname())
    return {"private_ip": private_ip}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8081)
