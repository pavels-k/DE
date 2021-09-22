select A_col,C_col, 
MAX(B_col) OVER(partition by C_col) as lag_B
from table1 t