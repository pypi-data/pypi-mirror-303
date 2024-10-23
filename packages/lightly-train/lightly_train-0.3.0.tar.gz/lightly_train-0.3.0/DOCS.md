## Installation

```bash
pip install lightly-train[tensorboard,timm]
```

## Usage

### Python

#### Training

```python
import lightly_train

lightly_train.train(
    out="my_output_dir",
    data="my_data_dir",
    model="torchvision/resnet18",
    method="simclr",
    batch_size=128,
    epochs=100,
    precision="16-mixed",
    optim_args=dict(lr=0.0001),
    method_args=dict(temperature=0.1),
)
```

In most cases you only have to specify `out`, `data`, and `model`. The rest is optional.

You can monitor your training process with the help of `tensorboard` and `wandb` loggers:

```
pip install "lightly-train[tensorboard, wandb]"
```

Configure the loggers from Python:

- `loggers={"tensorboard": True}`: Enable `tensorboard` logger with default arguments.
- `loggers={"wandb": True}`: Enable `wandb` logger with default arguments.
- `loggers={"wandb": {"project": "my-project"}}`: Configure `wandb` logger with custom arguments.

LightlyTrain uses the PyTorchLightning loggers under the hood. Learn more about their configuration:

- https://lightning.ai/docs/pytorch/stable/api/lightning.pytorch.loggers.wandb.html
- https://lightning.ai/docs/pytorch/stable/api/lightning.pytorch.loggers.tensorboard.html

#### Exporting

```python
import lightly_train

lightly_train.export(
    out="my_output_dir/model_state_dict.pt",
    checkpoint="my_output_dir/checkpoints/last.ckpt",
    part="model",
    format="torch_state_dict",
)
```

#### Embedding

```python
import lightly_train

lightly_train.embed(
    out="my_output_dir/embeddings.csv",
    data="my_data_dir",
    checkpoint="my_output_dir/checkpoints/last.ckpt",
    format="csv",
)
```

#### Supported Models

```python
import lightly_train
print(lightly_train.list_models())
```

#### Supported Methods

```python
import lightly_train
print(lightly_train.list_methods())
```

### Command Line

#### Help

```
lightly-train help
```

#### Training

```
lightly-train train \
    out=my_output_dir \
    data=my_data_dir \
    model=torchvision/resnet18 \
    method=simclr \
    batch_size=128 \
    epochs=100 \
    precision=16-mixed \
    optim_args.lr=0.0001 \
    method_args.temperature=0.1
```

In most cases you only have to specify `out`, `data`, and `model`. The rest is optional.

You can monitor your training process with the help of `tensorboard` and `wandb` loggers:

```
pip install "lightly-train[tensorboard, wandb]"
```

Configure the loggers from the command-line:

- `loggers.tensorboard=True`: Enable `tensorboard` logger with default arguments.
- `loggers.wandb=True`: Enable `wandb` logger with default arguments.
- `loggers.wandb.project="my-project"`: Configure `wandb` logger with custom arguments.

LightlyTrain uses the PyTorchLightning loggers under the hood. Learn more about their configuration:

- https://lightning.ai/docs/pytorch/stable/api/lightning.pytorch.loggers.wandb.html
- https://lightning.ai/docs/pytorch/stable/api/lightning.pytorch.loggers.tensorboard.html

```
tensorboard --logdir my_output_dir
```

#### Embedding

```
lightly-train embed \
    out=my_output_dir/embeddings.csv \
    data=my_data_dir \
    checkpoint=my_output_dir/checkpoints/last.ckpt \
    format=csv
```

#### Exporting

```
lightly-train export \
    out=my_output_dir/model_state_dict.pt \
    checkpoint=my_output_dir/checkpoints/last.ckpt \
    part=model \
    format=torch_state_dict
```

#### Supported Models

```
lightly-train list_models
```

#### Supported Methods

```
lightly-train list_methods
```
