# AWS Glue with Boto3
Full Hands-on for AWS Glue with Boto3

&nbsp; 

## ⚙️ **Prerequisites and Installation**

To start working with ``AWS Glue`` using ``Boto3``, you need to set up your Python environment on your laptop.  
  
In summary, this is what you will need:
- Python 3
- Boto3
- AWS CLI tools
- virtualenv

&nbsp; 

```bash
$ pip3 install virtualenv

#Test your installation:
$ virtualenv --version

# Create your virtual environment
$ python3 -m venv .venv-aws-glue

# you can activate the virtual environment by just input
source .venv-aws-glue/bin/activate

# then you can deactivate it by just type in deactivate.
source .venv-aws-glue/bin/deactivate

# If you want to delete that virtual env, simply do
rm -rf .venv-aws-glue
```

&nbsp; 

Once the virtualenv is activated, you can install the required dependencies.

```bash
$ pip install -r requirements.txt
```

&nbsp; 

&nbsp; 

## 🧰 **Define AWS Credentials**

Save your credentials in ``~/.aws/credentials`` add. Then define ENV variable using: 
```
$ export AWS_PROFILE=my_aws_profile

$ env
````
 
&nbsp; 

&nbsp; 

&nbsp; 

&nbsp; 

## **Sources:**
- Resolving the Boto3 NoCredentialsError in Python: https://rollbar.com/blog/python-boto3-nocredentialserror/

- 


