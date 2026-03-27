# Data Science Learning Path

> Learn pandas, numpy, matplotlib, seaborn, and scikit-learn using `data.csv` (~126K research publication records)

## Learning Order

### 1. NumPy (Foundation)

Array operations, math, and statistics.

**What to practice:**
- Basic array creation, reshaping, slicing
- Statistical functions (`mean`, `std`, `median`) on numeric columns like `abstract_words`, `authors_count`
- Boolean masking, filtering, sorting
- Random sampling from arrays

**Exercise ideas:**
- Calculate average `abstract_words` across all papers
- Find papers with `authors_count` above the 95th percentile
- Create a boolean mask for papers with more than 200 words in abstract
- Compute standard deviation of `authors_count` per year

---

### 2. Pandas (Core)

Data loading, manipulation, cleaning, and analysis.

**What to practice:**
- `read_csv`, `head()`, `info()`, `describe()`, `shape`
- Filtering: papers from `USA`, year `2024`, `open_access == TRUE`
- `groupby`: count papers by `country`, `journal`, `pub_year`
- `value_counts()`, `isna()`, missing data handling
- String operations on `title`, `abstract`, `keywords`
- Sorting, merging, pivot tables
- `apply()` and lambda functions

**Exercise ideas:**
- Load `data.csv` and explore the first 10 rows
- Find total papers per country (top 20)
- Count missing values in each column
- Filter papers that contain "machine learning" in the abstract
- Group by `pub_year` and count papers per year
- Create a pivot table: `country` vs `research_type` with paper counts
- Extract the first keyword from the `keywords` column into a new column
- Find the journal with the most publications

---

### 3. Matplotlib (Basic Plots)

Visualization foundation.

**What to practice:**
- Bar chart: top 10 countries by paper count
- Histogram: distribution of `abstract_words`
- Line chart: papers published per year
- Pie chart: `research_type` distribution
- Subplots and figure customization
- Labels, titles, legends, colors

**Exercise ideas:**
- Bar chart of top 10 countries by number of papers
- Histogram showing distribution of `abstract_words` (bins=50)
- Line chart of papers published per year
- Pie chart of `open_access` TRUE vs FALSE
- Create a 2x2 subplot grid combining the above charts
- Customize colors, fonts, and add grid lines

---

### 4. Seaborn (Statistical Plots)

Beautiful and informative statistical visualizations.

**What to practice:**
- `countplot`: papers by `language`
- `boxplot`: `authors_count` by top 5 countries
- `heatmap`: correlation matrix of numeric columns
- `catplot`: `open_access` vs `research_type`
- `barplot` with confidence intervals
- `violinplot`: `abstract_words` distribution by `open_access`

**Exercise ideas:**
- Count plot of top 10 `major_topic` categories
- Box plot comparing `authors_count` across top 5 countries
- Heatmap of correlation between `abstract_words`, `authors_count`, `pub_year`, `pub_month_num`
- Violin plot of `abstract_words` split by `open_access`
- Bar plot showing average `authors_count` per `research_type`
- Pair plot of all numeric columns

---

### 5. Scikit-learn (Machine Learning)

Classification, clustering, and text analysis.

**What to practice:**
- Text vectorization: TF-IDF on `abstract` or `title`
- Classification: predict `major_topic` from abstract text
- Clustering: group similar papers using K-Means
- Train/test split
- Accuracy, precision, recall, confusion matrix
- Feature importance

**Exercise ideas:**
- Use TF-IDF to vectorize paper abstracts
- Build a classifier to predict `open_access` (TRUE/FALSE) from `abstract_words`, `authors_count`, `pub_year`
- Train a text classifier to predict `major_topic` from `title`
- Cluster papers into groups using K-Means on TF-IDF features
- Evaluate model with confusion matrix and classification report
- Compare Logistic Regression vs Random Forest accuracy

---

## Useful Resources

| Library | Documentation |
|---------|--------------|
| NumPy | https://numpy.org/doc/stable/ |
| Pandas | https://pandas.pydata.org/docs/ |
| Matplotlib | https://matplotlib.org/stable/contents.html |
| Seaborn | https://seaborn.pydata.org/ |
| Scikit-learn | https://scikit-learn.org/stable/ |
