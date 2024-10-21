# 4 Solution strategy

## 4.1 Support for API usage and CLI usage

We want promptarchitect to be used in production and during development to make sure there are fewer differences between the two environments. We want to execute prompts in production and test them in development.

To make this possible we provide an API to execute prompts in production, and a CLI tool to test prompts in development and during testing.

## 4.2 Flexible reporting structure

Prompt validation is important to business users as well because they seek reliable AI solutions. A report that matches the styling and layout of the business helps to increase the confidence level of business users. We therefore support building HTML reports using templating, so the testing reports can be formatted to match what the business users expect.

## 4.3 Support multiple forms of testing

It's important to understand that there's not one method to validate prompts. We need to look at multiple aspects of a
prompt depending on the scenario we're using the prompt in. Therefore, we support multiple forms of testing:

- Format validation: Some prompts need to produce output in JSON, HTML or another format.
- Text property validation: In some cases we expect the prompt to produce a list of 5 items or similar.
- Semantic validation: In many cases we need to validate that the prompt follows semantic rules.
- Scoring: In cases where we're building RAG systems we need to score output for faithfulness and other metrics.

Promptarchitect supports these forms of tests through various types of test cases.

## 4.4 Prompt templating

We know that engineers build prompts that are structured with placeholders to insert pieces of information into a prompt. We support using placeholders in prompts to ensure that engineers are free to build prompts the way they want.
We use a well-known templating format [Mustache](https://mustache.github.io/) for this purpose.

## 4.5 Prompt file design

In section 4.1 we established that we're using a CLI and an API. For CLI usage, we introduce a concept called a prompt file. The prompt file defines the prompt with associated settings and tests. This file can be discussed with the business to establish what a prompt should do. It can also be provided to the CLI to validate the prompt. Finally, it can be used to load the prompt, so we can execute it in production.

Please find the full specication for the prompt file in the [User documentation](../user/).

## 4.6 Open formats

### 4.1 Overview

The solution strategy emphasizes the use of open formats and open protocols to ensure that PromptArchitect can be easily integrated into existing IT infrastructures. This approach mitigates the risk of vendor lock-in and promotes interoperability, allowing organizations to leverage the benefits of PromptArchitect while maintaining flexibility in their technology stack.

### 4.6.1 Key Principles

1. **Openness and Interoperability**:
   - The system is designed to use open formats (like Markdown, JSON, HTML) and open protocols (such as OpenTelemetry) to ensure that it can be integrated seamlessly with existing tools and infrastructure. This strategy reduces the risk of being locked into proprietary systems and allows organizations to adopt PromptArchitect without compromising their ability to switch tools or vendors in the future.

### 4.6.2 Architectural Decisions

1. **Use of Open Formats**:
   - **Rationale**: To ensure that the outputs of PromptArchitect can be easily consumed, shared, and integrated with other systems, we chose to adopt widely accepted open formats for various aspects of the system.
   - **Implementation**:
     - **Engineered Prompts**: Prompts are specified in Markdown format, which is both human-readable and machine-processable. A header specific to PromptArchitect is added to provide metadata and configuration details. However, the core content of the prompt remains usable outside of PromptArchitect, ensuring flexibility.
     - **Reporting**: Test reports are generated in JSON and HTML formats. JSON allows for easy integration with monitoring systems, logging tools, and automated workflows, while HTML provides a user-friendly format that can be published on platforms like Wiki or SharePoint.
   - **Trade-offs**: Using open formats increases the system's versatility but may require additional handling to ensure compatibility with all desired outputs.

2. **Adoption of OpenTelemetry**:
   - **Rationale**: For logging and monitoring, we adopted OpenTelemetry, an open protocol that provides a standardized way to collect and transmit telemetry data. This choice aligns with our strategy of openness and ensures that organizations can integrate PromptArchitect with their existing monitoring and logging infrastructure without being tied to proprietary solutions.
   - **Implementation**:
     - **Standard Collector**: PromptArchitect includes a standard collector for OpenTelemetry data, allowing users to start monitoring quickly out of the box.
     - **Custom Collectors**: Organizations have the option to implement custom collectors if they have specific requirements or need to integrate with specialized monitoring systems.
   - **Trade-offs**: While OpenTelemetry is widely supported, it may require additional configuration or customization to fit into certain legacy systems.

### 4.6.3 Summary

The use of open formats and protocols is a strategic choice that aligns with the goal of making PromptArchitect highly interoperable and flexible. By adopting open standards like Markdown, JSON, HTML, and OpenTelemetry, PromptArchitect ensures that it can be easily integrated into a wide range of IT environments, reducing the risk of vendor lock-in and allowing organizations to retain control over their infrastructure and data.
