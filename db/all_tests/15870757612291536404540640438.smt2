;  depth   = 3
;  nconst  = 3
;  assertions = 4
;  timeout = 10
;  time    = {'../SMT_Solvers/QF_S/cvc4/run.sh': 0.046195030212402344, '../SMT_Solvers/QF_S/z3str3/run.sh': 0.09127044677734375}
;  score   = 0.046195030212402344
;  result  = {'../SMT_Solvers/QF_S/cvc4/run.sh': 'sat', '../SMT_Solvers/QF_S/z3str3/run.sh': 'sat'}
(set-logic QF_S)(declare-fun var0 () String)(declare-fun var1 () String)(declare-fun var2 () String)(declare-fun var3 () Int)(declare-fun var4 () Int)(declare-fun var5 () Int)(declare-fun var6 () Bool)(declare-fun var7 () Bool)(declare-fun var8 () Bool)(assert (str.prefixof (str.at "@]F@q9d{\\K" var4) (str.substr var2 var5 var3)))(assert (str.prefixof (str.replace var1 var2 var2) (str.replace var0 var2 var2)))(assert (>= (str.len (str.substr var0 var5 var3)) (str.len (str.substr var2 var4 var5))))(assert (str.suffixof (str.substr (str.at var2 var5) (str.len var2) (str.indexof var1 var0 var3)) (str.substr var2 var4 var5)))(check-sat)