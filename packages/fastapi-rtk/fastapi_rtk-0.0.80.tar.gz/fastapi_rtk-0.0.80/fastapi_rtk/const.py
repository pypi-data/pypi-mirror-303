import logging
from typing import Literal

__all__ = ["logger"]

USER_TABLE = "ab_user"
USER_SEQUENCE = "ab_user_id_seq"
ROLE_TABLE = "ab_role"
ROLE_SEQUENCE = "ab_role_id_seq"
PERMISSION_TABLE = "ab_permission"
PERMISSION_SEQUENCE = "ab_permission_id_seq"
API_TABLE = "ab_view_menu"
API_SEQUENCE = "ab_view_menu_id_seq"
PERMISSION_API_TABLE = "ab_permission_view"
PERMISSION_API_SEQUENCE = "ab_permission_view_id_seq"
ASSOC_PERMISSION_API_ROLE_TABLE = "ab_permission_view_role"
ASSOC_PERMISSION_API_ROLE_SEQUENCE = "ab_permission_view_role_id_seq"
ASSOC_USER_ROLE_TABLE = "ab_user_role"
ASSOC_USER_ROLE_SEQUENCE = "ab_user_role_id_seq"
OAUTH_TABLE = "ab_oauth_account"
OAUTH_SEQUENCE = "ab_oauth_account_id_seq"

FASTAPI_RTK_TABLES = [
    USER_TABLE,
    ROLE_TABLE,
    PERMISSION_TABLE,
    API_TABLE,
    PERMISSION_API_TABLE,
    ASSOC_PERMISSION_API_ROLE_TABLE,
    ASSOC_USER_ROLE_TABLE,
    OAUTH_TABLE,
]

BASE_APIS = Literal[
    "AuthApi",
    "InfoApi",
    "PermissionsApi",
    "PermissionViewApi",
    "RolesApi",
    "UsersApi",
    "ViewsMenusApi",
]

EXCLUDE_ROUTES = Literal[
    "info", "download", "bulk", "get_list", "get", "post", "put", "delete"
]

PERMISSION_PREFIX = "can_"
DEFAULT_ADMIN_ROLE = "Admin"
DEFAULT_PUBLIC_ROLE = "Public"

DEFAULT_TOKEN_URL = "/api/v1/auth/jwt/login"
DEFAULT_SECRET = "SUPERSECRET"
DEFAULT_COOKIE_NAME = "dataTactics"
DEFAULT_BASEDIR = "app"
DEFAULT_STATIC_FOLDER = DEFAULT_BASEDIR + "/static"
DEFAULT_TEMPLATE_FOLDER = DEFAULT_BASEDIR + "/templates"
DEFAULT_PROFILER_FOLDER = DEFAULT_STATIC_FOLDER + "/profiles"

COOKIE_CONFIG_KEYS = [
    "cookie_name",
    "cookie_max_age",
    "cookie_path",
    "cookie_domain",
    "cookie_secure",
    "cookie_httponly",
    "cookie_samesite",
]
COOKIE_STRATEGY_KEYS = [
    "cookie_lifetime_seconds",
    "cookie_token_audience",
    "cookie_algorithm",
]
JWT_STRATEGY_KEYS = [
    "jwt_lifetime_seconds",
    "jwt_token_audience",
    "jwt_algorithm",
]
ROLE_KEYS = ["auth_admin_role", "auth_public_role"]


logging.basicConfig(format="%(asctime)s:%(levelname)s:%(name)s:%(message)s")
logger = logging.getLogger("DT_FASTAPI")
