from app.db.prisma import db

async def connect_db():
    await db.connect()

async def disconnect_db():
    await db.disconnect()
