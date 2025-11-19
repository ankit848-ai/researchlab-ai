import json
import matplotlib.pyplot as plt
import re

class Analyst:
    def process(self, result, session_id):
        stdout = result["stdout"]

        # Extract accuracy from stdout
        match = re.search(r"ACCURACY:\s*([0-9.]+)", stdout)
        if match:
            acc = float(match.group(1))
        else:
            acc = 0.0

        # Save plot
        plt.figure(figsize=(6, 4))
        plt.bar(["Accuracy"], [acc])
        plt.title("Model Accuracy")
        plt.ylabel("Score")
        plot_path = f"artifacts/{session_id}/accuracy.png"
        plt.savefig(plot_path)

        # Save metrics
        metrics = {"accuracy": acc}
        metrics_path = f"artifacts/{session_id}/metrics.json"
        with open(metrics_path, "w") as f:
            json.dump(metrics, f, indent=4)

        return metrics
