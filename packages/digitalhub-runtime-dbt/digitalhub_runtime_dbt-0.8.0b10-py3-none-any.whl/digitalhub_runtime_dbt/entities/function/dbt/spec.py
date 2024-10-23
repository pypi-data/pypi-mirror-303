from __future__ import annotations

from digitalhub_runtime_dbt.entities.function.dbt.models import SourceCodeStructDbt, SourceCodeValidatorDbt

from digitalhub.entities.function._base.spec import FunctionSpec, FunctionValidator


class FunctionSpecDbt(FunctionSpec):
    """
    FunctionSpecDbt specifications.
    """

    def __init__(
        self,
        source: dict | None = None,
        code_src: str | None = None,
        handler: str | None = None,
        code: str | None = None,
        base64: str | None = None,
        lang: str | None = None,
    ) -> None:
        super().__init__()

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
        self.source = SourceCodeStructDbt(**source_checked)

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
        return SourceCodeStructDbt.source_check(source)

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


class FunctionValidatorDbt(FunctionValidator, SourceCodeValidatorDbt):
    """
    FunctionValidatorDbt validator.
    """
