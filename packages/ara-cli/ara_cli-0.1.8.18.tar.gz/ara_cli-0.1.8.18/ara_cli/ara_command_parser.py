import argparse
from ara_cli.classifier import Classifier
from ara_cli.commandline_completer import ArtefactCompleter, ParentNameCompleter
from ara_cli.template_manager import SpecificationBreakdownAspects


classifiers = Classifier.ordered_classifiers()
aspects = SpecificationBreakdownAspects.VALID_ASPECTS


def create_parser(subparsers):
    create_parser = subparsers.add_parser("create", help="Create a classified artefact with data directory")
    create_parser.add_argument("classifier", choices=classifiers, help="Classifier that also serves as file extension for the artefact file to be created. Valid Classifiers are: businessgoal, capability, keyfeature, feature, epic, userstory, example, task")
    create_parser.add_argument("parameter", help="Artefact name that serves as filename").completer = ArtefactCompleter()

    option_parser = create_parser.add_subparsers(dest="option")

    contribution_parser = option_parser.add_parser("contributes-to")
    contribution_parser.add_argument("parent_classifier", choices=classifiers, help="Classifier of the parent")
    contribution_parser.add_argument("parent_name",  help="Name of a parent artefact").completer = ParentNameCompleter()

    aspect_parser = option_parser.add_parser("aspect")
    aspect_parser.add_argument("aspect", choices=aspects, help="Adds additional specification breakdown aspects in data directory.")


def delete_parser(subparsers):
    delete_parser = subparsers.add_parser("delete", help="Delete an artefact file including its data directory")
    delete_parser.add_argument("classifier", choices=classifiers, help="Classifier of the artefact to be deleted")
    delete_parser.add_argument("parameter", help="Filename of artefact").completer = ArtefactCompleter()
    delete_parser.add_argument("-f", "--force", dest="force", action="store_true", help="ignore nonexistent files and arguments, never prompt")


def rename_parser(subparsers):
    rename_parser = subparsers.add_parser("rename", help="Rename a classified artefact and its data directory")
    rename_parser.add_argument("classifier", choices=classifiers, help="Classifier of the artefact")
    rename_parser.add_argument("parameter", help="Filename of artefact").completer = ArtefactCompleter()
    rename_parser.add_argument("aspect", help="New artefact name and new data directory name")


def list_parser(subparsers):
    list_parser = subparsers.add_parser("list", help="List files with optional tags")
    list_parser.add_argument("tags", nargs="*", help="Tags for listing files")


def get_tags_parser(subparsers):
    tags_parser = subparsers.add_parser("get-tags", help="Show tags")
    tags_parser.add_argument("--json", "-j", help="Output tags as JSON", action=argparse.BooleanOptionalAction)


def add_chat_arguments(chat_parser):
    chat_parser.add_argument("chat_name", help="Optional name for a specific chat. Pass the .md file to continue an existing chat", nargs='?', default=None)

    chat_parser.add_argument("-r", "--reset", dest="reset", action=argparse.BooleanOptionalAction, help="Reset the chat file if it exists")
    chat_parser.set_defaults(reset=None)

    chat_parser.add_argument("--out", dest="output_mode", action="store_true", help="Output the contents of the chat file instead of entering interactive chat mode")

    chat_parser.add_argument("--append", nargs='*', default=None, help="Append strings to the chat file")

    chat_parser.add_argument("--restricted", dest="restricted", action=argparse.BooleanOptionalAction, help="Start with a limited set of commands")


def prompt_parser(subparsers):
    prompt_parser = subparsers.add_parser("prompt", help="Base command for prompt interaction mode")

    steps = ['init', 'load', 'send', 'load-and-send', 'extract', 'update', 'chat', 'init-rag']
    steps_parser = prompt_parser.add_subparsers(dest='steps')
    for step in steps:
        step_parser = steps_parser.add_parser(step)
        step_parser.add_argument("classifier", choices=classifiers, help="Classifier of the artefact")
        step_parser.add_argument("parameter", help="Name of artefact data directory for prompt creation and interaction").completer = ArtefactCompleter()
        if step == 'chat':
            add_chat_arguments(step_parser)


def chat_parser(subparsers):
    chat_parser = subparsers.add_parser("chat", help="Command line chatbot. Chat control with SEND/s | RERUN/r | QUIT/q")
    add_chat_arguments(chat_parser)


def template_parser(subparsers):
    template_parser = subparsers.add_parser("template", help="Outputs a classified ara template in the terminal")
    template_parser.add_argument("classifier", choices=classifiers, help="Classifier of the artefact type")


def fetch_templates_parser(subparsers):
    subparsers.add_parser("fetch-templates", help="Fetches templates and stores them in .araconfig")


def action_parser():
    parser = argparse.ArgumentParser(description="Ara tools for creating files and directories.")

    subparsers = parser.add_subparsers(dest="action", help="Action to perform")
    create_parser(subparsers)
    delete_parser(subparsers)
    rename_parser(subparsers)
    list_parser(subparsers)
    get_tags_parser(subparsers)
    prompt_parser(subparsers)
    chat_parser(subparsers)
    template_parser(subparsers)
    fetch_templates_parser(subparsers)

    return parser
