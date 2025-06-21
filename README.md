# Olympic Data Analysis - Azure Data Engineering Project

## 📚 Project Overview

This project demonstrates a complete **end-to-end Azure Data Engineering pipeline** built on top of the following technologies:

- **GitHub** – Source CSV data files
- **Azure Data Factory (ADF)** – Ingest CSV data from GitHub via HTTP and store in Azure Data Lake Storage (ADLS) in **Parquet format (Staging Layer)**
- **Azure Data Lake Storage Gen2 (ADLS)** – Cloud storage for both staging and transformed data layers
- **Azure Databricks** – Read, transform, and process Parquet data from staging; write the transformed data as **CSV files (Transform Layer)**
  --Azure key vault
- **Azure Synapse Analytics** – Read transformed CSV files from ADLS and create **Lake Databases and Tables**; perform analytical queries using T-SQL.

---

## 📂 Data Flow Architecture

GitHub (CSV files)
│
▼
Azure Data Factory (HTTP Connector)
│
▼
Azure Data Lake Storage Gen2 (Staging Layer - Parquet)
│
▼
Azure Databricks (Transformations in PySpark)
│
▼
Azure Data Lake Storage Gen2 (Transform Layer - CSV)
│
▼
Azure Synapse Analytics (Lake Database & Analysis)

---

## 🔧 Technologies Used

| Component                   | Technology                               |
| --------------------------- | ---------------------------------------- |
| Data Source                 | GitHub (CSV Files)                       |
| Ingestion                   | Azure Data Factory (HTTP)                |
| Storage                     | Azure Data Lake Storage Gen2             |
| Processing & Transformation | Azure Databricks (PySpark)               |
| Security                    | Azure key vault                          |
| Serving & Analysis          | Azure Synapse Analytics (Serverless SQL) |

---

## 🔄 Process Details

### 1. **Data Ingestion (ADF)**

- Fetch raw **CSV files from GitHub** using HTTP linked service.
- Convert and store data into **Parquet format in ADLS Gen2 Staging layer**.

### 2. **Data Transformation (Databricks)**

- Read Parquet files from **Staging Layer**.
- Apply transformations using **PySpark** (e.g., schema correction, filtering, type casting).
- Write transformed data as **CSV files into ADLS Gen2 Transform Layer**.

### 3. **Data Serving & Analysis (Synapse Analytics)**

- Read transformed CSV files from ADLS Gen2 into **Lake Databases in Synapse**.
- Create external tables over these files.
- Execute analytical **SQL scripts** (example: medal analysis, country-wise performance, event statistics).

---

## 🚀 Project Highlights

- **End-to-End Azure-native pipeline** without any on-prem components.
- Demonstrates **multi-layer storage design (Staging & Transform layers)**.
- Uses **ADF for ingestion**, **Databricks for ETL**, and **Synapse for analytics**.
- Shows best practices like **Parquet for intermediate storage** and **CSV for transformed outputs**.

---
