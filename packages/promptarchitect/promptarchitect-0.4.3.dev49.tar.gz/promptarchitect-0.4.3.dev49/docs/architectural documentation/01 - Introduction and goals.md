# 1. Introduction and Goals

## 1.1 Requirements Overview

### About Engineered Prompts and PromptArchitect

In the rapidly evolving landscape of artificial intelligence, the concept of an "engineered prompt" is gaining prominence, especially in environments leveraging large language models (LLMs) and other AI systems. Engineered prompts are meticulously crafted inputs designed to interact with AI models in a way that ensures consistent and reliable outputs. These prompts are structured tools integral to the automated processes in which they function.

PromptArchitect is a product designed to facilitate the development, deployment, management and monitoring of engineered prompts. It provides a structured approach to creating inputs for AI models, ensuring precision, reusability, and scalability.

PromptArchitect is built on the principle that developing software on top of Large Language Models (LLMs) requires the same high standards as traditional software development. This includes a strong emphasis on robustness, scalability, maintainability, testability, and overall quality. By ensuring that the outcomes of the system are verifiable, consistent, and of high quality, PromptArchitect meets the demands of businesses that rely on these systems.

### Support for Ollama Models

PromptArchitect now supports the use of open-source models running locally via [Ollama](https://ollama.ai). This feature allows you to leverage powerful, locally hosted models such as Gemma2, Llama3.1, and Mistral, giving you greater control and flexibility over your AI model deployments.

#### Supported Models

- **Gemma2**: A robust and versatile model ideal for various natural language processing tasks.
- **Llama3.1**: An advanced model offering cutting-edge performance in language understanding and generation.
- **Mistral**: A lightweight, efficient model designed for quick responses and lower resource usage.

### Definition and Purpose

An engineered prompt is a carefully designed input used to generate a specific type of response from an AI model. Unlike casual or ad-hoc prompts, engineered prompts are developed through a rigorous process that considers the nuances of the model’s language understanding and output capabilities. They are akin to code in software development, serving as fundamental components that interact with AI to execute specific tasks reliably.

### Characteristics of Engineered Prompts

- **Precision and Clarity**: Engineered prompts are precise, unambiguous, and tailored to elicit specific responses or behaviors from AI models.
- **Reusability**: These prompts are designed to be reusable across similar tasks or models, ensuring efficiency and consistency in automated processes.
- **Scalability**: Engineered prompts can be scaled or modified according to different requirements or changes in the AI model’s behavior.

### Development and Maintenance

Just like software code, engineered prompts require a structured development and maintenance process to remain effective and safe for use:

- **Versioning**: Keeping track of different versions of prompts is crucial as models and requirements evolve. Versioning allows developers to manage changes systematically, revert to previous versions if needed, and understand the evolution of prompt effectiveness over time.
- **Documentation**: Comprehensive documentation detailing the design rationale, expected outputs, model compatibility, and dependencies is essential. This is vital for both current use and future modifications.
- **Testing and Validation**: Rigorous testing, including unit testing, integration testing, and validation testing, ensures the prompt generates the expected outputs.
- **Performance Tests**: Performance testing evaluates how well the prompt works in terms of speed and resource utilization, ensuring efficiency even at scale.
- **Regression Testing**: Particularly critical when the underlying AI model is updated or when switching to a model from a different provider, regression tests help verify that updates or changes do not negatively affect the prompt's performance.

## 1.2 Quality Goals

### Primary Quality Goals

1. **Enterprise-Grade Integration**: Provide features and workflows that align with enterprise-level development standards, making it easy to integrate PromptArchitect into existing development environments.
2. **Testability**: Integrate testing deeply into the development workflow, ensuring that every aspect of the system can be tested and verified.
3. **Reliability**: Ensure that prompts consistently produce the intended outputs.
4. **Efficiency**: Prompts should be efficient in terms of resource utilization and speed.
5. **Maintainability**: Prompts should be easy to maintain, with clear versioning and documentation.
6. **Scalability**: Prompts should be adaptable to different models and tasks without requiring extensive rework.
7. **Correctness**: Prompts must pass semantic, format, and calculated tests to ensure they generate accurate and reliable results.
8. **Consistency**: Prompts should perform consistently across different scenarios and model versions, validated through rigorous regression testing.
9. **Flexibility**: With the introduction of Ollama models, prompts must now seamlessly switch between local and cloud-hosted models to suit user needs.
10. **Flexibility**: Enhance the flexibility of prompt generation by allowing dynamic substitution of template strings, ensuring that the same prompt template can be reused for various scenarios with different input values.

### Secondary Quality Goals

1. **Usability**: Prompts should be user-friendly and easy to implement.
2. **Security**: Ensure that prompts do not expose vulnerabilities in the AI models.
3. **Cost Efficiency**: By enabling the use of locally hosted models, reduce reliance on cloud services and associated costs.

## 1.3 Stakeholders

### Primary Stakeholders

- **Developers**: Responsible for creating and maintaining engineered prompts.
- **Project Managers**: Oversee the prompt development process and ensure alignment with project goals.
- **End Users**: Utilize the outputs generated by the AI models based on the engineered prompts.

### Secondary Stakeholders

- **System Administrators**: Manage the infrastructure supporting the AI models and prompts, particularly relevant with the new support for locally hosted Ollama models.
- **Quality Assurance**: Ensure the prompts meet the specified quality goals and requirements.
- **Business Analysts**: Define requirements and validate that the prompts meet business needs.

## 1.4 Key Drivers

### Business Drivers

- **Automation**: Enhance automated processes by providing reliable and consistent AI interactions.
- **Efficiency**: Reduce the time and effort required to develop and maintain AI interactions.
- **Scalability**: Support the growing demand for AI-driven solutions across various domains.
- **Cost Control**: With the ability to use locally hosted models, reduce operational costs associated with cloud-based AI services.

### Technical Drivers

- **Advanced AI Capabilities**: Leverage the latest advancements in AI and LLMs to create sophisticated prompts.
- **Integration**: Ensure seamless integration with existing AI models and infrastructure, including new support for Ollama-hosted models.
- **Innovation**: Continuously improve prompt design and development techniques to stay ahead in the AI landscape.

## 1.5 Summary

PromptArchitect is a tool designed to streamline the development, deployment, and management of engineered prompts, which are structured inputs crucial for interacting with AI models reliably and consistently. By ensuring precision, reusability, and scalability, PromptArchitect aims to enhance the efficiency and effectiveness of automated processes that leverage AI technologies. The addition of support for Ollama models, including Gemma2, Llama3.1, and Mistral, further empowers users by providing more flexible and cost-effective AI model deployment options.

The tool also offers a flexible Command Line Interface (CLI) for advanced usage and integration into existing workflows, as well as support for custom dashboard themes, allowing users to personalize their interface according to their organizational needs.

## 1.6 References

- [Testing Language Models (and Prompts) Like We Test Software](https://towardsdatascience.com/testing-large-language-models-like-we-test-software-92745d28a359)
- [Beyond Accuracy: Behavioral Testing of NLP Models with CheckList](https://homes.cs.washington.edu/~marcotcr/acl20_checklist.pdf)
- [Ollama AI](https://ollama.ai) - Information on the open-source models now supported by PromptArchitect.

---
