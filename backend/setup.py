import getpass
import os
import subprocess
import sys


def colored(text, color):
    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "purple": "\033[95m",
        "end": "\033[0m",
    }
    return f"{colors.get(color, '')}{text}{colors['end']}"


def print_banner(message, color="blue"):
    width = len(message) + 4
    print(colored("┌" + "─" * width + "┐", color))
    print(colored("│  " + message + "  │", color))
    print(colored("└" + "─" * width + "┘", color))


def get_input(prompt, default=None):
    if default:
        user_input = input(f"{prompt} [{default}]: ")
        return user_input if user_input else default
    return input(f"{prompt}: ")


def setup_env():
    print_banner("FastAPI Environment Setup", "blue")

    # Choose which environment to configure
    while True:
        env_type = get_input(
            "Which environment do you want to configure? (development/production)",
            "development",
        ).lower()

        if env_type in ["development", "production"]:
            break
        print(colored("Please enter either 'development' or 'production'", "red"))

    # Common settings
    settings = {
        "ENVIRONMENT": env_type,
        "TITLE": get_input("Project title", "My FastAPI Project"),
        "DESCRIPTION": get_input("Project description", "API Documentation"),
        "VERSION": get_input("API version", "0.1.0"),
    }

    # Database settings
    print_banner("Database Configuration", "green")
    settings["POSTGRES_USER"] = get_input("Database user", "postgres")
    settings["POSTGRES_PASSWORD"] = (
        getpass.getpass("Database password (hidden): ") or "postgres"
    )
    settings["POSTGRES_HOST"] = get_input("Database host", "localhost")
    settings["POSTGRES_PORT"] = get_input("Database port", "5432")
    settings["POSTGRES_DB"] = get_input("Database name", "myapp")

    # API settings
    print_banner("API Configuration", "green")
    settings["API_HOST"] = get_input("API host", "0.0.0.0")
    settings["API_PORT"] = get_input("API port", "8000")

    if env_type == "development":
        settings["FRONTEND_ORIGIN"] = get_input(
            "Frontend origin", "http://localhost:5173"
        )
    else:
        settings["FRONTEND_ORIGIN"] = get_input(
            "Frontend origin", "https://myapp.example.com"
        )

    # JWT settings
    print_banner("Security Configuration", "green")
    if env_type == "development":
        settings["JWT_SECRET_KEY"] = get_input(
            "JWT secret key", "development_secret_key"
        )
    else:
        import secrets

        suggested_key = secrets.token_urlsafe(32)
        settings["JWT_SECRET_KEY"] = get_input("JWT secret key", suggested_key)

    settings["JWT_ALGORITHM"] = get_input("JWT algorithm", "HS256")

    # Redis settings
    print_banner("Redis Configuration", "green")
    settings["REDIS_HOST"] = get_input("Redis host", "localhost")
    settings["REDIS_PORT"] = get_input("Redis port", "6379")
    settings["REDIS_DB"] = get_input("Redis DB", "0")

    # Write to the file
    env_file = f".env.{env_type}"
    with open(env_file, "w") as file:
        for key, value in settings.items():
            file.write(f"{key}={value}\n")

    # If development, also create the default .env file
    if env_type == "development":
        with open(".env", "w") as f:
            for key, value in settings.items():
                f.write(f"{key}={value}\n")

    print_banner(f"Environment configured: {env_type.upper()}", "green")
    print(f"Configuration saved to {env_file}")

    if env_type == "development":
        print("A copy was also saved as .env (default)")

    return env_type


def activate_environment(env_type) -> bool:
    env_file = f".env.{env_type}"
    if not os.path.exists(env_file):
        print(colored(f"Error: {env_file} not found. Run setup first.", "red"))
        return False

    with open(env_file) as source, open(".env", "w") as target:
        target.write(source.read())

    color = "green" if env_type == "development" else "yellow"
    print_banner(f"Activated {env_type.upper()} environment", color)
    return True


def start_app(env_type):
    if env_type == "production":
        confirm = get_input(
            colored(
                "⚠️  You are about to start the app in PRODUCTION mode. "
                "Continue? (yes/no)",
                "yellow",
            ),
            "no",
        )
        if confirm.lower() != "yes":
            print("Operation cancelled.")
            return

    print_banner(
        f"Starting app in {env_type.upper()} mode",
        "green" if env_type == "development" else "yellow",
    )

    # Start the app using uvicorn
    cmd = ["uvicorn", "app.main:app"]
    if env_type == "development":
        cmd.append("--reload")

    subprocess.run(cmd)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:")
        print("  setup.py setup - Configure environment settings")
        print("  setup.py dev - Activate development environment")
        print("  setup.py prod - Activate production environment")
        print("  setup.py start - Start the app using current environment")
        print("  setup.py start:dev - Start the app in development mode")
        print("  setup.py start:prod - Start the app in production mode")
        sys.exit(1)

    command = sys.argv[1].lower()

    if command == "setup":
        env_type = setup_env()
    elif command == "dev":
        activate_environment("development")
    elif command == "prod":
        activate_environment("production")
    elif command == "start":
        # Read current environment from .env file
        if not os.path.exists(".env"):
            print(colored("Error: .env not found. Run setup first.", "red"))
            sys.exit(1)

        with open(".env") as f:
            for line in f:
                if line.startswith("ENVIRONMENT="):
                    env_type = line.split("=")[1].strip()
                    start_app(env_type)
                    break
    elif command.startswith("start:"):
        env_type = command.split(":")[1]
        if env_type in ["dev", "development"]:
            if activate_environment("development"):
                start_app("development")
        elif env_type in ["prod", "production"]:
            if activate_environment("production"):
                start_app("production")
        else:
            print(colored(f"Unknown environment: {env_type}", "red"))
    else:
        print(colored(f"Unknown command: {command}", "red"))
