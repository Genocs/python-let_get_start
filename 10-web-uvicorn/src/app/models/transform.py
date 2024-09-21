
from typing import Optional
from pydantic import BaseModel



class TransformRequest(BaseModel):
    """ Request model for the code transformation. 
    """
    domain: Optional[str] = "Microsoft"
    subdomain: Optional[str] = "msal"
    existing_language: Optional[str] = "python"
    desired_language: Optional[str] = "typescript-react"
