# 5. Building Block View

## 5.1 Overview

The system is composed of several key components that work together to handle prompt-based interactions. With the recent updates, the system has expanded its capabilities to include executing prompts across multiple files, chaining prompts, retrieving cost and duration, and iterating over multiple prompts. These new features necessitate updates to the existing components and introduce new ones.

### Primary Components

1. **Prompt Engine**
   - **Role:** Handles the execution of individual prompts, including managing the lifecycle from input processing to output generation.
   - **Changes:** Enhanced to support prompt chaining and iteration over multiple prompts. Now includes logic for handling sequences of prompts where the output of one prompt can serve as the input for another.

2. **File Processor**
   - **Role:** Manages the reading, processing, and output of data across multiple files.
   - **Changes:** New functionality added to allow the execution of a single prompt across multiple files or to handle multiple files as a batch in a single operation.

3. **Cost and Duration Tracker**
   - **Role:** Monitors and logs the cost and duration associated with executing prompts.
   - **New Component:** This is a newly introduced component that tracks the computational resources consumed during prompt execution, providing detailed metrics for optimization and reporting.

4. **Template Manager**
   - **Role:** Manages the storage, retrieval, and application of templates in conjunction with prompts.
   - **Changes:** Updated to work seamlessly with the prompt engine’s new chaining and iteration features, ensuring that templates can be applied consistently across multiple prompts or files.

5. **User Interface (UI)**
   - **Role:** Provides an interface for users to interact with the system, define prompts, configure settings, and view results.
   - **Changes:** Updated to accommodate new user options for executing prompts across multiple files, chaining prompts, and viewing cost and duration information.

6. **Configuration Manager**
   - **Role:** Manages system configuration, including model selection and custom meta model options.
   - **Changes:** Expanded to include new options for configuring prompt execution behavior (e.g., chaining, iteration), as well as toggling the tracking of cost and duration.
7. **Dashboard**
     - **Description**: The user interface for managing prompts, viewing reports, and configuring settings.
     - **Customization**: Supports custom themes like the `github-pajamas-theme`, allowing users to modify the appearance and branding of the dashboard.

8. **Engineered Prompt Analyzer**
   - **Role:** Analyzes test cases in a `.prompt` file and provides improvement suggestions.
   - **New Component:** This newly introduced component reads a `.prompt` file and generates a list of suggestions for test cases with attributes like `test_id`, `description`, `analysis`, and `recommendations`.

## 5.2 Detailed Design

### Prompt Engine

- **Core Logic:** The prompt engine now includes additional logic for handling prompt chains. Each prompt can be linked to the next, forming a sequence where outputs from earlier prompts become inputs for subsequent ones. This chain is managed using a stack-based approach, ensuring that each prompt is processed in the correct order.
- **Iteration Support:** The prompt engine has been extended to support iteration over multiple prompts. This allows the system to handle bulk operations efficiently, iterating through a list of prompts and applying each to a designated input or set of inputs.

### File Processor

- **Batch Processing:** The file processor has been extended to support batch processing of files. It can now take a list of files as input and execute a given prompt across all of them, either sequentially or in parallel.
- **Integration with Prompt Engine:** The file processor is tightly integrated with the prompt engine, ensuring that prompts can be executed in a consistent manner across all files in a batch, with results being aggregated as needed.

### Cost and Duration Tracker

- **Tracking Mechanism:** This new component captures detailed metrics for each prompt execution, including the time taken (duration) and computational cost. This information is stored and can be retrieved for analysis and optimization.
- **Reporting:** Provides a summary of costs and latencies to the user interface, giving users visibility into the performance and cost implications of their prompts.

### Configuration Manager

- **New Options:** Includes new configuration options for enabling or disabling features like prompt chaining, iteration, and cost tracking. Users can also configure how the system handles batch processing of files and whether to prioritize cost or speed during prompt execution.

### Engineered Prompt Analyzer

- **Purpose and Functionality:** The `EngineeredPromptAnalyzer` class is designed to read a `.prompt` file and provide suggestions for test cases. It includes a function to iterate over tests and retrieve `test_id`, `description`, `score`, `analysis`, and `recommendations`.
- **Interaction with Other Components:** The `EngineeredPromptAnalyzer` interacts with the `EngineeredPrompt` class to get the analysis, using the `.prompt` file as `input_file` and `analyze_test_cases.prompt` as the `prompt_file`.

## 5.3 Interfaces

### Prompt Engine ↔ File Processor

- **Data Flow:** Prompts are sent from the prompt engine to the file processor along with configuration details. The file processor handles the batch execution and returns results to the prompt engine for further processing (e.g., chaining).

### Prompt Engine ↔ Cost and Duration Tracker

- **Data Flow:** After each prompt execution, the prompt engine sends execution data (e.g., time taken, resources used) to the cost and duration tracker. This data is logged and made available for reporting.

### Configuration Manager ↔ All Components

- **Data Flow:** The configuration manager interacts with all components to apply user-defined settings, ensuring that each component operates according to the user's specifications.

### Prompt Testing

- **Description**: This building block is dedicated to the validation and refinement of engineered prompts. It is an essential part of PromptArchitect, ensuring that prompts meet high standards of correctness and efficiency through a comprehensive testing framework.
- **Types of Tests**:
  - **Semantic Tests**: These tests verify that the prompt generates outputs that are semantically accurate, ensuring that the AI's responses align with the intended meaning and context of the input.
  - **Format Tests**: These tests ensure that the output follows the required format, which is critical for tasks where the structure and organization of the response are as important as the content.
  - **Calculated Tests**: These tests involve verifying that the outputs meet specific calculated criteria, such as numerical accuracy or logical consistency.
- **Purpose**:
  - **Correctness**: Ensur  es that prompts produce accurate and reliable results.
  - **Regression Testing**: Verifies that updates to prompts or underlying AI models do not introduce new errors or degrade performance.
  - **Performance Testing**: Evaluates the speed and resource utilization of prompts, ensuring they are efficient even under varying loads.
  - **Prompt Refinement**: Provides insights into how prompts can be improved to better meet testing criteria, leading to more effective and robust AI interactions.

### 5.3 Level 3: Component Interactions

The interactions between these building blocks are essential for the overall functionality of PromptArchitect:

- **Prompt Execution Engine** works closely with the **Prompt Testing** block to ensure that any prompt executed has been thoroughly validated for correctness, efficiency, and reliability.
- The **Dashboard** interfaces with both the **Prompt Execution Engine** and **Prompt Testing** to provide users with an intuitive way to manage prompts, view test results, and refine prompts as needed.
- **CLI Interface** allows advanced users to automate prompt execution and testing workflows, integrating with the broader ecosystem through custom scripts and pipelines.

#### 5.2.4 Prompt Management (or Prompt Execution Engine)

- **Description**: This component includes the management and manipulation of prompt files, including the ability to substitute template strings within a prompt. This allows for more dynamic and flexible prompt generation by allowing users to replace placeholders with specific values before executing the prompt.
- **Key Functionality**:
  - **Template String Substitution**: Allows users to define template strings within a prompt file and replace these with actual values at runtime, facilitating dynamic prompt generation.
  - **Example Use Case**: A user can create a general prompt template that generates titles for different types of media (e.g., podcasts, blog posts) and specify the type and number dynamically at runtime.
