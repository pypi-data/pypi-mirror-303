#!/usr/bin/env python3
from argparse import ArgumentParser, RawDescriptionHelpFormatter
import sys
import logging
import yaml
import re

from asteval import Interpreter
from rich.console import Console
from rich import print as rprint


# Set logging to timestamped entries to stderr
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')



class TColr:
    def __init__(self, arguments):
        self.config = None
        self.args = self.__class__.defaults()
        self.args.update(arguments)
        numeric_level = getattr(logging, self.args['log_level'].upper(), None)
        logging.basicConfig(stream=sys.stderr, level=numeric_level)
        logging.getLogger().setLevel(numeric_level)

    @classmethod
    def defaults(cls):
        default_keys = {
            'log_level': 'error',
            'config': 'config.yaml',
        }
        return default_keys



    @classmethod
    def setup_args(cls, arguments):
        parser = ArgumentParser(
            formatter_class=RawDescriptionHelpFormatter,
            exit_on_error=False,
            description='''

Color the tabular output based on the given config file


'''
        )
        defaults = cls.defaults()
        parser.set_defaults(**(cls.defaults()))
        parser.add_argument('--log-level', help="Logging level", default=defaults['log_level'])
        parser.add_argument('--input', '-i', help="Input file")
        parser.add_argument('--config', '-c', help="Config file", default=defaults['config'])
        _args = vars(parser.parse_args(arguments))
        return _args

    @staticmethod
    def to_ansi(text, style):
        tmp_console = Console(file=None, highlight=False, color_system='standard')
        with tmp_console.capture() as capture:
            tmp_console.print(text, style=style, soft_wrap=True, end='')
        retval = capture.get()
        return retval

    @staticmethod
    def generate_columns(header):
        columns = []
        for col in re.findall(r'(\S+\s+)', header):
            columns.append({'name': col.strip(), 'length': len(col)})
        match = re.search(r'(\S+)$', header)
        if match:
            columns.append({'name': match.group(1), 'length': 9999 })
        logging.debug(columns)
        return columns

    @staticmethod
    def generate_values_from_columns(line, columns):
        values = {}
        for col in columns:
            values[col['name']] = line[:col['length']]
            line = line[col['length']:]
        return values

    @staticmethod
    def is_match(value, match):
        # compare based on regex match
        match = re.match(match, value)
        if match:
            return match
        return False

    def apply_color_rules(self, values, user_vars=None):
        if user_vars is None:
            user_vars = dict()
        for rule in self.config.get('rules', []):
            column = rule['column']
            match = rule['match']
            color = rule['color']
            when = rule.get('when', None)
            logging.info(f'Testing color rule: {rule} to {values[column]}')
            if column not in values:
                continue
            if when:
                aeval = Interpreter()
                aeval.symtable.update(user_vars)
                result = aeval(when)
                if not result:
                    logging.debug('when condition failed')
                    continue
            if self.is_match(values[column], match):
                logging.info(f'Applying color rule: {rule} to {values[column]}')
                values[column] = self.to_ansi(values[column], color)
        return values


    @staticmethod
    def print_header(columns):
        line = ''
        for col in columns:
            if col['length'] == 9999:
                line += col['name']
            else:
                line += col['name'].ljust(col['length'])
        logging.debug('[O] ' + line)
        print(line.strip())

    @staticmethod
    def print_line(values, columns):
        line = ''
        for col in columns:
            if col['length'] == 9999:
                line += values[col['name']]
            else:
                line += values[col['name']].ljust(col['length'])
        logging.debug('[O] ' + line)
        print(line.strip())

    def generate_user_vars(self, values):
        user_vars = {}
        for rule in self.config.get('variables', []):
            name = rule['name']
            column = rule['column']
            match = rule['match']
            logging.info(f'Generating variable: {rule} to {values[column]}')
            if column in values:
                match = self.is_match(values[column], match)
                logging.info(f'Generating variable: {rule} to {match}')
                if match:
                    logging.info(f'Matched: {name} to {values[column]}')
                    user_vars[name] = match.group(1)
        return user_vars


    def process_line(self, line, columns, outcolumns):
        logging.debug('[I] ' + line)

        values = self.generate_values_from_columns(line, columns)
        logging.debug(values)
        user_vars = self.generate_user_vars(values)
        logging.debug(f'Generated user variables: {user_vars}')
        colored_values = self.apply_color_rules(values, user_vars)
        logging.debug(colored_values)
        self.print_line(colored_values, outcolumns)

    def generate_output_columns(self, columns):
        config = self.config.get('columns', None)
        if config is None:
            return columns
        retval = []
        for i in config:
            found = list(filter(lambda x: x['name'] == i, columns))
            if not found:
                raise RuntimeError(f'Column {i} not found - referenced in config')
            if len(found) > 1:
                raise RuntimeError(f'Multiple matches found for column {i}')
            retval += found
        logging.info(f"Found  {retval}")
        return retval

    def process_stream(self, stream):
        # read first line from stream for processing into headers
        header = stream.readline().strip()
        columns = self.generate_columns(header)
        outcolumns = self.generate_output_columns(columns)
        logging.debug('[H] ' + header)
        self.print_header(outcolumns)
        for line in stream:
            self.process_line(line, columns, outcolumns)

    def run(self, overrides=None):
        if overrides:
            self.args.update(overrides)
        # open the config file
        with open(self.args['config'], 'r') as f:
            self.config = yaml.safe_load(f)
        logging.debug(self.config)

        # Read from input file or stdin
        if self.args['input']:
            with open(self.args['input'], 'r') as f:
                self.process_stream(f)
        else:
            self.process_stream(sys.stdin)


def main(sys_args=None):
    try:
        if sys_args is None:
            sys_args = sys.argv
        args = TColr.setup_args(sys_args[1:])
        cli = TColr(args)
        return cli.run()
    except RuntimeError as e:
        logging.error(str(e))
        return 1
    except SystemExit as ex:
        logging.error(str(ex))
        return 3
    except Exception as e:
        # Unexpected error - show full stack trace
        logging.exception(str(e))
        return 2


if __name__ == '__main__':
    sys.exit(main())
