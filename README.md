# lambda-instance-operation

This repository is AWS Lambda function's upload files.

## Language

- python2.7.10

## Package

- boto3

## How To Use

### 1.clone git repository

```
git clone https://github.com/mkawabata-linkbal/lambda-instance-operation.git
```

### 2.edit tag name

```
cd lambda-instance-operation
vi lambda-instance-operation.py
-----------
    tag_name = "<TAG_NAME>"
-----------
```

### 3.prepare upload zip file

```
zip -r ../lambda-instance-operation.zip .
```

### see also

- http://tech.linkbal.co.jp
