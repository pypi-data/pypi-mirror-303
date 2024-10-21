import re as _re
import pyserials as _ps

from conventional_commits.message import ConventionalCommitMessage as _ConventionalCommitMessage


class ConventionalCommitParser:
    def __init__(self, types: tuple[str, ...] | list[str] | set[str] | str | None = None):
        if types is None:
            self._types = None
            types_pattern = r"[\w-]+"
        else:
            if isinstance(types, str):
                types = [types]
            elif not isinstance(types, (list, tuple, set)):
                raise TypeError(
                    f"Argument 'types' must be a string or list/tuple/set of strings, "
                    f"but got type '{type(types)}': {types}"
                )
            type_pattern = _re.compile(r"^[\w-]+$")
            for typ in types:
                if not isinstance(typ, str):
                    raise TypeError(
                        f"Argument 'types' must be a list/tuple/set of strings, "
                        f"but element {typ} has type '{type(typ)}'."
                    )
                if not type_pattern.match(typ):
                    raise ValueError(
                        f"Type '{typ}' does not match the regex pattern '{type_pattern.pattern}'."
                    )
            self._types = set(types)
            types_pattern = "|".join(self._types)
        pattern_summary = rf"""
            ^
            (?P<typ>{types_pattern})         # type
            (?:\((?P<scope>[^\)]+)\))?       # optional scope within parentheses
            :[ ](?P<description>.+)              # commit description after ": "
            $
        """
        self._pattern_summary = _re.compile(pattern_summary, flags=_re.VERBOSE)
        return

    @property
    def types(self) -> set[str] | None:
        return self._types

    def parse(self, message: str) -> _ConventionalCommitMessage | None:
        if not isinstance(message, str):
            raise TypeError(f"Invalid commit message type: {type(message)}")
        message = message.strip()
        if not message:
            return
        lines = message.splitlines()
        summary = lines[0]
        summary_match = self._pattern_summary.match(summary)
        if not summary_match:
            return
        commit_parts = summary_match.groupdict()
        commit_parts["scope"] = (
            tuple(scope.strip() for scope in commit_parts["scope"].split(","))
            if commit_parts["scope"] else ""
        )
        commit_parts["description"] = commit_parts["description"].strip()
        commit_parts |= {"body": "", "footer": None}
        if len(lines) == 1:
            return _ConventionalCommitMessage(**commit_parts)
        for line_idx, line in enumerate(lines[1:]):
            if line.startswith("---") and all(c == "-" for c in line):
                break
        else:
            line_idx += 1
        commit_parts["body"] = "\n".join(lines[1:line_idx + 1]).strip()
        commit_parts["footer"] = self._parse_footer(lines[line_idx + 2:]) or None
        return _ConventionalCommitMessage(**commit_parts)

    @staticmethod
    def _parse_footer(footers: list[str]) -> dict:
        selected_lines = []
        for footer in footers:
            # Sometimes GitHub adds a second horizontal line after the original footer; skip it
            if not footer or _re.fullmatch("-{3,}", footer):
                continue
            selected_lines.append(footer)
        footer_str = "\n".join(selected_lines)
        try:
            footer_dict = _ps.read.yaml_from_string(data=footer_str)
        except _ps.exception.read.PySerialsReadFromStringException as e:
            raise ValueError(f"Invalid footer: {footer_str}") from e
        if not isinstance(footer_dict, dict):
            raise ValueError(f"Invalid footer: {footer_dict}")
        return footer_dict


def create(
    types: tuple[str, ...] | list[str] | set[str] | str | None = None
) -> ConventionalCommitParser:
    return ConventionalCommitParser(types)


def parse(
    message: str, types: tuple[str, ...] | list[str] | set[str] | str | None = None
) -> _ConventionalCommitMessage | None:
    return ConventionalCommitParser(types).parse(message)


# class CommitParser:
#     def __init__(self, types: list[str], logger: Logger = None):
#         self._types = types
#         self._logger = logger or Logger()
#         pattern = rf"""
#             ^
#             (?P<typ>{"|".join(types)})         # type
#             (?:\((?P<scope>[^\)\n]+)\))?       # optional scope within parentheses
#             :[ ](?P<title>[^\n]+)              # commit description after ": "
#             (?:(?P<body>.*?)(\n-{{3,}}\n)|$)?  # optional commit body
#                                                #   everything until first "\n---" or end of string
#             (?P<footer>.*)?                    # optional footers
#             $
#         """
#         self._pattern = re.compile(pattern, flags=re.VERBOSE | re.DOTALL)
#         return
#
#     def parse(self, msg: str) -> CommitMsg | None:
#         match = self._pattern.match(msg)
#         if not match:
#             return
#         commit_parts = match.groupdict()
#         if commit_parts["scope"]:
#             commit_parts["scope"] = [scope.strip() for scope in commit_parts["scope"].split(",")]
#         commit_parts["title"] = commit_parts["title"].strip()
#         commit_parts["body"] = commit_parts["body"].strip() if commit_parts["body"] else ""
#         if commit_parts["footer"]:
#             parsed_footers = {}
#             footers = commit_parts["footer"].strip().splitlines()
#             for footer in footers:
#                 # Sometimes GitHub adds a second horizontal line after the original footer; skip it
#                 if not footer or re.fullmatch("-{3,}", footer):
#                     continue
#                 match = re.match(r"^(?P<key>[\w-]+)( *:* *(?P<value>.*))?$", footer)
#                 if match:
#                     key = match.group("key")
#                     val = match.group("value").strip() if match.group("value") else "true"
#                     if key in parsed_footers:
#                         self._logger.error(f"Duplicate footer: {footer}")
#                     try:
#                         parsed_footers[key] = json.loads(val)
#                     except json.JSONDecodeError:
#                         self._logger.error(f"Invalid footer value: {footer}")
#                     # footer_list = parsed_footers.setdefault(match.group("key"), [])
#                     # footer_list.append(match.group("value").strip() if match.group("value") else True)
#                 else:
#                     # Otherwise, the footer is invalid
#                     self._logger.warning(f"Invalid footer: {footer}")
#             commit_parts["footer"] = parsed_footers
#         return CommitMsg(**commit_parts)
