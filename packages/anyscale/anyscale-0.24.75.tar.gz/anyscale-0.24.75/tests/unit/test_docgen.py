from dataclasses import dataclass, field
import os
import re
from tempfile import TemporaryDirectory
import traceback
from typing import Dict, List, Optional, Tuple, Union

import click
from click.testing import CliRunner
import pytest

from anyscale._private.docgen.__main__ import ALL_MODULES, generate
from anyscale._private.docgen.generator import MarkdownGenerator, Module
from anyscale._private.docgen.generator_legacy import parse_legacy_sdks
from anyscale._private.models import ModelBase, ModelEnum
from anyscale._private.sdk import sdk_command
from anyscale.commands.util import AnyscaleCommand, LegacyAnyscaleCommand


def test_full_smoke_test():
    runner = CliRunner()
    with TemporaryDirectory() as d:
        result = runner.invoke(generate, [d])
        # should have an output per module
        expected_output_count = len(ALL_MODULES)

        if result.exception:
            e = result.exception
            stacktrace = traceback.format_exception(type(e), e, e.__traceback__)
            formatted_exception = "".join(stacktrace)

        assert result.exit_code == 0, result.output or formatted_exception
        assert result.output.count("Writing output file") == expected_output_count


def test_parse_legacy_sdks():
    _TEST_API_MD = """\
some random text here

### fake_legacy_sdk

this is a fake legacy [sdk](./models.md#fakesdk)
"""

    _TEST_MODEL_MD = """\
this is random

## FakeLegacyModel

this is a fake legacy [model](#fakemodel)

# next section
"""

    with TemporaryDirectory() as tmp:
        with open(os.path.join(tmp, "api.md"), "w") as f:
            f.write(_TEST_API_MD)

        with open(os.path.join(tmp, "model.md"), "w") as f:
            f.write(_TEST_MODEL_MD)

        legacy_sdks, legacy_models = parse_legacy_sdks(
            os.path.join(tmp, "api.md"), os.path.join(tmp, "model.md"),
        )
        assert legacy_sdks[0].name == "fake_legacy_sdk"
        assert (
            legacy_sdks[0].docstring == "this is a fake legacy [sdk](#fakesdk-legacy)"
        )
        assert legacy_models[0].name == "FakeLegacyModel"
        assert (
            legacy_models[0].docstring
            == "this is a fake legacy [model](#fakemodel-legacy)"
        )


def _fake_module(
    *,
    name: str = "Fake",
    models: Optional[List] = None,
    cli_commands: Optional[List] = None,
    sdk_commands: Optional[List] = None,
    cli_command_group_prefix: Optional[Dict[click.Command, str]] = None,
    legacy_cli_commands: Optional[List] = None,
) -> Module:
    return Module(
        title=name,
        filename=f"{name.lower()}.md",
        cli_prefix=f"anyscale {name.lower()}",
        cli_commands=cli_commands or [],
        sdk_prefix=f"anyscale.{name.lower()}",
        sdk_commands=sdk_commands or [],
        models=models or [],
        cli_command_group_prefix=cli_command_group_prefix,
        legacy_cli_prefix=f"anyscale legacy {name.lower()}",
        legacy_cli_commands=legacy_cli_commands or [],
    )


