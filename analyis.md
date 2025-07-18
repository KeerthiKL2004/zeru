# 📊 Analysis: Zeru DeFi Wallet Credit Scoring

## 🧠 Objective

The goal of this project was to develop a system that assigns **credit scores ranging from 0 to 1000** to wallets interacting with the **Aave V2 protocol**. The score reflects how responsible and trustworthy each wallet is based on its on-chain transaction behavior.

---

## 📂 Data Overview

- **Source**: Aave V2 DeFi protocol logs
- **Records**: 100,000 JSON transaction entries
- **Fields Used**: 
  - `userWallet`: wallet address
  - `action`: the type of activity (`deposit`, `borrow`, `repay`, etc.)
  - `timestamp`, `blockNumber`, and other metadata

---

## 🧮 Scoring Methodology

Each wallet’s score is based on a **heuristic approach** that uses the frequency of various DeFi actions:

| Action              | Weight     | Reasoning                                                             |
|---------------------|------------|-----------------------------------------------------------------------|
| `repay`             | +4 points  | Shows responsibility by paying back borrowed funds                   |
| `deposit`           | +3 points  | Indicates contribution to protocol liquidity                         |
| `borrow`            | +2 points  | Involves some risk but shows engagement                              |
| `redeemUnderlying`  | +1 point   | Neutral action; withdrawing depos
