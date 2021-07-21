###############################################################################
#General config. All you need is an admin command line account. State is in bucket.
provider "aws" {
	region = "us-east-1"
	allowed_account_ids = [
		"088838630371"
	]
}

terraform {
	backend "s3" {
		bucket = "aws-seas-wattslab-acct-tfstate.us-east-1"
		key = "tfstate"
		region = "us-east-1"
	}
}

##################################################################################
#Existing resources. Subnet and VPC.
#These have been brought into the state via import

#terraform import vpc-032a8f6c60eb7b535 | aws-seas-wattslab-acct
data "aws_vpc" "tveyes_vpc" {
	id = "vpc-032a8f6c60eb7b535"
}

#terraform import aws-seas-wattslab-acct Private01
data "aws_subnet" "tveyes_subnet" {
	id = "subnet-0e152ecb7836e2760"
}

#terraform import aws-seas-wattslab-acct Private01
resource "aws_security_group" "tveyes_security_group" {
	description = "allow tveyes fargate tasks to reach network for SSM params"
	egress = [
		{
			cidr_blocks = [
				"0.0.0.0/0",
			]
			ipv6_cidr_blocks = ["::/0"]
			description = ""
			from_port = 0
			prefix_list_ids = []
			protocol = "-1"
			security_groups = []
			self = false
			to_port = 0
		}
	]

	vpc_id = data.aws_vpc.tveyes_vpc.id
	tags = {
		Owner = var.owner_tag
		Budget = var.budget_tag
		Project = var.project_tag
		Email = var.email_tag
	}
}

#################################################################################
#S3 Resources
data "aws_s3_bucket" "xml_bucket" {
	bucket = "edu-upenn-wattslab-tveyes-preprocessing"
}

####################################################################################
#Kinesis stream
resource "aws_kinesis_stream" "tveyes_kinesis_stream" {
	name = "tveyes_kinesis_stream"
	shard_count = 1
	retention_period = 24

	shard_level_metrics = [
		"IncomingBytes",
		"OutgoingBytes",
		"IteratorAgeMilliseconds",
		"IncomingRecords",
		"ReadProvisionedThroughputExceeded",
		"WriteProvisionedThroughputExceeded",
		"OutgoingBytes"
	]

	tags = {
		Owner = var.owner_tag
		Budget = var.budget_tag
		Project = var.project_tag
		Email = var.email_tag
	}	
}

//
//resource "aws_kinesis_firehose_delivery_stream" "tveyes_delivery_stream" {
//  name = "tveyes-delivery-stream"
//  destination = "extended_s3"
//  depends_on = [aws_iam_role_policy_attachment.collect_tveyes_firehose_attachment]
//
//  kinesis_source_configuration {
//  	kinesis_stream_arn = aws_kinesis_stream.tveyes_kinesis_stream.arn
//		role_arn = aws_iam_role.tveyes_firehose_role.arn	
//  }
//
//  extended_s3_configuration {
//  	role_arn = aws_iam_role.tveyes_firehose_role.arn
// 		bucket_arn = aws_s3_bucket.xml_bucket.arn
//
//		buffer_size = 128
//		buffer_interval = 300
//
//		s3_backup_mode = "Enabled"
//
//		data_format_conversion_configuration {
//			input_format_configuration {
//				deserializer {
//					open_x_json_ser_de {}	
//				}	
//			}
//
//			output_format_configuration {
//				serializer {
//					parquet_ser_de {}
//				}
//			}
//
//			schema_configuration {
//				database_name = aws_glue_catalog_table.tveyes_glue_table.database_name
//				role_arn = aws_iam_role.tveyes_firehose_role.arn
//				table_name = aws_glue_catalog_table.tveyes	
//			}
//  	}
//
//		s3_backup_configuration {
//		
//			role_arn = aws_iam_role.tveyes_firehose_role.arn		
//			bucket_arn = aws_s3_bucket.tveyes_glacier.arn
//
//  	}
//
//		processing_configuation {
//			enabled = "true"
//
//			processors {
//				type = "Lambda"
//			
//				parameters {
//					parameter_name = "LambdaArn"
//					parameter_value = "${aws_lambda_function.tveyes_transform_lambda.arn}:$LATEST"
//				}
//				parameters {
//					parameter_name = "BufferSizeInMBs"
//					parameter_value = 3
//				}
//				parameters {
//					parameter_name = "BufferIntervalSeconds"
//					parameter_value = 60
//				}	
//			}	
//		}
//
//		cloudwatch_logging_options {
//			enabled = "true"
//			log_group_name = aws_cloudwatch_log_group.collect_tveyes_cw_group_name.name
//			log_stream_name = aws_cloudwatch_log_stream.collect_tveyes_firehouse_cw_stream.name	
//  	}
//	}
//	Tags = {
//		Owner = var.owner_tag
//		Budget = var.budget_tag
//		Project = var.project_tag
//		Email = var.email_tag	
//	}
//}

