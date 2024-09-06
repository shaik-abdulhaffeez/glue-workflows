# AWS Glue Workflow with Multi-Threading and Observer Pattern
This project demonstrates the implementation of an AWS Glue workflow using multi-threading and the Observer pattern. The workflow is designed to handle multiple ETL jobs concurrently, improving performance and efficiency.

## Directory Structure
```
glue_workflow/
│
├── etl_jobs/
│   ├── init.py
│   ├── base.py
│   ├── data_etl_job.py
│   ├── log_etl_job.py
│   ├── email_etl_job.py
│
├── observers/
│   ├── init.py
│   ├── base.py
│   ├── job_observer.py
│
├── glue_job.py
│
├── main.py
│
└── README.md
```

## Usage

1. Clone the repository:
    ```bash
    git clone https://github.com/shaik-abdulhaffeez/glue-workflows.git
    cd glue_workflow

## Run the main script:

python main.py

## Components

     etl_jobs: Contains the base class and specific implementations for different types of ETL jobs.

     observers: Contains the base class and specific implementations for observers.

     glue_job.py: The main Glue job class that acts as the subject in the Observer pattern.

     main.py: The entry point for running the Glue job.

## Benefits

     Improved Performance: By executing multiple ETL jobs concurrently, the workflow improves overall performance.

     Scalability: The Observer pattern allows easy addition or removal of observers, making the workflow scalable and adaptable.

     Maintainability: The Observer pattern decouples the components of the ETL process, making the workflow more maintainable.
     
## Contributing

Feel free to contribute to this project by submitting issues or pull requests. Please follow the guidelines below:

1. Fork the repository: Create a fork of this repository to your GitHub account.
2. Create a branch: Create a new branch for your feature or bug fix.
3. Make changes: Implement your changes and ensure they are well-documented.
4. Submit a pull request: Submit a pull request to the main repository for review.

## Contact

For any questions or support, please contact abdulhaffeez on [LinkedIn](https://www.linkedin.com/in/shaik-abdul-haffeez-84719882?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3B3AeT1%2FumQ9SRbkNo711Y7A%3D%3D).
