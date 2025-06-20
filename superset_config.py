
FEATURE_FLAGS = {
    "EMBEDDED_SUPERSET": True
    }
PUBLIC_ROLE_LIKE = "Gamma"
TALISMAN_ENABLED = False

ENABLE_CORS = True
CORS_OPTIONS = {
    "supports_credentials": True,
    "allow_headers": ["*"],
    "expose_headers": ["*"],
    "resources": ["*"],
    "origins": ["http://localhost:3000", "http://localhost:8000","https://fe-shopee-project.onrender.com","https://be-shopee-project.onrender.com"]
}

ENABLE_GUEST_TOKEN = True
GUEST_TOKEN_JWT_EXP_SECONDS = 18000


WTF_CSRF_ENABLED = False
