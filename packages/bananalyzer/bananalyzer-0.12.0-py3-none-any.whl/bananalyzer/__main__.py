# Separate banana-lyzer args from pytest args
# Look for an instance of Banana-lyzer in the current directory
# If it doesn't exist, error
import argparse
import ast
import importlib.util
import os
import sys
from pathlib import Path
from typing import List
from urllib.parse import urlparse

from bananalyzer import AgentRunner
from bananalyzer.data.example_fetching import (
    download_examples,
    get_examples_path,
    get_test_examples,
    get_training_examples,
)
from bananalyzer.data.example_s3 import download_har, download_mhtml
from bananalyzer.runner.generator import PytestTestGenerator
from bananalyzer.runner.runner import run_tests
from bananalyzer.schema import AgentRunnerClass, Args, PytestArgs, XDistArgs


def print_intro() -> None:
    # https://www.asciiart.eu/food-and-drinks/bananas
    print(
        r"""
//\
V  \
 \  \_
  \,'.`-.
   |\ `. `.
   ( \  `. `-.                        _,.-:\
    \ \   `.  `-._             __..--' ,-';/
     \ `.   `-.   `-..___..---'   _.--' ,'/
      `. `.    `-._        __..--'    ,' /
        `. `-_     ``--..''       _.-' ,'
          `-_ `-.___        __,--'   ,'
             `-.__  `----'''    __.-'
                  `--..____..--'
"""
    )

    print("Bananalyzing... 🍌")


def parse_args() -> Args:
    file_name = "bananalyzer-agent.py"
    parser = argparse.ArgumentParser(
        description="Run the agent inside a bananalyzer agent definition file "
        "against the benchmark",
    )
    parser.add_argument(
        "path", type=str, nargs="?", default=None, help=f"Path to the {file_name} file"
    )
    parser.add_argument(
        "--headless", action="store_true", help="Whether to run headless or not"
    )
    parser.add_argument(
        "-s",
        "--s",
        action="store_true",
        help="Shortcut for --capture=no in pytest. Will print stdout and stderr",
    )
    parser.add_argument(
        "-id",
        "--id",
        type=lambda s: s.replace("_", "-").split(","),
        default=None,
        help="Filter tests by id. "
        "Ids could be of shape a4c8292a_079c_4e49_bca1_cf7c9da205ec or a4c8292a-079c-4e49-bca1-cf7c9da205ec, "
        "and can be passed as a comma-separated list.",
    )
    parser.add_argument(
        "-tags",
        "--tags",
        type=lambda s: s.split(","),
        default=None,
        help="Filter tests by tag. Can be passed as a comma-separated list.",
    )
    parser.add_argument(
        "-skip_tags",
        "--skip_tags",
        type=lambda s: s.split(","),
        default=None,
        help="Tags to avoid selecting. Can be passed as a comma-separated list.",
    )
    parser.add_argument(
        "-d",
        "--domain",
        type=str,
        default=None,
        help="Filter tests by a particular URL domain",
    )
    parser.add_argument(
        "-i",
        "--intent",
        type=str,
        default=None,
        help="Filter tests by a particular intent",
    )
    parser.add_argument(
        "-c",
        "--category",
        type=str,
        default=None,
        help="Filter tests by a particular category",
    )
    parser.add_argument(
        "--subcategory",
        type=str,
        default=None,
        help="Filter tests by a particular subcategory",
    )
    parser.add_argument(
        "-n",
        "--n",
        type=str,
        default="logical",
        help="Number of test workers to use. The default is 1",
    )
    parser.add_argument(
        "-skip",
        "--skip",
        type=lambda s: s.split(","),
        default=[],
        help="A list of ids to skip tests on, separated by commas",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Will increase the verbosity of pytest.",
    )
    parser.add_argument(
        "--single_browser_instance",
        action="store_true",
        help="Run tests in a single browser instance as opposed to creating a browser "
        "instance per test. This is faster but less reliable as test contexts can "
        "occasionally bleed into each other, causing tests to fail",
    )
    parser.add_argument(
        "--type",
        type=str,
        default=None,
        help="Filter tests by a particular type",
    )
    parser.add_argument(
        "--source_type",
        type=str,
        default=None,
        help="Filter tests by a particular source type (e.g. mhtml, hosted, har)",
    )
    parser.add_argument(
        "--download",
        action="store_true",
        help="Will re-download training and test examples",
    )
    parser.add_argument(
        "--examples_bucket",
        type=str,
        default=None,
        help="Download examples from the specified public S3 bucket",
    )
    parser.add_argument(
        "--test",
        action="store_true",
        help="Use test set examples instead of training set examples",
    )
    parser.add_argument(
        "--count",
        type=int,
        default=None,
        help="The number of times to run an individual test. Won't work for detail pages",
    )
    parser.add_argument(
        "--junitxml",
        type=str,
        default=None,
        help="The path for the junitxml report file",
    )
    parser.add_argument(
        "--dist",
        type=str,
        default="loadscope",
        help="The distribution mode for pytest-xdist",
    )

    args = parser.parse_args()
    if args.download and not args.path:
        args.path = "DOWNLOAD_ONLY"

    if not args.path:
        print(
            f"Please provide the path to a {file_name} file. "
            f"Use the --help flag for more information."
        )
        exit(1)

    return Args(
        path=args.path,
        headless=args.headless,
        intent=args.intent,
        id=args.id,
        domain=args.domain,
        category=args.category,
        subcategory=args.subcategory,
        skip=args.skip,
        single_browser_instance=args.single_browser_instance,
        type=args.type,
        source_type=args.source_type,
        test=args.test,
        download=args.download,
        examples_bucket=args.examples_bucket,
        count=args.count,
        pytest_args=PytestArgs(
            s=args.s,
            v=args.verbose,
            xml=args.junitxml,
        ),
        xdist_args=XDistArgs(
            n=args.n,
            dist=args.dist,
        ),
        tags=args.tags,
        skip_tags=args.skip_tags,
    )


