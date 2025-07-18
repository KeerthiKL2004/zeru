import json
import pandas as pd
import os

def load_data(json_path):
    print("📂 Loading JSON data...")
    try:
        with open(json_path, 'r') as file:
            data = json.load(file)
        print(f"✅ Loaded {len(data)} records")
        return pd.DataFrame(data)
    except Exception as e:
        print(f"❌ Error loading file: {e}")
        return None

def score_wallets(df):
    print("⚙️ Scoring wallets...")

    # Count actions per wallet
    action_counts = df.groupby(['userWallet', 'action']).size().unstack(fill_value=0)

    # Score weights
    weights = {
        'deposit': 5,
        'repay': 4,
        'borrow': -3,
        'redeemunderlying': -2,
        'liquidationcall': -10
    }

    # Compute raw scores
    score = sum(
        action_counts.get(action, 0) * weight
        for action, weight in weights.items()
    )

    # Replace negative scores with 0
    score = score.clip(lower=0)

    # Normalize to 0–1000
    max_score = score.max()
    if max_score > 0:
        normalized_score = (score / max_score) * 1000
    else:
        normalized_score = score

    # Prepare final DataFrame
    scored_df = pd.DataFrame({
        'userWallet': score.index,
        'creditScore': normalized_score.round(2)
    })

    print("✅ Scoring complete. Top 3 wallets:")
    print(scored_df.sort_values(by="creditScore", ascending=False).head(3))
    return scored_df

if __name__ == "__main__":
    print("✅ Your script is starting...")

    # Make sure output folder exists
    os.makedirs("output", exist_ok=True)

    # Load data
    df = load_data("data/user-wallet-transactions.json")
    if df is None or df.empty:
        print("❌ Failed to load or parse JSON.")
    else:
        print(f"📊 Here are the first 3 rows:\n{df.head(3)}\n")
        
        # Score wallets
        score_df = score_wallets(df)

        # Save to CSV
        output_path = "output/credit_scores.csv"
        score_df.to_csv(output_path, index=False)
        print(f"📁 Output saved to {output_path}")

    print("✅ Script finished.")
