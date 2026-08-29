"""System diagnostics and telemetry helper for NexaAI."""
import os
import platform
import sys
import time
from datetime import datetime
from pathlib import Path

START_TIME = time.time()

def get_system_diagnostics():
    uptime_seconds = int(time.time() - START_TIME)
    modules_path = Path(__file__).resolve().parent / "modules"
    module_count = len(list(modules_path.glob("*.py"))) if modules_path.exists() else 0

    return {
        "status": "healthy",
        "service": "NexaAI API Platform",
        "version": "1.2.0",
        "uptime_seconds": uptime_seconds,
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "environment": {
            "python_version": sys.version.split()[0],
            "os_platform": platform.platform(),
            "processor": platform.processor() or "Generic x86_64 / ARM",
            "active_domain_modules": module_count,
        },
        "resources": {
            "pid": os.getpid(),
            "telemetry_enabled": True
        }
    }
