from aws_cdk import (
    aws_lambda as _lambda,
    aws_apigateway as apigw,
    aws_eks as eks,
    aws_ec2 as ec2,
    core,
)

class CdkworkshopStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Define a Lambda resource
        # my_lambda = _lambda.Function(
        #     self, 'HelloHandler',
        #     runtime=_lambda.Runtime.PYTHON_3_7,
        #     code=_lambda.Code.asset('lambda'),
        #     handler='hello.handler',
        # )

        # apigw.LambdaRestApi(
        #     self, 'Endpoint',
        #     handler=my_lambda,
        # )
        eks_cluster = eks.Cluster(
            self, "andrii_test_cdk_cluster",
            default_capacity=0,# disabled default capacity
            default_capacity_instance=ec2.InstanceType("t2.small")
        )
        eks_cluster.add_capacity("frontend-nodes",
            instance_type=ec2.InstanceType("t2.small"),
            desired_capacity=2,
            vpc_subnets={"subnet_type": ec2.SubnetType.PUBLIC}
        )
