# 💳 Zeru DeFi Wallet Credit Score Model

This project builds a **credit score system (0–1000)** for wallets that have interacted with the **Aave V2** DeFi protocol. The solution is built using Python and processes a sample of **100,000 transaction records** to assign each wallet a credit score based on their behavior.

---

## 📌 Problem Statement

**Objective**:  
Given raw transaction-level data from the Aave V2 protocol, develop a model that assigns a **credit score between 0 and 1000** to each wallet address based on actions such as:

- `deposit`
- `borrow`
- `repay`
- `redeemUnderlying`
- `liquidationCall`

---

## ✅ Features

- Parses large JSON transaction datasets
- Scores each wallet based on behavior heuristics
- Outputs a CSV file with wallet scores
- Generates plots to visualize score distributions

---

## 📁 Folder Structure

