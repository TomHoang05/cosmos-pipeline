A personal data engineering project built around space-related data, covering objects and phenomena across Earth, the solar system, deep space, and beyond.

## What This Project Is

Cosmos pipeline is a full-stack data engineering system designed and built from the ground up as a learning environment. The domain, space data, is a vehicle for that purpose: it provides a rich, varied, and publicly available source of information that naturally lends itself to the kinds of problems data engineering is meant to solve. Datasets range from near-real-time telemetry on near-Earth asteroids to static catalogs of stars and galaxies, which means the system has to handle different ingestion patterns, storage strategies, and processing requirements depending on the source.

The project is not a demo or a prototype built to prove a concept quickly. It's a working system developed over time, where each component is designed with real engineering decisions in mind, tradeoffs between simplicity and flexibility, between normalized and denormalized data models, between batch and streaming approaches. The goal is to build something that reflects how production data systems actually work, even if the scale is personal.

## Motivation

Most learning resources for data engineering treat individual tools and technologies in isolation. You learn about Airflow, then Spark, then Kafka, but rarely in the context of a system that actually uses them together to solve a real problem. This project aims to take a different approach: build the system first, learn the tools as they become necessary.

The pipeline is developed layer by layer, starting from raw data ingestion and working upward through storage, transformation, modeling, and eventually orchestration, distributed processing, and cloud infrastructure. Each layer builds on the one below it, which means concepts are learned in context rather than abstracted away from the problems they're meant to solve. The result is a more connected and practical understanding of data engineering - not just familiarity with individual tools, but an understanding of how they fit together and why.

## Pipeline Structure

**Ingestion** is handled primarily in Python. Data is pulled from public APIs and data sources covering a wide range of space-related content: orbital data for solar system objects, asteroid close-approach information, stellar catalogs, exoplanet datasets, and more. The ingestion layer is designed to accommodate both batch pulls and event-driven or streaming sources, depending on the nature of the data.

**Storage** is structured around the distinction between raw and processed data. Raw data is preserved as-is at the point of ingestion, so that transformation logic can be iterated on without needing to re-fetch source data. Processed and modeled data is stored separately, with schema design treated as a first-class concern rather than an afterthought.

**Processing and transformation** are where the bulk of the pipeline logic lives. This includes cleaning, normalizing, enriching, and reshaping data into forms that are useful downstream. For larger datasets or computationally intensive transformations, distributed processing with Apache Spark is part of the architecture — not because the data volume necessarily demands it, but because designing for scale is part of the learning objective.

**Orchestration** is handled through Apache Airflow, which manages scheduling, dependency resolution, and monitoring across the pipeline. Workflow design (how to structure DAGs, handle failures gracefully, and manage retries) is treated as a meaningful engineering concern, not just a configuration task.

**Messaging and streaming** infrastructure, built around Apache Kafka, supports data sources that produce continuous or event-driven updates. This adds a layer of architectural complexity that reflects how modern data systems handle real-time data alongside batch processing.

**Data modeling and warehousing** sit at the top of the pipeline. Data is organized into schemas designed for analytical use — dimensional models, aggregations, and structured representations that make the data queryable and useful. SQL is the primary tool for querying and modeling at this layer.

**Cloud infrastructure** concepts inform how the system is designed to be deployed and scaled. Even where components run locally, they're built with portability and infrastructure-as-code practices in mind.

## Core Concepts

Beyond the tools themselves, the project is organized around a set of engineering concepts that run through every layer of the system.

**Data architecture design** — understanding how the components of a pipeline relate to each other, and making deliberate choices about where data lives and how it moves.

**Pipeline design** — structuring workflows that are reliable, maintainable, and observable, with clear separation between ingestion, transformation, and serving layers.

**Scalability and reliability** — designing components that can handle growth in data volume or source complexity without requiring a full rewrite, and building in the error handling and retry logic that makes pipelines robust in practice.

**Schema design and data organization** — thinking carefully about how data is structured at rest, how that structure evolves over time, and how it affects the usability of the data downstream.

## Technologies

| Layer | Tools |
|---|---|
| Ingestion & scripting | Python |
| Storage | SQL databases, data lakes |
| Processing | dbt, Pandas, Polars, Apache Spark |
| Processing Platform | Native Python, Databricks |
| Orchestration | Apache Airflow |
| Streaming | Apache Kafka |
| Modeling & querying | SQL |
| Infrastructure | Cloud platforms, containerization |

## Data Domain

The space domain was chosen deliberately. Public datasets are abundant and well-documented — NASA, ESA, the Minor Planet Center, and others publish data under open licenses. The domain is also naturally multi-scale: data ranges from precise orbital mechanics for individual asteroids to statistical catalogs of millions of stars. That variety creates realistic engineering problems around schema design, ingestion frequency, and storage strategy without requiring synthetic or contrived data.
