from __future__ import annotations

from digitalhub_runtime_container.entities.function.container.models import (
    SourceCodeStructContainer,
    SourceCodeValidatorContainer,
)

from digitalhub.entities.function._base.spec import FunctionSpec, FunctionValidator


class FunctionSpecContainer(FunctionSpec):
    """
    FunctionSpecContainer specifications.
    """

    def __init__(
        self,
        image: str | None = None,
        base_image: str | None = None,
        command: str | None = None,
        args: list[str] | None = None,
        source: dict | None = None,
        code_src: str | None = None,
        handler: str | None = None,
        code: str | None = None,
        base64: str | None = None,
        lang: str | None = None,
    ) -> None:
        super().__init__()

        self.image = image
        self.base_image = base_image
        self.command = command
        self.args = args

        # Give source precedence
        if source is not None:
            source_dict = source
        else:
            source_dict = {
                "source": code_src,
                "handler": handler,
                "code": code,
                "base64": base64,
                "lang": lang,
            }

        source_checked = self.source_check(source_dict)
        self.source = SourceCodeStructContainer(**source_checked)

    @staticmethod
    def source_check(source: dict) -> dict:
        """
        Check source.

        Parameters
        ----------
        source : dict
            Source.

        Returns
        -------
        dict
            Checked source.
        """
        return SourceCodeStructContainer.source_check(source)

    def show_source_code(self) -> str:
        """
        Show source code.

        Returns
        -------
        str
            Source code.
        """
        return self.source.show_source_code()

    def to_dict(self) -> dict:
        """
        Override to_dict to exclude code from source.

        Returns
        -------
        dict
            Dictionary representation of the object.
        """
        dict_ = super().to_dict()
        dict_["source"] = self.source.to_dict()
        return dict_


class FunctionValidatorContainer(FunctionValidator, SourceCodeValidatorContainer):
    """
    FunctionValidatorContainer validator.
    """

    image: str = None
    """Name of the Function's container image."""

    base_image: str = None
    """Function's base container image."""

    command: str = None
    """Command to run inside the container."""

    args: list[str] = None
    """Arguments to pass to the entrypoint."""
