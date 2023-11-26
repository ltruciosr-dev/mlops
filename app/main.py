from fastapi import FastAPI, Query
from typing import List
from fastapi.responses import JSONResponse
import torch
import io

app = FastAPI()

# Load the pre-trained PyTorch model (for demonstration purposes)
MODEL_PATH = '/models/doubleit_model.pt'
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
MODEL = torch.jit.load(MODEL_PATH, map_location=DEVICE)
MODEL.eval()

# Function to perform inference
def predict_array(values):
    input_tensor = torch.tensor(values)
    input_batch = input_tensor.unsqueeze(0)
    
    with torch.no_grad():
        output = MODEL(input_batch)
    
    return output.tolist()

# API endpoint to predict over an uploaded list
@app.post("/predict/")
async def predict(values: List[float] = Query([])):
    try:
        output = predict_array(values)
        return JSONResponse(content={"output": output}, status_code=200)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)