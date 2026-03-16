"""Entry point for `python -m app` from the webapp/ directory."""
import sys
import webbrowser
import threading
import uvicorn

from app.config import settings


def open_browser():
    """Open the default browser after a short delay to let the server start."""
    import time
    time.sleep(1.0)

    # Detect first-run: open to /onboarding if no config.json
    from app.services import config_svc
    if config_svc.is_first_run():
        url = f"http://localhost:{settings.port}/onboarding"
    else:
        url = f"http://localhost:{settings.port}"

    webbrowser.open(url)


def main():
    # Open browser in background thread
    threading.Thread(target=open_browser, daemon=True).start()

    try:
        uvicorn.run(
            "app.main:app",
            host="127.0.0.1",
            port=settings.port,
            log_level="info",
        )
    except OSError as e:
        if "Address already in use" in str(e) or "address already in use" in str(e):
            print(f"\nError: Port {settings.port} is already in use.")
            print(f"Stop the other process or set a different port.")
            sys.exit(1)
        raise


if __name__ == "__main__":
    main()
