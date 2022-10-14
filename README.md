# POC - KOALA RESEARCH INSIGHTS

## Overview
1. [Mission Statement](#Mission-Statement)
1. [Use-cases](#Use-cases)
1. [The knowledge graph](#The-knowledge-graph)
1. [Sample of answers from graph](#Sample-of-answers-from-graph)
1. [Scraping PubMed](#Scraping-PubMed)
1. [Data preprocessing](#Data-preprocessing)
1. [Data enrichment (NER)](#Data-enrichment-(NER))
1. [Neo4j graph creation](#Neo4j-graph-creation)

## Mission Statement
This case study gives a taste of the type of information you can extract from knowledge graphs based on PubMed articles in the domain of [Koala research](https://en.wikipedia.org/wiki/Koala).

The core information source for this task are scientific abstracts from PubMed. Using named-entity-recognition (NER) from natural-language-processing (NLP) discipline and graphs we are able to extract latent information that provides insights into the koala-related research field.

For example, using the generated knowledge graph, one can easily find answers to questions below in [use cases](##Use-cases)

<img src="figures\360px-Koala_climbing_tree.jpg" alt="drawing" width="180"/>

## Use-cases
1. Who is the most productive researcher writing papers on koalas?
1. What is the most common topic in publications on koalas?
1. What diseases affect the animal?
1. What chemical factors are related to these diseases?
1. What are the rare diseases?
1. How does the prevalence of these diseases change over time?
1. Discover similar papers based on Keywords
1. Discover similar papers based on Diseases

## The knowledge graph
Schema of the generated graph showing the node types and their relationships:

<img src="figures\schema.png" alt="drawing" width="300"/>

An example of two connected papers in the knowledge graph and their connected nodes with relationships:

<img src="figures\graph_preview.png" alt="drawing" width="400"/>

## Sample of answers from graph

**What is the most common topic in publications on koalas?**

<img src="figures\query2.png" alt="drawing" width="500"/>

**Find similar papers based on Diseases**

<img src="figures\query8.png" alt="drawing" width="800"/>

[Link to notebook](preprocess.ipynb) that has answer to all the abovementioned use-cases.

##  Scraping PubMed
- Selenium package was used to scrape content from PubMed and BeautifulSoup was used to parse the content of the HTML
- Abstract, title, author names, year of publication, keywords, PMID and URL are saved to a dataframe
- [Link to notebook](scraper.ipynb)

##  Data preprocessing
- Content is cleaned to remove line breaks and to parse keywords into a list
- [Link to notebook](preprocess.ipynb)

##  Data enrichment (NER)
- Transformer based NER models from HuggingFace were used to extract a number of entities
- "dslim/bert-base-NER" was used to extract locations and organizations
- "alvaroalon2/biobert_*_ner" was used to extract biological entities such as diseases, chemicals and genetic entities
- [Link to notebook](enrich_ner.ipynb)

##  Neo4j graph creation
- The graph was created using a combination of the Neo4j python package and Cypher 
- [Link to notebook](build_graph.ipynb)
