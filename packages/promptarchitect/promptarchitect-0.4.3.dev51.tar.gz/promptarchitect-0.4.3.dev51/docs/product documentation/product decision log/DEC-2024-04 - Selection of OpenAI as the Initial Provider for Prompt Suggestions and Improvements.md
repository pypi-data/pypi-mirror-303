# Selection of OpenAI as the Initial Provider for Prompt Suggestions and Improvements

**Decision ID:** DEC-2024-04

**Date:** September 3, 2024

## Decision

We have decided to select OpenAI as the initial provider for prompt suggestions and improvements.

## Context

In the development of our product, which includes features for generating prompt suggestions and improvements, we have the option to choose from various AI model providers. These providers offer different models, each with its strengths and limitations. The choice of provider has significant implications for product maintenance, client satisfaction, and data privacy.

## Rationale

**Client Licenses**: The majority of our clients already have OpenAI licenses through Azure. Leveraging these existing licenses allows us to integrate seamlessly with our clients' existing infrastructure, reducing friction in adoption and ensuring a consistent experience across our user base.

**Data Privacy and Compliance**: By using OpenAI through Azure, we directly benefit from the robust data privacy protections and legal agreements provided by Microsoft Azure Cloud. This ensures that all data shared during prompt suggestions and improvements adheres to the same stringent privacy standards as other data managed within Azure, aligning with our commitment to data security and compliance.

**Maintenance Considerations**: Selecting a single provider reduces the complexity of maintaining integrations with multiple AI models. This decision minimizes the burden on our development and operations teams, allowing us to focus on delivering a high-quality, stable product.

## Impact

**Maintenance:** Reduced complexity and lower ongoing maintenance costs.
**Client Experience:** Streamlined integration for clients using Azure, ensuring a smooth and compliant deployment.
**Data Privacy:** Assurance of data protection through existing Azure agreements.
**Reevaluation:** This decision will be reevaluated if a paying client explicitly requests an alternative provider for prompt suggestions. At that time, we will consider the client's needs and the potential benefits of integrating with another provider.

### Status

Finalized
