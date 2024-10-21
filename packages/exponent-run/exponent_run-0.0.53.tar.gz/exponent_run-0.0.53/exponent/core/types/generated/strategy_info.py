# Auto-generated, do not edit directly. Run `make generate_strategy_info` to update.

import enum

from pydantic import BaseModel

from exponent.core.remote_execution.types import ChatMode


class StrategyName(str, enum.Enum):
    FULL_FILE_REWRITE = "FULL_FILE_REWRITE"
    NATURAL_EDIT = "NATURAL_EDIT"
    UDIFF = "UDIFF"
    SEARCH_REPLACE = "SEARCH_REPLACE"
    OPEN_FILE_SEARCH_REPLACE = "OPEN_FILE_SEARCH_REPLACE"
    SEARCH_FILES = "SEARCH_FILES"
    FUNCTION_CALLING = "FUNCTION_CALLING"
    RAW_GPT = "RAW_GPT"
    STRUCT_OUT = "STRUCT_OUT"


class StrategyInfo(BaseModel):
    strategy_name: StrategyName
    display_name: str
    description: str
    disabled: bool
    display_order: int


CHAT_MODE_DEFAULTS: dict[ChatMode, StrategyName] = {
    ChatMode.DEFAULT: StrategyName.RAW_GPT,
    ChatMode.CLI: StrategyName.NATURAL_EDIT,
    ChatMode.CLOUD: StrategyName.NATURAL_EDIT,
    ChatMode.PYTHON_INTERPRETER: StrategyName.NATURAL_EDIT,
}

STRATEGY_INFO_LIST: list[StrategyInfo] = [
    StrategyInfo(
        strategy_name=StrategyName.NATURAL_EDIT,
        display_name="Natural Edit",
        description="A natural file editing strategy.",
        disabled=False,
        display_order=0,
    ),
    StrategyInfo(
        strategy_name=StrategyName.FULL_FILE_REWRITE,
        display_name="Full File Rewrites",
        description="Rewrites the full file every time. Use this if your files are generally less than 300 lines.",
        disabled=False,
        display_order=1,
    ),
    StrategyInfo(
        strategy_name=StrategyName.UDIFF,
        display_name="Unified Diff",
        description="Generates diffs to edit files",
        disabled=False,
        display_order=2,
    ),
    StrategyInfo(
        strategy_name=StrategyName.SEARCH_REPLACE,
        display_name="Search and Replace",
        description="Replaces chunks of code with new version of code. Recommended strategy for larger more complex files.",
        disabled=False,
        display_order=3,
    ),
    StrategyInfo(
        strategy_name=StrategyName.OPEN_FILE_SEARCH_REPLACE,
        display_name="Open + Search/Replace",
        description="Uses the Open File command to open files and Search/Replace to edit.",
        disabled=False,
        display_order=4,
    ),
    StrategyInfo(
        strategy_name=StrategyName.SEARCH_FILES,
        display_name="Search Files",
        description="Natural edit version that exposes a search_files command.",
        disabled=True,
        display_order=5,
    ),
    StrategyInfo(
        strategy_name=StrategyName.FUNCTION_CALLING,
        display_name="Function Calling",
        description="No description",
        disabled=True,
        display_order=99,
    ),
    StrategyInfo(
        strategy_name=StrategyName.RAW_GPT,
        display_name="Raw GPT",
        description="No description",
        disabled=True,
        display_order=99,
    ),
    StrategyInfo(
        strategy_name=StrategyName.STRUCT_OUT,
        display_name="Structured Output",
        description="Uses GPTs strict json_schema format.",
        disabled=True,
        display_order=99,
    ),
]


ENABLED_STRATEGY_INFO_LIST: list[StrategyInfo] = [
    StrategyInfo(
        strategy_name=StrategyName.NATURAL_EDIT,
        display_name="Natural Edit",
        description="A natural file editing strategy.",
        disabled=False,
        display_order=0,
    ),
    StrategyInfo(
        strategy_name=StrategyName.FULL_FILE_REWRITE,
        display_name="Full File Rewrites",
        description="Rewrites the full file every time. Use this if your files are generally less than 300 lines.",
        disabled=False,
        display_order=1,
    ),
    StrategyInfo(
        strategy_name=StrategyName.UDIFF,
        display_name="Unified Diff",
        description="Generates diffs to edit files",
        disabled=False,
        display_order=2,
    ),
    StrategyInfo(
        strategy_name=StrategyName.SEARCH_REPLACE,
        display_name="Search and Replace",
        description="Replaces chunks of code with new version of code. Recommended strategy for larger more complex files.",
        disabled=False,
        display_order=3,
    ),
    StrategyInfo(
        strategy_name=StrategyName.OPEN_FILE_SEARCH_REPLACE,
        display_name="Open + Search/Replace",
        description="Uses the Open File command to open files and Search/Replace to edit.",
        disabled=False,
        display_order=4,
    ),
]
