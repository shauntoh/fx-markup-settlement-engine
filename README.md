# Agentic Settlement Engine

A simple HTML + JavaScript demo that simulates a settlement agent decision.

## What it does

The demo collects:
- Transaction amount
- Transaction currency
- Settlement currency
- FX rate
- FX markup %
- Settlement speed (T+1, T+3)
- Cross-border flag (yes/no)

When you click **Run Settlement Agent**, it will:
1. Calculate merchant net payout
2. Calculate FX margin earned
3. Display settlement timing
4. Show a short explanation of the decision

## Run locally

No build tools are required.

### Option 1: Open directly
1. Open `index.html` in your browser.

### Option 2: Serve with a local web server (recommended)
From this repository directory:

```bash
python3 -m http.server 8000
```

Then visit:

- http://localhost:8000

## Notes on calculations

- `convertedBase = transactionAmount × fxRate`
- `fxMargin = convertedBase × (fxMarkup% / 100)`
- `merchantNetPayout = convertedBase - fxMargin`

All results are displayed in the selected settlement currency.
