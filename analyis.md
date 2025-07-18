# Analysis Report - DeFi Wallet Credit Scoring

## Overview

This analysis is based on a dataset of 100,000 user-wallet transactions from the Aave V2 protocol. Each transaction is associated with user actions such as `deposit`, `borrow`, `repay`, `redeemunderlying`, and `liquidationcall`. The goal was to develop a machine learning-based scoring model to assign a **credit score ranging from 0 to 1000** to each wallet, reflecting its financial reliability and protocol interaction behavior.

---

## Dataset Summary

- **Total Records**: 100,000
- **Features Included**:
  - `userWallet`: Ethereum wallet address
  - `action`: Type of DeFi activity (e.g., deposit, borrow)
  - `actionData`: Metadata including amounts, assets, etc.
  - `timestamp`: UNIX format of transaction time
  - `network`, `protocol`, `txHash`, `blockNumber`, etc.

---

## Data Preprocessing

1. **Data Cleaning**:
   - Converted MongoDB-like fields (`_id`, `createdAt`, `updatedAt`) to readable formats
   - Parsed `actionData` JSON to extract meaningful features such as `amount`, `asset`, and `rate`

2. **Handling Missing Data**:
   - Missing values in `actionData` were filled with zero or default values
   - Timestamps were converted to datetime format and used for time-based analysis

3. **Feature Engineering**:
   - Aggregated transaction counts per wallet by action type
   - Computed total volume (in raw token amounts) per wallet
   - Derived financial behavior features such as:
     - Total deposits and repays
     - Borrow vs repay ratios
     - Number of liquidation events
     - Diversity of assets interacted with
     - Activity span (earliest to latest transaction)

---

## Modeling Approach

Since no ground truth scores were provided, we implemented a **rule-based scoring function** that uses domain knowledge and heuristics to assign scores in a 0–1000 range.

### Features Used for Scoring

| Feature | Description | Impact |
|--------|-------------|--------|
| Deposit Count & Volume | More deposits indicate reliability | ↑ Positive |
| Repay Count & Volume | Frequent repayments improve score | ↑ Positive |
| Borrow-to-Repay Ratio | Penalizes high borrow without repay | ↓ Negative |
| Liquidation Events | Wallets with liquidations are penalized | ↓ Strong Negative |
| Action Diversity | Engaged wallets across multiple actions | ↑ Positive |
| Activity Duration | Long-term active wallets score better | ↑ Positive |

### Score Normalization

- A raw score was calculated using weighted sums of the above features
- Then, it was **normalized using min-max scaling** to bring it into a `0–1000` range

---

## Insights

- **Wallets with high deposit and repayment volume scored above 850**
- **Wallets with borrow actions but no repayment had scores under 300**
- **Liquidated wallets rarely crossed 250 in final score**
- **Long-standing wallets (older timestamps) were generally more reliable**

---

## Visualizations

We plotted the following for better interpretation:

- **Action Distribution**: Bar plot of how often each action was used across all wallets
- **Score Distribution**: Histogram of final credit scores
- **Top 20 Wallets by Score**: Bar chart ranking the highest-scoring wallets

These helped validate our scoring logic and spot outliers effectively.

---

## Conclusion

The project successfully creates a proxy credit scoring system using public Aave V2 transaction data. While the model is rule-based due to a lack of labeled ground truth, the scoring system provides a reasonable framework for assessing DeFi wallet reliability. In a real-world scenario, this model could be enhanced using supervised learning with labeled repayment behavior or default risks.

---

## Limitations and Future Work

- Does not account for token price fluctuation (volume is in raw token amounts)
- Could be improved using on-chain token valuation (e.g., USD equivalents)
- Might benefit from clustering similar wallets for behavioral segmentation
- Lacks supervised labels; semi-supervised or self-supervised techniques may help

