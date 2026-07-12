#tree based feature 
#Feature Importance tells us how much each feature contributed to 
# the model's predictions.

# ============================================
# STEP 1 : Import Libraries
# ============================================

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# ============================================
# STEP 2 : Create Dataset
# ============================================

df = pd.DataFrame({
    "Age":[22,25,30,35,40,45,50,55,60,65],
    "Salary":[25000,30000,45000,60000,80000,
              100000,120000,150000,170000,200000],
    "Experience":[1,2,3,5,7,10,12,15,18,20],
    "Purchased":[0,0,0,0,1,1,1,1,1,1]
})

print("Original Dataset")
print(df)

# ============================================
# STEP 3 : Separate Features and Target
# ============================================

X = df.drop("Purchased", axis=1)

y = df["Purchased"]

print("\nFeatures (X)")
print(X)

print("\nTarget (y)")
print(y)

# ============================================
# STEP 4 : Split Dataset
# ============================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining Shape :", X_train.shape)
print("Testing Shape :", X_test.shape)

# ============================================
# STEP 5 : Create Random Forest Model
# ============================================

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# ============================================
# STEP 6 : Train Model
# ============================================

model.fit(X_train, y_train)

# ============================================
# STEP 7 : Feature Importance
# ============================================

importance = model.feature_importances_

print("\nFeature Importance Values")
print(importance)

# ============================================
# STEP 8 : Convert to DataFrame
# ============================================

importance_df = pd.DataFrame({
    "Feature": X.columns,
    "Importance": importance
})

# ============================================
# STEP 9 : Sort Feature Importance
# ============================================

importance_df = importance_df.sort_values(
    by="Importance",
    ascending=False
)

print("\nSorted Feature Importance")
print(importance_df)

# ============================================
# STEP 10 : Plot Graph
# ============================================

plt.figure(figsize=(8,5))

plt.bar(
    importance_df["Feature"],
    importance_df["Importance"]
)

plt.title("Random Forest Feature Importance")
plt.xlabel("Features")
plt.ylabel("Importance Score")

plt.show()