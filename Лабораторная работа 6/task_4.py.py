import json

INPUT_FILE = 'input.csv'


def csv_to_list_dict(filename, delimiter=',', new_line='\n') -> list[dict]:
    with open(filename) as f:
        list_ = []
        for ind, ln in enumerate(f):
            fields = ln.strip(new_line).split(delimiter)
            if ind == 0:
                heads = fields
                continue
            list_.append({})
            for i, _ in enumerate(heads):
                list_[-1][heads[i]] = fields[i]
    return list_
      # TODO реализовать конвертер из csv в json


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