class TestGenerateModelType:
    def test_basic(self):
        @dataclass(frozen=True)
        class FakeConfig(ModelBase):
            """FakeConfig does really special things."""

            foo: str = field(metadata={"docstring": "Foo docstring."})

            # Private fields should not be documented.
            _private: str

            __doc_yaml_example__ = """\
config: file"""

            __doc_py_example__ = """\
run_python_command()
"""

        output = MarkdownGenerator(
            modules=[_fake_module(models=[FakeConfig])]
        ).generate()
        assert len(output) == 1
        assert "## `FakeConfig`" in output["fake.md"]
        assert "FakeConfig does really special things." in output["fake.md"]
        assert "**`foo` (str)**: Foo docstring." in output["fake.md"]
        assert "_private" not in output["fake.md"]

        # Check that model methods are added.
        assert "def __init__(self, **fields) -> FakeConfig" in output["fake.md"]
        assert "def options(self, **fields) -> FakeConfig" in output["fake.md"]
        assert "def to_dict(self) -> Dict[str, Any]" in output["fake.md"]

        # Check that examples were generated.
        assert '<TabItem value="yamlconfig" label="YAML">' in output["fake.md"]
        assert "config: file" in output["fake.md"]
        assert '<TabItem value="pythonsdk" label="Python">' in output["fake.md"]
        assert "run_python_command()" in output["fake.md"]

    def test_missing_field_docstring(self):
        @dataclass(frozen=True)
        class FakeConfig(ModelBase):
            """FakeConfig does really special things."""

            foo: str

        with pytest.raises(
            ValueError,
            match="Model 'FakeConfig' is missing a docstring for field 'foo'",
        ):
            MarkdownGenerator(modules=[_fake_module(models=[FakeConfig])]).generate()

    def test_missing_py_example(self):
        @dataclass(frozen=True)
        class FakeConfig(ModelBase):
            """FakeConfig does really special things."""

            __doc_yaml_example__ = "fake: config"

        with pytest.raises(
            ValueError, match="Model 'FakeConfig' is missing a '__doc_py_example__'",
        ):
            MarkdownGenerator(modules=[_fake_module(models=[FakeConfig])]).generate()

    def test_invalid_py_example(self):
        @dataclass(frozen=True)
        class FakeConfig(ModelBase):
            """FakeConfig does really special things."""

            __doc_yaml_example__ = "fake: config"
            __doc_py_example__ = "FakeConfig('hi': 123)"

        with pytest.raises(
            ValueError,
            match="'FakeConfig.__doc_py_example__' is not valid Python syntax",
        ):
            MarkdownGenerator(modules=[_fake_module(models=[FakeConfig])]).generate()

    def test_missing_yaml_example(self):
        @dataclass(frozen=True)
        class FakeConfig(ModelBase):
            """FakeConfig does really special things."""

            __doc_py_example__ = "FakeConfig()"

        with pytest.raises(
            ValueError,
            match="Config model 'FakeConfig' is missing a '__doc_yaml_example__'",
        ):
            MarkdownGenerator(modules=[_fake_module(models=[FakeConfig])]).generate()

    def test_invalid_yaml_example(self):
        @dataclass(frozen=True)
        class FakeConfig(ModelBase):
            """FakeConfig does really special things."""

            __doc_yaml_example__ = "fake: config: oops"
            __doc_py_example__ = "FakeConfig()"

        with pytest.raises(
            ValueError,
            match="'FakeConfig.__doc_yaml_example__' is not valid YAML syntax",
        ):
            MarkdownGenerator(modules=[_fake_module(models=[FakeConfig])]).generate()

    def test_non_config_does_not_have_constructors(self):
        """Models that don't end in "Config" shouldn't document constructor methods."""

        @dataclass(frozen=True)
        class FakeStatus(ModelBase):
            """FakeStatus is so cool."""

            foo: str = field(metadata={"docstring": "Foo docstring."})

            __doc_py_example__ = "FakeStatus()"
            __doc_yaml_example__ = "foo: hi"

        output = MarkdownGenerator(
            modules=[_fake_module(models=[FakeStatus])]
        ).generate()

        assert "def __init__(self, **fields)" not in output["fake.md"]
        assert "def options(self, **fields)" not in output["fake.md"]
        assert "def to_dict(self) -> Dict[str, Any]" in output["fake.md"]

    def test_type_hints(self):
        @dataclass(frozen=True)
        class FakeEnum(ModelEnum):
            pass

        @dataclass(frozen=True)
        class FakeStatus(ModelBase):
            """FakeStatus is so cool."""

            __doc_py_example__ = "FakeConfig()"

        @dataclass(frozen=True)
        class FakeConfig(ModelBase):
            """FakeConfig does really special things."""

            foo: str = field(metadata={"docstring": "foo docs"})
            bar: Optional[str] = field(metadata={"docstring": "bar docs"})
            baz: Dict[str, FakeStatus] = field(metadata={"docstring": "baz docs"})
            qux: List[Optional[FakeEnum]] = field(metadata={"docstring": "qux docs"})

            __doc_py_example__ = "FakeConfig()"
            __doc_yaml_example__ = "fake: config"

        output = MarkdownGenerator(
            modules=[_fake_module(models=[FakeConfig, FakeStatus, FakeEnum])]
        ).generate()

        assert "**`foo` (str)**: foo docs" in output["fake.md"]
        assert "**`bar` (str | None)**: bar docs" in output["fake.md"]
        assert (
            "**`baz` (Dict[str, [FakeStatus](fake.md#fakestatus)])**: baz docs"
            in output["fake.md"]
        )
        assert (
            "**`qux` (List[[FakeEnum](fake.md#fakeenum) | None])**: qux docs"
            in output["fake.md"]
        )

    def test_customer_hosted_cloud_only(self):
        @dataclass(frozen=True)
        class FakeConfig(ModelBase):
            """FakeConfig does special things."""

            # Should not be labeled as customer-hosted cloud only.
            foo: str = field(metadata={"docstring": "Foo docstring."})

            __doc_yaml_example__ = """\
config: file"""

            __doc_py_example__ = """\
run_python_command()
"""

        output = MarkdownGenerator(
            modules=[_fake_module(models=[FakeConfig])]
        ).generate()

        # By default options should not be labeled as customer-hosted cloud only.
        assert "Only available on [customer-hosted clouds]" not in output["fake.md"]

        @dataclass(frozen=True)
        class FakeConfigTwo(ModelBase):
            """FakeConfigTwo does really special things."""

            # Should be labeled as customer-hosted cloud only.
            foo: str = field(
                metadata={"docstring": "Foo docstring.", "customer_hosted_only": True}
            )

            __doc_yaml_example__ = """\
config: file"""

            __doc_py_example__ = """\
run_python_command()
"""

        output = MarkdownGenerator(
            modules=[_fake_module(models=[FakeConfigTwo])]
        ).generate()

        assert "Only available on [customer-hosted clouds]" in output["fake.md"]


