"""Builds site/index.html from src/index.src.html, embedding assets/ita-logo.png as a data URI."""
import base64, pathlib
root = pathlib.Path(__file__).parent
logo = base64.b64encode((root / "assets/ita-logo.png").read_bytes()).decode()
src = (root / "src/index.src.html").read_text()
(root / "site/index.html").write_text(src.replace("__LOGO__", "data:image/png;base64," + logo))
print("built site/index.html")
