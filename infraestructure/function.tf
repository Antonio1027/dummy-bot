data "archive_file" "bot_message_processor_code" {
    type = "zip"
    source_dir = "${path.module}/../src/"
    output_path = "${path.module}/../src/bot_message_processor.zip"
}

resource "aws_iam_role" "lambda_role" {
  name = "lambda-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
    {
      Action = "sts:AssumeRole",
      Effect = "Allow",
      Principal = {
        Service = "lambda.amazonaws.com"
      }
    }
  ]
})
}

resource "aws_iam_role_policy" "sm_policy" {
  name = "sm_access_permissions"
  role = aws_iam_role.lambda_role.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = [
          "secretsmanager:GetSecretValue",
          "secretsmanager:DescribeSecret",
        ]
        Effect   = "Allow"
        Resource = "*"
      },
    ]
  })
}

resource "aws_lambda_function" "bot_message_processor" {
    filename = data.archive_file.bot_message_processor_code.output_path
    function_name = "bot-message-processor"
    role = aws_iam_role.lambda_role.arn
    handler = "main.handler"
    runtime = "python3.9"
    depends_on = [ aws_iam_role_policy_attachment.lambda_exec_policy, aws_iam_role_policy.sm_policy]
    source_code_hash =  data.archive_file.bot_message_processor_code.output_base64sha256

}

resource "aws_iam_role_policy_attachment" "lambda_exec_policy" {
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
  role = aws_iam_role.lambda_role.name
}

resource "aws_lambda_permission" "apigateway_lambda" {
  statement_id = "AllowExecutionFromAPIGateway"
  action = "lambda:InvokeFunction"
  function_name = aws_lambda_function.bot_message_processor.function_name
  principal = "apigateway.amazonaws.com"
  source_arn = "${aws_api_gateway_rest_api.bot.execution_arn}/*/*/*"
}