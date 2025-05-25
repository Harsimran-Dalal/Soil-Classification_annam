"""
Author: Harsimran Singh Dalal
Team Name: Dirt Detectives
Team Members: Member-1 (Harsimran Singh Dalal)
Leaderboard Rank: 19
"""

import pandas as pd
import numpy as np

def preprocessing(train_path="train.csv", test_path="test.csv"):
    print("Starting preprocessing...")

    # Load datasets
    train_df = pd.read_csv(train_path)
    test_df = pd.read_csv(test_path)
    # 1. Handle missing values
    train_df.fillna(train_df.mean(numeric_only=True), inplace=True)
    test_df.fillna(test_df.mean(numeric_only=True), inplace=True)
    # 2. Encode categorical variables (if any)
    categorical_cols = train_df.select_dtypes(include=['object']).columns
    train_df = pd.get_dummies(train_df, columns=categorical_cols)
    test_df = pd.get_dummies(test_df, columns=categorical_cols)
    # 3. Align train and test sets
    train_df, test_df = train_df.align(test_df, join='left', axis=1, fill_value=0)
    # Save preprocessed files
    train_df.to_csv("train_preprocessed.csv", index=False)
    test_df.to_csv("test_preprocessed.csv", index=False)

    print("✅ Preprocessing completed and files saved as train_preprocessed.csv and test_preprocessed.csv")
    return 0
