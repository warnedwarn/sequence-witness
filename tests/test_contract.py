from pathlib import Path
import ast
S=(Path(__file__).parents[1]/'contracts/contract.py').read_text()
def test_parse():ast.parse(S)
def test_bound_consensus():assert "mine['verdict']==theirs.get('verdict')" in S and "mine['digests']==theirs.get('digests')" in S
