from fastapi import APIRouter, Depends
from app.core.security import get_current_user
from app.db.prisma import db

router = APIRouter(prefix="/transactions", tags=["transactions"])

@router.post("/")
async def create_transaction(amount: float, user=Depends(get_current_user)):
    tx = await db.transaction.create(
        data={
            "amount": amount,
            "userId": user.id
        }
    )

    await db.riskassessment.create(
        data={
            "transactionId": tx.id,
            "userId": user.id,
            "riskLevel": "normal"
        }
    )

    return tx
