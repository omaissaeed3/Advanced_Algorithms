# Advanced_Algorithms_Tips

This repo demonstrates a pure-Python pipeline (**no notebooks**) for a restaurant tips dataset.

## Data
- `data/tip.csv` — raw dataset (place yours here; a copy is included if you provided one).
- `data/restaurant_tips_cleaned_scaled.csv` — processed output (written by the pipeline).

## Setup
```bash
python -m venv .venv
# Windows:
.\.venv\Scripts\Activate.ps1
# macOS/Linux:
source .venv/bin/activate
pip install -r requirements.txt
```

## Run
```bash
python src/main.py --data data/tip.csv --save data/restaurant_tips_cleaned_scaled.csv
# or simply:
python src/main.py
```

## What it does
- **EDA**: prints head/info/describe
- **Cleaning**: drops empty rows, fills numeric NA (median), trims outliers with robust IQR
- **Feature engineering**: adds `tip_rate = tip / total_bill` if those columns exist; one-hot encodes common categoricals `sex/smoker/day/time`
- **Scaling**: standardizes numeric columns

Adjust modules in `src/` to match your final assignment decisions and document them here.
