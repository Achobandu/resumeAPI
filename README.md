
[![Deploy Lambda and s3](https://github.com/Achobandu/resumeAPI/actions/workflows/deploy.yml/badge.svg)](https://github.com/Achobandu/resumeAPI/actions/workflows/deploy.yml)
# Resume API with AWS Lambda, API Gateway, and S3 Hosting

This project implements a resume system using AWS Lambda for backend processing, API Gateway for API management, and S3 for frontend hosting. It allows for easy updating and displaying of resume data in a stylized web format.

## Table of Contents

- [Features](#features)
- [Architecture](#architecture)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Installation](#installation)
- [Detailed Configuration](#detailed-configuration)
- [Deployment](#deployment)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Customization](#customization)
- [Troubleshooting](#troubleshooting)
- [FAQ](#faq)
- [Security Considerations](#security-considerations)
- [Contributing](#contributing)
- [Credits](#credits)
- [License](#license)

## Features

- Serverless backend using AWS Lambda and DynamoDB
- Static frontend hosted on AWS S3
- Dynamic content loading via API calls through API Gateway
- Stylized resume display with responsive design
- Easy-to-update JSON-based resume data
- GitHub Actions for automated deployment

## Architecture

- **Backend**: AWS Lambda function (Python) + API Gateway
- **Database**: Amazon DynamoDB
- **Frontend**: HTML/CSS/JavaScript hosted on S3
- **Deployment**: GitHub Actions for CI/CD

## Prerequisites

- AWS account
- Python 3.12 installed
- Git installed

## Setup

1. **AWS Configuration**:
   - Set up an AWS account if you don't have one.

2. **DynamoDB Table Setup**:
   - Create a DynamoDB table named `ResumeChallenge` with the appropriate schema using the AWS Management Console. For example:
     - **Primary Key**: `resume_id` (String)
     - **Attributes**: Include other attributes like `name`, `education`, `experience`, etc.

3. **Lambda Function**:
   - Create a Lambda function via the AWS Management Console:
     - **Runtime**: Python 3.12
     - **Handler**: `lambda_function.lambda_handler`
     - **Role**: Create a new role with basic Lambda execution permissions and DynamoDB access.
   - Upload the `lambda_function.py` to AWS Lambda using the AWS Management Console.

4. **API Gateway**:
   - Create a new REST API in API Gateway using the AWS Management Console.
   - Create a new resource and method (e.g., `GET` method for `/resume`):
     - **Integration Type**: Lambda Function
     - **Lambda Function**: Select your Lambda function
   - Deploy the API to a stage (e.g., `dev`) and note the invoke URL.

5. **S3 Hosting**:
   - Create an S3 bucket and enable static website hosting using the AWS Management Console.
   - Upload `index.html`, `style.css`, and any other necessary frontend files to the S3 bucket.
   - Configure the bucket policy to allow public read access if necessary.

6. **GitHub Actions**:
   - Set up GitHub Secrets for AWS credentials (e.g., `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`).
   - Configure the `.github/workflows/deploy-lambda.yml` file for automated deployment.

## Installation

1. **Create a New Repository**:
   - Create a new repository on GitHub and initialize it with a README.

2. **Set Up Local Repository**:
   - Clone the new repository to your local machine:
     ```bash
     git clone https://github.com/yourusername/resume-api.git
     cd resume-api
     ```

## Detailed Configuration

1. **DynamoDB Table Setup**:
   - Define the table schema, primary key, and any indexes required using the AWS Management Console.

2. **Environment Variables**:
   - Set environment variables in the Lambda function configuration via the AWS Management Console:
     - `DYNAMODB_TABLE`: `ResumeChallenge`
     - Any other variables as needed.

3. **API Gateway Configuration**:
   - Set up API Gateway to call the Lambda function and retrieve data from DynamoDB using the AWS Management Console:
     - **Method Request**: Configure method request settings.
     - **Integration Request**: Set the integration type to Lambda function. Select proxy integration.
     - **Method Response**: Configure response settings.

## Deployment

1. **Deploy Lambda Function**:
   - Upload the `lambda_function.zip` file via the AWS Management Console.

2. **Deploy to S3**:
   - Upload the necessary frontend files (`index.html`, etc.) via the AWS Management Console.

## Usage

1. Update your resume data in the DynamoDB table.
2. The Lambda function serves this data via API Gateway.
3. The S3-hosted webpage fetches and displays the data using the API Gateway invoke URL.

To view resume, visit the S3 website URL:(https://resumestaticweb.s3.us-east-1.amazonaws.com/index.html).

## API Endpoints

- `GET https://your-api-id.execute-api.us-east-1.amazonaws.com/your-stage/resume` (https://rcn2ynee74.execute-api.us-east-1.amazonaws.com/resume-test/resume)

## Testing

1. **Manual Testing**:
   - Test the API endpoints using the invoke url or tools like Postman or cURL.

## Customization

- Modify `index.html` to change the layout and styling of the resume.
- Update the Lambda function to add more data processing or features.
- Customize the DynamoDB schema to include additional resume sections.

## Troubleshooting

- **Common Errors**:
  - **Lambda Function Errors**: Check CloudWatch logs for detailed error messages.
  - **API Gateway Errors**: Verify the API Gateway configuration and ensure the Lambda function permissions are set correctly.
  - **S3 Hosting Issues**: Ensure the S3 bucket policy allows public read access if necessary.

## FAQ

- **How to add new resume sections?**
  - Update the DynamoDB schema to include new attributes.
  - Modify the Lambda function to handle new data.
  - Update the frontend to display new sections.

- **How to update styling for the resume?**
  - Modify the `index.html` file in the frontend directory.

## Security Considerations

- **Securing API Gateway**:
  - Use IAM roles and policies to restrict access to the Lambda function and DynamoDB table.

- **IAM Roles and Policies**:
  - Ensure the Lambda function has the necessary permissions to access DynamoDB.
  - Use least privilege principle when setting IAM policies.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Credits

- **Third-Party Libraries**:

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
