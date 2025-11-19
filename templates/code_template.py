"""
Auto-generated experiment template.

This template is used by the CoderExecutor agent to build ML experiments.
"""

from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

def run_experiment():
    # Generate synthetic data
    X, y = make_classification(
        n_samples=500,
        n_features=20,
        random_state=42
    )

    # Split
    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2)

    # Model
    clf = RandomForestClassifier(n_estimators=15)
    clf.fit(Xtr, ytr)

    # Evaluate
    acc = clf.score(Xte, yte)
    print("ACCURACY:", acc)
