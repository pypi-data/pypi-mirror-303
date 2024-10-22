from __future__ import annotations

from dataclasses import dataclass

from .term import CollectedMsgs, ConcatMsgs, Message, NullMsg, PrintOnlyIfHasLeaves


@dataclass(frozen=True)
class ValidationResult:
    is_success: bool
    message: Message = NullMsg()

    def __and__(self, other: ValidationResult) -> ValidationResult:
        assert isinstance(other, ValidationResult)
        return ValidationResult(
            self.is_success and other.is_success,
            message=ConcatMsgs([self.message, other.message]),
        )

    def __or__(self, other: ValidationResult) -> ValidationResult:
        assert isinstance(other, ValidationResult)
        return ValidationResult(
            self.is_success or other.is_success,
            message=ConcatMsgs([self.message, other.message]),
        )

    def with_header_msg(self, header_msg: Message) -> ValidationResult:
        return ValidationResult(
            self.is_success,
            PrintOnlyIfHasLeaves(CollectedMsgs([self.message], header_msg=header_msg)),
        )
