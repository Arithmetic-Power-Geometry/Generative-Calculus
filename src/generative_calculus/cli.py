from __future__ import annotations
import argparse, json
from pathlib import Path
from .benchmarks import run_all
from .core import (
    blackwell_binary_deficiency,
    convex_reconstruction_identity,
    cyclic_reversal_cost,
    marginal_incompleteness_example,
    parity_projection_profile,
)


def main():
    p=argparse.ArgumentParser(prog='generative-calculus')
    sub=p.add_subparsers(dest='cmd',required=True)
    r=sub.add_parser('reproduce'); r.add_argument('--output',default='results')
    s=sub.add_parser('sensor'); s.add_argument('--source',type=float,default=.75); s.add_argument('--target',type=float,default=.90)
    m=sub.add_parser('marginal'); m.add_argument('--low',type=float,default=1); m.add_argument('--high',type=float,default=3); m.add_argument('--budget',type=float,default=1)
    q=sub.add_parser('projection'); q.add_argument('--m',type=int,default=5)
    c=sub.add_parser('reconstruction'); c.add_argument('--t',type=float,default=.73); c.add_argument('--steps',type=int,default=100)
    v=sub.add_parser('reversal'); v.add_argument('--n',type=int,default=10)
    a=p.parse_args()
    if a.cmd=='reproduce':
        print(json.dumps(run_all(Path(a.output)),indent=2,default=str))
    elif a.cmd=='sensor':
        print(blackwell_binary_deficiency(a.source,a.target))
    elif a.cmd=='marginal':
        print(json.dumps(marginal_incompleteness_example(a.low,a.high,a.budget),indent=2,default=str))
    elif a.cmd=='projection':
        print(json.dumps(parity_projection_profile(a.m),indent=2))
    elif a.cmd=='reconstruction':
        print(json.dumps(convex_reconstruction_identity([(0,0),(2,0),(0,1)],[(0,0),(1,0),(0,3)],a.t,a.steps),indent=2))
    elif a.cmd=='reversal':
        print(json.dumps(cyclic_reversal_cost(a.n),indent=2))

if __name__=='__main__':
    main()
