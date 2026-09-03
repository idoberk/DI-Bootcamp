# Progress Log

This is the running, human-readable log kept by the Student Progress Coach. Each daily review is prepended as a new entry at the top, so the most recent entry is always first. See `CLAUDE.md` for the full coaching contract and entry format.

## 2026-09-03

**Note:** the commit reviewed here (`e969cc2`, merged via `1596e14`) was made 2026-09-02 at 17:26, a few hours after that day's review already ran — so this is a continuation of yesterday's coding session, not a fresh day of work.

**Since yesterday:** 1 commit, 3 files (42,148 lines, mostly a 34,937-line power plant CSV) — NumPy fundamentals, Pandas/NumPy/Matplotlib integration, permutation-based ANOVA, eigen decomposition

**What I saw:** `Week4/Day2/ExerciseXP/exercise_xp.ipynb` runs through the standard 10-exercise NumPy/Pandas/Matplotlib set — determinants and matrix inverses via `np.linalg.det`/`np.linalg.inv`, grayscale vs. RGB image representation as 2D/3D arrays, and a from-scratch effect-size calculation (`mean_diff / std_diff`) for the productivity hypothesis test — competent but templated work, no surprises. `Week4/Day2/DailyChallenge/daily_challenge.ipynb` (Global Power Plant Database, 34,936 plants) is the strongest notebook in the repo so far: `clean_power_plants()` and `completeness_rating()` are documented helper functions that classify each column's missingness before deciding whether to impute, drop, or leave it, rather than blanket-dropping rows. `anova_permutation_test()` builds a rank-based, assumption-free ANOVA entirely from NumPy — factorizing fuel-type labels, computing an observed F-statistic, then generating a null distribution via 2000 random shuffles with `np.random.default_rng(seed)`. That's a direct pickup of the 2026-08-31 recommendation to standardize on `default_rng()` over legacy `np.random.rand`, and it's now driving a real statistical test rather than just array generation. Section 6 also explicitly reframes `groupby().sum()` as one-hot matrix multiplication (`capacity_by_category_matrix()`), and Section 7 uses `np.percentile` to derive capacity-tier cutoffs from the data instead of hand-picked thresholds. The chart-selection reasoning is consistently justified in markdown too — log-scaled axes for the capacity histogram and fuel boxplot ("a normal chart would just show one tall bar near zero"), a 100%-stacked bar instead of a smooth area chart for the by-decade fuel mix ("we don't [have data for every year in between]... implying more continuity than the data actually has").

**Recommendations:**
- `fuel_type_stats()` and `anova_permutation_test()` in `daily_challenge.ipynb` both re-derive the same per-fuel grouping and `min_n` filtering logic independently — worth factoring the "filter groups by minimum sample size" step into one shared helper the two functions call, the same way `iqr_bounds()` and `pareto_analysis` candidates were flagged for consolidation in the 2026-08-30 review.
- `exercise_xp.ipynb`'s Exercise 6 hypothesis test computes an effect size but never states a threshold or conclusion (e.g. Cohen's d convention: small/medium/large) — the daily challenge notebook's habit of following every statistic with an explicit interpretation sentence (flagged as a strength on 2026-09-02) hasn't carried over to the exercise notebooks yet; worth closing that gap next.

