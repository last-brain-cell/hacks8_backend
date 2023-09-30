from fastapi import Body, APIRouter, HTTPException

from models.disaster import DisasterReport, DisasterReportData, DisasterReportVerify

router = APIRouter()


@router.post("/report", response_model=DisasterReport)
async def create_disaster_report(disaster_report: DisasterReport = Body(...)):
    return await disaster_report.create()

@router.post("/verify_disaster", response_model=DisasterReport)
async def verify_disaster(disaster: DisasterReportVerify = Body(...)):
    disaster_exists = await DisasterReport.find_one(DisasterReport.disaster_id == disaster.disaster_id)
    if disaster_exists:
        disaster_exists.verified = True
        await disaster_exists.save()
    else:
        HTTPException(
            status_code=404, detail="Disaster doesn't exist"
        )
    return disaster_exists
