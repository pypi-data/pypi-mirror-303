from __future__ import annotations

from dataclasses import dataclass
from functools import cached_property
from pathlib import Path
from typing import Sequence

from loam.base import ConfigBase, Section
from loam.cli import CLIManager, Subcmd
from loam.collections import MaybeEntry, TupleEntry
from loam.tools import command_flag, path_entry

from .cmake_builder import BuildOutcome, CmakeBuilder
from .dirs import TestsOutputDirectory
from .pipeline import (
    CompareStage,
    PipelineByTest,
    PipelineStage,
    PrepStage,
    RunStage,
    SelfCheckStage,
)
from .repo import (
    TestRepository,
    TestRepositoryBase,
    TestsMatchingPatterns,
    TestsWithAllTags,
    TestsWithAnyTag,
)
from .source_tree import GitRepository, MusicSourceTree, NoOpRepository, Repository
from .term import (
    TERMCOLOR_GREEN,
    LogFile,
    Message,
    StrMsg,
    TeeTerm,
    Term,
    TermBase,
    err_msg,
    info_msg,
    warn_msg,
)
from .utils import Timer


@dataclass
class TestSelection(Section):
    """Test selection options."""

    repo: Path = path_entry(path="tests", doc="Path to the tests repository")
    names: Sequence[str] = TupleEntry(str).entry(
        cli_short="n",
        doc=(
            "Comma separated list of test names to run, see `--list` for a list of tests. "
            "Supports shell-like glob patters, e.g. '2dim/vortex*'. "
            "Defaults to all available tests."
        ),
    )
    tags_all: Sequence[str] = TupleEntry(str).entry(
        cli_short="t",
        doc=(
            "Restrict selection to tests with ALL of these tags; use '~tag' to negate tag."
            " See `--list` for tests and their tags."
        ),
    )
    tags_any: Sequence[str] = TupleEntry(str).entry(
        cli_short="T",
        doc="Restrict selection to tests with ANY of these tags.",
    )


@dataclass
class BaseDirectory(Section):
    """Base directory options."""

    output: Path = path_entry(
        path="tests_out", cli_short="o", doc="Path to the tests output base directory"
    )
    music: Path = path_entry(path=Path(), doc="Path to the MUSIC source tree")
    build: Path | None = MaybeEntry(Path).entry(
        cli_short="B",
        doc="External build tree to reuse",
    )
    ref: Path = path_entry(
        path="tests_out.ref",
        cli_short="r",
        doc="Tests output directory to use for comparison, if exists",
    )


@dataclass
class Behaviour(Section):
    """Behaviour control."""

    keep: bool = command_flag(
        shortname="k",
        doc="Do not delete tests output base directory before running",
    )
    no_git: bool = command_flag(
        doc="Disable calls to git; don't store VCS information in the test directory",
    )


@dataclass
class CommandHooks(Section):
    """Hooks for some specific commands."""

    mpi_exec: Sequence[str] = TupleEntry(str).entry(
        default=("mpirun", "-np", "{ntasks}"),
        doc="How to execute MPI processes, supports `{ntasks}` placeholder",
    )
    with_music_self_tests: bool = command_flag(
        doc="Run MUSIC self tests on top of regular tests (time consuming!)",
    )


@dataclass
class Logging(Section):
    """Logging and display control."""

    write_log: Path | None = MaybeEntry(Path).entry(
        cli_short="w",
        doc="Also write test system output to the given file; obeys `--ascii` flag",
    )
    verbose: bool = command_flag(
        shortname="v",
        doc="Show output of code execution on standard output",
    )
    no_color: bool = command_flag(
        shortname="C",
        doc="Disable colored output on terminal",
    )
    ascii: bool = command_flag(
        shortname="a",
        doc="Only use ASCII characters in test system outputs",
    )


@dataclass
class Config(ConfigBase):
    selection: TestSelection
    dirs: BaseDirectory
    behaviour: Behaviour
    command_hooks: CommandHooks
    io: Logging


CONFIG_FILE = Path("music_test.toml")


