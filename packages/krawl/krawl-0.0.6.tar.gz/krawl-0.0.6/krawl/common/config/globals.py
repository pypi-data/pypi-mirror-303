from __future__ import annotations


class Folders:
    model_dir = "./krawl/common/ml_models/classifier/"
    save_dir = "./krawl/common/data/output/"


class Files:
    html_node_classifier = f"{Folders.model_dir}html_tag_clf.pkl"
    record_file = f"{Folders.save_dir}record.jsonl"
