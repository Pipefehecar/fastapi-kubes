from fastapi import FastAPI

app=FastAPI()

@app.get('/health')
async def health_check():
    return {'status':'ok =)'} 

if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")
