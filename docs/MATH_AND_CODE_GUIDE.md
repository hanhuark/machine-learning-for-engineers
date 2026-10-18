---
layout: default
title: Math and short-code authoring guide
---

# Math and short-code authoring guide

Use this guide when adding or revising a module. The same notation should render in GitHub and on the curriculum's GitHub Pages site.

## Equations

Use GitHub-compatible TeX syntax. Write short expressions inline, such as `$\mathrm{Fo}=\alpha t/L^2$`. Put a long or referenced equation on separate lines with a blank line above and below:

$$
\mathrm{MAE}=\frac{1}{n}\sum_{i=1}^{n}\left|y_i-\hat{y}_i\right|.
$$

Define every symbol at first use, including its unit where it carries a physical dimension. For the expression above, `MAE` has the same unit as the target $y$; `n` is a count; and $\hat{y}_i$ is the prediction associated with observation $i$. Do not use an equation image when editable TeX is possible.

The repository's Markdown pages render `$...$` and `$$...$$` natively on GitHub. The [`head-custom.html`](_includes/head-custom.html) configuration loads MathJax 3 for GitHub Pages and also accepts `\(...\)` and `\[...\]` from legacy pages. New material should use dollar delimiters consistently.

## Short-code demonstrations

Use the [short-code demonstrations](../course_content/short_code_demos/) as the model:

1. Begin with an engineering quantity, its unit, and a bounded assumption.
2. Show the smallest executable calculation that exposes one ML or AI concept.
3. Print a metric or limiting-case check; do not present training loss or a successful run as validation.
4. End with a modification and explanation prompt that changes an assumption, split, threshold, constraint, or operating condition.

Keep examples public-safe and illustrative unless they identify a traceable data source, license, and evidence class. Do not embed student work, restricted data, credentials, or answer keys.

## Preview before publishing

For Markdown-link and readiness checks, run:

```powershell
python tools/check_course_integrity.py
```

For the compact examples, run:

```powershell
python -m unittest tests.test_short_code_demos -v
```

GitHub Pages rendering depends on the external MathJax content delivery service. If a browser blocks that service, the TeX source remains visible and editable, but rendered equations cannot be confirmed in that browser.
