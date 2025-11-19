import subprocess
import os

class CoderExecutor:
    def generate_code(self, plan, session_id):
        code_path = f"artifacts/{session_id}/experiment.py"

        with open(code_path, "w") as f:
            f.write("""
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Generate synthetic dataset
X, y = make_classification(n_samples=800, n_features=20, random_state=42)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
clf = RandomForestClassifier(n_estimators=20, random_state=42)
clf.fit(Xtr, ytr)

# Evaluate
acc = clf.score(Xte, yte)
print("ACCURACY:", acc)
""")

        return code_path

    def execute_code(self, path, session_id):
        run = subprocess.run(
            ["python", path], capture_output=True, text=True
        )

        result = {
            "stdout": run.stdout,
            "stderr": run.stderr,
            "returncode": run.returncode,
        }

        # Save logs
        log_path = f"artifacts/{session_id}/run_logs.txt"
        with open(log_path, "w") as f:
            f.write("STDOUT:\n" + run.stdout + "\n\n")
            f.write("STDERR:\n" + run.stderr + "\n\n")

        return result
