import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

# -------------------------------
# Create Dataset
# -------------------------------

df = pd.DataFrame({
    "Age":[22,25,30,35,40,45,50,55],
    "Salary":[25000,30000,45000,60000,
              80000,100000,120000,150000],
    "Purchased":[0,0,0,1,1,1,1,1]
})

print("Original Dataset")
print(df)

# -------------------------------
# Separate Features and Target
# -------------------------------

X = df.drop("Purchased", axis=1)

y = df["Purchased"]

# -------------------------------
# Train Test Split
# -------------------------------

X_train,X_test,y_train,y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# -------------------------------
# Create Scaler
# -------------------------------

scaler = MinMaxScaler()

# -------------------------------
# Fit and Transform Training Data
# -------------------------------

X_train_scaled = scaler.fit_transform(X_train)

# -------------------------------
# Transform Test Data
# -------------------------------

X_test_scaled = scaler.transform(X_test)

print("\nTraining Data")
print(X_train)

print("\nScaled Training Data")
print(X_train_scaled)

print("\nTesting Data")
print(X_test)

print("\nScaled Testing Data")
print(X_test_scaled)