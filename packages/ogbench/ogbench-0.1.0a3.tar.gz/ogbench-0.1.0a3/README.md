<div align="center">
<img src="assets/ogbench.svg" width="300px"/>

<hr>


# OGBench: Benchmarking Offline Goal-Conditioned RL


<a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.8%2B-598BE7?style=for-the-badge&logo=python&logoColor=598BE7&labelColor=F0F0F0"/></a> &emsp;
<a href="https://docs.astral.sh/ruff/"><img src="https://img.shields.io/badge/Code style-ruff-598BE7?style=for-the-badge&labelColor=F0F0F0"/></a> &emsp;
<a href="https://github.com/seohongpark/OGBench/blob/master/LICENSE"><img src="https://img.shields.io/badge/License-MIT-598BE7?style=for-the-badge&labelColor=F0F0F0"/></a>

![image](assets/env_teaser.png)


</div>


## Overview

OGBench is a benchmark designed to facilitate algorithms research
in offline goal-conditioned reinforcement learning (RL).
It consists of 8 types of environments, 85 datasets, and 6 reference implementations of
offline goal-conditioned RL algorithms (GCBC, GCIVL, GCIQL, QRL, CRL, and HIQL).


## How can I use the OGBench environments?

### Installation

OGBench can be easily installed via PyPI.
It requires Python 3.8+ and has only three dependencies: `mujoco >= 3.1.6`, `dm_control >= 1.0.20`,
and `gymnasium`.
To install OGBench, simply run:

```shell
pip install ogbench
```

### Quick start

