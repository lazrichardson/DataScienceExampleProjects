# Data Science Example Projects

This repository highlights my example projects for datascience.

## Bag of Words and Latent Semantic Analysis

This project implements a bag of words and topic clustering using Latent Semantic Analysis

This project uses the IndieGogo Dataset (https://webrobots.io/indiegogo-dataset/) to download at least 5 files. It takes
the “title” for each project in the dataset.

Then, the article titles are put into a “bag of words” format. Finally, Latent Semantic Analysis (LSA) is used to cluser
them into related topics.

## Dimensionality Reduction

This project is focused on dimensionality reduction of textual data.

- This project downloads at least 200 Pubmed articles. 100 include the term “obesity”, and the other 100 include the
  term “cancer”.
- Their textual corpus is analyzed to feed them into a dimensionality reduction method.
- Finally, Principal Component Analysis (PCA), T-distributed stochastic neighbor embedding (tSNE), and Uniform Manifold
  Approximation and Projection for Dimension Reduction (UMAP) algorithms are applied to the dataset to visualize the

## Graph Analysis

This project explores different approaches to graph analysis.

* Dijkstra's shortest path visualized on a graph.
* Prim's, and Kruskal's minimum spanning tree algorithms to find the MST between two arbitrary nodes
* Visualization of Page rank and HITS algorithm to order the graph nodes based on their importance
* Visualization of the Louvain and Leiden algorithms for community detection

## Sentiment Analysis

This project collects tweets about soccer to analyze their sentiment, comparing results of Afinn and FastText.

* Search, clean, and load the tweets using the Twitter API
* Calculate sentiments using Afinn
* Train a FastText model
* Find sentiments using FastText model

## Distribution Analysis and Testing

This project is focused on exploring different testing methods using the IndieGogo dataset

It demonstrates:

* Testing for Gaussian distributions using Q-Q plots, and the Shapiro Wilk test
* Parametric testing using the Welch Two Sample t-test
* Non-Parametric testing using Two-sample Kolmogorov-Smirnov test and Wilcoxon rank sum test with continuity correction
* Calculation of effect size to quantify the magnitude of differences using Cohen's D
* Correlation Coefficient testing (Pearson, Spearman, KendallTau)
