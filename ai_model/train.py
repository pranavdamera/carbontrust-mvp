import pandas as pd
from torch.utils.data import DataLoader, Dataset
import torch
from biomass_model import BiomassRegressor

# Load processed NDVI and labels
df = pd.read_csv('../data/sample_labels.csv', parse_dates=['date'])

class BioDataset(Dataset):
    def __init__(self, df):
        self.X = torch.tensor(df[['ndvi']].values, dtype=torch.float32)
        self.y = torch.tensor(df['biomass'].values, dtype=torch.float32).unsqueeze(1)
    def __len__(self): return len(self.X)
    def __getitem__(self, i): return self.X[i], self.y[i]

dataset = BioDataset(df)
loader = DataLoader(dataset, batch_size=16, shuffle=True)
model = BiomassRegressor()
opt = torch.optim.Adam(model.parameters())
crit = nn.MSELoss()

for epoch in range(50):
    for X,y in loader:
        pred = model(X)
        loss = crit(pred,y)
        opt.zero_grad(); loss.backward(); opt.step()
    print(f'Epoch {epoch}: {loss.item()}')

torch.save(model.state_dict(), 'biomass_model.pt')