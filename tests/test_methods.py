"""Small numerical checks for use in an installed scientific runtime."""
import unittest

import numpy as np
import torch

import ast
import json
import math
import re
from pathlib import Path
import torch.nn.functional as F
ROOT = Path(__file__).resolve().parents[1]

def load_functions(filename, names):
    notebook = json.loads((ROOT/'notebooks'/filename).read_text(encoding='utf-8'))
    nodes = [node for cell in notebook['cells'] if cell['cell_type']=='code'
             for node in ast.parse(''.join(cell['source'])).body
             if isinstance(node, ast.FunctionDef) and node.name in names]
    assert {node.name for node in nodes} == set(names)
    namespace = {'np': np, 'torch': torch, 'F': F, 'math': math}
    exec(compile(ast.Module(body=nodes, type_ignores=[]), filename, 'exec'), namespace)
    return [namespace[name] for name in names]

attention, = load_functions('Attempt 3.ipynb', ['attention'])
topk_filtering, topp_filtering = load_functions('Notes on Attention and everything.ipynb', ['topk_filtering','topp_filtering'])
aggregate_tokens, = load_functions('Attempt 5.ipynb', ['aggregate_tokens'])
RE_PATTERN = re.compile(r'(?u)\b[a-zA-Z]{3,}\b')
jaccard, = load_functions('Attempt 6.ipynb', ['jaccard'])
score_chunks, segment_representations = load_functions('Attempt 7.ipynb', ['score_chunks','segment_representations'])


class MethodTests(unittest.TestCase):
    def test_topk_keeps_only_requested_support(self):
        values = topk_filtering(torch.tensor([0.4, 0.3, 0.2, 0.1]), k=2)
        self.assertEqual(torch.count_nonzero(values).item(), 2)
        self.assertAlmostEqual(values.sum().item(), 1.0, delta=1e-6)
        self.assertTrue(torch.equal(values[2:], torch.zeros(2)))

    def test_topp_includes_the_threshold_crossing_token(self):
        values = topp_filtering(torch.tensor([0.55, 0.30, 0.15]), p=0.6)
        self.assertEqual(torch.count_nonzero(values).item(), 2)
        self.assertAlmostEqual(values[0].item(), 0.55 / 0.85, places=6)
        self.assertAlmostEqual(values.sum().item(), 1.0, delta=1e-6)

    def test_attention_cannot_read_future_tokens(self):
        q = torch.eye(3)
        v = torch.arange(6.0).reshape(3, 2)
        out, weights = attention(q, q, v, torch.tril(torch.ones(3, 3)))
        self.assertTrue(torch.equal(torch.triu(weights, diagonal=1), torch.zeros(3, 3)))
        self.assertTrue(torch.allclose(weights.sum(dim=1), torch.ones(3)))
        self.assertTrue(torch.equal(out[0], v[0]))

    def test_word_aggregation_uses_only_overlapping_story_subwords(self):
        rows = aggregate_tokens(
            "A haunted house.", np.array([[0, 1], [2, 5], [5, 9], [10, 15], [15, 16]]),
            np.array([50.0, 2.0, 4.0, 3.0, 100.0]), RE_PATTERN,
            mask=np.array([False, True, True, True, False]),
        )
        self.assertEqual([row["word"] for row in rows], ["haunted", "house"])
        self.assertEqual(rows[0]["token_indices"], [1, 2])
        self.assertEqual(rows[0]["grad_mean"], 3.0)
        self.assertEqual(rows[1]["grad_mean"], 3.0)

    def test_segments_pool_their_own_spans(self):
        hidden = torch.tensor([[1.0, 0.0]] * 4 + [[0.0, 1.0]] * 4)
        vectors, spans = segment_representations(hidden, [0, 4, 8])
        self.assertEqual(spans, [(0, 4), (4, 8)])
        self.assertTrue(torch.equal(vectors, torch.eye(2)))
        scores = score_chunks(hidden, w=2)
        self.assertGreater(scores[4].item(), scores[2].item())

    def test_jaccard_uses_intersection_over_union(self):
        self.assertEqual(jaccard({"ghost", "house"}, {"house", "love"}), 1 / 3)


if __name__ == "__main__":
    unittest.main()
