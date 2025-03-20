## TOC
- [TOC](#toc)
- [Description](#description)
- [Structure](#structure)
- [Devcontainer](#devcontainer)
- [Usage](#usage)

## Description
Simple example of Dagger python module that uses an agent to fix Dockerfile

## Structure

- `test_dag` - directory with the main Dagger module.
- `test_dag/workspace` - directory with the Dagger module that's used as Workspace for the agent.
- `scripts` - helper bash scripts.
- `.devcontainer` - directory with the devcontainer configuration.

## Devcontainer

I recommend to use VSCode + devcontainer to run this example.
https://code.visualstudio.com/docs/devcontainers/containers

## Usage

1. Open the project in VSCode.
2. Reopen the project in a devcontainer: `<CTRL/CMD+SHIFT+P> -> Dev Containers: Rebuild and Reopen in Container`.
3. Configure LLM endpoints: https://docs.dagger.io/ai-agents/#2configure-llm-endpoints
4. Run the agent: `dagger call test-agent`
