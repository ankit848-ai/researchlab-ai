import argparse
from agents.orchestrator import Orchestrator

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--topic", type=str, required=True)
    parser.add_argument("--mode", type=str, default="demo")
    
    args = parser.parse_args()
    orch = Orchestrator()
    res = orch.run(args.topic, mode=args.mode)
    print("Pipeline executed. Artifacts saved in artifacts/")
