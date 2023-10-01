from fastapi import Body, APIRouter, HTTPException

from models.disaster import (
    DisasterReport,
    DisasterReportVerify,
)

router = APIRouter()


@router.post("/report", response_model=DisasterReport)
async def create_disaster_report(disaster_report: DisasterReport = Body(...)):
    print(disaster_report)
    return await disaster_report.create()


@router.post("/update_status", response_model=DisasterReport)
async def update_disaster_status(disaster: DisasterReportVerify = Body(...)):
    print(disaster)
    disaster_exists = await DisasterReport.find_one(
        DisasterReport.disaster_id == disaster.disaster_id
    )
    if disaster_exists:
        disaster_exists.status = disaster.status
        await disaster_exists.save()
    else:
        HTTPException(status_code=404, detail="Disaster doesn't exist")
    return disaster_exists


@router.post("/display_disasters")
async def display_disasters():
    disasters = await DisasterReport.find(DisasterReport.status > 0).to_list()
    return disasters
