from fastapi import Body, APIRouter, HTTPException
from models.event import DisasterReport, DisasterReportData, DisasterReportCreate

router = APIRouter()


@router.post("/report", response_model=DisasterReportData)
async def createDisasterReport(disaster_report: DisasterReportCreate = Body(...)):
    return disaster_report
