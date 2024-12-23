# <img src="assets/images/logo.png" alt="etura logo" width="40"/> etura Retriever

<div align="center">

<!-- [![Build status](https://github.com/etura-org/etura/workflows/build/badge.svg?branch=main&event=push)](https://github.com/etura-org/etura/actions?query=workflow%3Abuild) -->

[![Code style: ruff](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/astral-sh/ruff)
[![Security: bandit](https://img.shields.io/badge/security-bandit-green.svg)](https://github.com/PyCQA/bandit)
[![Semantic Versions](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--versions-e10079.svg)](https://github.com/etura-org/etura/releases)
[![License](https://img.shields.io/github/license/etura-org/etura)](https://github.com/etura-org/etura/blob/main/LICENSE)
![Coverage Report](assets/images/coverage.svg)

An enterprise-grade AI retriever designed to streamline AI integration into your applications, ensuring cutting-edge accuracy.

</div>

## 📝 Description

etura Retriever combines multiple search technologies into a single platform. It utilizes **gradient boosting (
xgboost)** machine learning technique to combine:

- **Keyword-based searches** that focus on fetching precisely what the query mentions.
- **Vector databases** that are great for finding a wide range of potentially relevant answers.
- **Machine Learning rerankers** that fine-tune the results to ensure the most relevant answers top the list.

* Our experiments on MTEB datasets show that the combination of keyword search, vector search and a reranker via a xgboost model (denoted as ES+VS+RR_n) can significantly improve the vector search (VS) baseline.

![mteb_ndcg_plot](mteb_ndcg_plot.png)

* **Check out etura Retriever experiments using the Anthropic Contextual Retrieval dataset at [here](https://github.com/Lumicrownai/Etura-agent/tree/master/experiments/data/contextual-embeddings)**.
## 🚀 Features

The initial release of etura Retriever provides the following features.

- Supporting heterogeneous retrievers such as **keyword search**, **vector search**, and **ML model reranking**
- Leveraging **xgboost** ML technique to effectively combine heterogeneous retrievers
- **State-of-the-art accuracy** on [MTEB](https://github.com/embeddings-benchmark/mteb) Retrieval benchmarking
- Demonstrating how to use etura retriever to power an **end-to-end applications** such as chatbot and semantic search

## 📦 Installation

We recommend installing Python via [Anaconda](https://www.anaconda.com/download), as we have received feedback about issues with Numpy installation when using the installer from https://www.python.org/downloads/. We are working on providing a solution to this problem. To install etura Retriever, you can run:

### Pip

```bash
pip install git+https://github.com/etura-org/etura.git#main
```

### Poetry

```bash
poetry add git+https://github.com/etura-org/etura.git#main
```

## 📃 Documentation

The official documentation is hosted on [retriever.etura.ai](https://retriever.etura.ai).
Click [here](https://retriever.etura.ai/docs/quick-start) to get started.

## 👨🏼‍💻 Development

You can start developing etura Retriever on your local machine.

See [DEVELOPMENT.md](DEVELOPMENT.md) for more details.

## 🛡 License

[![License](https://img.shields.io/github/license/denser-org/etura)](https://github.com/Lumicrownai/Etura-agent/blob/master/LICENSE)

This project is licensed under the terms of the `MIT` license.
See [LICENSE](https://github.com/denser-org/denser-retriever/blob/main/LICENSE) for more details.

## 📃 Citation

```bibtex
@misc{etura,
  author = {etura-org},
  title = {An enterprise-grade AI retriever designed to streamline AI integration into your applications, ensuring cutting-edge accuracy.},
  year = {2024},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/etura-org/etura}}
}
```
