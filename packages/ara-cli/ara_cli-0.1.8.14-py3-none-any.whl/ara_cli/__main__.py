# PYTHON_ARGCOMPLETE_OK
from ara_cli.ara_command_parser import action_parser
from ara_cli.version import __version__
from ara_cli.ara_command_action import create_action, delete_action, rename_action, list_action, get_tags_action, prompt_action, chat_action, template_action, fetch_templates_action
import argcomplete
import sys


def define_action_mapping():
    return {
        "create": create_action,
        "delete": delete_action,
        "rename": rename_action,
        "list": list_action,
        "get-tags": get_tags_action,
        "prompt": prompt_action,
        "chat": chat_action,
        "template": template_action,
        "fetch-templates": fetch_templates_action
    }


def handle_invalid_action(args):
    sys.exit("Invalid action provided. Type ara -h for help")


def cli():
    parser = action_parser()
    parser.add_argument('-v', '--version', action='version', version=f'%(prog)s {__version__}')

    action_mapping = define_action_mapping()

    argcomplete.autocomplete(parser)

    args = parser.parse_args()
    if not hasattr(args, 'action') or not args.action:
        parser.print_help()
        return
    action = action_mapping.get(args.action, handle_invalid_action)
    action(args)


if __name__ == "__main__":
    cli()
