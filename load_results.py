"""
Data loading and preparation utilities for sbmlsim reporting
"""
import json
import pandas as pd
import numpy as np
from pathlib import Path
from typing import Dict, Tuple

def load_optimization_results(filepath: str = 'sample_results.json') -> Dict:
    """Load optimization results from JSON file"""
    with open(filepath, 'r') as f:
        data = json.load(f)
    return data

def get_parameter_table(data: Dict) -> pd.DataFrame:
    """Extract parameter table with confidence intervals"""
    params = data['optimization_results']['parameters']
    df = pd.DataFrame(params)
    return df

def generate_fit_data(n_points: int = 100, seed: int = 42) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Generate mock goodness-of-fit data for visualization"""
    np.random.seed(seed)
    x = np.linspace(0, 10, n_points)
    y_true = 2 * x + 1 + np.sin(x) * 0.5
    y_pred = y_true + np.random.normal(0, 0.3, n_points)
    return x, y_true, y_pred

if __name__ == '__main__':
    # Test loading
    data = load_optimization_results()
    print("✓ Loaded results:")
    print(f"  Model: {data['metadata']['model_id']}")
    print(f"  AIC: {data['optimization_results']['aic']}")
    print(f"  RMSE: {data['optimization_results']['rmse']}")
    print(f"  R²: {data['optimization_results']['r_squared']}")
    
    params = get_parameter_table(data)
    print("\n✓ Parameters:")
    print(params[['name', 'value', 'unit']])
