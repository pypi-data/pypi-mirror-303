import base64
import gzip
import os
import json

from rich import print
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.progress import Progress
from rich.prompt import Prompt
from rich.table import Table
console = Console()
    
OUTPUT_FORMAT = 'text'
    
def set_output_format(format):
    global OUTPUT_FORMAT
    OUTPUT_FORMAT = format
    
def lumeo_logo():
    encoded_data = "H4sIACZdkGMCA8WUMQ7AIAhFd07hURkcHBicPKAnaUxqqy1qVbTNnxr8L5APSt2fd1pEkBmaZYqgxRgG6Z3dRQySg2KiZjFF7iArTRYOMbD0EvPAVihlf+JmSkz11YSd8W6PkqkYIFRCQl2EEHd+t/hpY8FpIkVaPc+TEfW/QScrJurLVvxwAtRGJEFzeaW7S3gCyky5e5H8gFelnZhYZzMAB0lpiLmGBwAA"
    decoded_data = base64.b64decode(encoded_data)
    decompressed_data = gzip.decompress(decoded_data)
    return decompressed_data.decode('utf-8')
    
def print_header(text, title=None, subtitle=None):
    if title:
        console.print(Panel(text, title=title, subtitle=subtitle, style="cyan"))
    else:
        console.print(Panel(text, style="cyan"))
    
def print_text(text):
    console.print(text)

def output_message(message, status, title=''):
    if OUTPUT_FORMAT == 'json':
        output = {'status': status, 'message': message}
        print_text(json.dumps(output))
    else:
        print_text(title)
        print_text(message)        

def output_data(headers, rows, title):
    if OUTPUT_FORMAT == 'json':
        # Convert headers and rows into a list of dictionaries
        output = {'status': 'success', 'data': []}
        headers_fixed = [header.replace(" ", "_").lower() for header in headers]
        for row in rows:
            output['data'].append(dict(zip(headers_fixed, row)))
        print(json.dumps(output))
    else:
        table = generate_table(headers, rows, title)
        console.print(table)
        
def generate_table(headers, rows, title):
    table = Table(title=title, style="cyan")
    for header in headers:
        table.add_column(header, style="cyan", no_wrap=True)
    for row in rows:
        table.add_row(*row)
    return table

def prompt_yes_no(msg, default_value):
    """Prompt for yes/no input with a default value."""
    while True:
        if os.environ.get('NO_PROMPT'):
            console.print(f"{msg} (using default: {default_value})")
            return default_value.lower() == 'y'
        
        response = input(f"{msg} [y/n] (default: {default_value}): ").lower()
        if response in ['y', 'n']:
            return response == 'y'
        elif response == '':
            return default_value.lower() == 'y'
        else:
            print("Please enter 'y' for Yes, 'n' for No, or press Enter for the default value.")


def prompt_input(msg):
    """Prompt for input with a default value."""
    return Prompt.ask(msg)