def find_agents(file_path: Path) -> List[AgentRunnerClass]:
    with open(file_path, "r") as source:
        node = ast.parse(source.read())

    runners: List[AgentRunnerClass] = []
    for clazz in [n for n in node.body if isinstance(n, ast.ClassDef)]:
        if "AgentRunner" in [getattr(base, "id", "") for base in clazz.bases]:
            runners.append(
                AgentRunnerClass(
                    class_name=clazz.name,
                    class_path=str(file_path),
                )
            )

    return runners


def load_agent_from_path(path: Path) -> AgentRunnerClass:
    if path.is_dir():
        files = [p for p in path.glob("**/*.py") if "venv" not in p.parts]
    else:
        files = [path]

    runners: List[AgentRunnerClass] = []
    for file in files:
        runners.extend(find_agents(file))

    if len(runners) == 0:
        raise RuntimeError(f"Could not find any agent runners in {path}")

    if len(runners) > 1:
        raise RuntimeError(f"Found multiple agent runners in {path}")

    runner = runners[0]
    runner_file = Path(runner.class_path)
    module_name = path.stem

    spec = importlib.util.spec_from_file_location(module_name, runner_file)
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load module from path {runner_file}")

    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)

    agent = getattr(module, runner.class_name)()
    if not isinstance(agent, AgentRunner):
        raise TypeError("User defined agent is is not an instance of AgentRunner")

    return runner


