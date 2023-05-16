def compute_f1_between_dicts(pred_dict, label_dict):
    assert len(label_dict) > 0
    if len(pred_dict) == 0:
        return 0, 0, 0
    overlap = 0
    for k, v in pred_dict.items():
        if k in label_dict and v == label_dict[k]:
            overlap += 1

    precision = overlap / len(pred_dict)
    recall = overlap / len(label_dict)
    if precision + recall == 0:
        return 0, 0, 0
    else:
        f1 = 2 * precision * recall / (precision + recall)
    return precision, recall, f1
