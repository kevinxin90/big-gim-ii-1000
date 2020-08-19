import csv
import os
from biothings.utils.dataload import dict_sweep


def load_data(data_folder):
    path = os.path.join(data_folder, "big-gim-ii-1000-genes-edges.tsv")
    with open(path) as f:
        reader = csv.reader(f, delimiter='\t')
        next(reader)
        for row in reader:
            yield dict_sweep({
                "_id": row[0].replace(':', '_') + '-' + row[4].replace(':', '_') + '-' + row[11].replace(':', '_').replace('NA', '') + '-' + row[13].replace(':', '_').replace('NA', ''),
                "subject": {
                    "id": row[0],
                    "HGNC": int(row[0].split(':')[-1]),
                    "NCBIGene": int(row[1]),
                    "SYMBOL": row[2],
                    "type": "gene"
                },
                "object": {
                    "id": row[4],
                    "HGNC": int(row[4].split(':')[-1]),
                    "NCBIGene": int(row[5]),
                    "SYMBOL": row[6],
                    "type": "gene"
                },
                "association": {
                    "edge_label": row[3],
                    "relation_id": row[7],
                    "relation_name": row[8].replace(' ', '_'),
                    "correlation": float(row[9]),
                    "pvalue": float(row[10]),
                    "context": {
                        "tissue": {
                            "id": row[11],
                            "UBERON": row[11],
                            "name": row[12]
                        },
                        "disease": {
                            "id": row[13],
                            "UBERON": row[13],
                            "name": row[14]
                        }
                    }
                }
            }, vals=['NA'])