class TestGenerateModelEnumType:
    def test_basic(self):
        @dataclass(frozen=True)
        class FakeEnum(ModelEnum):
            """FakeEnum is highly important."""

            FOO = "FOO"
            BAR = "BAR"

            __docstrings__ = {
                "FOO": "Foo is quite important.",
                "BAR": "But bar is even more so.",
            }

        output = MarkdownGenerator(modules=[_fake_module(models=[FakeEnum])]).generate()
        assert len(output) == 1
        assert "FakeEnum is highly important." in output["fake.md"]
        assert "**`FOO`**: Foo is quite important." in output["fake.md"]
        assert "**`BAR`**: But bar is even more so." in output["fake.md"]

    def test_reject_value_missing_docstring(self):
        with pytest.raises(
            ValueError,
            match=re.escape(
                "ModelEnum 'FakeEnum.__docstrings__' is missing docstrings for values: ['BAR', 'FOO']"
            ),
        ):

            @dataclass(frozen=True)
            class FakeEnum(ModelEnum):
                """FakeEnum is highly important."""

                FOO = "FOO"
                BAR = "BAR"

        with pytest.raises(
            ValueError,
            match=re.escape(
                "ModelEnum 'FakeEnumTwo.__docstrings__' is missing docstrings for values: ['BAR']"
            ),
        ):

            @dataclass(frozen=True)
            class FakeEnumTwo(ModelEnum):
                """FakeEnumTwo is also important."""

                FOO = "FOO"
                BAR = "BAR"

                __docstrings__ = {
                    "FOO": "Foo is quite important.",
                }


