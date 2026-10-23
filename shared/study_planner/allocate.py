from ..contract import Task
from ..contract import Block 

def allocate(tasks: list[Task], hours: float) -> list[Block]:
    block_list: list[Block] = []
    for task in tasks:
        if (hours <= 0):
            break
        using_hour = min(hours, task.effort_h) 
        block_list.append(Block(task, using_hour))
        hours -= using_hour
    return block_list
