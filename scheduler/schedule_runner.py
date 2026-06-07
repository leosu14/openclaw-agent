from apscheduler.schedulers.blocking import BlockingScheduler
from agents.autonomous_teacher import (
run_daily_teacher_agent
)
scheduler = BlockingScheduler()

scheduler.add_job(
    run_daily_teacher_agent,
    'cron',
    hour=10,
    minute=0
)
print(" Spanish Teacher Agent Running...")
scheduler.start()