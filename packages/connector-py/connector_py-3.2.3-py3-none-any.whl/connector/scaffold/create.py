import os
import re
from argparse import Namespace
from pathlib import Path

TEMPLATE_DIR = Path(__file__).parent / "templates"


def snakecase(name: str) -> str:
    return name.lower().replace(" ", "_").replace("-", "_")


def hyphenate(name: str) -> str:
    return name.lower().replace(" ", "-").replace("_", "-")


def namecase(name: str) -> str:
    return name.replace("_", " ").replace("-", " ").title()


def pascalcase(name: str) -> str:
    parts = [part.title() for part in name.replace("_", "-").split("-")]
    return "".join(parts)


class ScaffoldError(Exception):
    pass


IGNORE_FILE_REGEX = re.compile("\\.pytest_cache|\\.pyc$")


def scaffold(args: Namespace):
    directory = args.directory
    name = args.name

    connector_dir = Path(directory)
    try:
        next(connector_dir.iterdir())
    except (StopIteration, FileNotFoundError):
        pass
    else:
        if not args.force_overwrite:
            raise FileExistsError(f"Directory {connector_dir} is not empty")
    connector_dir.mkdir(parents=True, exist_ok=True)

    author = input("Author: ")
    author_email = input("Author email: ")

    # Copy template files to the new connector directory
    output_paths = []
    try:
        for template_file in TEMPLATE_DIR.rglob("*"):
            if template_file.is_file() and not IGNORE_FILE_REGEX.search(str(template_file)):
                with template_file.open() as f:
                    try:
                        content = f.read()
                    except UnicodeDecodeError:
                        raise TypeError(f"Non-unicode file at {str(template_file)}") from None
                print(f"scaffolding:{template_file}")
                content = content.format(
                    author=author,
                    author_email=author_email,
                    name=snakecase(name),
                    title=namecase(name),
                    pascal=pascalcase(name),
                    hyphenated_name=hyphenate(name),
                )
                # Preserve the relative path of the template file
                relative_path = template_file.relative_to(TEMPLATE_DIR)
                output_path = connector_dir / relative_path
                output_path = Path(str(output_path).replace("connector_name_here", snakecase(name)))
                output_path.parent.mkdir(parents=True, exist_ok=True)
                if os.path.isfile(output_path) and not args.force_overwrite:
                    raise ScaffoldError(
                        f"Refusing to overwrite without --force-overwrite: {output_path}"
                    )
                output_paths.append(output_path)
                with output_path.open("w") as f:
                    f.write(content)
    except Exception as e:
        for output_path in output_paths:
            output_path.unlink()
        raise ScaffoldError(f"Failed to scaffold connector: {e}") from e
