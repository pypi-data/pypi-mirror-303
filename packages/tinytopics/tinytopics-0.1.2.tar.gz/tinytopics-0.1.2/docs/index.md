# tinytopics <img src="assets/logo.png" align="right" width="120" />

[![PyPI version](https://img.shields.io/pypi/v/tinytopics)](https://pypi.org/project/tinytopics/)
![License](https://img.shields.io/pypi/l/tinytopics)
![Python versions](https://img.shields.io/pypi/pyversions/tinytopics)

Topic modeling via sum-to-one constrained Poisson non-negative
matrix factorization, built with PyTorch, runs on both CPUs and GPUs.

## Installation

You can install tinytopics from PyPI:

```bash
pip3 install tinytopics
```

Or install the development version from GitHub:

```bash
git clone https://github.com/nanxstats/tinytopics.git
cd tinytopics
python3 -m pip install -e .
```

## GPU support

The above will install the CPU version of PyTorch by default. To enable GPU support,
follow the [PyTorch official guide](https://pytorch.org/get-started/locally/)
to install the appropriate PyTorch version.

For example, to install PyTorch for Windows with CUDA 12.4:

```bash
pip3 uninstall torch
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
```

To manage the PyTorch dependency under a project context using virtual
environments, you might want to set up manual sources. For example,
[using Rye](https://rye.astral.sh/guide/faq/#how-do-i-install-pytorch).

## Get started

After tinytopics is installed, try the example from the
[getting started guide](https://nanx.me/tinytopics/articles/get-started/)
or see the [speed benchmark](https://nanx.me/tinytopics/articles/benchmark/).

## License

MIT
