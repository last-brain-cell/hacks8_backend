from fastapi import Body, APIRouter

from models.disaster import DisasterReportData, DisasterReportCreate

router = APIRouter()


@router.post("/report", response_model=DisasterReportData)
async def create_disaster_report(disaster_report: DisasterReportCreate = Body(...)):
    return disaster_report