@dataclass
class Commands:
    conf: Config
    sub_cmd: str

    def __post_init__(self) -> None:
        # Check that --output is not a parent of --repo or --music,
        # or we may run into trouble.
        output_path = self.conf.dirs.output.resolve()
        for path in [self.conf.selection.repo, self.conf.dirs.music]:
            if output_path in path.resolve().parents:
                raise ValueError(
                    f"output directory '{self.conf.dirs.output}' is a parent path of '{path}'"
                )

    @staticmethod
    def from_cmd_args() -> Commands:
        conf = Config.default_()
        if CONFIG_FILE.is_file():
            conf.update_from_file_(CONFIG_FILE)
        climan = CLIManager(
            config_=conf,
            config=Subcmd("Create configuration file."),
            run=Subcmd(
                "Automate compilation, execution and validation of MUSIC tests problems.",
                "selection",
                "dirs",
                "behaviour",
                "command_hooks",
                "io",
            ),
            build=Subcmd(
                "Build test targets.",
                "selection",
                "dirs",
                "behaviour",
                "io",
            ),
            prepare=Subcmd(
                "Prepare test run directories.",
                "selection",
                "dirs",
                "behaviour",
                "io",
            ),
            list=Subcmd(
                "List selected tests.",
                "selection",
                "io",
            ),
        )
        args = climan.parse_args()
        return Commands(conf, sub_cmd=args.loam_sub_name)

    @cached_property
    def term(self) -> TermBase:
        term: TermBase = Term(
            has_color=not self.conf.io.no_color, has_unicode=not self.conf.io.ascii
        )
        if self.conf.io.write_log is not None:
            term = TeeTerm(
                [
                    term,
                    LogFile(self.conf.io.write_log, has_unicode=not self.conf.io.ascii),
                ]
            )
        return term

    @cached_property
    def vcs_repo(self) -> Repository:
        return (
            NoOpRepository()
            if self.conf.behaviour.no_git
            else GitRepository(self.conf.dirs.music)
        )

    @cached_property
    def music_tree(self) -> MusicSourceTree:
        return MusicSourceTree(self.conf.dirs.music, self.vcs_repo)

    @cached_property
    def tests_out_dir(self) -> TestsOutputDirectory:
        return TestsOutputDirectory(self.music_tree, self.conf.dirs.output)

    @cached_property
    def builder(self) -> CmakeBuilder:
        return CmakeBuilder(
            music_dir=self.conf.dirs.music,
            outdir=self.tests_out_dir,
            external_build=self.conf.dirs.build,
        )

    @cached_property
    def test_repo(self) -> TestRepositoryBase:
        repo: TestRepositoryBase = TestRepository(
            self.conf.selection.repo, self.builder
        )
        if self.conf.selection.names:
            repo = TestsMatchingPatterns(repo, self.conf.selection.names)
        if self.conf.selection.tags_any:
            repo = TestsWithAnyTag(repo, self.conf.selection.tags_any)
        if self.conf.selection.tags_all:
            repo = TestsWithAllTags(repo, self.conf.selection.tags_all)
        return repo

    @cached_property
    def build_outcome(self) -> BuildOutcome:
        timer = Timer()

        self.tests_out_dir.prepare(wipe=not self.conf.behaviour.keep)

        # Build necessary binaries
        try:
            build_outcome = self.builder.build_targets(
                self.test_repo.targets(), output_to=self.term, indent=1
            )
        except Exception:
            err_msg(
                "Build of test targets failed.", "The encountered error was:"
            ).print_to(self.term, 1)
            raise
        build_msg: Message = (
            StrMsg(
                f"Built all necessary targets in {timer.time_str()}.",
                termcolor=TERMCOLOR_GREEN,
            )
            if build_outcome.all_successful
            else warn_msg(f"Some builds failed, build phase took {timer.time_str()}.")
        )
        build_msg.print_to(self.term, 1)
        return build_outcome

    @cached_property
    def _prep_stage(self) -> PrepStage:
        return PrepStage(
            tests_out_dir=self.tests_out_dir,
            build_outcome=self.build_outcome,
            reuse_if_ready=self.conf.behaviour.keep,
        )

    def create_config(self) -> int:
        self.conf.to_file_(CONFIG_FILE)
        return 0

    def list_tests(self) -> int:
        self.test_repo.print_tests()
        return 0

    def build(self) -> int:
        return 0 if self.build_outcome.all_successful else 1

    def _run_stages(self, stages: Sequence[PipelineStage]) -> int:
        timer = Timer()

        # Run the pipeline
        tally = PipelineByTest(stages).process(self.test_repo.tests(), self.term)

        # Report results
        self.term.print_line("")
        tally.print_report_to(self.term)
        self.term.print_line("")

        num_failures = tally.count_failures()
        msg = info_msg if num_failures == 0 else err_msg
        msg(
            f"Processed {tally.num_tests} test(s) in {timer.time_str()}, "
            f"{num_failures} failure(s)"
        ).print_to(self.term, 0)

        self.term.close()  # FIXME: term should be handled with a context manager

        return 0 if num_failures == 0 else 1

    def prepare(self) -> int:
        return self._run_stages((self._prep_stage,))

    def run_pipeline(self) -> int:
        # Reference repository and comparison
        ref_path = self.conf.dirs.ref
        compare_stage: CompareStage | None = None
        if (
            ref_path.is_dir()
            and ref_path.resolve() != self.tests_out_dir.path.resolve()
        ):
            # Reference directory was specified, and is different from output directory
            ref_dir = TestsOutputDirectory(self.music_tree, ref_path)
            info_msg(f"using ReferenceOutputDirectory '{ref_path}'").print_to(
                self.term, 0
            )
            compare_stage = CompareStage(
                self.music_tree.path,
                self.tests_out_dir,
                ref_dir,
            )
        else:
            # Reference directory not specified: skip all comparisons
            warn_msg(
                f"ReferenceOutputDirectory '{ref_path}' not found, comparisons disabled"
            ).print_to(self.term, 0)

        # Assemble pipeline
        stages = [
            self._prep_stage,
            RunStage(
                self.tests_out_dir,
                reuse_if_ready=self.conf.behaviour.keep,
                verbose=self.conf.io.verbose,
                hooks=self.conf.command_hooks,
            ),
            SelfCheckStage(
                self.tests_out_dir,
            ),
        ]
        if compare_stage is not None:
            stages.append(compare_stage)
        return self._run_stages(stages)

    def run_command(self) -> int:
        if self.sub_cmd == "config":
            return self.create_config()
        if self.sub_cmd == "list":
            return self.list_tests()
        if self.sub_cmd == "build":
            return self.build()
        if self.sub_cmd == "prepare":
            return self.prepare()
        if self.sub_cmd == "run":
            return self.run_pipeline()
        err_msg("use `-h|--help` for valid commands").print_to(self.term, 0)
        return 1

    def print_dirs(self) -> None:
        info_msg(f"using TestRepoDirectory '{self.test_repo.path}'").print_to(
            self.term, 0
        )
        info_msg(f"using TestsOutputDirectory '{self.tests_out_dir.path}'").print_to(
            self.term, 0
        )


def main() -> int:
    cmds = Commands.from_cmd_args()
    cmds.print_dirs()
    return cmds.run_command()
