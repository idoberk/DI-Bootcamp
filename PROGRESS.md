# Progress Log

This is the running, human-readable log kept by the Student Progress Coach. Each daily review is prepended as a new entry at the top, so the most recent entry is always first. See `CLAUDE.md` for the full coaching contract and entry format.

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
