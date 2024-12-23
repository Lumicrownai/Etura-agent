# <img src="assets/images/logo.png" alt="LumiCrown logo" width="40"/> Etura

<div align="center">

<!-- [![Build status](https://github.com/denser-org/etura/workflows/build/badge.svg?branch=main&event=push)](https://github.com/denser-org/etura/actions?query=workflow%3Abuild) -->

[![Python Version](https://img.shields.io/pypi/pyversions/etura.svg)](https://pypi.org/project/etura/)
[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/denser-org/etura/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)

[![Code style: ruff](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/astral-sh/ruff)
[![Security: bandit](https://img.shields.io/badge/security-bandit-green.svg)](https://github.com/PyCQA/bandit)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/denser-org/etura/blob/main/.pre-commit-config.yaml)
[![Semantic Versions](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--versions-e10079.svg)](https://github.com/denser-org/etura/releases)
[![License](https://img.shields.io/github/license/denser-org/etura)](https://github.com/denser-org/etura/blob/main/LICENSE)
![Coverage Report](assets/images/coverage.svg)

An enterprise-grade AI retriever designed to streamline AI integration into your applications, ensuring cutting-edge accuracy.

</div>

## 📝 Description

Etura combines multiple search technologies into a single platform. It utilizes **gradient boosting (
xgboost)** machine learning technique to combine:

- **Keyword-based searches** that focus on fetching precisely what the query mentions.
- **Vector databases** that are great for finding a wide range of potentially relevant answers.
- **Machine Learning rerankers** that fine-tune the results to ensure the most relevant answers top the list.

* Our experiments on MTEB datasets show that the combination of keyword search, vector search and a reranker via a xgboost model (denoted as ES+VS+RR_n) can significantly improve the vector search (VS) baseline.

![mteb_ndcg_plot](mteb_ndcg_plot.png)

* **Check out Etura experiments using the Anthropic Contextual Retrieval dataset at [here](https://github.com/denser-org/etura/tree/main/experiments/data/contextual-embeddings)**.
## 🚀 Features

The initial release of Etura provides the following features.

- Supporting heterogeneous retrievers such as **keyword search**, **vector search**, and **ML model reranking**
- Leveraging **xgboost** ML technique to effectively combine heterogeneous retrievers
- **State-of-the-art accuracy** on [MTEB](https://github.com/embeddings-benchmark/mteb) Retrieval benchmarking
- Demonstrating how to use Etura to power an **end-to-end applications** such as chatbot and semantic search

## 📦 Installation

We recommend installing Python via [Anaconda](https://www.anaconda.com/download), as we have received feedback about issues with Numpy installation when using the installer from https://www.python.org/downloads/. We are working on providing a solution to this problem. To install Etura, you can run:

### Pip

```bash
pip install git+https://github.com/denser-org/etura.git#main
```

### Poetry

```bash
poetry add git+https://github.com/denser-org/etura.git#main
```

## 📃 Documentation

The official documentation is hosted on [retriever.denser.ai](https://retriever.denser.ai).
Click [here](https://retriever.denser.ai/docs/quick-start) to get started.

## 👨🏼‍💻 Development

You can start developing Etura on your local machine.

See [DEVELOPMENT.md](DEVELOPMENT.md) for more details.

## 🛡 License

[![License](https://img.shields.io/github/license/denser-org/etura)](https://github.com/denser-org/etura/blob/main/LICENSE)

This project is licensed under the terms of the `MIT` license.
See [LICENSE](https://github.com/denser-org/etura/blob/main/LICENSE) for more details.

## 📃 Citation

```bibtex
@misc{etura,
  author = {denser-org},
  title = {An enterprise-grade AI retriever designed to streamline AI integration into your applications, ensuring cutting-edge accuracy.},
  year = {2024},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/denser-org/etura}}
}
```
