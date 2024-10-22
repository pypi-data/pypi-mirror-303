# 7. Deployment View

## 7.1 Overview

The deployment view outlines the technical infrastructure used to execute PromptArchitect, with a focus on the environments, computers, and networks involved in deploying and running the system. This section includes the mapping of software building blocks to the underlying infrastructure, particularly highlighting the new support for locally hosted AI models via the Ollama framework.

### Environments

PromptArchitect is typically deployed across multiple environments, each with specific configurations:

- **Development Environment**: Used for developing and testing engineered prompts and integrations. This environment includes local instances of the Ollama framework for testing AI models such as Gemma2, Llama3.1, and Mistral.
  
- **Test Environment**: A controlled environment where integration and system tests are performed. This includes testing the compatibility and performance of prompts across cloud-based models and locally hosted models via Ollama.
  
- **Production Environment**: The live environment where PromptArchitect is deployed for use by end-users. In this environment, users can choose to interact with either cloud-based AI models or locally hosted models depending on their requirements.

### Infrastructure Components

- **Cloud Servers**: These servers host the cloud-based AI models (e.g., OpenAI, Anthropic) and are accessed by PromptArchitect via API calls. The cloud servers are managed by external AI providers and are connected to PromptArchitect through secure network channels.
  
- **Local Servers/Workstations**: These are user-managed machines where the Ollama framework and locally hosted AI models (Gemma2, Llama3.1, Mistral) are installed. These servers execute prompts locally, leveraging the user's hardware resources.
  
- **Network**: Secure network connections are established between PromptArchitect and cloud-based AI providers. When executing locally hosted models, the network infrastructure within the user's environment is used, potentially including VPNs for secure access in enterprise settings.

### Continuous Integration

PromptArchitect uses a continuous integration (CI) pipeline hosted on GitHub. The CI pipeline automates the building, testing, and deployment processes to ensure that all changes to the codebase are validated before being merged into the main branch. The CI setup includes:

- **Automated Testing**: Tests are run on every commit to the repository, ensuring that the code is functional and that no regressions are introduced.
- **Build Process**: The CI pipeline builds the project into a Python package, which is then made available for installation.

### Installation

PromptArchitect is distributed as a Python package named `promptarchitect`. Developer users can install it using Python's package manager, pip:

```bash
pip install promptarchitect
```

This installation method simplifies the deployment process, making it easy for developers to integrate PromptArchitect into their local or server environments. The package includes all necessary dependencies, and the installation process is consistent across different platforms.

### Deployment Diagram

The following diagram provides a high-level overview of the deployment architecture:

```
+---------------------------------+
|            Cloud                |
| +-----------------------------+ |
| | Cloud-based AI Models       | |
| | (e.g., OpenAI, Anthropic)   | |
| +-------------+---------------+ |
|               |                 |
|       +-------+------+          |
|       |    Internet   |          |
+-------+-------+-------+----------+
                |
      +---------+----------+
      |      Network        |
      +---------+----------+
                |
+---------------+----------------+
|              User              |
| +-----------------------------+|
| | Local Server/Workstation    | |
| | +-------------------------+ | |
| | | Ollama Framework        | | |
| | | +---------------------+ | | |
| | | | Locally Hosted AI   | | | |
| | | | Models (Gemma2,     | | | |
| | | | Llama3.1, Mistral)  | | | |
| | | +---------------------+ | | |
| | +-------------------------+ | |
| +-----------------------------+ |
+---------------------------------+
```

## 7.2 Mapping of Software Building Blocks

The software components of PromptArchitect are mapped to the deployment infrastructure as follows:

### 7.2.1 Prompt Execution Engine

- **Location**: This core component is deployed across all environments (development, test, production).
- **Mapping**:
  - For cloud-based AI models, the Prompt Execution Engine interacts with cloud servers via API calls.
  - For locally hosted models, it interfaces directly with the Ollama framework installed on the local server or workstation.

### 7.2.2 Configuration Manager

- **Location**: Deployed within all environments to manage and distribute configuration settings.
- **Mapping**:
  - Manages configurations for both cloud-based and locally hosted models, ensuring that the correct API endpoints or local model paths are used depending on the deployment.

### 7.2.3 Ollama Integration

- **Location**: Deployed only on local servers or workstations where locally hosted AI models are to be used.
- **Mapping**:
  - This component interfaces with the Ollama framework to execute prompts on models such as Gemma2, Llama3.1, and Mistral. It ensures seamless integration and compatibility with the existing Prompt Execution Engine.

### 7.2.4 User Interfaces

- **Location**: Accessed from any environment, including web applications or automation scripts.
- **Mapping**:
  - Users interact with PromptArchitect through these interfaces, which in turn communicate with the Prompt Execution Engine. Depending on the user's configuration, the interfaces may trigger prompts executed either on cloud-based models or locally hosted models.

## 7.3 Deployment Considerations

### 7.3.1 Performance

- **Consideration**: Running AI models locally via Ollama requires adequate computational resources. Users must ensure their hardware is capable of handling the processing requirements of models like Gemma2, Llama3.1, and Mistral.

### 7.3.2 Security

- **Consideration**: When using locally hosted models, it is essential to maintain a secure environment to protect data and ensure the integrity of the AI models. This includes securing the local network and the machines running the Ollama framework.

### 7.3.3 Scalability

- **Consideration**: While locally hosted models offer flexibility and control, scalability might be constrained by the user's hardware capabilities. For large-scale deployments or heavy workloads, users may need to consider hybrid approaches, using both local and cloud-based models.

### 7.3.4 Maintenance

- **Consideration**: The Ollama framework and locally hosted models must be regularly updated to ensure compatibility with PromptArchitect and to benefit from performance improvements and security patches.

### 7.3.5 Continuous Integration and Deployment

- **Consideration**: The CI pipeline on GitHub ensures that all changes to the codebase are automatically tested and built before deployment. This reduces the risk of introducing errors into production environments and ensures a smooth installation process for developers using the `promptarchitect` Python package.

---