class TestGenerateCLICommand:
    def test_basic(self):
        @click.command("do-something", cls=AnyscaleCommand, example="infinite loop")
        @click.argument("the-arg")
        @click.option("-m", "--maybe", help="Maybe do something else.")
        def do_something():
            """This is the description of what to do."""

        output = MarkdownGenerator(
            modules=[_fake_module(cli_commands=[do_something])]
        ).generate()
        assert "## `anyscale fake do-something`" in output["fake.md"]
        assert "anyscale fake do-something [OPTIONS] THE_ARG" in output["fake.md"]
        assert "This is the description of what to do." in output["fake.md"]
        assert "**`-m/--maybe`**: Maybe do something else." in output["fake.md"]
        assert "--help" not in output["fake.md"]

    def test_secondary_opts(self):
        @click.command("do-something", cls=AnyscaleCommand, example="infinite loop")
        @click.argument("the-arg")
        @click.option("--enable/--disable", help="Enable or disable something.")
        def do_something():
            """This is the description of what to do."""

        output = MarkdownGenerator(
            modules=[_fake_module(cli_commands=[do_something])]
        ).generate()
        assert "## `anyscale fake do-something`" in output["fake.md"]
        assert "anyscale fake do-something [OPTIONS] THE_ARG" in output["fake.md"]
        assert "This is the description of what to do." in output["fake.md"]
        assert (
            "**`--enable/--disable`**: Enable or disable something."
            in output["fake.md"]
        )
        assert "--help" not in output["fake.md"]

    def test_command_with_group(self):
        @click.group("my_group", help="This is my group.")
        def my_group() -> None:
            pass

        @my_group.command("do-something", cls=AnyscaleCommand, example="infinite loop")
        def do_something():
            """This is the description of what to do."""

        output = MarkdownGenerator(
            modules=[
                _fake_module(
                    cli_commands=[do_something],
                    cli_command_group_prefix={do_something: "my_group"},
                ),
            ]
        ).generate()
        assert "## `anyscale fake my_group do-something`" in output["fake.md"]
        assert "anyscale fake my_group do-something [OPTIONS]" in output["fake.md"]
        assert "--help" not in output["fake.md"]
        assert '<TabItem value="cli" label="CLI">' in output["fake.md"]
        assert "infinite loop" in output["fake.md"]

    def test_legacy_command_with_group(self):
        @click.group("my_group", help="This is my group.")
        def my_group() -> None:
            pass

        @my_group.command("new", cls=AnyscaleCommand, example="infinite loop")
        def new():
            """This is the description of what to do."""

        @my_group.command(
            "old", cls=LegacyAnyscaleCommand, new_cli=new, new_prefix="anyscale"
        )
        def old():
            """This is the description of what to do."""

        @my_group.command("limited", cls=LegacyAnyscaleCommand, is_limited_support=True)
        def limited():
            """This is the description of what to do."""

        output = MarkdownGenerator(
            modules=[_fake_module(legacy_cli_commands=[old, limited],),]
        ).generate()
        assert "### `anyscale legacy fake old`" in output["fake.md"]
        assert '<span class="label-h3 label-legacy">Legacy</span>' in output["fake.md"]
        assert (
            "This command is deprecated. Upgrade to [anyscale new](#anyscale-new)."
            in output["fake.md"]
        )
        assert "### `anyscale legacy fake limited`" in output["fake.md"]
        assert '<span class="label-h3 label-legacy">Legacy</span>' in output["fake.md"]
        assert (
            "This command is not actively maintained. Use with caution."
            in output["fake.md"]
        )

    def test_beta_command_with_group(self):
        @click.group("my_group", help="This is my group.")
        def my_group() -> None:
            pass

        @my_group.command(
            "new", cls=AnyscaleCommand, example="infinite loop", is_beta=True
        )
        def new():
            """This is the description of what to do."""

        output = MarkdownGenerator(
            modules=[_fake_module(cli_commands=[new])]
        ).generate()
        assert "### `anyscale fake new`" in output["fake.md"]
        assert '<span class="label-h3 label-beta">Beta</span>' in output["fake.md"]
        assert (
            "This command undergoes rapid iteration. Users must be tolerant of change."
            in output["fake.md"]
        )


