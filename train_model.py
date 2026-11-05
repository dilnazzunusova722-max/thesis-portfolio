"""Запуск: python train_model.py [файл.csv]
Без аргумента обучает на синтетических данных, с аргументом: на ваших реальных."""
import sys
import pandas as pd
from ai_model import train, FEATURES, TARGET

if len(sys.argv) > 1:
    data = pd.read_csv(sys.argv[1])
    missing = [c for c in FEATURES + [TARGET] if c not in data.columns]
    if missing:
        sys.exit(f"В CSV нет столбцов: {missing}")
    _, metrics = train(data)
else:
    _, metrics = train()
print(metrics)
