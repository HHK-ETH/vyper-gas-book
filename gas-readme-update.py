from pathlib import Path

contents = Path("./gas-report").read_text()

contents = contents.split(
    "[100%]"
)  # split using [100%] as it's last line before gas printing

gas_report = contents[len(contents) - 1].replace(
    "INFO: Stopping 'anvil' process.\n", ""
)  # Remove last line

readme = Path("./README.md").read_text()

readme = (
    readme.split("## Gas report")[0] + "## Gas report \n\n" + "```" + gas_report + "```"
)

Path("./README.md").write_text(readme)
