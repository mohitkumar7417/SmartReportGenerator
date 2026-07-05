from apscheduler.schedulers.blocking import BlockingScheduler
from report_generator import generate_report
from pdf_generator import generate_pdf

def run_reports():
    file_path = "data/sales.csv"

    print("\n[Scheduler] Running Reports...")

    generate_report(file_path)
    generate_pdf(file_path)

    print("[Scheduler] Reports Generated Successfully!\n")


scheduler = BlockingScheduler()

# Run every 1 minute (for testing)
scheduler.add_job(run_reports, 'interval', seconds=30)

print("Scheduler Started... Reports will run every 1 minute")

scheduler.start()