resource "aws_cloudwatch_log_group" "collect_tveyes_cw_group_name" {
	name = "/aws/lambda/collect-tveyes-firehose"
	retention_in_days = 14
	tags = {
		Owner = var.owner_tag
		Budget = var.budget_tag
		Project = var.project_tag
		Email = var.email_tag
	}
}

resource "aws_cloudwatch_log_stream" "collect_tveyes_firehose_cw_stream" {
	name = "collect-tveyes-firehose-cw-stream"
	log_group_name = aws_cloudwatch_log_group.collect_tveyes_cw_group_name.name
}

resource "aws_iam_role_policy_attachment" "collect_tveyes_firehose_attachment" {
	role = aws_iam_role.tveyes_firehose_role.name
	policy_arn = aws_iam_policy.tveyes_firehose_role_policy.arn
}

resource "aws_iam_role" "tveyes_firehose_role" {
	name = "collect-tveyes-firehose-role"

	assume_role_policy = <<EOF
{
	"Version": "2012-10-17",
	"Statement": [
		{
			"Action": "sts:AssumeRole",
			"Principal": {
				"Service": "firehose.amazonaws.com"
			},
			"Effect": "Allow",
			"Sid": ""
		}
	]
}
EOF
	tags = {
		Owner = var.owner_tag
		Project = var.project_tag
		Budget = var.budget_tag
		Email = var.email_tag
	}
}

//	{
//		"Sid": "",
//		"Effect": "Allow",
//		"Action": [
//			"lambda:InvokeFunction",
//			"lambda:GetFunctionConfiguration"
//		],
//		"Resource": "arn:aws:lambda:*:*:function:${aws_lambda_function.tveyes_transform_lambda.function_name}:$LATEST"
//	},
//
resource "aws_iam_policy" "tveyes_firehose_role_policy" {
	name = "collect-tveyes-firehose-role-policy"
	policy = <<EOF
{
	"Version": "2012-10-17",
	"Statement": [
		{
			"Sid": "",
			"Effect": "Allow",
			"Action": [
				"glue:GetTableVersions"
			],
			"Resource": "*"
		},
		{
			"Sid": "",
			"Effect": "Allow",
			"Action": [
				"s3:AbortMutipartUpload",
				"s3:GetBucketLocation",
				"s3:GetObject",
				"s3:ListBucket",
				"s3:ListBucketMultipartUploads",
				"s3:PutObject"
			],
			"Resource": [
				"arn:aws:s3:::${data.aws_s3_bucket.xml_bucket.id}",
				"arn:aws:s3:::${data.aws_s3_bucket.xml_bucket.id}/*"
			]
		},
		{
			"Sid": "",
			"Effect": "Allow",
			"Action": [
				"logs:PutLogEvents"
			],
			"Resource": [
				"arn:aws:logs:*:*:log-group:/aws/kinesisfirehose/*:log-stream:*"
			]
		},
		{
			"Sid": "",
			"Effect": "Allow",
			"Action": [
				"kinesis:DescribeStream",
				"kinesis: GetShardIterator",
				"kinesis: GetRecords"
			],
			"Resource": "arn:aws:kinesis:*:*:stream/${aws_kinesis_stream.tveyes_kinesis-stream.name}"
		}
	]
}
EOF
}

################################################################################################################
# ECS Stuff
#TODO: deployment of ecs tasks should be automated. push to master should trigger docker build, tag, and push. 
# also update of task definition and ecs service configuration to force deployment
resource "aws_ecs_cluster" "collect_tveyes_cluster" {
	name = "collect_tveyes_cluster"
	capacity_providers = [
		"FARGATE"]
	tags = {
		Owner = var.owner_tag
		Budget = var.budget_tag
		Project = var.project_tag
		Email = var.email_tag
	}
}

