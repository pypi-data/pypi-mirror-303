import os
import sys
import time
import torch


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ecoscape_connectivity import StochasticRepopulateFast

NUM_SIMULATIONS = 1000
NUM_SPREADS = 45

BORDER_SIZE = 250
TILE_SIZE = 1000

EDGE = TILE_SIZE + 2 * BORDER_SIZE

device = (torch.device('cuda') if torch.cuda.is_available() else 
          torch.device('mps') if torch.backends.mps.is_available() else
          torch.device('cpu'))

print(f"Device: {device}")

habitat = (torch.rand(EDGE, EDGE, device=device) < 0.5).float()
terrain = torch.rand(EDGE, EDGE, device=device)

rep = StochasticRepopulateFast(
    habitat, terrain, 
    num_spreads = NUM_SPREADS,
)

seed_probability = 4 / (1 + 2 * NUM_SPREADS) ** 2

if device == torch.device('mps'):
    PYTORCH_MPS_HIGH_WATERMARK_RATIO=0.8

start = time.time()    
rep.zero_grad()
for _ in range(NUM_SIMULATIONS):
    seeds = torch.rand(EDGE, EDGE, device=device) < seed_probability
    pop = rep(seeds)
    s = torch.sum(pop)
    s.backward()
    _ = rep.get_grad()
end = time.time()
print(f"Time for {NUM_SIMULATIONS} flow simulations: {end - start:.2f} seconds.")

with torch.no_grad():
    start = time.time()
    for _ in range(NUM_SIMULATIONS):
        seeds = torch.rand(EDGE, EDGE, device=device) < seed_probability
        pop = rep(seeds)
    end = time.time()
    print(f"Time for {NUM_SIMULATIONS} repopulation simulations: {end - start:.2f} seconds.")

