from fastapi import Body, APIRouter, HTTPException

from models.disaster import DisasterReport, DisasterReportData, DisasterReportCreate, DisasterReportVerify

router = APIRouter()


@router.post("/report", response_model=DisasterReportData)
async def create_disaster_report(disaster_report: DisasterReport = Body(...)):
    try:
        return await disaster_report.create()
    except:
        raise HTTPException(status_code=401, detail="Unexpected Error")


@router.post("/verify_report", response_model=DisasterReportData)
async def verify_disaster(disaster: DisasterReportVerify = Body(...)):
    disaster_exists = await DisasterReport.find_one(DisasterReport.disaster_id == disaster.disaster_id)
    if disaster_exists:
        disaster_exists.verified = True
    else:
        HTTPException(
            status_code=404, detail="Disaster doesn't exist"
        )