# TODO: Use terraform import so that subnet is not hardcoded
resource "aws_ecs_service" "collect_tveyes_service" {
	name = "collect-tyeyes"
	launch_type = "FARGATE"
	cluster = aws_ecs_cluster.collect_tveyes_cluster.id
	task_definition = aws_ecs_task_definition.collect_tveyes_task.arn
	desired_count = 1

	# iam_role        = aws_iam_role.ecs_service_role.arn
	network_configuration {
		subnets = [
			data.aws_subnet.tveyes_subnet.id]
		assign_public_ip = true
		security_groups = [aws_security_group.tveyes_security_group.id]	
	}

	tags = {
    	Owner = var.owner_tag
    	Budget = var.budget_tag
    	Project = var.project_tag
    	Email = var.email_tag
  	}
}

resource "aws_ecr_repository" "collect_tveyes_repo" {
	name = "collect_tveyes_repo"
	image_tag_mutability = "MUTABLE"

	tags = {
    	Owner = var.owner_tag
    	Budget = var.budget_tag
    	Project = var.project_tag
    	Email = var.email_tag
  	}

}

/*
resource "null_resource" "collect_tveyes_container" {
	provisioner "local-exec" {
		command = "./build_docker.bash ${aws_ecr_repository.collect_tveyes_repo.repository_url}"	
	}
}
*/

resource "aws_iam_role_policy_attachement" "ecs_service_role_attachment" {
	role = aws_iam_role.ecs_service_role.name
	policy_arn = aws_iam_policy.ecs_service_role_policy.arn
}

resource "aws_iam_role" "ecs_service_role" {
	name = "collect_tveyes_ecsServiceRole"

	assume_role_policy = <<EOF
{
	"Version": "2012-10-17",
	"Statement": [
		{
			"Action": "sts:AssumeRole",
			"Principal": {
				"Service": "ecs-tasks.amazonaws.com"
			},
			"Effect": "Allow"
			"Sid": ""
		}
	]
}
EOF

	tags = {
		Owner = var.owner_tag
		Budget = var.budget_tag
		Project = var.project_tag
		Email = var.email_tag
	}
}

#TODO: tighten this up and remove hardcoding as necessary
resource "aws_iam_policy" "ecs_service_role_policy" {
	name = "collect_tveyes_ecsServiceRolePolicy"

	policy = <<EOF
{
		"Version": "2012-10-17",
		"Statement": [
			{
				"Sid": "ECSTaskManagement",
				"Effect": "Allow",
				"Action": [
					"ec2:AttachNetworkInterface",
					"ec2:CreateNetworkInterface",
					"ec2:CreateNetworkInterfacePermission",
					"ec2:DeleteNetworkInterface",
					"ec2:DeleteNetworkInterfacePermission",
					"ec2:Describe*",
					"ec2:DetachNetworkInterface",
					"elasticloadbalancing:DeregisterInstancesFromLoadBalancer",
					"elasticloadbalancing:DeregisterTargets",
					"elasticloadbalancing:Describe*",
					"elasticloadbalancing:RegisterInstancesWithLoadBalancer",
					"elasticloadbalancing:RegisterTargets",
					"route53:ChangeResourceRecordSets",
					"route53:CreateHealthCheck",
					"route53:DeleteHealthCheck",
					"route53:Get*",
					"route53:List*",
					"route53:UpdateHealthCheck",
					"servicediscovery:DeregisterInstance",
					"servicediscovery:Get*",
					"servicediscovery:List*",
					"servicediscovery:RegisterInstance",
					"servicediscovery:UpdateInstanceCustomHealthStatus",
				],
				"Resource": "*"
			},
			{
				"Sid": "AutoScaling",
				"Effect": "Allow",
				"Action": [
					"autoscaling:Describe*"
				],
				"Resource": "*"
			},
			{
				"Sid": "AutoScalingManagement",
				"Effect": "Allow,
				"Action": [
					"autoscaling:DeletePolicy",
					"autoscaling:PutSecurityPolicy",
					"autoscaling:SetInstanceProtection",
					"autoscaling:UpdateAutoScalingGroup"
				],
				"Resource": "*",
				"Condition": {
					"Null": {
						"autoscaling:ResourceTag/AmazonECSManaged": "false"
					}
				}
			},
			{
				"Sid": "AutoScalingManagement",
				"Effect": "Allow",
				"Action": [
					"autoscaling:DeletePolicy",
					"autoscaling:PutScalingPolicy",
					"autoscaling:SetInstanceProtection",
					"autoscaling:UpdateAutoScalingGroup"
				],
				"Resource": "*",
				"Condition": {
					"Null": {
						"autoscaling:ResourceTag/AmazonECSManaged": "false"
					}
				}
			},
			{
				"Sid": "AutoScalingPlanManagement",
				"Effect": "Allow",
				"Action": [
					"autoscaling-plans:CreateScalingPlan",
					"autoscaling-plans:DeleteScalingPlan",
					"autoscaling-plans:DescribeScalingPlans"
				],
				"Resource": "*"
			},
			{
				"Sid": "CWAlarmManagement",
				"Effect": "Allow",
				"Action": [
					"cloudwatch:DeleteAlarms",
					"cloudwatch:DescribeAlarms",
					"cloudwatch:PutMetricAlarm"
				],
				"Resource": "arn:aws:cloudwatch:*:*:alarm:*"
			},
			{
				"Sid": "ECSTagging",
				"Effect": "Allow",
				"Action": [
					"ec2:CreateTags"
				],
				"Resource": "arn:aws:ec2:*:*:network-interface/*"
			},
			{
				"Sid": "",
				"Effect": "Allow",
				"Action": [
					"logs:*"
				],
				"Resource": "*"
			},
			{
				"Effect": "Allow",
				"Action": [
					"s3:PutObject",
					"s3:GetObject",
					"s3:PutObjectAcl"
				],
				"Resource": [
					"arn:aws:s3:::${data.aws_s3_bucket.xml_bucket.id}",
					"arn:aws:s3:::${data.aws_s3_bucket.xml_bucket.id}/*"
				]
			},
			{
				"Effect": "Allow",
				"Action": "s3:ListBucket",
				"Resource": [
					"arn:aws:s3:::${data.aws_s3_bucket.xml_bucket.id}",
					"arn:aws:s3:::${data.aws_s3_bucket.xml_bucket.id}/*"
				]
			},
			{
				"Effect": "Allow",
				"Action": "kinesis:PutRecord",
				"Resource": [
					"arn:aws:kinesis:us-east-1:088838630371:stream/tveyes_kinesis_stream"
				]
			}
		]
}
EOF
}

