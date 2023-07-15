import motor.motor_asyncio
from pymongo.collection import Collection
from models.visitor import Visitor
from models.dream import Dream

from config.config import settings

client = motor.motor_asyncio.AsyncIOMotorClient(
    f'mongodb+srv://{settings.MONGODB_ADMIN}:{settings.MONGODB_PASSWORD}@asa-cerita-wanita.fdzvpvm.mongodb.net/?retryWrites=true&w=majority')
db = client['asa-cerita-wanita']
collection_visitor: Collection[Visitor] = db['visitor']
collection_dream: Collection[Dream] = db['dream']