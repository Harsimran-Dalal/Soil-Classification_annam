"""
Author: Harsimran Singh Dalal
Team Name: Dirt Detectives
Team Members: Member-1 (Harsimran Singh Dalal)
Leaderboard Rank: 19
"""

import pandas as pd

def postprocessing(predictions_path="submission.csv", output_path="final_submission.csv"):
    print("Starting postprocessing...")

    # Load existing submission file
    submission = pd.read_csv(predictions_path)

    # Optional: validate structure
    if "image_id" not in submission.columns or "soil_type" not in submission.columns:
        raise ValueError("submission.csv must contain 'image_id' and 'soil_type' columns.")

    # Post-processing steps if needed:
    # For example, ensure soil_type is integer or within range:
    # submission["soil_type"] = submission["soil_type"].round().astype(int)

    # Save final submission
    submission.to_csv(output_path, index=False)

    print(f"✅ Postprocessing completed. Final submission saved to {output_path}")
    return 0
