;  depth   = 3
;  nconst  = 3
;  assertions = 4
;  timeout = 10
;  time    = {'../SMT_Solvers/QF_S/cvc4/run.sh': 0.03368830680847168, '../SMT_Solvers/QF_S/z3str3/run.sh': 0.05425429344177246}
;  score   = 0.03368830680847168
;  result  = {'../SMT_Solvers/QF_S/cvc4/run.sh': 'unsat', '../SMT_Solvers/QF_S/z3str3/run.sh': 'unsat'}
(set-logic QF_S)(declare-fun var0 () String)(declare-fun var1 () String)(declare-fun var2 () String)(declare-fun var3 () Int)(declare-fun var4 () Int)(declare-fun var5 () Int)(declare-fun var6 () Bool)(declare-fun var7 () Bool)(declare-fun var8 () Bool)(assert (< (str.indexof var2 var0 var4) (str.indexof var2 var2 var4)))(assert (< (str.len var0) (str.len var0)))(assert (<= (str.indexof var1 var1 var5) (str.len var1)))(assert (<= (str.indexof (str.replace var1 var0 var1) (str.replace var2 var2 var1) (str.len var1)) (str.len var0)))(check-sat)