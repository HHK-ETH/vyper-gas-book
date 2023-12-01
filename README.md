# vyper-gas-book

## getting started

- `virtualenv venv`
- `source venv/bin/activate`
- `pip install -r requirements.txt`
- `ape compile`
- `ape test --network ethereum:local:foundry --gas`

## Gas report 

### Hardhat
Report not available.
### Foundry (Anvil)
```
================================= Gas Profile ==================================
                      OptimizedDiv Gas                      
                                                            
  Method     Times called    Min.    Max.    Mean   Median  
 ────────────────────────────────────────────────────────── 
  __init__              1    9830    9830    9830     9830  
  divide                1   21441   21441   21441    21441  
                                                            
                    NonOptimizedDiv Gas                     
                                                            
  Method     Times called    Min.    Max.    Mean   Median  
 ────────────────────────────────────────────────────────── 
  __init__              1   12230   12230   12230    12230  
  divide                1   21476   21476   21476    21476  
                                                            

============================== 2 passed in 0.66s ===============================
```