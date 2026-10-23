from shared.contract import Block


def render(blocks: list[Block]) -> str:
    """Render blocks in input order, with hours displayed to two decimal places.

    Include a total for every plan and a message when there are no blocks.
    """
    lines = ["Study plan:"]
    if not blocks:
        lines.append("No study blocks.")

    for block in blocks:
        lines.append(f"- {block.task.title}: {block.hours:.2f} h")

    total_hours = sum(block.hours for block in blocks)
    lines.append(f"Total: {total_hours:.2f} h")
    return "\n".join(lines)
