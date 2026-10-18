# Book companion

This directory is a maintained, downstream companion to the proposed book
*Machine Learning for Mechanical Engineering: Python-Based Data-Driven Modeling
and Engineering Applications*. It does not determine the repository's
architecture or replace the one-semester course sequence. The platform first
develops and verifies reusable engineering capabilities; the companion maps
stable tutorials, cases, exercises, and verification standards to book
chapters.

Start with the [chapter map](CHAPTER_MAP.md). It identifies the canonical
repository material for each planned chapter, its current readiness, and the
work still required before a chapter-level release. The [chapter contract](CHAPTER_CONTRACT.md)
defines the minimum public evidence package for a chapter. The first detailed
implementation is [Chapter 3: Regression and Surrogate Modeling](chapters/ch03_regression/).

## Scope boundary

The companion links to existing modules and data sources rather than copying
raw research payloads, student work, answer keys, or instructor-held tests.
Each engineering case must state its evidence class, units, rights boundary,
split rule, baseline, and valid-use limit. Fast-changing AI tools are kept in
maintained companion material rather than being treated as permanent textbook
claims.

## Release states

- **Mapped:** existing material is linked, but chapter assets are incomplete.
- **In development:** an intended chapter has a documented implementation path
  but lacks a complete public evidence package.
- **Reference implementation:** the chapter has a reproducible, versioned
  teaching route that demonstrates the chapter contract.

The map describes repository readiness only. It does not imply that a final
publisher manuscript, external dataset, agent integration, or engineering
deployment is complete or validated. See the [engineering AI platform roadmap](../ENGINEERING_AI_PLATFORM_ROADMAP.md)
for the governing development sequence.