After installing OGBench, you can make an environment and datasets by calling `ogbench.make_env_and_datasets`.
The environment follows the [Gymnasium](https://gymnasium.farama.org/) interface.
The datasets will be automatically downloaded on the first run.
Here is an example of how to use OGBench:

```python
import ogbench

# Make an environment and load datasets (they will be automatically downloaded if you haven't already).
dataset_name = 'antmaze-large-navigate-v0'
env, train_dataset, val_dataset = ogbench.make_env_and_datasets(dataset_name)

# Train your offline goal-conditioned RL agent using `train_dataset` here.
# ...

# Evaluate the agent.
for task_id in [1, 2, 3, 4, 5]:
    # Reset the environment and set the evaluation task.
    ob, info = env.reset(
        options=dict(
            task_id=task_id,  # Set evaluation task. Each environment provides five evaluation goals and `task_id` must be in [1, 5].
            render_goal=True,  # Set to `True` to get a rendered goal image (optional).
        )
    )

    goal = info['goal']  # Get the goal observation that can be passed to the agent.
    goal_rendered = info['goal_rendered']  # Get the rendered goal image (optional).

    done = False
    while not done:
        action = env.action_space.sample()  # Replace this with your agent's action.
        ob, reward, terminated, truncated, info = env.step(action)  # OGBench follows the Gymnasium interface.
        # If the agent reaches the goal, `terminated` will be `True`.
        # If the episode length exceeds the maximum length without reaching the goal, `truncated` will be `True`.
        done = terminated or truncated
        frame = env.render()  # Render the current frame (optional).

    success = info['success']  # Whether the agent reached the goal (0 or 1). `terminated` also indicates this.
```

### Dataset APIs

OGBench provides several APIs to download and load datasets.
The simplest way is to use `ogbench.make_env_and_datasets`, which makes an environment
as well as training and validation datasets.
The datasets will automatically be downloaded to the directory specified by `dataset_dir` on the first run
(default: `~/.ogbench/data`).
It also provides the `compact_dataset` option to get a compact dataset without the `next_observations` field.
For example:
```python
import ogbench

# Make an environment and load datasets.
dataset_name = 'antmaze-large-navigate-v0'
env, train_dataset, val_dataset = ogbench.make_env_and_datasets(
    dataset_name,  # Dataset name.
    dataset_dir='~/.ogbench/data',  # Directory to save datasets (optional, default: `~/.ogbench/data`).
    compact_dataset=False,  # Whether to use a compact dataset (optional, default: `False`); see below.
)

# Assume each dataset trajectory has length 4, and (s0, a0, s1), (s1, a1, s2), (s2, a2, s3), (s3, a3, s4) are the transition tuples.
# If `compact_dataset` is `False`, the dataset will have the following structure:
#                       |<- traj 1 ->|  |<- traj 2 ->|  ...
# ----------------------------------------------------------
# 'observations'     : [s0, s1, s2, s3, s0, s1, s2, s3, ...]
# 'actions'          : [a0, a1, a2, a3, a0, a1, a2, a3, ...]
# 'next_observations': [s1, s2, s3, s4, s1, s2, s3, s4, ...]
# 'terminals'        : [ 0,  0,  0,  1,  0,  0,  0,  1, ...]

# If `compact_dataset` is `True`, the dataset will have the following structure, where the `next_observations` field is omitted,
# and it instead has a `valids` field that indicates whether the next observation is valid:
#                       |<--- traj 1 --->|  |<--- traj 2 --->|  ...
# ------------------------------------------------------------------
# 'observations'     : [s0, s1, s2, s3, s4, s0, s1, s2, s3, s4, ...]
# 'actions'          : [a0, a1, a2, a3, a4, a0, a1, a2, a3, a4, ...]
# 'terminals'        : [ 0,  0,  0,  1,  1,  0,  0,  0,  1,  1, ...]
# 'valids'           : [ 1,  1,  1,  1,  0,  1,  1,  1,  1,  0, ...]
```

If you want to download multiple datasets at once, you can use `ogbench.download_datasets`:
```python
import ogbench

dataset_names = ['humanoidmaze-medium-navigate-v0', 'visual-puzzle-3x3-play-v0', 'powderworld-easy-play-v0']
ogbench.download_datasets(
    dataset_names,  # List of dataset names.
    dataset_dir='~/.ogbench/data',  # Directory to save datasets (optional, default: `~/.ogbench/data`).
)
```


## How can I use the reference implementations?

OGBench also provides Jax-based reference implementations of offline goal-conditioned RL algorithms
(GCBC, GCIVL, GCIQL, QRL, CRL and HIQL).
They are provided in the `impls` directory as a **standalone** codebase.
You can safely remove the other parts of the repository if you only want to use the reference implementations
and do not want to modify the environments.

### Installation

Our reference implementations require Python 3.9+ and additional dependencies, including `jax >= 0.4.26`.
To install these dependencies, run:

```shell
cd impls
pip install -r requirements.txt
```

By default, it uses the PyPI version of OGBench.
If you want to use a local version of OGBench (e.g., to modify the environments),
you can replace the PyPI version with the local version with `pip install -e .` in the root directory.

### Running the reference implementations

Each algorithm is implemented in a separate file in the `agents` directory.
We provide implementations of the following offline goal-conditioned RL algorithms:

- `gcbc.py`: Goal-Conditioned Behavioral Cloning (GCBC)
- `gcivl.py`: Goal-Conditioned Implicit V-Learning (GCIVL)
- `gciql.py`: Goal-Conditioned Implicit Q-Learning (GCIQL)
- `qrl.py`: Quasimetric Reinforcement Learning (QRL)
- `crl.py`: Contrastive Reinforcement Learning (CRL)
- `hiql.py`: Hierarchical Implicit Q-Learning (HIQL)

To train an agent, you can run the `main.py` script.
Here are some examples (see [hyperparameters.sh](impls/hyperparameters.sh) for the full list of commands):

```shell
# antmaze-large-navigate-v0 (GCBC)
python main.py --env_name=antmaze-large-navigate-v0 --agent=agents/gcbc.py
# antmaze-large-navigate-v0 (GCIVL)
python main.py --env_name=antmaze-large-navigate-v0 --agent=agents/gcivl.py --agent.alpha=10.0
# antmaze-large-navigate-v0 (GCIQL)
python main.py --env_name=antmaze-large-navigate-v0 --agent=agents/gciql.py --agent.alpha=0.3
# antmaze-large-navigate-v0 (QRL)
python main.py --env_name=antmaze-large-navigate-v0 --agent=agents/qrl.py --agent.alpha=0.003
# antmaze-large-navigate-v0 (CRL)
python main.py --env_name=antmaze-large-navigate-v0 --agent=agents/crl.py --agent.alpha=0.1
# antmaze-large-navigate-v0 (HIQL)
python main.py --env_name=antmaze-large-navigate-v0 --agent=agents/hiql.py --agent.high_alpha=3.0 --agent.low_alpha=3.0
```

### Notes on hyperparameters and flags

To reproduce the results in the paper, you need to use the hyperparameters provided in the paper.
We provide the exact command-line flags to reproduce the entire main benchmark table in the paper in [hyperparameters.sh](impls/hyperparameters.sh).
We highlight some important hyperparameters and common gotchas below:

- Regardless of the algorithms, one of the most important hyperparameters is `agent.alpha` (i.e., the temperature (AWR) or the BC coefficient (DDPG+BC))
for the actor loss. It is crucial to tune this hyperparameter when running an algorithm on a new environment.
In the paper, we provide a separate table of the policy extraction hyperparameters,
which are individually tuned for each environment and dataset category.
- By default, actor goals are uniformly sampled from the future states in the same trajectory.
We found this to work the best in most cases, but you can adjust this (e.g., by setting
`--agent.actor_p_trajgoal=0.5 --agent.actor_p_randomgoal=0.5`) to allow random actor goals.
This is especially important for datasets that require stitching.
See the hyperparameter table in the paper for the values we used for benchmarking.
- For GCIQL, CRL, and QRL, we provide two policy extraction methods: AWR and DDPG+BC.
In general, DDPG+BC works better than AWR (see [this paper](https://arxiv.org/abs/2406.09329) for the reasons),
but DDPG+BC is usually more sensitive to the `alpha` hyperparameter than AWR.
Hence, in a new environment, we may recommend starting with AWR and then switching to DDPG+BC to further improve the performance.
- Our QRL implementation provides two quasimetric parameterizations: MRN and IQE.
We found that IQE (default) works better in general, but MRN is faster to train.
- In CRL, we found that using `--agent.actor_log_q=True` (which is set by default) is important for achieving strong performance, especially in locomotion environments.
We also found that this doesn't help much with other algorithms.
- In HIQL, it is crucial to set `--agent.low_actor_rep_grad=True` (which is `False` by default) in pixel-based environments.
This allows gradients to flow from the low-level actor loss to the subgoal representation, which helps maintain better representations.
Generally, we found that subgoal representation learning is often the bottleneck in HIQL.
- In pixel-based environments, don't forget to set `agent.encoder`. We used `--agent.encoder=impala_small` on all pixel-based environments.
- In discrete-action environments (e.g., Powderworld), don't forget to set `--agent.discrete=True`.
- In Powderworld, we used `--eval_temperature=0.3`, which helps prevent the agent from getting stuck at some states.


## How can I reproduce the datasets?

We provide the full scripts and exact command-line flags to reproduce all the datasets in OGBench.
We believe this not only ensures reproducibility but also enables various ablation studies and extensions.
The scripts are provided in the `data_gen_scripts` directory.

### Installation

Data-generation scripts for locomotion environments require Python 3.9+ and additional dependencies,
including `jax >= 0.4.26`, to train and load expert agents.
For manipulation and drawing environments, you don't need any additional dependencies.
To install the additional dependencies for locomotion environments, run in the root directory:
```shell
pip install -e ".[train]"
```

### Reproducing the datasets

To reproduce the datasets, you can run the scripts in the `data_gen_scripts` directory.
For locomotion environments, you need to download the expert policies first.
We provide the exact command-line flags to reproduce the datasets in [commands.sh](data_gen_scripts/commands.sh).
Here is an example of how to reproduce a dataset for the `antmaze-large-navigate-v0` task:

```shell
cd data_gen_scripts
# Download the expert policies for locomotion environments (not required for manipulation and drawing environments).
wget https://rail.eecs.berkeley.edu/datasets/ogbench/experts.tar.gz
tar xf experts.tar.gz && rm experts.tar.gz
# Run the scripts to generate the datasets.
mkdir -p data  # Directory to save the datasets.
export PYTHONPATH="../impls:${PYTHONPATH}"  # Add the `impls` directory to PYTHONPATH. Alternatively, you can simply add `PYTHONPATH=../impls` before the python command.
python generate_locomaze.py --env_name=antmaze-large-v0 --save_path=data/antmaze-large-navigate-v0.npz --dataset_type=navigate --num_episodes=1000 --max_episode_steps=1001 --restore_path=experts/ant --restore_epoch=400000
```

### Reproducing the expert policies

If you want to train your own expert policies from scratch, you can run the corresponding commands in [commands.sh](data_gen_scripts/commands.sh).
For example, to train an Ant expert policy, you can run in the `data_gen_scripts` directory after setting `PYTHONPATH` as above:
```shell
python main_sac.py --env_name=online-ant-xy-v0 --train_steps=400000 --eval_interval=100000 --save_interval=400000 --log_interval=5000
```

## Acknowledgments

This codebase is inspired by and partly uses the code from the following repositories:
- [D4RL](https://github.com/Farama-Foundation/D4RL) for the dataset structure and the AntMaze environment.
- [Gymnasium](https://github.com/Farama-Foundation/Gymnasium) and [dm_control](https://github.com/google-deepmind/dm_control) for the agents (Ant and Humanoid) in the locomotion environments.
- [MuJoCo Menagerie](https://github.com/google-deepmind/mujoco_menagerie) for the robot descriptions (Universal Robots UR5e and Robotiq 2F-85) in the manipulation environments.
- [jaxlie](https://github.com/brentyi/jaxlie) for the Lie group operations in the manipulation environments.
- [Meta-World](https://github.com/Farama-Foundation/Metaworld) for the objects (drawer, window, and button) in the manipulation environments.
- [Powderworld](https://github.com/kvfrans/powderworld) for the Powderworld environment.
- [NumPyConv2D](https://github.com/99991/NumPyConv2D) for the NumPy Conv2D implementation in the Powderworld environment.
- [jaxrl_m](https://github.com/dibyaghosh/jaxrl_m), [rlbase](https://github.com/kvfrans/rlbase_stable),
  [HIQL](https://github.com/seohongpark/HIQL), and [cmd-notebook](https://github.com/vivekmyers/cmd-notebook)
  for the Jax-based implementations of RL algorithms.

We especially thank [Kevin Zakka](https://kzakka.com/) for providing the initial codebase for the manipulation environments.

## Citation

```bibtex
@article{ogbench_park2024,
  title={OGBench: Benchmarking Offline Goal-Conditioned RL},
  author={Seohong Park and Kevin Frans and Benjamin Eysenbach and Sergey Levine},
  journal={ArXiv},
  year={2024},
  volume={abs/...}
}
```