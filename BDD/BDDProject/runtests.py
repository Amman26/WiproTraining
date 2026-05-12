import os
import shutil
from datetime import datetime

from utils.logger import LogGen
logger = LogGen.loggen()

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
logger.info("========================================")
logger.info("AUTOMATION EXECUTION STARTED")

# Clean Old Allure Results (Raw JSON data)
if os.path.exists("reports/allure-results"):
    logger.info("Deleting old allure-results folder")
    shutil.rmtree("reports/allure-results")

# Clean Old Allure Report (The finished HTML site)
if os.path.exists("reports/allure-report"):
    logger.info("Deleting old allure-report folder")
    shutil.rmtree("reports/allure-report")

# Recreate the directory
os.makedirs("reports/allure-results", exist_ok=True)

# Execute Behave Tests (Simplified!)
logger.info("Starting Behave Test Execution")
behave_status = os.system("behave")
logger.info(f"Behave Execution Completed with status code : {behave_status}")

# Generate Allure HTML Report
logger.info("Generating Allure HTML Report")
allure_generate_status = os.system(
    "allure generate reports/allure-results -o reports/allure-report --clean"
)
logger.info(f"Allure Report Generated with status code : {allure_generate_status}")
logger.info("AUTOMATION EXECUTION COMPLETED")
logger.info("========================================")