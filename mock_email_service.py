"""DEPRECATED: mock_email_service removed.

This project no longer uses the mock email service. The file remains as a placeholder
to avoid import errors in older branches. Do not use.
"""


def deprecated_placeholder(*args, **kwargs):
    raise RuntimeError("mock_email_service is removed. Email logging is disabled.")


log_email_to_file = deprecated_placeholder
get_sent_emails = lambda: []
get_email_for_user = lambda email: None
clear_email_log = lambda: None
