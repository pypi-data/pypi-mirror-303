from cs_ai_common.logging.internal_logger import InternalLogger
from fastapi import HTTPException, Request, status
from fastapi.responses import JSONResponse
from pydantic import ValidationError



async def catch_exceptions_middleware(request: Request, call_next):
    try:
        return await call_next(request)
    except ValueError as e:
        InternalLogger.LogError(f"ValueError: {str(e)}")
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST, content={"message": str(e)}
        )
    except ValidationError as e:
        InternalLogger.LogError(f"ValidationError: {str(e)}")
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST, content={"message": str(e)}
        )
    except HTTPException as e:
        InternalLogger.LogError(f"HTTPException: {e.status_code} - {e.detail}")
        return JSONResponse(status_code=e.status_code, content={"message": e.detail})
    except Exception as e:
        InternalLogger.LogError(f"Exception: {str(e)}")
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"message": str(e)},
        )