#Best practices to create role and policy separately and join with an attachment
resource "aws_iam_role_policy_attachment" "ecs_task_execution_role_attachment" {
	role = aws_iam_role.ecs_task_execution_role.name
	policy_arn = aws_iam_policy.ecs_task_execution_role_policy.arn
}

resource "aws_iam_role" "ecs_task_execution_role" {
	name = "collect_tveyes_ecsTaskExecutionRole"

	assume_role_policy = <<EOF
{
	"Version": "2012-10-17",
	"Statement": [
		"Action": "sts:AssumeRole",
		"Principal": {
			"Service": "ecs-tasks.amazonaws.com"
		},
		"Effect": "Allow",
		"Sid": ""
	]
}
EOF

	tags = {
		Owner = var.owner_tag
		Budget = var.budget_tag
		Project = var.project_tag
		Email = var.email_tag
	}
}

resource "aws_iam_policy" "ecs_task_execution_role_policy" {
	name = "collect_tveyes_ecsTaskExecutionRolePolicy"

	policy = <<EOF
{
	"Version": "2012-10-17",
	"Statement": [
		{
			"Sid": "",
			"Effect": "Allow",
			"Action": "kinesis:*",
			"Resource": [
				"arn:aws:kinesis:*:*:stream/*",
				"arn:aws:kinesis:*:*:*/*/consumer/*:*"
			]
		},
		{
			"Effect": "Allow",
			"Action": [
				"s3:PutObject",
				"s3:GetObject",
				"s3:PutObjectAcl"
			],
			"Resource": [
				"arn:aws:s3:::${data.aws_s3_bucket.xml_bucket.id}",
				"arn:aws:s3:::${data.aws_s3_bucket.xml_bucket.id}/*"
			]
		},
		{
			"Effect": "Allow",
			"Action": "s3:ListBucket",
			"Resource": [
				"arn:aws:s3:::${data.aws_s3_bucket.xml_bucket.id}",
                "arn:aws:s3:::${data.aws_s3_bucket.xml_bucket.id}/*"
			]
		},
		{
			"Effect": "Allow",
			"Action": [
				"ssm:GetParam*",
				"secretsmanager:GetSecretValue",
				"kms:Decrypt"
			],
			"Resource": [
				"arn:aws:ssm:us-east-1:088838630371:parameter/*",
				"arn:aws:secretsmanager:us-east-1:088838630371:*:*",
				"arn:aws:kms:us-east-1:088838630371:key/*"
			]
		},
		{
			"Effect": "Allow",
			"Action": [
				"logs:*"
			],
			"Resource": "*"
		}
	]
}
EOF
}

