import litellm
import os
# log raw request/response

if os.environ.get("LANGFUSE_PUBLIC_KEY") and os.environ.get("LANGFUSE_SECRET_KEY"):
    litellm.log_raw_request_response = True
    # set langfuse as a callback, litellm will send the data to langfuse
    litellm.success_callback = ["langfuse"]

# litellm.log_raw_request_response = True

# from https://cloud.langfuse.com/
# os.environ["LANGFUSE_PUBLIC_KEY"] = ""
# os.environ["LANGFUSE_SECRET_KEY"] = ""
# # Optional, defaults to https://cloud.langfuse.com
# os.environ["LANGFUSE_HOST"] # optional

# # LLM API Keys
# os.environ['OPENAI_API_KEY']=""
