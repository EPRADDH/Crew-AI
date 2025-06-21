# Crew-AI
Crew AI framework : orchestrating high performing AI agents with ease and scale

# Crew-AI Debate Project
An AI-powered debate system using CrewAI framework to orchestrate high-performing AI agents for automated debates.

## Table of Contents
- [Project Overview](#project-overview)
- [Installation](#installation)
- [Project Setup](#project-setup)
- [CrewAI Components Used](#crewai-components-used)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)

## Project Overview

This project implements an automated debate system using CrewAI framework. The system consists of two main agents:
- **Debater Agent**: Can argue both for and against a given motion
- **Judge Agent**: Evaluates the arguments and decides the winner

The debate follows a sequential process where the debater presents arguments for and against the motion, and then the judge evaluates both sides to determine the winner.

## Installation

### Prerequisites
- Python 3.10 or higher (but less than 3.14)
- pip package manager

### Step 1: Install Dependencies
```bash
cd first_proj_crewai_debate
pip install -e .
```

### Step 2: Set Up Environment Variables
Create a `.env` file in the project directory:
```bash
# .env
OPENAI_API_KEY=your_openai_api_key_here
```

### Step 3: Verify Installation
```bash
python -c "import crewai; print('CrewAI installed successfully!')"
```

## Project Setup

### Project Structure
```
first_proj_crewai_debate/
├── src/
│   └── first_proj_crewai_debate/
│       ├── config/
│       │   ├── agents.yaml          # Agent configurations
│       │   └── tasks.yaml           # Task configurations
│       ├── tools/
│       │   └── custom_tool.py       # Custom tools for agents
│       ├── crew.py                  # Main crew implementation
│       └── main.py                  # Entry point
├── knowledge/
│   └── user_preference.txt          # User context information
├── output/                          # Generated debate outputs
│   ├── propose.md
│   ├── oppose.md
│   └── judg_decide.md
├── pyproject.toml                   # Project configuration
└── README.md
```

## CrewAI Components Used

### 1. CrewBase Decorator
The project uses the `@CrewBase` decorator to create a structured crew class:

```python
@CrewBase
class Debate():
    """Debate crew"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'
```

### 2. Agents
Two specialized agents are defined using the `@agent` decorator:

#### Debater Agent
- **Role**: Compelling debater who can argue for or against a given topic
- **Goal**: Present the best and clear arguments either in favor of or against the given motion
- **Backstory**: Experienced debater with a knack for giving concise but convincing arguments
- **LLM**: OpenAI GPT-4o-mini

#### Judge Agent
- **Role**: Decide the winner of the debate based on the arguments presented
- **Goal**: Evaluate arguments for and against the motion and decide which side is more convincing
- **Backstory**: Fair judge with reputation for weighing arguments without personal bias
- **LLM**: OpenAI GPT-4o-mini

### 3. Tasks
Three sequential tasks are defined using the `@task` decorator:

#### Propose Task
- **Description**: Argue in favor of the motion
- **Agent**: Debater
- **Output**: Clear argument in favor of the motion
- **File**: `output/propose.md`

#### Oppose Task
- **Description**: Argue against the motion
- **Agent**: Debater
- **Output**: Clear argument against the motion
- **File**: `output/oppose.md`

#### Judge Decide Task
- **Description**: Review arguments and decide the winner
- **Agent**: Judge
- **Output**: Decision on which side is more convincing
- **File**: `output/judg_decide.md`

### 4. Crew Configuration
The crew is configured with:
- **Process**: Sequential execution
- **Verbose**: True for detailed logging
- **Agents**: Automatically created by decorators
- **Tasks**: Automatically created by decorators

### 5. YAML Configuration
The project uses YAML files for agent and task configurations, making it easy to modify behavior without changing code.

## Usage

### Running the Debate
```bash
# From the project directory
python -m first_proj_crewai_debate.main

# Or using the installed script
first_proj_crewai_debate
```

### Customizing the Motion
Edit the `main.py` file to change the debate motion:

```python
inputs = {
    'motion': 'Your custom debate motion here',
}
```

### Output Files
After running the debate, check the `output/` directory for:
- `propose.md`: Arguments in favor of the motion
- `oppose.md`: Arguments against the motion
- `judg_decide.md`: Judge's decision and reasoning

## Configuration

### Agent Configuration (`config/agents.yaml`)
```yaml
debater:
  role: "A compelling debater who can argue for or against a given topic"
  goal: "Present the best and clear arguments either in favor of or against the given motion"
  backstory: "You're an experienced debater with a knack for giving concise but convincing arguments"
  llm: "openai/gpt-4o-mini"

judge:
  role: "Decide the winner of the debate based on the arguments presented"
  goal: "Given arguments for and against this motion, decide which side is more convincing"
  backstory: "You are a fair judge with a reputation for weighing up arguments without factoring in your own views"
  llm: "openai/gpt-4o-mini"
```

### Task Configuration (`config/tasks.yaml`)
```yaml
propose:
  description: "You are proposing the motion: {motion}. Come up with a clear argument in favor of the motion."
  expected_output: "Your clear argument in favor of the motion, in a concise manner."
  agent: debater
  output_file: output/propose.md

oppose:
  description: "You are in opposition to the motion: {motion}. Come up with a clear argument against the motion."
  expected_output: "Your clear argument against the motion, in a concise manner."
  agent: debater
  output_file: output/oppose.md

judg_decide:
  description: "Review the arguments presented by the debaters and decide which side is more convincing."
  expected_output: "Your decision on which side is more convincing, and why."
  agent: judge
  output_file: output/judg_decide.md
```

## Troubleshooting

### Common Issues

#### 1. Import Error: Module not found
**Solution**: Ensure the project is installed in development mode:
```bash
pip install -e .
```

#### 2. API Key Error
**Solution**: Set your OpenAI API key in the `.env` file:
```bash
OPENAI_API_KEY=your_actual_api_key_here
```

#### 3. Permission Denied Error
**Solution**: Use virtual environment:
```bash
python -m venv debate_env
source debate_env/bin/activate  # On Windows: debate_env\Scripts\activate
pip install -e .
```

#### 4. Output Directory Issues
**Solution**: Ensure the output directory exists:
```bash
mkdir -p output
```

### Getting Help

1. **Documentation**: Visit [CrewAI Documentation](https://docs.crewai.com/)
2. **GitHub Issues**: Check [CrewAI GitHub Issues](https://github.com/joaomdmoura/crewAI/issues)
3. **Community**: Join the [CrewAI Discord](https://discord.gg/crewai)

## Best Practices

1. **Clear Motion Definition**: Define specific, debatable motions
2. **Balanced Arguments**: Ensure both sides have equal opportunity to present arguments
3. **Output Review**: Regularly review generated arguments for quality
4. **Configuration Management**: Use YAML files for easy customization
5. **Error Handling**: Implement proper error handling for API calls
6. **Logging**: Use verbose mode to monitor agent interactions

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

For support and questions:
- Create an issue on GitHub
- Check the documentation

---

**Happy Debating! 🎭**

