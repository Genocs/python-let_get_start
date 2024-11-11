# routes/main.py

from fastapi import APIRouter, HTTPException

from app.models.transform import TransformRequest, TransformResponse


# Create a new FastAPI router
router = APIRouter()


@router.post("/transform", response_model=TransformResponse)
async def transform_code(req: TransformRequest):
    """
    Summary:
    Transform the code using the selected transformer.
    Description:
    Transform the code using the selected transformer.
    Parameters:
    - req: TransformRequest: The request object containing the code and transformer.
    Returns:
    - TransformResponse: The response object containing the transformed code.
    """
    try:
        return await {"code": req.code, "transformer": req.transformer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
