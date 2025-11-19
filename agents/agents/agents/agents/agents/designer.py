class Designer:
    def create_plan(self, literature, topic):
        plan = {
            "goal": f"Build a classifier on a synthetic dataset related to: {topic}",
            "model": "RandomForestClassifier",
            "metric": "accuracy",
            "dataset": "synthetic classification dataset (20 features, 800 samples)",
            "steps": [
                "Generate synthetic dataset",
                "Split into train/test",
                "Train RandomForest model",
                "Evaluate accuracy",
                "Return metrics and plots"
            ]
        }
        return plan
