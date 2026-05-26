# ==========================================
# IMPORT REQUEST OBJECT
# ==========================================

from fastapi import Request


# ==========================================
# CUSTOM LOGGING MIDDLEWARE
# ==========================================

async def log_requests(request: Request, call_next):

    # Print request method
    #
    # Example:
    # GET
    # POST
    print(f"Method: {request.method}")

    # Print request URL path
    #
    # Example:
    # /tasks
    # /login
    print(f"Path: {request.url.path}")


    # IMPORTANT:
    # call_next(request)
    #
    # sends request to actual route
    response = await call_next(request)


    # Print response status code
    #
    # Example:
    # 200
    # 404
    # 401
    print(f"Status Code: {response.status_code}")

    print("===================================")

    # Return response back to client
    return response