# AWS Student Registration Application

## Project Description

The AWS Student Registration Application is a web-based application developed using Python Flask. It allows users to register student details and upload student photos. The application uses Amazon EC2 to host the application, Amazon RDS to store student information, and Amazon S3 to store uploaded files.

## Technologies Used

* **Python** – Programming language
* **Flask** – Web application framework
* **Amazon EC2** – Hosting the application
* **Amazon RDS (MySQL)** – Student database
* **Amazon S3** – File storage
* **AWS IAM** – Access permissions
* **HTML** – Web page design

## Features

* Student registration form
* Collection of student name, email, and course
* Student photo/file upload
* Storage of student information in MySQL
* Storage of uploaded files in Amazon S3
* Integration of multiple AWS services

## Project Architecture

1. The user opens the student registration web page.
2. The Flask application runs on Amazon EC2.
3. The user enters student details and uploads a file.
4. The uploaded file is stored in Amazon S3.
5. Student details and the file URL are stored in Amazon RDS MySQL.
6. A success message is displayed after registration.

## AWS Services Configuration

* **EC2:** Hosts the Flask application.
* **RDS:** Stores student registration details.
* **S3:** Stores uploaded student files.
* **IAM Role:** Allows the EC2 instance to access the S3 bucket.
* **VPC and Security Groups:** Provide network isolation and control access.

## Project Files

```text
pythoncodeAWS/
├── app.py
├── requirements.txt
├── Dockerfile
├── Jenkinsfile
├── README.md
└── templates/
    └── index.html
```

## Installation and Execution

### 1. Install dependencies

```bash
pip3 install -r requirements.txt
```

### 2. Configure the database

Set the database password using the `DB_PASSWORD` environment variable. Configure the RDS endpoint and database name in the application.

### 3. Configure AWS access

Attach an IAM role to the EC2 instance with the required permissions to upload files to the designated S3 bucket.

### 4. Run the application

```bash
python3 app.py
```

The application runs on port 5000. Open the EC2 public IP address with port `5000` in a browser, provided the security group permits access.

## Database

The application uses a MySQL database named `studentdb` with a `students` table containing:

* Student ID
* Name
* Email
* Course
* Photo URL

## Expected Output

After submitting the registration form successfully, the application displays:

**Student Registered Successfully**

## Security Notes

* Do not upload database passwords, private keys, or other credentials to GitHub.
* Use IAM roles instead of hardcoding AWS access keys.
* Keep the S3 bucket private unless public access is specifically required.
* Restrict security group access to trusted IP addresses wherever possible.

## Conclusion

This project demonstrates how to deploy a Python Flask web application on AWS and integrate Amazon EC2, Amazon RDS, Amazon S3, IAM, and VPC networking to build a cloud-based student registration system.