**Streak:** 2 days (continuation of 2026-09-02's session, same underlying streak — not a new calendar day of activity)

## 2026-09-02

**Since yesterday:** 3 commits, 6 files — inferential statistics (t-test, ANOVA, correlation), aviation-crash EDA, PCA/dimensionality reduction

**What I saw:** Strong session across three notebooks. `Week3/Day3/ExerciseXP/exercise_xp.ipynb` is the first appearance of `scipy.stats` in the repo — a two-sample t-test, one-way ANOVA on fertilizer groups, and a from-scratch linear regression writeup, each followed by a markdown cell that actually interprets the p-value rather than just reporting it (e.g. "P-Value of 0.0000275 is far below the standard significance level"). `Week3/Day3/DailyChallenge/daily_challenge.ipynb` analyzes the 1908-2023 airplane crash dataset and is a clear step up from earlier "Findings" sections that left placeholders unfilled (flagged in the 2026-08-31 review): it runs a genuine Mann-Whitney U test comparing 1990s vs. 2010s fatality distributions (p=0.68, correctly concluded "not meaningfully less severe"), quantifies right-skew with mean vs. median (22.4 vs. 11.0), and closes with an honest "Caveats" section calling out that `Region` is derived from a messy free-text field. `Week3/Day2/DailyChallenge/daily_challenge.ipynb` (job-salary dataset) is the most technically ambitious: it one-hot/frequency-encodes categoricals, standardizes, fits full PCA to find 9-of-12 components are needed for 90% variance, then explicitly reasons about *why* — one-hot columns are close to orthogonal so there's little redundancy to compress — and separately flags the Executive salary group (n=13, mean $76k vs. median $46k) as too small and skewed to trust. `Week3/Day2/ExerciseXP/exercise_xp.ipynb` only picked up formatting churn this round (single→double quotes, long lines wrapped, execution counts reset to null) — looks like an autoformatter (Black-style) ran over it, no logic changes.

**Recommendations:**
- The PC1-loading interpretation in `Week3/Day2/DailyChallenge/daily_challenge.ipynb` (noting `experience_level_Senior` at ~0.62 vs. a ~0.29 baseline) is exactly the kind of "why" reasoning that was missing from earlier PCA/stats work — worth carrying that same loadings-inspection habit into Exercise 5/6 of `Week3/Day3/ExerciseXP/exercise_xp.ipynb`, where the ANOVA and t-test conclusions are correct but stop at the p-value without checking effect size (e.g. Cohen's d or eta-squared).
- Since an autoformatter now appears to be running on save (the Day2 ExerciseXP diff is 100% quote-style/line-wrap changes), consider adding a `pyproject.toml`/`.jupytext.toml` config or just applying it consistently across all notebooks in one pass, so future diffs aren't mixed formatting-noise + content changes — right now it's easy to miss the real change buried in reformatted lines.

**Streak:** 1 day (yesterday, 2026-09-01, had no exercise commits, so this restarts the count)

## 2026-09-01

**Since yesterday:** No new exercise commits — the only commit in the repo since the last review (`2b0da17`) is yesterday's own progress-coach entry, not student work. No uncommitted changes in the working tree either.

**What I saw:** Nothing to report today — the repo is exactly where it was left after the 2026-08-31 review (still at `15d15f8`, the Week 4 Day 1 NumPy/Pandas/Matplotlib work). No new notebooks, no in-progress files.

**Recommendations:**
- Pick back up on Week 4 — the two open items flagged in the 2026-08-31 entry (standardizing on `np.random.default_rng()` in `exercise_xp.ipynb`, and filling in the placeholder city names in `daily_challenge.ipynb`'s Findings cell) are both still outstanding and quick to close out.

**Streak:** broken — no exercise commits today

## 2026-08-31

**Note:** the single commit reviewed here (`15d15f8`) was made on 2026-08-30, shortly after yesterday's review already ran — so this is the same coding session as yesterday's entry, just caught on today's run rather than a fresh day of work.

**Since yesterday:** 1 commit, 2 files — NumPy fundamentals, NumPy/Pandas/Matplotlib integration

**What I saw:** `Week4/Day1/ExerciseXP/exercise_xp.ipynb` runs through 10 focused NumPy basics — `np.arange`, dtype conversion via `.astype(int)`, `reshape`, `np.eye`, slicing/reversal, and boolean-mask filtering (`ex_10_arr = ex_1_arr[ex_1_arr % 2 == 1]` for odd numbers). `Week4/Day1/DailyChallenge/daily_challenge.ipynb` is the more interesting piece: it builds a synthetic 10-city x 12-month temperature dataset and does real analysis on it — `annual_avg = temp_df.mean(axis=1)` with `idxmax()`/`idxmin()` to find hottest/coldest cities, a bar chart that color-codes the hottest (red) and coldest (blue) bars via a list comprehension keyed off city name, and a `plt.imshow` heatmap of the full city x month grid. The closing "Findings" markdown cell shows genuine reflection rather than boilerplate — it correctly reasons that the line plot looks jagged and non-seasonal specifically *because* the data was generated with `np.random.uniform` independently per month, not because of a plotting mistake.

**Recommendations:**
- `daily_challenge.ipynb` uses the newer `rng = np.random.default_rng(42)` Generator API, but `exercise_xp.ipynb` Exercise 4 still calls the legacy `np.random.rand(4, 5)` — worth standardizing on `default_rng()` everywhere now that it's been used successfully once, since it's more reproducible and is the NumPy-recommended approach going forward.
- The "Findings" cell in `daily_challenge.ipynb` still has unfilled placeholders — `_(value printed above, e.g. Cairo)_` for both hottest and coldest city — even though the cell right above it already computed and printed the real answers (New York / Nairobi). Worth going back and swapping those placeholders for the actual values so the write-up reads as finished.

**Streak:** 1 day (same calendar day as the last review, not a new day of activity)

## 2026-08-30 (delayed/catch-up review)

**Note:** this is a delayed review — the last run was 2026-08-27, so this entry covers three days of gap plus today's single commit, not a normal next-day check-in.

**Since last review:** 1 commit, 3 files — data visualization, geographic mapping (Plotly choropleth), Pareto/80-20 analysis

**What I saw:** `707cfa2` adds two week-3 mini-projects built on the US Superstore dataset. `Week3/Day5/DailyChallenge/mini_project_interactive_data_vis.ipynb` goes past the two prior notebooks' interactivity: `plot_sales_trend(category="All")` is a proper parameterized function (not just an inline `interact()` lambda) wired to a `Dropdown`, and a new technique shows up — a `plotly.express.choropleth` state-by-state sales map using the `us` package to convert full state names to postal abbreviations (`us.states.lookup(name).abbr`), including a manual fix for `"District of Columbia"` which the `us` lookup doesn't resolve to `"DC"` on its own. The notebook closes with a written "Matplotlib vs. Seaborn" comparison and an f-string-driven executive summary that computes top state, top product, and high-discount loss rate. `Week3/Day5/ExerciseXP/mini_project_marketing_strategy.ipynb` is the bigger piece of growth: it implements Pareto (80/20) analysis from scratch, twice — once for customer profit (cell with `pareto_df["Cumulative Profit %"]`) and again for customer sales (`sales_pareto_df`) — each computing a cumulative-percentage curve and counting how many customers account for 80% of the total, then plotting it against the 80/20 reference lines with `axhline`/`axvline`. That's the first time a cumulative-distribution technique like this has shown up in the repo.

**Recommendations:**
- The two Pareto blocks in `mini_project_marketing_strategy.ipynb` (profit vs. sales) are near-identical except for the column name — this is a good candidate to factor into a `pareto_analysis(df, group_col, value_col)` helper the way `iqr_bounds()` was factored out back in the Day2 outlier-handling notebook; it would also make it easy to add a third Pareto cut (e.g. by product) later without copy-pasting again.
- Several code comments in `mini_project_marketing_strategy.ipynb` pose the analysis question as a genuine open question in-line (e.g. `# Finding who is an outstanding customer in New York (What does outstanding means in this context?...)`) but the notebook picks profit without stating why in a markdown cell — worth adding a one-line rationale next to that decision so the choice reads as deliberate rather than arbitrary when revisited later.

**Streak:** 1 day (previous streak broke — no exercise commits between 2026-08-27 and 2026-08-29)

## 2026-08-27

**Since yesterday:** 2 commits, 4 files — data visualization (Matplotlib, Seaborn, Plotly, ipywidgets)

**What I saw:** `Week3/Day4/DailyChallenge/daily_challenge.ipynb` is a genuine step up in scope: a full Superstore sales analysis that chains cleaning (`drop_duplicates`, `Postal Code` fillna), feature engineering (`Profit Margin`, `Order Year`/`Month` via `.dt` accessors), an interactive Matplotlib time-series plot driven by an `ipywidgets` `Dropdown`, a `Seaborn` `barplot` with value annotations for top-10 profitable products, and a `scatterplot` + `regplot` combo to visualize the discount/profit relationship by category. `ipywidgets` and interactivity hadn't shown up in this repo before, and this notebook also tackles all three optional advanced challenges rather than stopping at the required scope: a 2x2 multi-chart dashboard (cell 22), outlier annotation labeling the top/bottom 3 transactions by profit (cell 24), and a Plotly rebuild of the discount/profit scatter with a written Matplotlib-vs-Plotly comparison (cell 26). `Week3/Day4/ExerciseXP/exercise_xp.ipynb` covers the fundamentals underneath that — line/bar/histogram/scatter plots — and cell 14's `sns.barplot` maps `"Do you have Anxiety?"` from `Yes`/`No` strings to `1`/`0` on the fly to get a proportion-by-gender chart, a clean way to turn a categorical column into something a bar chart can aggregate.

**Recommendations:**
- The Plotly comparison in cell 26 of the daily challenge notebook is a good start, but the "Plotly Advantages" list gets cut off mid-print — worth finishing that comparison with at least one concrete disadvantage of Plotly too (e.g. file size, offline rendering) to make it a genuinely two-sided evaluation like the brief asks for.
- `exercise_xp.ipynb` exercise 6 (cell 16) maps `"Do you have Panic attack?"` to 0/1 but never checks for typos or inconsistent casing in that column the way the daily challenge notebook checks `isnull().sum()` up front — a quick `df["Do you have Panic attack?"].unique()` before mapping would catch that class of bug before it silently mismaps values.

**Streak:** 1 day (previous streak broke — no exercise commits between 2026-08-24 and 2026-08-26)

## 2026-08-26

**Since yesterday:** 0 exercise commits — 2 non-exercise commits touched the repo (`c92d9f0`, the coach's own reconciliation commit, and `95ffa21`, a `CLAUDE.md` update to the coaching instructions)

**What I saw:** No exercise files changed since the 2026-08-25 review. `95ffa21` reworked `CLAUDE.md` itself (29 insertions/13 deletions) rather than any code under `Week3/` or elsewhere, so there's nothing to review from a coding standpoint today — just noting the gap honestly rather than padding this entry with unrelated praise.

**Recommendations:**
- Get back to `Week3/Day2/ExerciseXP/exercise_xp.ipynb`'s follow-up from the last real review (the missing-value re-check after imputation) or move on to the next day's exercise — the pipeline work there was strong and worth building on rather than letting it sit.

**Streak:** broken — no exercise commits between 2026-08-24 and 2026-08-26

## 2026-08-25 (reconciled)

**Note:** this entry and the one below it were reconstructed on 2026-08-25 after discovering that scheduled runs from 2026-08-19 through 2026-08-25 had been landing in isolated worktrees (worktree isolation was on) and never merging back to `main`, so they never reached this file. Worktree isolation has since been turned off. This entry covers `2d66e64`, committed 2026-08-24.

**Since previous entry:** 1 commit, 3 files — data preprocessing, feature engineering, outlier handling, scikit-learn

**What I saw:** `2d66e64` (Week3/Day2) is a real step up from Day1's mostly-descriptive work: a full Titanic preprocessing pipeline in `Week3/Day2/ExerciseXP/exercise_xp.ipynb` that chains duplicate removal, `SimpleImputer(strategy='median')` for `Age`, mode-fill for `Embarked`, feature engineering (`Family Size` from `SibSp`+`Parch`, `Title` extracted from `Name` via regex with rare-title collapsing), IQR-based outlier detection with a reusable `iqr_bounds()` helper, three outlier treatments (capping, log transform, row removal) compared side by side, and `StandardScaler` vs `MinMaxScaler` chosen deliberately per feature's skew (cell 40 reasons about `Age` being symmetric vs `Fare` staying right-skewed after capping). That's a coherent, justified pipeline rather than isolated snippets.

**Recommendations:**
- `Week3/Day2/ExerciseXP/exercise_xp.ipynb` never re-checks `titanic_data.isna().sum()` after the Age/Cabin/Embarked fixes in Exercise 2 — worth adding a quick verification cell there to confirm no missing values remain before moving on to feature engineering, since that's a good habit for any future pipeline.

**Streak:** 2 days (2026-08-23, 2026-08-24)

## 2026-08-24 (delayed/catch-up review, reconciled)

**Note:** last review before this one ran 2026-08-18. This catches up on everything committed since, which turned out to be a single commit, `ba88f6e`, from 2026-08-23.

**Since yesterday:** 1 commit, 8 files — pandas I/O, Kaggle datasets, qualitative/quantitative classification

**What I saw:** `Week3/Day1/ExerciseXP/exercise_xp.ipynb` covers a good range of new pandas I/O: `pd.read_csv` on three real-world datasets, `kagglehub.dataset_load` to pull the Iris dataset straight from Kaggle (cell 10), `df.to_excel` / `df.to_json` for export (cell 20), and `pd.read_json` for import (cell 22) — none of these I/O paths showed up in earlier work. There's a conceptual mix-up running through the whole notebook, though: continuous numeric columns are consistently labeled "Qualitative" instead of Quantitative. Cell 3 calls "AVG hours per day sleeping" qualitative "because it's a continuous value," and the same mistake repeats for `Age`/`Debt`/`YearsEmployed` in cell 7 and for all four Iris measurements (`sepal_length`, `sepal_width`, `petal_length`, `petal_width`) in cell 11. A continuous, arithmetic-friendly value is the textbook definition of quantitative, so the label and the reasoning point in opposite directions every time.

**Recommendations:**
- Revisit the qualitative-vs-quantitative labels in cells 3, 5, 7, and 11 — anywhere the write-up says "continuous value" or "arithmetic operations are useful," the column should be marked Quantitative, not Qualitative. This comes up again in Exercise 6/7's structured-vs-unstructured discussion, so worth a pass now.
- Exercise 7 (cell 17) trails off mid-sentence on the audio-recordings example ("keywords (type of complaints, product") — worth finishing that thought since the blog-post example right above it is a solid, complete answer to model it on.

**Streak:** 1 day (previous streak broke — no commits between 2026-08-18 and 2026-08-23)

## 2026-08-18

**Since yesterday:** 2 commits, 3 files — modules, documentation

**What I saw:** This is the first real diff-based review since setup. The backfilled `daily_challenge_translator.py` builds a French→English dict with `deep_translator.GoogleTranslator` in a plain `for` loop — correct and matches the challenge spec. The other change is small and deliberate: in `Week2/Day5/ExerciseXP/game.py:62`, the `get_user_item` docstring was tightened from "return it" to "return the input," removing a pronoun that didn't clearly point back to its antecedent — consistent with the "Method that/to ..." style already used on the other three docstrings in that class.

**Recommendations:**
- `daily_challenge_translator.py:18-21`'s loop-based dict build works, but it's a clean fit for a dict comprehension: `{word: GoogleTranslator(source="fr", target="en").translate(text=word) for word in french_words}` — no comprehension has shown up in the repo yet, worth trying next time this shape comes up.
- The docstring fix is honestly minor on its own — a good moment to apply that same clarity pass to `get_game_result` and `play` in the same file, since their one-liners ("returns the result of the game," "ties up all the game together") are a bit vague about what's actually returned or done.

**Streak:** 1 day
