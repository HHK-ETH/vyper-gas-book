from pathlib import Path


def extract_gas_report(path: str, node: str) -> str:
    file = Path(path)

    if not file.exists():
        return "Report not available."

    contents = file.read_text().split(
        "[100%]"
    )  # split using [100%] as it's last line before gas printing

    return (
        "```"
        + contents[len(contents) - 1].replace(
            "\nINFO: Stopping '{node}' process.\n".format(node=node), ""
        )
        + "\n```"
    )  # Remove last line and put in code block


old_readme = Path("./README.md").read_text()

new_readme = "{old_readme}## Gas report \n\n### Hardhat\n{hardhat_gas_report}\n### Foundry (Anvil)\n{foundry_gas_report}"

Path("./README.md").write_text(
    new_readme.format(
        old_readme=old_readme.split("## Gas report")[0],
        hardhat_gas_report=extract_gas_report("./hardhat-gas-report", "Hardhat node"),
        foundry_gas_report=extract_gas_report("./foundry-gas-report", "anvil"),
    )
)
