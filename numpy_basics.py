"""
NumPy Basics - Learning Guide
Using the research publications dataset (data.csv)
"""

import numpy as np
import csv
import sys

# Increase CSV field size limit (some abstracts are very long)
csv.field_size_limit(sys.maxsize)


# ============================================================
# SECTION 1: Loading Data from CSV
# ============================================================

def load_dataset():
    """Load data.csv and return as list of dicts."""
    with open("data.csv", "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)

data = load_dataset()
print(f"Total records loaded: {len(data)}")
print(f"Columns: {list(data[0].keys())}")
print()


# ============================================================
# SECTION 2: Creating NumPy Arrays from Dataset
# ============================================================

def safe_int(value, default=0):
    """Convert to int safely, return default for bad data."""
    try:
        return int(value)
    except (ValueError, TypeError):
        return default

# Extract numeric columns into numpy arrays (handling dirty data)
authors_count = np.array([safe_int(row["authors_count"]) for row in data])
abstract_words = np.array([safe_int(row["abstract_words"]) for row in data])
pub_years = np.array([safe_int(row["pub_year"]) for row in data])

print("--- Creating Arrays ---")
print(f"authors_count shape: {authors_count.shape}, dtype: {authors_count.dtype}")
print(f"abstract_words shape: {abstract_words.shape}, dtype: {abstract_words.dtype}")
print(f"pub_years shape: {pub_years.shape}, dtype: {pub_years.dtype}")
print()


# ============================================================
# SECTION 3: Basic Array Operations
# ============================================================

print("--- Basic Array Operations ---")

# Arithmetic on arrays (element-wise)
doubled_authors = authors_count * 2
print(f"First 5 author counts: {authors_count[:5]}")
print(f"Doubled:               {doubled_authors[:5]}")

# Array addition
combined = authors_count + abstract_words
print(f"authors + abstract_words (first 5): {combined[:5]}")

# Scalar operations
words_per_author = abstract_words / np.where(authors_count == 0, 1, authors_count)
print(f"Words per author (first 5): {np.round(words_per_author[:5], 1)}")
print()


# ============================================================
# SECTION 4: Statistical Functions
# ============================================================

print("--- Statistics on Author Count ---")
print(f"Mean:     {np.mean(authors_count):.2f}")
print(f"Median:   {np.median(authors_count):.2f}")
print(f"Std Dev:  {np.std(authors_count):.2f}")
print(f"Min:      {np.min(authors_count)}")
print(f"Max:      {np.max(authors_count)}")
print(f"Sum:      {np.sum(authors_count)}")
print()

print("--- Statistics on Abstract Word Count ---")
print(f"Mean:     {np.mean(abstract_words):.2f}")
print(f"Median:   {np.median(abstract_words):.2f}")
print(f"Std Dev:  {np.std(abstract_words):.2f}")
print(f"Min:      {np.min(abstract_words)}")
print(f"Max:      {np.max(abstract_words)}")
print()


# ============================================================
# SECTION 5: Indexing and Slicing
# ============================================================

print("--- Indexing & Slicing ---")

# Basic indexing
print(f"First element:  {authors_count[0]}")
print(f"Last element:   {authors_count[-1]}")

# Slicing [start:stop:step]
print(f"First 5:        {authors_count[:5]}")
print(f"Last 5:         {authors_count[-5:]}")
print(f"Every 100th:    {authors_count[::100][:10]}")  # first 10 of every 100th

# Fancy indexing - pick specific indices
indices = np.array([0, 10, 50, 100])
print(f"Elements at indices {indices}: {authors_count[indices]}")
print()


# ============================================================
# SECTION 6: Boolean Indexing (Filtering)
# ============================================================

print("--- Boolean Indexing (Filtering) ---")

# Papers with more than 10 authors
many_authors = authors_count[authors_count > 10]
print(f"Papers with >10 authors: {len(many_authors)}")

# Papers with abstract between 100-200 words
mid_length = abstract_words[(abstract_words >= 100) & (abstract_words <= 200)]
print(f"Papers with 100-200 word abstracts: {len(mid_length)}")

# Papers from 2024
papers_2024 = pub_years[pub_years == 2024]
print(f"Papers from 2024: {len(papers_2024)}")

# Combining conditions: 2024 papers with >5 authors
mask = (pub_years == 2024) & (authors_count > 5)
print(f"2024 papers with >5 authors: {np.sum(mask)}")
print()


# ============================================================
# SECTION 7: Reshaping Arrays
# ============================================================

print("--- Reshaping ---")

# Take first 12 elements for demo
sample = authors_count[:12]
print(f"Original (12 elements): {sample}")

# Reshape to 3x4 matrix
matrix = sample.reshape(3, 4)
print(f"Reshaped to 3x4:\n{matrix}")

# Reshape to 4x3
matrix2 = sample.reshape(4, 3)
print(f"Reshaped to 4x3:\n{matrix2}")

# Flatten back
flat = matrix.flatten()
print(f"Flattened back: {flat}")

# Transpose
print(f"Transposed (4x3):\n{matrix.T}")
print()


# ============================================================
# SECTION 8: Aggregation with axis
# ============================================================

print("--- Aggregation with axis ---")

matrix = authors_count[:20].reshape(4, 5)
print(f"4x5 Matrix:\n{matrix}")

# Sum along axis 0 (columns) - collapses rows
print(f"Sum along columns (axis=0): {np.sum(matrix, axis=0)}")

# Sum along axis 1 (rows) - collapses columns
print(f"Sum along rows (axis=1):    {np.sum(matrix, axis=1)}")

# Mean along each axis
print(f"Mean per column (axis=0):   {np.mean(matrix, axis=0)}")
print(f"Mean per row (axis=1):      {np.mean(matrix, axis=1)}")
print()


# ============================================================
# SECTION 9: Sorting
# ============================================================

print("--- Sorting ---")

sample = authors_count[:10].copy()
print(f"Original:    {sample}")
print(f"Sorted:      {np.sort(sample)}")
print(f"Reverse:     {np.sort(sample)[::-1]}")

# argsort - returns indices that would sort the array
sort_indices = np.argsort(sample)
print(f"Sort indices: {sort_indices}")
print(f"Sorted via indices: {sample[sort_indices]}")

# Top 5 papers by author count in the full dataset
top5_idx = np.argsort(authors_count)[-5:][::-1]
print(f"Top 5 author counts: {authors_count[top5_idx]}")
print()


# ============================================================
# SECTION 10: Unique Values and Counts
# ============================================================

print("--- Unique Values & Counts ---")

unique_years, year_counts = np.unique(pub_years, return_counts=True)
print("Publication years distribution:")
for year, count in zip(unique_years, year_counts):
    print(f"  {year}: {count} papers")

unique_author_counts = np.unique(authors_count)
print(f"\nDistinct author counts: {len(unique_author_counts)}")
print(f"Range: {unique_author_counts[0]} to {unique_author_counts[-1]}")
print()


# ============================================================
# SECTION 11: Array Creation Functions
# ============================================================

print("--- Array Creation Functions ---")

# zeros, ones, full
print(f"zeros(5):      {np.zeros(5)}")
print(f"ones(5):       {np.ones(5)}")
print(f"full(5, 42):   {np.full(5, 42)}")

# arange and linspace
print(f"arange(0,10,2):     {np.arange(0, 10, 2)}")
print(f"linspace(0,1,5):    {np.linspace(0, 1, 5)}")

# eye (identity matrix)
print(f"eye(3):\n{np.eye(3)}")

# random arrays
np.random.seed(42)
print(f"random 5 ints (0-100): {np.random.randint(0, 100, 5)}")
print(f"random 5 floats:       {np.round(np.random.random(5), 3)}")
print()


# ============================================================
# SECTION 12: Stacking and Concatenation
# ============================================================

print("--- Stacking & Concatenation ---")

a = authors_count[:5]
b = abstract_words[:5]

# Horizontal stack (side by side)
h_stack = np.hstack([a, b])
print(f"a:          {a}")
print(f"b:          {b}")
print(f"hstack:     {h_stack}")

# Vertical stack (as rows in a matrix)
v_stack = np.vstack([a, b])
print(f"vstack:\n{v_stack}")

# Column stack (each array becomes a column)
c_stack = np.column_stack([a, b])
print(f"column_stack:\n{c_stack}")
print()


# ============================================================
# SECTION 13: Where (Conditional Selection)
# ============================================================

print("--- np.where (Conditional) ---")

sample_authors = authors_count[:10]
print(f"Author counts: {sample_authors}")

# Label as "team" (>3 authors) or "solo/small"
labels = np.where(sample_authors > 3, "team", "solo/small")
print(f"Labels:        {labels}")

# Replace zeros with NaN for calculations
authors_float = authors_count.astype(float)
authors_no_zero = np.where(authors_float == 0, np.nan, authors_float)
print(f"Mean (with zeros):    {np.mean(authors_float):.2f}")
print(f"Mean (without zeros): {np.nanmean(authors_no_zero):.2f}")
print()


# ============================================================
# SECTION 14: Percentiles and Histogram Bins
# ============================================================

print("--- Percentiles & Histogram Bins ---")

print(f"25th percentile (authors): {np.percentile(authors_count, 25)}")
print(f"50th percentile (authors): {np.percentile(authors_count, 50)}")
print(f"75th percentile (authors): {np.percentile(authors_count, 75)}")
print(f"90th percentile (authors): {np.percentile(authors_count, 90)}")

# Histogram bins for abstract word counts
counts, bin_edges = np.histogram(abstract_words, bins=5)
print(f"\nAbstract word count distribution (5 bins):")
for i in range(len(counts)):
    print(f"  {bin_edges[i]:.0f}-{bin_edges[i+1]:.0f}: {counts[i]} papers")
print()


# ============================================================
# SECTION 15: Practical Analysis - Putting It All Together
# ============================================================

print("=" * 50)
print("PRACTICAL ANALYSIS: Research Publications Dataset")
print("=" * 50)

# Extract countries for text-based analysis
countries = np.array([row["country"] for row in data])
open_access = np.array([row["open_access"] == "TRUE" for row in data])

# 1. Open access percentage
oa_pct = np.mean(open_access) * 100
print(f"\nOpen Access papers: {oa_pct:.1f}%")

# 2. Author count statistics by year
for year in np.unique(pub_years):
    year_mask = pub_years == year
    year_authors = authors_count[year_mask]
    print(f"\nYear {year}:")
    print(f"  Papers: {np.sum(year_mask)}")
    print(f"  Avg authors: {np.mean(year_authors):.1f}")
    print(f"  Max authors: {np.max(year_authors)}")
    print(f"  Avg abstract words: {np.mean(abstract_words[year_mask]):.0f}")

# 3. Correlation between authors count and abstract length
correlation = np.corrcoef(authors_count, abstract_words)[0, 1]
print(f"\nCorrelation (authors vs abstract length): {correlation:.4f}")

# 4. Top countries by paper count
unique_countries, country_counts = np.unique(countries, return_counts=True)
top_idx = np.argsort(country_counts)[-10:][::-1]
print("\nTop 10 countries by paper count:")
for i in top_idx:
    print(f"  {unique_countries[i]}: {country_counts[i]}")

print("\nDone! You've covered the core NumPy operations.")