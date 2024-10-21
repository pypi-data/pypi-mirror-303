import copy as _copy

import pyserials as _ps


class ConventionalCommitMessage:
    def __init__(
        self,
        typ: str,
        description: str,
        scope: str | tuple[str, ...] | list[str] = "",
        body: str = "",
        footer: dict[str, str | bool | int | float | list | dict] | None = None,
    ):
        for arg, arg_name in ((typ, "typ"), (description, "description")):
            if not isinstance(arg, str):
                raise TypeError(f"Argument '{arg_name}' must be a string, but got {type(arg)}: {arg}")
            if not arg:
                raise ValueError(f"Argument '{arg_name}' must not be empty.")
            if "\n" in arg:
                raise ValueError(f'Argument `{arg_name}` must not contain a newline, but got: """{arg}"""')
            if ":" in arg:
                raise ValueError(f'Argument `{arg_name}` must not contain a colon, but got: """{arg}"""')
        self._type = typ
        self._description = description
        if isinstance(body, str):
            self._body = body.strip()
        else:
            raise TypeError(f"Argument 'body' must be a string or None, but got {type(body)}: {body}")
        if scope == "":
            scope = []
        if isinstance(scope, (list, tuple)):
            self._scope = tuple(str(s) for s in scope)
        elif isinstance(scope, str):
            self._scope = (scope, )
        else:
            raise TypeError(
                f"Argument 'scope' must be a string or list/tuple of strings, but got {type(scope)}: {scope}"
            )
        if footer is None:
            self._footer = {}
        elif isinstance(footer, dict):
            self._footer = {str(key): value for key, value in footer.items()}
        else:
            raise TypeError(f"Argument 'footer' must be a dict, but got {type(footer)}: {footer}")
        return

    @property
    def type(self) -> str:
        return self._type

    @property
    def scope(self) -> tuple[str, ...]:
        return self._scope

    @property
    def description(self) -> str:
        return self._description

    @property
    def body(self) -> str:
        return self._body

    @property
    def footer(self) -> dict[str, str | bool | int | float | list | dict]:
        return _copy.deepcopy(self._footer)

    @property
    def summary(self) -> str:
        scope = f"({', '.join(self._scope)})" if self._scope else ""
        return f"{self._type}{scope}: {self._description}"

    @property
    def footerless(self) -> str:
        commit = self.summary
        if self._body:
            commit += f"\n\n{self._body}"
        return commit.strip()

    def __str__(self):
        commit = self.footerless
        if self._footer:
            commit += f"\n\n{'-'*10}\n\n"
            commit += _ps.write.to_yaml_string(self._footer)
        return commit.strip()

    def __repr__(self):
        return (
            f"ConventionalCommitMessage("
            f"typ='{self._type}', "
            f"description='{self._description}', "
            f"scope={self._scope}, "
            f"body='{self._body}', "
            f"footer={self._footer})"
        )


def create(
    typ: str,
    description: str,
    scope: str | tuple[str, ...] | list[str] = "",
    body: str = "",
    footer: dict[str, str | bool | int | float | list | dict] | None = None,
) -> ConventionalCommitMessage:
    return ConventionalCommitMessage(typ=typ, description=description, scope=scope, body=body, footer=footer)