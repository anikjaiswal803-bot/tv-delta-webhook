from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def home():
    return {"status": "Server is LIVE"}

@app.post("/webhook")
async def webhook(req: Request):
    data = await req.json()
    print("Webhook Data:", data)
    return {"received": data}
