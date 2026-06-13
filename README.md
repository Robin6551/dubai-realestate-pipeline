# Dubai Real Estate Analytics Pipeline 🏙️

An end-to-end data engineering pipeline built on **787,000+ real Dubai Land Department transactions**, transforming raw property data into a star schema data warehouse and business intelligence dashboard.

![Dashboard](screenshots/dashboard.png)

---

## 📊 Key Business Insights

- **AED 1.76 Trillion** in total market value analyzed
- **Marsa Dubai (Dubai Marina)** leads with 82,930 transactions — the most active area in Dubai
- **2022 was the peak boom year** — 97,073 transactions worth AED 244 billion, a 60% surge from 2021
- **November is the highest-volume month** — post-summer market surge drives peak activity
- **Palm Jumeirah** commands the highest average price at AED 4.57M per transaction
- **Units dominate** at 48% of total market value — the most accessible property type

---

## 🏗️ Architecture

```
Raw CSV (1M+ rows, Dubai Land Department)
        │
        ▼
   extract.py        → Load raw data into Pandas
        │
        ▼
   transform.py      → Clean, model into star schema
        │
        ▼
    load.py          → Load into PostgreSQL
        │
        ▼
  PostgreSQL DW      → Star schema (fact + 4 dim tables)
        │
        ▼
   Power BI          → Business intelligence dashboard
```

---

## 🗄️ Data Warehouse Schema

**Fact Table:**
| Table | Rows | Description |
|---|---|---|
| `fact_transactions` | 787,052 | Core property transaction records |

**Dimension Tables:**
| Table | Rows | Description |
|---|---|---|
| `dim_date` | 6,851 | Date breakdowns — year, month, quarter, day |
| `dim_area` | 234 | Dubai areas with nearest landmark, metro, mall |
| `dim_property` | 117 | Property type, sub-type, usage, rooms, parking |
| `dim_procedure` | 18 | Transaction procedure and registration type |

---

## ⚙️ Tech Stack

- **Python** — pipeline logic
- **Pandas** — data extraction and transformation
- **PostgreSQL** — data warehouse
- **SQLAlchemy** — database connection and loading
- **Power BI** — business intelligence dashboard

---

## 📁 Project Structure

```
dubai-realestate-pipeline/
│
├── data/               # Place dataset here (see below)
├── screenshots/        # Dashboard screenshots
├── extract.py          # Load raw CSV into DataFrame
├── transform.py        # Clean data + build star schema
├── load.py             # Load tables into PostgreSQL
├── main.py             # Pipeline orchestrator
└── requirements.txt    # Dependencies
```

---

## 🚀 How to Run

**1. Clone the repository**
```bash
git clone https://github.com/Robin6551/dubai-realestate-pipeline.git
cd dubai-realestate-pipeline
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Download the dataset**

Download from Kaggle: [Dubai Real Estate Transactions Dataset](https://www.kaggle.com/datasets/alexefimik/dubai-real-estate-transactions-dataset)

Place the CSV file in the `data/` folder as `Transactions.csv`

**4. Configure PostgreSQL**

Update the connection string in `load.py`:
```python
return create_engine("postgresql://postgres:your_password@localhost:5432/dubai_realestate")
```

**5. Run the pipeline**
```bash
python main.py
```

---

## 📈 Dashboard Visuals

- **KPI Cards** — Total Transactions, Avg Property Price, Total Market Value
- **Yearly Market Growth** — transaction volume and value trends 2000–2023
- **Top 10 Areas by Transaction Value** — Dubai Marina, Burj Khalifa, Palm Jumeirah
- **Market Share by Property Type** — Units, Villas, Land, Buildings
- **Monthly Seasonality (2022)** — peak and trough months in the boom year

---

## 💡 Key Learnings

- Designing star schema data models for large-scale analytical workloads
- Building modular ETL pipelines handling 1M+ rows in Python
- Data cleaning and transformation with Pandas at scale
- Loading structured data warehouses using SQLAlchemy
- Translating raw transaction data into actionable business insights
- Building executive-level dashboards in Power BI

---

## 👤 Author

**Kamrul Islam Robin**
- GitHub: [@Robin6551](https://github.com/Robin6551)
- LinkedIn: [linkedin.com/in/robin-3b721b34a](https://www.linkedin.com/in/robin-3b721b34a)
- Location: Sharjah, UAE
- Stack: Python · SQL · PostgreSQL · Power BI · ETL Pipelines

---

*Dataset source: Dubai Land Department via Kaggle. This project is part of my data engineering portfolio.*