resource "aws_cloudwatch_log_group" "collect_tveyes_cw_group" {
	name = "/aws/ecs/tveyes-collection"
	retention_in_days = 14
	tags = {
		Owner = var.owner_tag
		Budget = var.budget_tag
		Project = var.project_tag
		Email = var.email_tag
	}
}

resource "aws_ecs_task_definition" "collect_tveyes_task" {
	family = "collect_tveyes_task"	
	requires_compatibilities = ["FARGATE"]
	network_mode = "awsvpc"
	cpu = 256
	memory1024
	task_role_arn = aws_iam_role.ecs_service_role.arn
	execution_role_arn = aws_iam_role.ecs_task_execution_role.arn
	container_definitions = file("collect_tveyes_containers.json")
	depends_on = [
		aws_ssm_parameter.tveyes_password,
		aws_ssm_parameter.tveyes_username,
		data.aws_s3_bucket.xml_bucket,
		aws_cloudwatch_log_group.collect_tveyes_cw_group
	]
	tags = {
		Owner = var.owner_tag
		Budget = var.budget_tag
		Project = var.project_tag
		Email = var.email_tag
	}
}
############################################################################################################
#Tveyes transform lambda
#TODO: tighten up policy
resource "aws_iam_policy" "tveyes_transform_role_policy" {
	name = "tveyes_transform_role_policy"
	policy = <<EOF
{
	"Version": "2012-10-17",
	"Statement": [
		{
			"Sid": "",
			"Effect": "Allow",
			"Action": "kinesis:*",
			"resource": [
				"arn:aws:kinesis:*:*:stream/*",
				"arn:aws:kinesis:*:*:*/*/consumer/*:*"
			]
		},
		{
			"Sid": "",
			"Effect": "Allow",
			"Action": "s3:*",
			"Resource": "*"
		},
		{
			"Effect": "Allow",
			"Action": [
				"logs:CreateLogGroup",
				"logs:CreateLogStream",
				"logs:PutLogEvents"
			],
			"Resource": "*"
		}
	]
}
EOF
}

resource "aws_iam_role" "tveyes_transform_role" {
	name = "tveyes_transform_role"

	assume_role_policy = <<EOF
{
	"Version": "2012-10-17",
	"Statement": [
		{
			"Action": "sts:AssumeRole",
			"Principal": {
				"Service": "lambda.amazonaws.com"
			},
			"Effect": "Allow",
			"Sid": ""
		}
	]
}
EOF
	tags = {
		Owner = var.owner_tag
		Budget = var.budget_tag
		Project = var.project_tag
		Email = var.email_tag
	}
}

/*
resource "null_resource" "tveyes_transform_zip" {
	provisioner "local-exec" {
		command = "zip -j tveyes_transform_payload.zip ../lib/tveyes_transform_lambda.py"
	}
}
*/

//resource "aws_lambda_function" "tveyes_transform_lambda" {
//	function_name = "tveyes_transform_lambda"
//	filename = "tveyes_transform_payload.zip"
//	role = aws_iam_role.tveyes_transform_role.arn
//	"tveyes_transform_lambda.lambda_handler"	
//
//	# The filebase64sha256() function is available in Terraform 0.11.12 and later
//	# For Terraform 0.11.11 and earlier, use the base64sha256() function and the file() function:
//	# source_code_hash = base64sha256(file("lambda_function_payload.zip"))
//	source_code_hash = filebase64sha256("tveyes_transform_payload.zip")
//	timeout = 60
//	runtime = "python3.6"
//
//	environment {
//		variable = {
//			topic_arn = aws_sns_topic.sns_to_slack_topic.arn
//		}
//	}
//
//
//	depends_on = [
//		aws_iam_role_policy_attachment.tveyes_transform_attachment,
//		#null_resource.tveyes_transform_zip
//	]
//
//	tags = {
//		Owner = var.owner_tag	
//		Budget = var_budget_tag
//		Project = var.project_tag
//		Email = var.email_tag
//	}
//}
//
//resource "aws_iam_role_policy_attachment" "tveyes_transform_attachment" {
//	role = aws_iam_role.tveyes_transform_role.name
//	policy_arn = aws_iam_policy.tveyes_transform_role_policy.arn	
//}

