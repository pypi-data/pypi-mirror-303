#!/usr/bin/env python

import logging


def slack_workflow_report(msg_handler, posts=None):
    """Calls the provided Message Handler object to build Slack payloads for a Slack Workflow.
    The payloads are built from the provided list of Slack Post (Tuples: "Title" / "Text").

    The payloads are posted by the Message Handler.

    Parameters
    ----------
    msg_handler : __init__.py
        A message_handler object
    posts : list
        The list Tuples of Slack Workflow messages to post [(Title, Text)...]

    Returns
    -------
    True
        If response from one or more of the POSTs have return code 200
    """

    # Proceed with the list of Slack Workflow Post if provided. The success counter is initially set to 0
    if isinstance(posts, list):
        success_counter = 0
        for title_, text_ in posts:
            msg_handler.build_payload(Title=title_, Text=text_)
            msg_handler.post_payload()

            # If any of the payloads are sent it is considered a success
            response_code = msg_handler.get_response_code()
            if isinstance(response_code, int) and response_code == 200:
                success_counter += 1
            else:
                logging.error(f"Failed to send message to Slack Workflow. Response code {str(response_code)}.")

        # Return True if success so that we know at least one message have been sent
        if success_counter:
            logging.info(f"{success_counter} messages posted to the Slack Workflow.")
            return True
