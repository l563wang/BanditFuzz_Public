;  depth   = 3
;  nconst  = 3
;  assertions = 4
;  timeout = 10
;  time    = {'../SMT_Solvers/QF_S/cvc4/run.sh': 0.04318809509277344, '../SMT_Solvers/QF_S/z3str3/run.sh': 0.05918693542480469}
;  score   = 0.04318809509277344
;  result  = {'../SMT_Solvers/QF_S/cvc4/run.sh': 'unsat', '../SMT_Solvers/QF_S/z3str3/run.sh': 'unsat'}
(set-logic QF_S)(declare-fun var0 () String)(declare-fun var1 () String)(declare-fun var2 () String)(declare-fun var3 () Int)(declare-fun var4 () Int)(declare-fun var5 () Int)(declare-fun var6 () Bool)(declare-fun var7 () Bool)(declare-fun var8 () Bool)(assert (str.suffixof var2 var2))(assert (str.suffixof (str.replace (str.at var2 var3) (str.replace var2 var0 var1) (str.at var1 var4)) (str.at var0 var5)))(assert (not (str.contains var1 var1)))(assert (<= (str.indexof (str.at var1 var3) (str.substr var0 var3 var3) (str.len var0)) (str.len (str.replace var1 var1 var2))))(check-sat)