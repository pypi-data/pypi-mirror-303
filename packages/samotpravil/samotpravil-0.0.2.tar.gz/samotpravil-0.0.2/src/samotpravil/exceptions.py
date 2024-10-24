class SamotpravilError(Exception):
    pass


class AuthorizationError(SamotpravilError):
    pass


class BadRequestError(SamotpravilError):
    pass


class StopListError(SamotpravilError):
    pass


class DomainNotTrustedError(SamotpravilError):
    pass
