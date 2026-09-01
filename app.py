from __future__ import annotations
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent/'src'))

import gradio as gr
import pandas as pd
from generative_calculus.core import (
    blackwell_binary_deficiency,
    canonical_reachability_system,
    convex_reconstruction_identity,
    cyclic_reversal_cost,
    equality_costs,
    feasible,
    generative_order_parity,
    marginal_incompleteness_example,
    parity_projection_profile,
    reachable_transport_audit,
    exact_program_qubits,
)


def sensor(source,target):
    d=blackwell_binary_deficiency(source,target)
    return pd.DataFrame([{'source_accuracy':source,'target_accuracy':target,'minimax_TV_deficiency':d,'exactly_simulable':d<1e-12}])


def pareto(low,high,budget_t,budget_e):
    ex=marginal_incompleteness_example(low,high,low)
    rows=[]
    for name,F in [('A',ex['A']),('B',ex['B'])]:
        rows.extend([{'world':name,'time':p[0],'energy':p[1]} for p in F])
    verdict=pd.DataFrame([{'budget_time':budget_t,'budget_energy':budget_e,
        'A_feasible':feasible(ex['A'],(budget_t,budget_e)), 'B_feasible':feasible(ex['B'],(budget_t,budget_e)),
        'A_coordinate_minima':str(ex['marginal_A']),'B_coordinate_minima':str(ex['marginal_B']),
        'coupling_gap':ex['coupling_gap']}])
    return pd.DataFrame(rows),verdict


def equality(n,epsilon):
    return pd.DataFrame([equality_costs(int(n),epsilon)])


def projection(m):
    rows=parity_projection_profile(int(m))
    return pd.DataFrame(rows), pd.DataFrame([{'m':int(m),'generative_order_rG':generative_order_parity(int(m))}])


def reconstruction(t,steps,directions):
    r=convex_reconstruction_identity([(0,0),(2,0),(0,1)],[(0,0),(1,0),(0,3)],float(t),int(steps),int(directions))
    return pd.DataFrame([r])


def reversal(n):
    return pd.DataFrame([cyclic_reversal_cost(int(n))])


def reachability(max_budget):
    graph,task_at=canonical_reachability_system()
    rows=reachable_transport_audit(graph,task_at,int(max_budget))
    df=pd.DataFrame(rows)
    return df, pd.DataFrame([{'rows':len(df),'all_transport_inclusions_hold':bool(df.transport_holds.all())}])


def program_bound(g):
    return pd.DataFrame([{'exact_generator_count':int(g),'minimum_program_qubits':exact_program_qubits(int(g))}])


def mlperf_table():
    base=Path(__file__).parent/'results'/'tables'
    parts=[]
    for name in ['mlperf_power_public_subset.csv','mlperf_portfolio_feasibility.csv','mlperf_synthetic_marginal_ideal.csv']:
        p=base/name
        if p.exists():
            df=pd.read_csv(p); df.insert(0,'source_table',name); parts.append(df.astype(str))
    return pd.concat(parts,ignore_index=True) if parts else pd.DataFrame([{'status':'Run reproduction first.'}])


def audits():
    base=Path(__file__).parent/'results'/'reports'
    return pd.read_csv(base/'novelty_scores.csv'), pd.read_csv(base/'theorem_status.csv'), pd.read_csv(base/'problem_comparison.csv')


with gr.Blocks(title='Generative Calculus v2.0') as demo:
    gr.Markdown('# Generative Calculus v2.0 — Embodied Operational Envelope Lab\nEvery tab labels validation reductions separately from scoped Generative Calculus results. No experimentally established new law of physics is claimed.')
    with gr.Tab('Blackwell / Le Cam'):
        s=gr.Slider(.5,1,.75,step=.01,label='Source accuracy'); t=gr.Slider(.5,1,.90,step=.01,label='Target accuracy')
        b=gr.Button('Compute'); o=gr.Dataframe(); b.click(sensor,[s,t],o)
    with gr.Tab('Marginal incompleteness'):
        lo=gr.Number(1,label='Low cost'); hi=gr.Number(3,label='High cost'); bt=gr.Number(1,label='Time budget'); be=gr.Number(1,label='Energy budget')
        b=gr.Button('Evaluate'); f=gr.Dataframe(); v=gr.Dataframe(); b.click(pareto,[lo,hi,bt,be],[f,v])
    with gr.Tab('Projection irreducibility'):
        m=gr.Slider(2,12,5,step=1,label='Number of capability coordinates m')
        b=gr.Button('Audit all projection orders'); p1=gr.Dataframe(); p2=gr.Dataframe(); b.click(projection,[m],[p1,p2])
    with gr.Tab('Convex reconstruction'):
        tt=gr.Slider(0,1,.73,step=.01,label='Path time t'); st=gr.Slider(1,500,100,step=1,label='Integration steps'); dr=gr.Slider(36,1440,720,step=36,label='Support directions')
        b=gr.Button('Reconstruct'); rr=gr.Dataframe(); b.click(reconstruction,[tt,st,dr],rr)
    with gr.Tab('Scalable reversal cost'):
        n=gr.Slider(1,30,10,step=1,label='n (cycle period 2^n)'); b=gr.Button('Compute'); r=gr.Dataframe(); b.click(reversal,[n],r)
    with gr.Tab('Reachable-envelope transport'):
        mb=gr.Slider(1,50,15,step=1,label='Maximum audited budget'); b=gr.Button('Audit theorem'); r1=gr.Dataframe(); r2=gr.Dataframe(); b.click(reachability,[mb],[r1,r2])
    with gr.Tab('Exact generator programmability'):
        g=gr.Slider(1,1048576,1024,step=1,label='Exact primitive generators'); b=gr.Button('Compute no-programming corollary'); oo=gr.Dataframe(); b.click(program_bound,[g],oo)
    with gr.Tab('Equality scaling'):
        n=gr.Slider(2,4096,128,step=1,label='Input length'); eps=gr.Slider(.01,.49,1/3,step=.01,label='Error tolerance')
        b=gr.Button('Compute'); oo=gr.Dataframe(); b.click(equality,[n,eps],oo)
    with gr.Tab('Public MLPerf Power'):
        b=gr.Button('Load reproduced public-data audit'); oo=gr.Dataframe(); b.click(mlperf_table,[],oo)
    with gr.Tab('Novelty / theorem audit'):
        b=gr.Button('Load audited matrices'); n1=gr.Dataframe(); n2=gr.Dataframe(); n3=gr.Dataframe(); b.click(audits,[],[n1,n2,n3])

if __name__=='__main__':
    demo.launch()
