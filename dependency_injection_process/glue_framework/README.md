# AWS Glue Data Engineering Framework

# Framework Overview

This framework leverages interface implementation and Dependency Injection (DI) to build flexible, maintainable, and scalable AWS Glue data engineering workflows. It includes a metadata system to capture the health state of each DI, ensuring robust monitoring and management.

## Table of Contents

- [Directory Structure](#directory-structure)
- [Components](#components)
- [Usage](#usage)
- [Orchestration with AWS Step Functions](#orchestration-with-aws-step-functions)
- [Technology Components](#technology-components)
- [Contributing](#contributing)
- [Contact](#contact)

## Directory Structure

The directory structure of the framework is as follows:

```
glue_framework/
│
├── jobs/
│   ├── __init__.py
│   ├── job_a.py
│   ├── job_b.py
│   └── glue_job_interface.py
│
├── injector/
│   ├── __init__.py
│   └── dependency_injector.py
│
├── manager/
│   ├── __init__.py
│   └── glue_job_manager.py
│
├── metadata/
│   ├── __init__.py
│   └── metadata_system.py
│
├── main.py
└── README.md
```

## Components

The framework consists of the following components:

- **Glue Job Interface**: Defines the contract for Glue jobs.
- **Job Implementations**: Different implementations of the Glue Job Interface for various data processing tasks.
- **Dependency Injector**: Manages the injection of dependencies into the Glue jobs.
- **Glue Job Manager**: Orchestrates the execution of Glue jobs based on the injected dependencies.
- **Metadata System**: Captures the health state of each DI and provides monitoring capabilities.

## Usage

To use the framework, follow these steps:

1. Initialize the Dependency Injector by registering the job implementations.
2. Initialize the Glue Job Manager by passing the dependency injector to the manager.
3. Initialize the Metadata System to track the health state of each job.
4. Run the jobs by executing them and updating the health states.

Example code:

```python
from injector.dependency_injector import DependencyInjector
from manager.glue_job_manager import GlueJobManager
from metadata.metadata_system import MetadataSystem
from jobs.job_a import JobA
from jobs.job_b import JobB

# Initialize Dependency Injector
injector = DependencyInjector()
injector.register("JobA", JobA())
injector.register("JobB", JobB())

# Initialize Glue Job Manager
manager = GlueJobManager(injector)

# Initialize Metadata System
metadata = MetadataSystem()

# Run Jobs
manager.run_job("JobA")
metadata.update_health_state("JobA", "Success")

manager.run_job("JobB")
metadata.update_health_state("JobB", "Success")

# Print Health States
print(metadata.get_health_state("JobA"))
print(metadata.get_health_state("JobB"))
```

## Orchestration with AWS Step Functions

AWS Step Functions can be used to orchestrate the execution of Glue jobs in a workflow. Here's how you can integrate AWS Step Functions with this framework:

1. Define Step Functions: Create a state machine in AWS Step Functions that defines the sequence of Glue jobs to be executed.
2. Invoke Glue Jobs: Use AWS Lambda functions or AWS Glue triggers to invoke the Glue jobs based on the state machine.
3. Monitor Execution: Use AWS CloudWatch to monitor the execution of the state machine and the health states of the Glue jobs.

Example Step Functions State Machine:

```json
{
    "Comment": "AWS Glue Data Engineering Workflow",
    "StartAt": "JobA",
    "States": {
        "JobA": {
            "Type": "Task",
            "Resource": "arn:aws:states:us-east-1:123456789012:activity:JobA",
            "Next": "JobB"
        },
        "JobB": {
            "Type": "Task",
            "Resource": "arn:aws:states:us-east-1:123456789012:activity:JobB",
            "End": true
        }
    }
}
```

## Technology Components

The framework utilizes the following technology components:

- **Python**: The primary programming language used for implementing the framework.
- **PySpark**: Used for large-scale data processing within AWS Glue jobs.
- **AWS Glue**: A fully managed ETL service that makes it easy to prepare and load data for analytics.
- **AWS Glue Crawlers**: Automatically discover the schema of your data and create metadata tables in the AWS Glue Data Catalog.
- **AWS Glue Connections**: Securely connect to your data sources using JDBC connections.
- **Amazon S3**: Used for storing raw data, processed data, and intermediate results.
- **AWS IAM**: Manages access control and permissions for AWS resources.
- **AWS Step Functions**: Orchestrates the execution of Glue jobs in a workflow.
- **AWS CloudWatch**: Monitors the execution of the state machine and the health states of the Glue jobs.
- **AWS RDS**: to maintain health state of entire application and also useful to bring observability capabilites.

## Contributing

Feel free to contribute to this project by submitting issues or pull requests. Please follow the guidelines below:

1. Fork the repository: Create a fork of this repository to your GitHub account.
2. Create a branch: Create a new branch for your feature or bug fix.
3. Make changes: Implement your changes and ensure they are well-documented.
4. Submit a pull request: Submit a pull request to the main repository for review.

## Contact

For any questions or support, please contact abdulhaffeez on [LinkedIn](https://www.linkedin.com/in/shaik-abdul-haffeez-84719882?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3B3AeT1%2FumQ9SRbkNo711Y7A%3D%3D).

