ERD Description

1. Batch Table:
batch_id: Primary Key
batch_name: Name of the batch
description: Description of the batch
active_status: Status of the batch

2. BatchRun Table
batchrun_id: Primary Key
batch_id: Foreign Key referencing batch(batch_id)
execution_date: Date of execution
status: Status of the batch run

3. Job Table
job_id: Primary Key
job_name: Name of the job
description: Description of the job
job_type: Type of the job
active_status: Status of the job
batch_id: Foreign Key referencing batch(batch_id)

4. JobRun Table
job_run_id: Primary Key
job_id: Foreign Key referencing job(job_id)
batchrun_id: Foreign Key referencing batch_run(batchrun_id)
execution_date: Date of execution
status: Status of the job run
log_message: Log message of the job run

5. JobArguments Table
argument_id: Primary Key
job_id: Foreign Key referencing job(job_id)
argument_name: Name of the argument
argument_value: Value of the argument


CREATE SEQUENCE batch_run_seq START 100;

CREATE TABLE pipeline.batch (
    batch_id SERIAL PRIMARY KEY,
    batch_name VARCHAR(255) NOT NULL,
    description TEXT,
    active_status BOOLEAN
);

CREATE SEQUENCE pipeline.batch_run_seq START 50;
-- BatchRun Table
CREATE TABLE pipeline.batch_run (
    batchrun_id INT DEFAULT NEXTVAL('batch_run_seq') PRIMARY KEY,
    batch_id INT NOT NULL,
    execution_date TIMESTAMP NOT NULL,
    status VARCHAR(50),
    FOREIGN KEY (batch_id) REFERENCES batch(batch_id)
);
-- Create a sequence starting from 0
CREATE SEQUENCE pipeline.job_id_seq START 0 MINVALUE 0;
-- Job Table
CREATE TABLE pipeline.job (
    job_id SERIAL PRIMARY KEY,
    job_name VARCHAR(255) NOT NULL,
    description TEXT,
    job_type VARCHAR(255),
    active_status BOOLEAN,
    batch_id INT,
    FOREIGN KEY (batch_id) REFERENCES batch(batch_id)
);

-- JobRun Table
CREATE TABLE pipeline.job_run (
    job_run_id SERIAL PRIMARY KEY,
    job_id INT NOT NULL,
    batchrun_id INT NOT NULL,
    execution_date TIMESTAMP NOT NULL,
    status VARCHAR(50),
    log_message TEXT,
    source_count int,
    processed_count int,
    unprocessed_count int,
    FOREIGN KEY (job_id) REFERENCES job(job_id),
    FOREIGN KEY (batchrun_id) REFERENCES batch_run(batchrun_id)
);

CREATE TABLE pipeline.job_arguments (
    argument_id SERIAL PRIMARY KEY,
    job_id INT NOT NULL,
    argument_name VARCHAR(255) NOT NULL,
    argument_value TEXT,
    FOREIGN KEY (job_id) REFERENCES job(job_id)
);