class TestGenerateSDKCommand:
    def test_basic(self):
        @sdk_command(
            "TEST_KEY",
            None,
            doc_py_example="do_something()",
            arg_docstrings={"s": "a string"},
        )
        def do_something(s: str, *, _sdk) -> int:
            """Might do something."""

        output = MarkdownGenerator(
            modules=[_fake_module(sdk_commands=[do_something])]
        ).generate()

        assert "## `anyscale.fake.do_something`" in output["fake.md"]
        assert "Might do something." in output["fake.md"]
        assert "**`s` (str)**: a string" in output["fake.md"]
        assert "**Returns**: int" in output["fake.md"]
        # Private arguments should not be documented.
        assert "_sdk" not in output["fake.md"]

    def test_no_return(self):
        @sdk_command(
            "TEST_KEY",
            None,
            doc_py_example="do_something()",
            arg_docstrings={"s": "a string"},
        )
        def do_something(s: str):
            """Might do something."""

        output = MarkdownGenerator(
            modules=[_fake_module(sdk_commands=[do_something])]
        ).generate()

        assert "Returns" not in output["fake.md"]

    def test_missing_docstring(self):
        @sdk_command(
            "TEST_KEY",
            None,
            doc_py_example="do_something()",
            arg_docstrings={"s": "a string"},
        )
        def do_something(s: str, *, _sdk):
            pass

        with pytest.raises(
            ValueError,
            match="SDK command 'anyscale.fake.do_something' is missing a docstring.",
        ):
            MarkdownGenerator(
                modules=[_fake_module(sdk_commands=[do_something])]
            ).generate()

    def test_missing_py_example(self):
        with pytest.raises(
            ValueError,
            match="SDK command 'do_something' must provide a non-empty 'doc_py_example'.",
        ):

            @sdk_command(
                "TEST_KEY", None, doc_py_example="", arg_docstrings={"s": "a string"},
            )
            def do_something(s: str, *, _sdk):
                """Might do something."""

    def test_missing_arg_docstring(self):
        @sdk_command(
            "TEST_KEY", None, doc_py_example="do_something()", arg_docstrings={},
        )
        def do_something(s: str, *, _sdk):
            """Might do something."""

        with pytest.raises(
            ValueError,
            match="SDK command 'anyscale.fake.do_something' is missing a docstring for argument 's'",
        ):
            MarkdownGenerator(
                modules=[_fake_module(sdk_commands=[do_something])]
            ).generate()

    def test_type_hints(self):
        """Models that don't end in "Config" shouldn't document constructor methods."""

        @dataclass(frozen=True)
        class FakeEnum(ModelEnum):
            pass

        @dataclass(frozen=True)
        class FakeStatus(ModelBase):
            """FakeStatus is so cool."""

            __doc_py_example__ = "FakeStatus()"

        @dataclass(frozen=True)
        class FakeConfig(ModelBase):
            """FakeConfig does really special things."""

            __doc_py_example__ = "FakeConfig()"
            __doc_yaml_example__ = "fake: config"

        @sdk_command(
            "TEST_KEY",
            None,
            doc_py_example="do_something()",
            arg_docstrings={
                "foo": "foo docs",
                "bar": "bar docs",
                "baz": "baz docs",
                "qux": "qux docs",
                "quux": "quux docs",
                "quuz": "quuz docs",
            },
        )
        def do_something(
            foo: FakeEnum,
            bar: Optional[FakeStatus],
            baz: Union[Optional[FakeConfig], FakeStatus],
            qux: List[FakeEnum],
            quux: Dict[str, Optional[FakeEnum]],
            quuz: Tuple[str, int],
        ) -> Optional[FakeStatus]:
            """Might do something."""

        output = MarkdownGenerator(
            modules=[
                _fake_module(
                    sdk_commands=[do_something],
                    models=[FakeEnum, FakeStatus, FakeConfig],
                )
            ]
        ).generate()

        assert "**`foo` ([FakeEnum](fake.md#fakeenum))**: foo docs" in output["fake.md"]
        assert (
            "**`bar` ([FakeStatus](fake.md#fakestatus) | None)**: bar docs"
            in output["fake.md"]
        )
        assert (
            "**`baz` ([FakeConfig](fake.md#fakeconfig) | None | [FakeStatus](fake.md#fakestatus))**: baz docs"
            in output["fake.md"]
        )
        assert (
            "**`qux` (List[[FakeEnum](fake.md#fakeenum)])**: qux docs"
            in output["fake.md"]
        )
        assert (
            "**`quux` (Dict[str, [FakeEnum](fake.md#fakeenum) | None])**: quux docs"
            in output["fake.md"]
        )
        assert "**`quuz` (Tuple[str, int])**: quuz docs" in output["fake.md"]
        assert (
            "**Returns**: [FakeStatus](fake.md#fakestatus) | None" in output["fake.md"]
        )
