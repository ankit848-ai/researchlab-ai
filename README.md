# ResearchLab-AI  
Autonomous Multi-Agent Research Lab that turns a topic into:
- literature review  
- experiment plan  
- runnable ML code  
- analysis & metrics  
- research paper PDF  
- slide deck (PPTX)

## 🔥 Demo
Run `demo/demo_pipeline.ipynb` inside Kaggle Notebook.  
The pipeline will:
1. Generate literature summary  
2. Design experiment  
3. Auto-generate Python code  
4. Execute it  
5. Analyze results  
6. Create paper.pdf + slides.pptx  

Artifacts will appear in `/artifacts/SESSION_ID/`.

## 🧠 Multi-Agent Architecture
ResearchLab-AI uses 6 agents:
- **Orchestrator** – controls workflow  
- **Researcher Agent** – does literature search + dataset discovery  
- **Designer Agent** – creates hypothesis + experiment plan  
- **Coder Executor Agent** – writes and runs ML code  
- **Analyst Agent** – computes metrics + creates plots  
- **Writer Agent** – generates PDF + PPT outputs  

Includes:
- Memory Bank  
- Session Manager  
- Custom tools  
- Observability (logs + metrics)  

## ▶️ How to Run Locally
