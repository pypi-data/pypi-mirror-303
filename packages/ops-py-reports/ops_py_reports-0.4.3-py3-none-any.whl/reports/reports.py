#!/usr/bin/env python

from bs4 import BeautifulSoup


########################################################################################################################


class SlackMessages(object):

    def __init__(self, config=None):
        if not config:
            self.config = {
                "ok": {
                    "emoji": ":white_check_mark:",
                    "txt": "OK"
                },
                "warning": {
                    "emoji": ":warning:",
                    "txt": "WARNING"
            },
                "critical": {
                    "emoji": ":bangbang:",
                    "txt": "CRITICAL!"

                },
                "expired": {
                    "emoji": ":rotating_light:",
                    "txt": "EXPIRED!!"
                },
                "error": {
                    "emoji": ":no_entry:",
                    "txt": "ERROR"
                },
                "unknown": {
                    "emoji": ":question:",
                    "txt": "UNKNOWN"
                }
            }

    def get_ssl_report(self, rows, title="SSL certificates report", skip_ok=True):
        out = ""
        if title:
            out += f"*{title}*\n"
        for row in rows:
            status = str(row.get("status")).lower()
            if skip_ok and status == "ok":
                continue

            emoji = ""
            txt = ""
            name = row.get("name", "?")
            comment = row.get("comment")
            expire_date = row.get("expire_date")
            if expire_date and not str(expire_date) == "-":
                comment += f" ({expire_date})"

            config = self.config.get(status)
            if config:
                emoji = config.get("emoji")
                txt = config.get("txt")

            if not txt:
                txt = str(status).upper()

            out += f"*{emoji} {txt}* - *{name}* - {comment.capitalize()}\n"

        return out


class HTMLTable(object):
    """Creates a html table based on provides list of header elements and row elements.

    Attributes
    ----------
    table_header : list
        A list of header elements - the heading of each column.
    html_table : str
        The html table

    Methods
    -------
    init_html_table(table_header)
        Generates the first part of the table - the header
    add_html_row(*args)
        Add each provides arguments as column items and finally appends the complete row to the table.
    get_table(*args)
        Finalize and returns the table.
    """

    def __init__(self, table_header, skip_ok=True, styles=None, text=None):
        """
        Parameters
        ----------
        table_header : list
            A list of header elements - the heading of each column.
        """

        self.table_header = table_header
        self.skip_ok = skip_ok
        self.html_rows = ""
        if not styles:
            self.styles = {
                "grey": " style='background-color: Grey; color: White; font-weight:bold'",
                "purple": " style='background-color: Purple; color: White; font-weight:bold'",
                "yellow": " style='background-color: Yellow; color: Black; font-weight:bold'",
                "red": " style='background-color: Red; color: White; font-weight:bold'",
                "green": " style='background-color: Green; color: White; font-weight:bold'"
            }
        if not text:
            self.text = {
                "disabled": "grey",
                "unknown": "grey",
                "warning": "yellow",
                "critical": "red",
                "ok": "green",
                "error": "red",
                "expired": "red"
            }

    def init_html_table(self):
        """generates a html table to be used in json output for MS Teams"""

        self.html_table = f"""<table bordercolor='black' border='2'>
    <thead>
    <tr style='background-color: Teal; color: White'>
"""
        for h in self.table_header:
            self.html_table += f"        <th>{h}</th>\n"

        self.html_table += """
    </tr>
    </thead>
    <tbody>
    """

    def get_style(self, arg):
        for k, v in self.text.items():
            if str(arg).lower() == str(k).lower():
                return self.styles.get(v)
        return ""

    def add_html_row(self, *args):
        """adds the table rows to the html table

        expected row elements:
            record_name, record_type, vault_name, updated, expires, comment

        Parameters
        ----------
        args : str
            The items which will be added to the current row.
        """

        if not self.html_table:
            return

        skip = False
        html_row = ""
        style = ""
        for arg in args:
            if self.skip_ok and str(arg).lower() == "ok":
                skip = True

            if not style:
                style = self.get_style(arg)
            arg = str(arg).replace(". ", "<br>").replace(" (", "<br>(")
            html_row += f"<td{style}>{arg}</td>"
            style = ""

        if not skip:
            self.html_rows += f"<tr>{html_row}</tr>"

    def get_table(self):
        """adding closing html tags and remove plural in days when it should not be used

        Returns
        -------
        html_table : str
            The finalized table.
        """

        if self.html_rows:
            self.html_table += self.html_rows
            self.html_table += "</tbody></table>"
            html_table = self.html_table.replace(" 1 days", " 1 day").replace("\n", "")
            return BeautifulSoup(html_table, 'html.parser').prettify()
        return ""


class Markdown(object):
    """Creates a plain text Markdown table from a list (rows) of lists (columns). The header is the first list in the list.

    Attributes
    ----------
    rows : list
        The list of rows to make out the table
    widths : dict
        A dict to store the column widths while parsing the columns for each row.

    Methods
    -------
    set_widths()
        Parses through the values of each column, in each row, in order to set the width of each column.
        Each column will have to be at least the size of the longest value in each column + an additional spacing.
    get_output(*args)
        Parses through each column in each row and adds the Markdown table char, the space and then the value.
        When the header row is done, the Markdown hyphen seperator row which separates the header and rows is added.
        The final result is returned
    """

    def __init__(self, rows):
        """
        Parameters
        ----------
        rows : list
            The list of rows to make ut the table.
        """
        self.rows = rows
        self.widths = {}

    def set_widths(self):
        """Parses through the values of each column, in each row, in order to set the width of each column."""

        for row in self.rows:
            for i, col in enumerate(row):
                cur_w = self.widths.get(i, 0)
                new_w = len(str(col).rstrip()) + 2
                if cur_w < new_w:
                    self.widths[i] = new_w

    def get_output(self, *args):
        """Parses through each column in each row and adds the Markdown table char, the space and then the value.

        Returns
        -------
        output : str
            The finalized table.

        """
        output = ""
        header_line = ""
        for n, row in enumerate(self.rows):
            for i, col in enumerate(row):
                value = f" {str(col).rstrip()} "

                if n == 0:
                    l = "-" * self.widths[i]
                    header_line += f"|{l: <{self.widths[i]}}"

                if n > 0 and i in args:
                    output += f"|{value: >{self.widths[i]}}"
                else:
                    output += f"|{value: <{self.widths[i]}}"

            output += "|\n"

            if header_line:
                output += f"{header_line}|\n"
                header_line = ""

        return output


########################################################################################################################


def dict_to_rows(rows):
    header = []
    result = []
    for row in rows:
        if not header:
            for k in row.keys():
                header.append(k)
            result.append(header)
        current_row = []
        for v in row.values():
            current_row.append(v)
        result.append(current_row)

    return result


def dict_to_csv(rows):
    out = ''
    for row in rows:
        if not out:
            for k in row.keys():
                out += f'"{k}",'
            out = out.rstrip(',')
            out += '\n'
        for v in row.values():
            out += f'"{v}",'
        out = out.rstrip(',')
        out += '\n'
    return out

