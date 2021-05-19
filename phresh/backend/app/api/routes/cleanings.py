import logging

from typing import List

from fastapi import APIRouter, Body, Depends, HTTPException, Path
from starlette.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND

from app.models.cleaning import CleaningCreate, CleaningPublic, CleaningInDB, CleaningUpdate
from app.db.repositories.cleanings import CleaningsRepository  
from app.api.dependencies.database import get_repository  

from fastapi import APIRouter

logger = logging.getLogger(__name__)
router = APIRouter()

# @router.get("/", name="cleanings: Sample GET")
# async def get_all_cleanings() -> List[dict]:
#     cleanings = [
#         {"id": 1, "name": "My house", "cleaning_type": "full_clean", "price_per_hour": 29.99},
#         {"id": 2, "name": "Someone else's house", "cleaning_type": "spot_clean", "price_per_hour": 19.99}
#     ]
#     return cleanings

@router.get("/", response_model=List[CleaningPublic], name="cleanings:get-all-cleanings")
async def get_all_cleanings(
    cleanings_repo: CleaningsRepository = Depends(get_repository(CleaningsRepository))
) -> List[CleaningPublic]:
    return await cleanings_repo.get_all_cleanings()

@router.get("/{id}/", response_model=CleaningPublic, name="cleanings:get-cleaning-by-id")
async def get_cleaning_by_id(
  id: int, cleanings_repo: CleaningsRepository = Depends(get_repository(CleaningsRepository))
) -> CleaningPublic:
    cleaning = await cleanings_repo.get_cleaning_by_id(id=id)
    if not cleaning:
        logger.warning("Unable to retrieve cleaning id=%s", id)
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="No cleaning found with id={id}.")
    return cleaning

@router.post("/", response_model=CleaningPublic, name="cleanings:create-cleaning", status_code=HTTP_201_CREATED)
async def create_new_cleaning(
    new_cleaning: CleaningCreate = Body(..., embed=True),
    cleanings_repo: CleaningsRepository = Depends(get_repository(CleaningsRepository)),
) -> CleaningPublic:
    """ Expect a CleaningCreate model validation """
    created_cleaning = await cleanings_repo.create_cleaning(new_cleaning=new_cleaning)
    return created_cleaning

@router.put("/{id}/", response_model=CleaningPublic, name="cleanings:update-cleaning-by-id")
async def update_cleaning_by_id(
    id: int = Path(..., ge=1, title="The ID of the cleaning to update"),
    cleaning_update: CleaningUpdate = Body(..., embed=True),
    cleanings_repo: CleaningsRepository = Depends(get_repository(CleaningsRepository))
) -> CleaningPublic:
    updated_cleaning = await cleanings_repo.update_cleaning(id=id, cleaning_update=cleaning_update)
    
    if not updated_cleaning:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="No cleaning found with id={id}")
    return updated_cleaning

@router.delete("/{id}/", response_model=int, name="cleanings:delete-cleaning-by-id")
async def delete_cleaning_by_id(
    id: int = Path(..., ge=1, title="The ID of the cleaning to delete."),
    cleanings_repo: CleaningsRepository = Depends(get_repository(CleaningsRepository)),
) -> int:
    deleted_id = await cleanings_repo.delete_cleaning_by_id(id=id)
    if not deleted_id:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="No cleaning found with that id.")
    return deleted_id