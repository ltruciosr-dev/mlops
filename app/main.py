from fastapi import FastAPI, Query
from typing import List
from fastapi.responses import JSONResponse
import torch
import io
import os

app = FastAPI()

# Load the pre-trained PyTorch model (for demonstration purposes)
CURRENT_DIR = os.getcwd()
MODEL_PATH = f'{CURRENT_DIR}/models/doubleit_model.pt'
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
MODEL = torch.jit.load(MODEL_PATH, map_location=DEVICE)
MODEL.eval()

def predict_array(values):
    """
    Perform inference using the pre-trained PyTorch model.

    Parameters:
    - values (List[float]): List of float values for prediction.

    Returns:
    - List[float]: List of predicted output values.
    """
    input_tensor = torch.tensor(values)
    input_batch = input_tensor.unsqueeze(0)
    
    with torch.no_grad():
        output = MODEL(input_batch)
    
    return output.tolist()

@app.post("/predict/")
async def predict(values: List[float] = Query([])):
    """
    API endpoint to predict over an uploaded list.

    Parameters:
    - values (List[float]): List of float values for prediction.

    Returns:
    - JSONResponse: JSON response containing the predicted output or an error message.
    """
    try:
        output = predict_array(values)
        return JSONResponse(content={"output": output}, status_code=200)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)