import logging
import os
import sys
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand
from django.template.base import Lexer, TokenType

from snart.models import Constant

logger = logging.getLogger(Path(__file__).name)


def yes_no_input(question, default="yes"):
    """Ask a yes/no question via input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
            It must be "yes" (the default), "no" or None (meaning
            an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True, "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        try:
            choice = input().lower()
        except KeyboardInterrupt:
            sys.stdout.write("\nExit...\n")
            sys.exit()
            return None
        if default is not None and choice == "":
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' " "(or 'y' or 'n').\n")


class Command(BaseCommand):
    help = "Collect all texts from snart tags across templates and register them in the DB."

    def handle(self, *args, **options):
        """
        Orchestrates the process of scanning all templates, discovering 'snart' tags,
        and logging the found texts or variables.
        """
        found_keys = set()
        template_dirs = settings.TEMPLATES[0].get("DIRS", [])

        for template_dir in template_dirs:
            found_keys.update(self.scan_template_dir(template_dir))

        db_keys = Constant.objects.values_list("key", flat=True)

        if found_keys:
            new_keys = set()

            for key in sorted(found_keys):
                checkbox = "[x]"
                if key not in db_keys:
                    key = self.format_db_key(key)
                    new_keys.add(key)
                    checkbox = checkbox.replace("x", " ")
                sys.stdout.write(f"{checkbox} {key}\n")

            if new_keys and yes_no_input(f"\nRegister new keys ({len(new_keys)})?", default="no"):
                self.create_db_records(new_keys)

    def format_db_key(self, key):
        return str(key).lower().strip()

    def create_db_records(self, keys):
        for key in keys:
            try:
                Constant.objects.get_or_create(key=key)
                logger.warning(f"New key registered: '{key}'")
            except Exception as e:
                logger.error(f"Can't register key '{key}' because of reasons: {e}")

    def scan_template_dir(self, template_dir):
        """
        Scans all HTML template files within a given directory for 'snart' tags.
        Uses a generator to process each file in a memory-efficient way.
        """
        for root, _, files in os.walk(template_dir):
            for filename in filter(lambda f: f.endswith(".html"), files):
                template_path = os.path.join(root, filename)
                logger.debug(f"Scanning template: {template_path}")
                yield from self.process_template_file(template_path)

    def process_template_file(self, template_path):
        """
        Reads and processes a template file, yielding 'snart' tag texts or variables.
        """
        with open(template_path, "r", encoding="utf-8") as template_file:
            lexer = Lexer(template_file.read())
            tokens = lexer.tokenize()

            for token in filter(lambda t: t.token_type == TokenType.BLOCK, tokens):
                yield from self.extract_snart_texts(token)

    def extract_snart_texts(self, token):
        """
        Extracts the first argument (text or variable) from a 'snart' block token.
        Yields parsed text if it's a 'snart' tag.
        """
        token_contents = token.split_contents()

        if token_contents[0] == "snart" and len(token_contents) > 1:
            first_argument = token_contents[1]
            yield self.parse_argument(first_argument)

    def parse_argument(self, arg):
        """
        Parses the argument of the 'snart' tag. If it's quoted, strips the quotes.
        Otherwise, treats it as a variable name and returns it as-is.
        """
        if (arg.startswith('"') and arg.endswith('"')) or (arg.startswith("'") and arg.endswith("'")):
            return arg[1:-1]  # Remove quotes
        return arg  # Return variable as-is
