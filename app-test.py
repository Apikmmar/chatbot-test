# Import required libraries
from flask import Flask, render_template, request, jsonify  # Flask web framework components
import boto3  # AWS SDK for Python
import json  # For JSON handling
import time  # For sleep/wait functionality
from botocore.exceptions import ClientError  # AWS client exceptions

# Initialize Flask application
app = Flask(__name__)

# Bedrock client setup
bedrock = boto3.client(
    service_name='bedrock-runtime',  # AWS Bedrock service
    region_name='ap-southeast-1'  # Singapore region
)

# Retry logic for handling API throttling
def invoke_model(payload):
    """
    Invokes the Bedrock model with retry logic for throttling errors.
    
    Args:
        payload: The input data for the model
        
    Returns:
        The model response
        
    Raises:
        Exception: If max retries are reached
    """
    max_retries = 5  # Maximum number of retry attempts
    
    for i in range(max_retries):
        try:
            # Attempt to invoke the model
            response = bedrock.invoke_model(
                modelId="anthropic.claude-3-5-sonnet-20240620-v1:0",  # Claude 3.5 Sonnet model
                body=json.dumps(payload),  # Convert payload to JSON string
                contentType="application/json",  # Request content type
                accept="application/json"  # Expected response format
            )
            return response
        except ClientError as e:
            # Handle throttling errors specifically
            if e.response['Error']['Code'] == 'ThrottlingException':
                wait_time = 2 ** i  # Exponential backoff (1, 2, 4, 8, 16 seconds)
                print(f"Throttled. Retrying in {wait_time} seconds...")
                time.sleep(wait_time)
            else:
                # Re-raise other types of errors
                raise e
    # If we get here, all retries failed
    raise Exception("Max retries reached")

# Claude 3.5 prompt wrapper with AWS-specific instructions
def ask_sonnet(prompt):
    """
    Processes a user prompt through Claude 3.5 with AWS-specific instructions.
    
    Args:
        prompt: The user's question/input
        
    Returns:
        tuple: (response_text, input_tokens, output_tokens)
    """
    # System instruction to constrain responses to AWS topics
    instruction = (
        "You are an assistant that only answers questions related to Amazon Web Services (AWS). "
        "If the question is not related to AWS, politely decline to answer."
    )

    # Construct the request body for Bedrock
    body = {
        "anthropic_version": "bedrock-2023-05-31",  # API version
        "messages": [
            {
                "role": "user",  # User role for the message
                "content": f"{instruction}\n\n{prompt}"  # Combined instruction and user prompt
            }
        ],
        "max_tokens": 1000  # Limit response length
    }

    # Invoke the model with our payload
    response = invoke_model(body)

    # Parse the response
    result = json.loads(response['body'].read())  # Read and parse the response body
    reply = result["content"][0]["text"]  # Extract the generated text

    # Get token usage (default to 0 if not provided)
    usage = result.get("usage", {"input_tokens": 0, "output_tokens": 0})
    return reply.strip(), usage["input_tokens"], usage["output_tokens"]

# Flask routes
@app.route("/")
def index():
    """Serve the main chat interface"""
    return render_template("index.html")  # Render the HTML template

@app.route("/ask", methods=["POST"])
def ask():
    """Handle chat requests from the frontend"""
    try:
        # Get the user message from the request
        user_message = request.json.get("message", "")
        
        # Get response from Claude
        reply, tokens_in, tokens_out = ask_sonnet(user_message)
        
        # Return the response as JSON
        return jsonify({
            "reply": reply,  # The generated response
            "tokens_in": tokens_in,  # Input token count
            "tokens_out": tokens_out  # Output token count
        })
    except Exception as e:
        # Return error response if something goes wrong
        return jsonify({
            "reply": f"Error: {str(e)}",  # Error message
            "tokens_in": 0,  # Zero tokens on error
            "tokens_out": 0
        }), 500  # HTTP 500 status code for server error

# Main entry point
if __name__ == "__main__":
    app.run(debug=True)  # Run in debug mode for development