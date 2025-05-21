# 🌱 Soil Classification using CNN Feature Extraction and Random Forest

This project is part of a computer vision competition where the objective is to classify soil types based on images. We leverage **deep learning for feature extraction** and **traditional machine learning for classification**. Specifically, we use a pretrained **ResNet-18** model to extract features and train a **Random Forest** classifier on those features.

---

## 📁 Dataset Structure

The dataset includes labeled training data and unlabeled test data.

soil_classification-2025/
├── train/
│ ├── 0001.jpg
│ ├── 0002.jpg
│ └── ...
├── test/
│ ├── 2001.jpg
│ ├── 2002.jpg
│ └── ...
├── train_labels.csv # Contains image_id and soil_type
└── test_ids.csv # Contains image_id only

---

## 🧠 Approach

1. **Preprocessing**:
    - Images resized to **224x224**
    - Transformed to tensors using `torchvision.transforms`

2. **Feature Extraction**:
    - Load **ResNet-18** pretrained on ImageNet
    - Replace final fully-connected layer (`fc`) with `Identity()` to get 512D feature vectors
    - Use this model to extract features from training and test images

3. **Modeling**:
    - Use **Stratified 5-Fold Cross Validation** with a **Random Forest** classifier
    - Evaluate performance using **macro F1-score**
    - Train final model on full training set and generate predictions on test set

---

## 🚀 How to Run

### 🔧 Requirements

Install required libraries with:

```bash
pip install torch torchvision scikit-learn pandas numpy tqdm pillow
```
▶️ Execution
Clone this repository:

bash
Copy
Edit
git clone https://github.com/<your-username>/soil-classification-cnn-rf.git
cd soil-classification-cnn-rf
Place your dataset inside a folder named soil_classification-2025.

Run the main script:

bash
Copy
Edit
python classify_soil.py
This will:

Extract CNN features from images

Train a Random Forest classifier

Print evaluation reports

Create submission.csv with test predictions