################################################################################################################
#Systems Manager Secure parameters
resource "aws_ssm_parameter" "tveyes_password" {
	name = "/tveyes/tveyes_password"
	type = "SecureString"
	value = var.tveyes_password

	tags = {
		Owner = var.owner_tag
		Budget = var.budget_tag
		Project = var.project_tag
		Email = var.email_tag
	}
}

resource "aws_ssm_parameter" "tveyes_username" {
	name = "/tveyes/tveyes_username"
	type = "SecureString"
	value = var.tveyes_username

	tags = {
		Owner = var.owner_tag
		Budget = var.budget_tag
		Project = var.project_tag
		Email = var.email_tag
	}
}

################################################################################################
# sns_to_slack_lambda
# takes any error messages from sns and reports them to slack
//resource "aws_iam_policy" "sns_to_slack_role_policy" {
//  name   = "sns_to_slack_role_policy"
//  policy = <<EOF
//{
//    "Version": "2012-10-17",
//    "Statement": [
//        {
//            "Effect": "Allow",
//            "Action": "logs:CreateLogGroup",
//            "Resource": "arn:aws:logs:*:*:*"
//        },
//        {
//            "Effect": "Allow",
//            "Action": [
//                "logs:CreateLogStream",
//                "logs:PutLogEvents"
//            ],
//            "Resource": [
//                "arn:aws:logs:*:*:log-group:/aws/lambda/sns_to_slack:*"
//            ]
//        }
//    ]
//}
//EOF
//}
//
//resource "aws_iam_role" "sns_to_slack_role" {
//  name = "sns_to_slack_role"
//
//  assume_role_policy = <<EOF
//{
//  "Version": "2012-10-17",
//  "Statement": [
//    {
//      "Action": "sts:AssumeRole",
//      "Principal": {
//        "Service": "lambda.amazonaws.com"
//      },
//      "Effect": "Allow",
//      "Sid": ""
//    }
//  ]
//}
//EOF
//  tags = {
//    Owner   = var.owner_tag
//    Budget  = var.budget_tag
//    Project = var.project_tag
//    Email   = var.email_tag
//  }
//}


//resource "aws_lambda_function" "sns_to_slack_lambda" {
//  function_name = "sns_to_slack"
//  filename      = "sns_to_slack_payload.zip"
//  role          = aws_iam_role.sns_to_slack_role.arn
//  handler       = "sns_to_slack_lambda.lambda_handler"
//  timeout       = 60
//
//  # The filebase64sha256() function is available in Terraform 0.11.12 and later
//  # For Terraform 0.11.11 and earlier, use the base64sha256() function and the file() function:
//  # source_code_hash = base64sha256(file("lambda_function_payload.zip"))
//  source_code_hash = filebase64sha256("sns_to_slack_payload.zip")
//
//  runtime = "python3.6"
//
//  #values are encrypted using default KMS key by default
//  #a more secure way might be use Secrets Manager and invoke it with boto3 from the lambda itself.
//  #that seems like overkill in this instance
//  environment {
//    variables = {
//      slackChannel = "#tveyes_collection"
//      hookurl = var.athena_overuse_hookurl
//    }
//  }
//
//  depends_on = [
//    aws_iam_role_policy_attachment.sns_to_slack_attachment
//  ]
//
//  tags = {
//    Owner   = var.owner_tag
//    Budget  = var.budget_tag
//    Project = var.project_tag
//    Email   = var.email_tag
//  }
//}

//resource "aws_iam_role_policy_attachment" "sns_to_slack_attachment" {
//  role       = aws_iam_role.sns_to_slack_role.name
//  policy_arn = aws_iam_policy.sns_to_slack_role_policy.arn
//}
//
//resource "aws_sns_topic" "sns_to_slack_topic" {
//  name = "sns_to_slack_topic"
//}
//
//resource "aws_sns_topic_subscription" "sns_to_slack_subscription" {
//  topic_arn = aws_sns_topic.sns_to_slack_topic.arn
//  protocol  = "lambda"
//  endpoint  = aws_lambda_function.sns_to_slack_lambda.arn
//}
//
//resource "aws_lambda_permission" "sns_to_slack_permission" {
//    statement_id = "AllowExecutionFromSNS"
//    action = "lambda:InvokeFunction"
//    function_name = aws_lambda_function.sns_to_slack_lambda.arn
//    principal = "sns.amazonaws.com"
//    source_arn = aws_sns_topic.sns_to_slack_topic.arn
//}


##############################################################################################


#tighten policies

