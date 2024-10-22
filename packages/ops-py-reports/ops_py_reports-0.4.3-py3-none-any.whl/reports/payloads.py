#!/usr/bin/env python

import logging


########################################################################################################################


class SlackApp(object):
    def __init__(self, title, content, max_chars=2500):
        self.title = title
        self.content = content
        self.max_chars = max_chars

    def get_payloads(self):
        # Building payloads for Slack app
        logging.info("Building payload for Slack App..")
        payloads = [{"text": f"*{self.title}*\n```{self.content}```"}]

        # If the payload is too large for the Slack App it will be split into multiple posts
        if len(str(payloads)) > self.max_chars:
            logging.info("The message will be to large. Splitting up into chunks..")
            payloads = self.split_msg()

        logging.info(f"{len(payloads)} slack app payloads created. ")

        return payloads

    def split_msg(self):
        results = []

        cb = "```"

        # Then the report is split into chucks
        report_lines = self.content.splitlines()

        # The two first lines of the report is the header, which will be used in every part
        header = f"{cb}{report_lines.pop(0)}\n{report_lines.pop(0)}\n"

        # The first part of the first report payload / txt is initialized
        part = 1
        txt = ""
        payload = {"text": f"*{self.title} - Part {part}*\n{header}"}

        # Parse through every line of data in the report and add it to individual payloads / txt
        for line in report_lines:
            if len(txt) <= self.max_chars:
                txt += f"{line}\n"
                payload["text"] += f"{line}\n"
            else:
                # When a payload / txt have reacted it's max size it is added to the list of results
                payload["text"] += cb
                results.append(payload)

                # Then a new payload / txt is initialized
                part += 1
                txt = f"{line}\n"
                payload = {"text": f"*{self.title} - Part {part}*\n{header}{txt}"}

        # If a remaining payload / txt exists, then it will also be added to the list of payloads
        if txt:
            payload["text"] += cb
            results.append(payload)

        logging.info(f"Message was split into {len(results)} chunks.")

        return results
