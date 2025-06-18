# ENABLE_JAVASCRIPT_CONTROLS = True

FEATURE_FLAGS = {
    "EMBEDDED_SUPERSET": True
    # "DASHBOARD_RBAC": True,
    # "ALLOW_JAVASCRIPT_EXECUTION": True,
    # "GUEST_ROLE": "Public",
}
PUBLIC_ROLE_LIKE = "Gamma"
TALISMAN_ENABLED = False

ENABLE_CORS = True
CORS_OPTIONS = {
    "supports_credentials": True,
    "allow_headers": ["*"],
    "expose_headers": ["*"],
    "resources": ["*"],
    "origins": ["http://localhost:3000", "http://localhost:8000"]
}

ENABLE_GUEST_TOKEN = True
GUEST_TOKEN_JWT_EXP_SECONDS = 18000


WTF_CSRF_ENABLED = False
# WTF_CSRF_EXEMPT_LIST = [r"^/api/v1/security/guest_token/?$", r"^/superset/embedded/.*$"]

# OVERRIDE_HTTP_HEADERS = {
#     "X-Frame-Options": "ALLOWALL"  # Cho phép iframe
# }