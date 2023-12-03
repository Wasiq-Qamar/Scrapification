from api.controllers.base import BaseController
from api.controllers.search import SearchController
from api.controllers.analyze import AnalyzeController

ROUTES = [
    {
        "name": "Base",
        "endpoints": ["/"],
        "resource": BaseController,
        "commands": ["GET"]
    },
    {
        "name": "Search",
        "endpoints": ["/search"],
        "resource": SearchController,
        "commands": ["GET"]
    },
    {
        "name": "Analyze",
        "endpoints": ["/analyze"],
        "resource": AnalyzeController,
        "commands": ["POST"]
    }
]