def main() -> int:
    """
    Load the agent from the provided path and run it against the benchmark

    Note that pytest creates a new global context when running tests.
    Because of this, we first load the agent and validate that it is of the correct type here.
    Then we pass the path to the agent runner and let it load it within the pytest context.
    Note your AgentRunner must be concurrency safe.
    """
    print_intro()

    # Load the agent
    args = parse_args()
    if args.download:
        print("##################################################")
        print("# Downloading examples, this may take a while... #")
        print("##################################################")
        download_examples(examples_bucket=args.examples_bucket)

        if args.path == "DOWNLOAD_ONLY":
            return 0

    agent = load_agent_from_path(Path(args.path))
    print(f"Loaded agent {agent.class_name} from {agent.class_name}")

    # Filter examples based on args
    examples = get_test_examples() if args.test else get_training_examples()

    filters = []
    if args.id:
        filters.append(lambda e: e.id in args.id if args.id else True)
    if args.tags:
        filters.append(lambda e: all(tag in e.tags for tag in args.tags or []))
    if args.skip_tags:
        filters.append(lambda e: not any(tag in e.tags for tag in args.skip_tags or []))
    if args.intent:
        filters.append(lambda e: e.type == args.intent)
    if args.type:
        filters.append(lambda e: e.type == args.type)
    if args.source_type:
        filters.append(lambda e: e.source.lower() == args.source_type.lower())  # type: ignore
    if args.domain:
        filters.append(
            lambda e: ".".join(urlparse(e.url).hostname.split(".")[-2:]) == args.domain
        )
    if args.category:
        filters.append(lambda e: e.category == args.category)
    if args.skip:
        filters.append(lambda e: e.id not in args.skip)
    if args.subcategory:
        filters.append(lambda e: e.subcategory == args.subcategory)

    # Test we actually have tests to run
    examples = [e for e in examples if all(f(e) for f in filters)]
    if len(examples) == 0:
        print()
        print("=======================================================================")
        print("🍌 No tests to run. Please ensure your filter parameters are correct 🍌")
        print("=======================================================================")
        return 0

    examples_path = get_examples_path()
    for example in examples:
        if example.resource_path is None:
            continue

        if example.source == "mhtml":
            mhtml_path = examples_path / example.id / "index.mhtml"
            if not mhtml_path.exists():
                mhtml_str = download_mhtml(example.resource_path)
                mhtml_path.parent.mkdir(parents=True, exist_ok=True)
                with open(mhtml_path, "w") as file:
                    file.write(mhtml_str)
        elif example.source == "har":
            parts = example.resource_path.split("/")
            if example.resource_path.startswith(
                "s3://"
            ) and example.resource_path.endswith(".tar.gz"):
                har_subpath = parts[-1].split(".")[0] + "/index.har"
                har_path = examples_path / har_subpath
                if not os.path.exists(har_path):
                    har_dir_path = os.path.dirname(har_path)
                    download_har(har_dir_path, example.resource_path)
            elif example.resource_path.endswith("/index.har"):
                har_subpath = "/".join(parts[-2:])
                har_path = examples_path / har_subpath
                if not os.path.exists(har_path):
                    raise ValueError(
                        f"Could not find HAR file at {har_path}. Please run `bananalyze --download` to download all example files. No S3 path is provided for this example."
                    )
            else:
                raise ValueError(
                    f"Could not find HAR resource at {example.resource_path}. Please ensure the example provides either the path to an index.har in a local bananalyzer examples subdirectory, or an S3 URL to a tar.gz of a HAR directory."
                )

    # Cap the number of workers to the number of examples
    if isinstance(args.xdist_args.n, int):
        count = max(args.count or 1, 1)
        multiplied_count = len(examples) * count
        args.xdist_args.n = min(multiplied_count, args.xdist_args.n)

    # Load the desired tests
    generator = PytestTestGenerator()
    tests = [generator.generate_test(e) for e in examples]

    if args.count:
        for i in range(args.count - 1):
            for e in examples:
                copy = e.model_copy()
                copy.id = f"{copy.id}_{i + 2}"
                tests.append(generator.generate_test(copy))

    # Run the tests and return the exit code
    return run_tests(
        tests,
        agent,
        args.pytest_args,
        args.xdist_args,
        args.headless,
        args.single_browser_instance,
    )


if __name__ == "__main__":
    exit(main())
