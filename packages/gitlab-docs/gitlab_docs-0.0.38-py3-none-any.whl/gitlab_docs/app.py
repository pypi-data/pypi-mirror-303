"""
Gitlab-Docs entrypoint to auto generate gitlab-ci documentation from yml configuration files
Author: Charlie Smith
"""

## Import Thirdparty Libraries
import logging
import os

# from datetime import datetime
# from datetime import timedelta
# from distutils.util import strtobool
# import time
import gitlab_docs.includes as includes
import gitlab_docs.jobs as jobs
import gitlab_docs.reset_docs as md_writer
import gitlab_docs.variables as variables
import gitlab_docs.workflows as workflows

# flake8: noqa: E501
# Logging Setup
LOG_LEVEL = os.getenv("LOG_LEVEL", "DEBUG").upper()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("GITLAB DOCS")
logger.setLevel(LOG_LEVEL)


def main():
    print("Welcome to Gitlab Docs")
    # resets markdown output file and adds GITLAB DOCS opening marker
    OUTPUT_FILE = os.getenv("OUTPUT_FILE", "GITLAB-DOCS.md")
    GLDOCS_CONFIG_FILE = os.getenv("GLDOCS_CONFIG_FILE", ".gitlab-ci.yml")

    md_writer.gitlab_docs_reset_writer(OUTPUT_FILE=OUTPUT_FILE, MODE="STARTING")
    variables.document_variables(GLDOCS_CONFIG_FILE=GLDOCS_CONFIG_FILE, WRITE_MODE="a",DISABLE_TITLE=True)
    includes.document_includes(GLDOCS_CONFIG_FILE=GLDOCS_CONFIG_FILE, WRITE_MODE="w",DISABLE_TITLE=True, DISABLE_TYPE_HEADING=True)
    workflows.document_workflows(GLDOCS_CONFIG_FILE=GLDOCS_CONFIG_FILE, WRITE_MODE="a",DISABLE_TITLE=True)
    jobs.get_jobs(GLDOCS_CONFIG_FILE=GLDOCS_CONFIG_FILE, WRITE_MODE="a", DISABLE_TITLE=True, DISABLE_TYPE_HEADING=False)

    # resets markdown output file and adds GITLAB DOCS closing marker
    md_writer.gitlab_docs_reset_writer(OUTPUT_FILE=OUTPUT_FILE, MODE="CLOSING")
