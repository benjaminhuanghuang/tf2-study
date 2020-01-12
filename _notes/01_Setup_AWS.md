


1. Create EC2
Deep learning AMI (ubuntu)
Instance type <= p2.xlarge
Download key pair file (default path is ~/.ssh/id_rsa)

2. SSH to EC2
```
chmod 400 ben-aws-ml.pem

ssh -i "ben-aws-ml.pem" -L localhost8888:localhost:8888 ubuntu@ec2-54-203-178-195.us-west-2.compute.amazonaws.com
```

3. Open jupyter
Open jupyter in EC2
```
jupyter notebook
```