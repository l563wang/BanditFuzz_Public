;  depth   = 3
;  nconst  = 3
;  assertions = 4
;  timeout = 10
;  time    = {'../SMT_Solvers/QF_S/cvc4/run.sh': 0.03631901741027832, '../SMT_Solvers/QF_S/z3str3/run.sh': 0.046602487564086914}
;  score   = 0.03631901741027832
;  result  = {'../SMT_Solvers/QF_S/cvc4/run.sh': 'unsat', '../SMT_Solvers/QF_S/z3str3/run.sh': 'unsat'}
(set-logic QF_S)(declare-fun var0 () String)(declare-fun var1 () String)(declare-fun var2 () String)(declare-fun var3 () Int)(declare-fun var4 () Int)(declare-fun var5 () Int)(declare-fun var6 () Bool)(declare-fun var7 () Bool)(declare-fun var8 () Bool)(assert (< (str.len var1) (str.indexof (str.at var2 var3) (str.substr var2 var4 var4) (str.indexof var0 var0 10))))(assert (str.contains (str.replace var1 var2 var1) (str.substr var1 var4 var3)))(assert (< (str.len var1) (str.indexof var1 var0 var5)))(assert (str.in.re (str.at var2 var4) (re.* re.allchar)))(check-sat)