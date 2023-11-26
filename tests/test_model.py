import torch
import os

CURRENT_DIR = os.getcwd()
MODEL_PATH = f'{CURRENT_DIR}/models/doubleit_model.pt'
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
MODEL = torch.jit.load(MODEL_PATH, map_location=DEVICE)
MODEL.eval()

def f(input: torch.tensor):
    """
    Function to double the input tensor.

    Parameters:
    - input (torch.tensor): Input tensor.

    Returns:
    - torch.tensor: Doubled tensor.
    """
    return 2 * input

def test_uniformity():
    """
    Test function to check uniformity of model predictions.

    Raises:
    - AssertionError: If predictions are not equal to expected values.
    """
    random1 = torch.rand(10)
    random2 = torch.rand(100)
    random3 = torch.rand(1000)
    random4 = torch.rand(1000)
    assert torch.equal(MODEL(random1), f(random1))
    assert torch.equal(MODEL(random2), f(random2))
    assert torch.equal(MODEL(random3), f(random3))
    assert torch.equal(MODEL(random4), f(random4))
    
def test_reproducibility():
    """
    Test function to check reproducibility of model predictions.

    Raises:
    - AssertionError: If predictions are not equal to expected values.
    """
    input = torch.tensor([1, 2, 4, 8, 16, 32, 64])
    expected_out = torch.tensor([2, 4, 8, 16, 32, 64, 128])
    assert torch.equal(MODEL(input), expected_out)