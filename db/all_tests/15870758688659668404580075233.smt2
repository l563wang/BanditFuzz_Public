;  depth   = 3
;  nconst  = 3
;  assertions = 4
;  timeout = 10
;  time    = {'../SMT_Solvers/QF_S/cvc4/run.sh': 0.04794478416442871, '../SMT_Solvers/QF_S/z3str3/run.sh': 0.0630190372467041}
;  score   = 0.04794478416442871
;  result  = {'../SMT_Solvers/QF_S/cvc4/run.sh': 'sat', '../SMT_Solvers/QF_S/z3str3/run.sh': 'sat'}
(set-logic QF_S)(declare-fun var0 () String)(declare-fun var1 () String)(declare-fun var2 () String)(declare-fun var3 () Int)(declare-fun var4 () Int)(declare-fun var5 () Int)(declare-fun var6 () Bool)(declare-fun var7 () Bool)(declare-fun var8 () Bool)(assert (str.contains (str.at var2 var3) (str.replace (str.substr var2 var5 var3) (str.replace var1 var1 var1) (str.replace "S>'Own[x->" var2 var0))))(assert (not (> var4 var3)))(assert (not (str.in.re var1 re.allchar)))(assert (not var8))(check-sat)