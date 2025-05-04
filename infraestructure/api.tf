resource "aws_api_gateway_rest_api" "bot" {
    name = "bot"
    description = "bot api"

    endpoint_configuration {
      types = ["REGIONAL"]
    }
}

resource "aws_api_gateway_resource" "root" {
    rest_api_id = aws_api_gateway_rest_api.bot.id
    parent_id = aws_api_gateway_rest_api.bot.root_resource_id
    path_part = "commercial-assistant"
}

resource "aws_api_gateway_method" "proxy" {
  rest_api_id = aws_api_gateway_rest_api.bot.id
  resource_id = aws_api_gateway_resource.root.id
  http_method = "POST"
  authorization = "NONE"
}

resource "aws_api_gateway_integration" "lambda_integration" {
  rest_api_id = aws_api_gateway_rest_api.bot.id
  resource_id = aws_api_gateway_resource.root.id
  http_method = aws_api_gateway_method.proxy.http_method
  integration_http_method = "POST"
  type = "AWS"
  uri = aws_lambda_function.bot_message_processor.invoke_arn
}

resource "aws_api_gateway_method_response" "proxy" {
  rest_api_id = aws_api_gateway_rest_api.bot.id
  resource_id = aws_api_gateway_resource.root.id
  http_method = aws_api_gateway_method.proxy.http_method
  status_code = "200"
}

resource "aws_api_gateway_integration_response" "proxy" {
  rest_api_id = aws_api_gateway_rest_api.bot.id
  resource_id = aws_api_gateway_resource.root.id
  http_method = aws_api_gateway_method.proxy.http_method
  status_code = aws_api_gateway_method_response.proxy.status_code

  depends_on = [
    aws_api_gateway_method.proxy,
    aws_api_gateway_integration.lambda_integration
  ]
}

resource "aws_api_gateway_deployment" "deployment" {
  rest_api_id = aws_api_gateway_rest_api.bot.id
  lifecycle {
    create_before_destroy = true
  }
  depends_on = [
    aws_api_gateway_integration.lambda_integration
  ]
}

resource "aws_api_gateway_stage" "dev" {
  deployment_id = aws_api_gateway_deployment.deployment.id
  rest_api_id = aws_api_gateway_rest_api.bot.id
  stage_name = "dev"
}
