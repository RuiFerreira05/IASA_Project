# Autonomous Agent Project

This project implements different types of autonomous agents (Reactive and Deliberative) in a simulation environment.

## Agent Types

### Reactive Agent (AgenteReact)

- Uses a reactive control architecture based on stimulus-response pairs
- Can perform exploration and item collection behaviors
- Makes decisions based on immediate perceptions of the environment

### Deliberative Agent (AgenteDelib)

- Uses a deliberative control architecture with an internal world model
- Can plan sequences of actions to achieve goals
- Uses A* search for pathfinding

### MDR Deliberative Agent (AgenteDelibPDM)

- Uses Markov Decision Process (MDP) for planning
- Takes into account uncertainty and rewards
- More sophisticated planning than basic deliberative agent
- Uses configurable gamma parameter (default 0.95) for future reward discounting

## Key Components

- SAE (Simulation Environment) - Provides the environment, visualization and basic agent infrastructure
- ECR (Stimulus-Response Control) - Framework for reactive behaviors
- Plan (Planning) - Planning components for deliberative agents
- PDM (Markov Decision Process) - MDP implementation for probabilistic planning

## Usage

The simulation can be run with different agents and environments:

```python
from agente.agente_delib import AgenteDelib
from sae import Simulador

# Create agent
agente = AgenteDelib()

# Run simulation with environment #4 and model visualization
simulador = Simulador(4, agente, vista_modelo=True)
simulador.executar()
```

## Testing

Tests are available for different components:

- Reactive agent behaviors
- World model updates
- Deliberative planning
- MDP planning

Run tests using doctest:

```python
python -m
