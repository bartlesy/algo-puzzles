import numpy as np

def get_changes(before: list, after: list):
    before_dict = {x: i for i, x in enumerate(before)}
    after_dict = {x: i for i, x in enumerate(after)}
    changes = []
    for ele, before_idx in before_dict.items():
        after_idx = after_dict.get(ele, -1)
        if after_idx == -1:
            changes.append([ele, 'deleted'])
        elif after_idx != before_idx:
            changes.append([ele, f"moved from {before_idx}->{after_idx}"])
            del after_dict[ele]
    if after_dict:
        changes.extend([[ele, "added"] for ele in after_dict.keys()])
    return changes



a1 = np.random.randint(low=0, high=69, size=int(1e8))
a2 = np.random.randint(low=0, high=69, size=int(1e8))
get_changes(a1, a2)
