# MultiAgentResearchAssistant

MultiAgentResearchAssistant is a lightweight framework that orchestrates multiple autonomous agents to assist with research tasks such as literature review, information extraction, and pipeline automation.

**Key features**
- Multi-agent coordination for research workflows
- Modular pipeline and tool components in `src/pipeline` and `src/Tools`
- Extensible agent implementations in `src/Agents`

**Requirements**
- Python (recommended via conda virtual environment)
- See `requirements.txt` for Python dependencies

**Setup (recommended)**
1. Create a conda environment (example):

```bash
conda create -n langagent python=3.14.2 -y
conda activate langagent
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

**Running the app**
- From the repository root you can run the main entrypoint:

```bash
python main.py
```

If you prefer, you can also run `app.py` depending on your workflow.

**Repository layout**
- `main.py` — CLI / entrypoint for launching the app
- `app.py` — application bootstrap (root-level alternative entry)
- `src/` — main source folder
	- `src/app.py` — library entry and shared utilities
	- `src/Agents/agents.py` — agent implementations and orchestration
	- `src/pipeline/pipeline.py` — pipeline definitions and orchestration
	- `src/Tools/tools.py` — helper tools used by agents and pipelines

**Development & contribution**
- Create feature branches, open PRs, and add tests for new functionality.
- Update `requirements.txt` and README when adding new dependencies or features.

**License**
This project is released under the terms of the LICENSE file in the repository.

---

If you'd like, I can: update the README with more detailed usage examples, add quickstart scripts, or generate a short CONTRIBUTING.md. Tell me which you'd prefer.

