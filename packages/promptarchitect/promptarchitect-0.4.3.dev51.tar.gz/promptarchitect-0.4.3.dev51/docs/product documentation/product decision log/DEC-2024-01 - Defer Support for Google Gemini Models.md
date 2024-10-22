# Defer Support for Google Gemini Models

**Decision ID:** DEC-2024-01

**Date:** August 29, 2024

## Decision

We have decided **not to support Google Gemini models** in the current version of PromptArchitect.

## Context

- The decision arises from the current customer base's lack of reliance on Google Cloud technologies.
- Google is currently perceived as lagging behind in the Large Language Models (LLM) field compared to other providers like OpenAI and Hugging Face.
- Allocating resources to integrate Google Gemini models at this stage does not align with our customers' immediate needs and would likely not provide significant benefits.

## Options Considered

1. **Integrate Google Gemini Models**:
   - Pros: Comprehensive support for all major LLM providers; future-proofing for potential shifts in the market.
   - Cons: High development cost and resource allocation for a feature unlikely to be used by current customers.

2. **Defer Integration Until Needed** (Chosen):
   - Pros: Focus on integrating models and technologies that are immediately relevant to our customers, optimizing resource allocation.
   - Cons: May require future development effort if customer demand for Google Gemini models increases.

3. **Permanent Exclusion of Google Gemini**:
   - Pros: Simplifies the product by narrowing the scope of supported models.
   - Cons: Potential loss of market share if Google Gemini gains significant traction in the future.

## Consequences

- **Short-Term**: Resources will be redirected towards enhancing support for currently popular and in-demand models like OpenAI and Hugging Face, aligning with customer needs.
- **Long-Term**: If market demand shifts and Google Gemini becomes a major player, we will need to revisit this decision and potentially integrate support, which could require additional development time and effort.

## Follow-Up Actions

- Monitor market trends and customer feedback to assess any growing demand for Google Gemini model support.
- Reevaluate this decision in six months or when there is a significant shift in market dynamics or customer requirements.

### Status

Finalized
