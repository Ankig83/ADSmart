import os
from datetime import datetime


def project(request):
    """
    Small set of globals available in all templates.
    Keep it minimal and stable for design/pixel-perfect work.
    """
    return {
        "PROJECT_NAME": os.getenv("PROJECT_NAME", "ADSmart"),
        "CURRENT_YEAR": datetime.now().year,
    }



