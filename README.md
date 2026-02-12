# Agentic Settlement Engine

A simple HTML + JavaScript demo that simulates settlement calculations with explicit formulas.

## What it does

The page collects:
- Transaction amount (TxAmt)
- Transaction currency
- Settlement currency
- FX rate (BaseRate)
- FX markup % (MarkupPct)

When you click **Run Settlement Agent**, it will:
1. Calculate merchant net payout
2. Calculate FX margin earned
3. Show a **Calculation Breakdown** table with each formula step

## Validation rules

- Amount must be **> 0**
- FX rate must be **> 0**
- FX markup % must be **>= 0**

If inputs are invalid, an error message is shown and calculations are not run.

## Run locally

No build tools are required.

### Option 1: Open directly
1. Open `index.html` in your browser.

### Option 2: Serve with a local web server
From this repository directory:

```bash
python3 -m http.server 8000
```

Then visit:

- http://localhost:8000

## Calculation formulas

1. `Converted amount = TxAmt * BaseRate`
2. `FX margin = Converted amount * (MarkupPct / 100)`
3. `Merchant net payout = Converted amount - FX margin`

All monetary outputs are shown in the selected settlement currency (except TxAmt row, which uses transaction currency).
