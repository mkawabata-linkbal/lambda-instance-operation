#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
# lambda-instance-operation

This repository is AWS Lambda function's upload files.
"""

__authour__ = "masaru.kawabata"
__version__ = 1.1

import boto3

def instance_start(event, context):
    """ Create Connection """
    try:
        ec2 = boto3.resource('ec2', region_name='ap-northeast-1')
    except:
        print('Connection Error')
        return 1

    """ Get EC2 Instance Info """
    tag_name = "<TAG_NAME>"
    instance = [i for i in ec2.instances.all() for t in i.tags if t["Value"] == tag_name][0]

    """ Start EC2 Instance """
    try:
        instance.start()
    except: 
        print('Start EC2 Instance Error')
        return 1

    return 0

def instalce_stop(event, context):
    """ Create Connection """
    try:
        ec2 = boto3.resource('ec2', region_name='ap-northeast-1')
    except:
        print('Connection Error')
        return 1

    """ Get EC2 Instance Info """
    tag_name = "<TAG_NAME>"
    instance = [i for i in ec2.instances.all() for t in i.tags if t["Value"] == tag_name][0]

    """ Stop EC2 Instance """
    try:
        instance.stop()
    except: 
        print('Stop EC2 Instance Error')
        return 1

    return 0
