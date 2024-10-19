import os
import fnmatch


def generate_markdown_listing(directories, file_types_to_be_listed, output_file_path="config.prompt_givens.md"):
    """
    Recursively walks through directories starting from each directory in 'directories',
    formats the files and directories in Markdown format using only files matching 'file_types_to_be_listed',
    and writes to a specified Markdown file in a specified path.
    This function now sorts files alphabetically within their respective directories.
    """
    markdown_lines = []
    # markdown_lines.append(f"### GIVENS")  # optional Adding prompt tag already in file listing
    for start_directory in directories:
        start_level = start_directory.count(os.sep)
        directory_name = os.path.basename(start_directory)
        markdown_lines.append(f"# {directory_name}")  # Adding root directory listing
        for root, dirs, files in os.walk(start_directory):
            level = root.count(os.sep) - start_level
            indent = '    ' * level
            dirs.sort(key=lambda x: x.lower())  # Sort directories alphabetically
            if level > 0:
                directory_name = os.path.basename(root)
                markdown_lines.append(f"{'#' * (level + 1)} {directory_name}")
            files.sort(key=lambda x: x.lower())  # Sort files alphabetically
            for file in sorted(files):
                if any(fnmatch.fnmatch(file, pattern) for pattern in file_types_to_be_listed):
                    markdown_lines.append(f"{indent} - [] {file}")

    with open(output_file_path, "w") as md_file:
        md_file.write('\n'.join(markdown_lines))

# Example usage
# generate_markdown_listing(['ara'], ['*.py'])
