
    type proposition = 
      False | 
      True | 
      Var of string | 
      And of proposition * proposition | 
      Or of proposition * proposition | 
      Not of proposition | 
      Imply of proposition * proposition | 
      Equiv of proposition * proposition | 
      If of proposition * proposition * proposition ;;




let rec ifify p =

match p
with False -> p |
True ->  p |
Var a -> p |
And(a, b) -> If(ifify a, ifify b, False) |
Or(a, b) -> If(ifify a, True, ifify b) |
Not a -> If(ifify a, False, True) |
Imply(a,b) -> If(ifify a, ifify b, True) |
Equiv(a,b) -> If(ifify a, ifify b, (If(ifify b, False, True))) |
If(a,b,a1) -> p ;;


print_string "Hello world!\n" ;;