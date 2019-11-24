# Home Cost Calculator

## Arguments

| Argument              | Description                                    | Example |
|-----------------------|------------------------------------------------|---------|
| -min                  | Starting home sale price in dollars.           | 80000   |
| -max                  | Ending home sale price in dollars.             | 400000  |
| -interval             | Interval to generate table results in dollars. | 10000   |
| -mortgage_rate        | Mortgage loan rate in percent.                 | 3.725   |
| -percent_down         | Mortgage down payment in percent.              | 20      |
| -closing_cost_rate    | Closing cost in percent.                       | 1.13    |
| -pmi_rate             | Rate of PMI insurance in percent.              | 1       |
| -tax_rate             | Property tax rate in percent.                  | 1.323   |
| -homeowners_insurance | Cost of insurance for a year in dollars.       | 2000    |
| -loan_length          | Length of mortgage in years.                   | 30      |
| -gross_income         | Income before taxes, expenses, etc in dollars. | 80000   |

## Example Useage

```python
homecostcalculator.py -min 80000 -max 400000 -interval 10000 -mortgage_rate 3.725 -percent_down 10 -closing_cost_rate 1.13 -pmi_rate 1 -tax_rate 1.323 -homeowners_insurance 2000 -loan_length 30 -gross_income 80000
```

## Example Results

|   House Cost |   Mortgage |   Initial Saved |   Monthly Payment |   Non-PMI Monthly Payment |   Total PMI |   Total Tax |   Total Home Insurance |   Total Cost |
|--------------|------------|-----------------|-------------------|---------------------------|-------------|-------------|------------------------|--------------|
|        80000 |      72000 |            8904 |           647.289 |                   587.289 |      4020   |       31752 |                  60000 |       215444 |
|        90000 |      81000 |           10017 |           707.367 |                   639.867 |      4522.5 |       35721 |                  60000 |       234875 |
|       100000 |      90000 |           11130 |           767.445 |                   692.445 |      5025   |       39690 |                  60000 |       254305 |
|       110000 |      99000 |           12243 |           827.523 |                   745.023 |      5527.5 |       43659 |                  60000 |       273736 |
|       120000 |     108000 |           13356 |           887.601 |                   797.601 |      6030   |       47628 |                  60000 |       293166 |
|       130000 |     117000 |           14469 |           947.678 |                   850.178 |      6532.5 |       51597 |                  60000 |       312597 |
|       140000 |     126000 |           15582 |          1007.76  |                   902.756 |      7035   |       55566 |                  60000 |       332027 |
|       150000 |     135000 |           16695 |          1067.83  |                   955.334 |      7537.5 |       59535 |                  60000 |       351458 |
|       160000 |     144000 |           17808 |          1127.91  |                  1007.91  |      8040   |       63504 |                  60000 |       370888 |
|       170000 |     153000 |           18921 |          1187.99  |                  1060.49  |      8542.5 |       67473 |                  60000 |       390319 |
|       180000 |     162000 |           20034 |          1248.07  |                  1113.07  |      9045   |       71442 |                  60000 |       409749 |
|       190000 |     171000 |           21147 |          1308.15  |                  1165.65  |      9547.5 |       75411 |                  60000 |       429180 |
|       200000 |     180000 |           22260 |          1368.22  |                  1218.22  |     10050   |       79380 |                  60000 |       448610 |
|       210000 |     189000 |           23373 |          1428.3   |                  1270.8   |     10552.5 |       83349 |                  60000 |       468041 |
|       220000 |     198000 |           24486 |          1488.38  |                  1323.38  |     11055   |       87318 |                  60000 |       487471 |
|       230000 |     207000 |           25599 |          1548.46  |                  1375.96  |     11557.5 |       91287 |                  60000 |       506902 |
|       240000 |     216000 |           26712 |          1608.53  |                  1428.53  |     12060   |       95256 |                  60000 |       526332 |
|       250000 |     225000 |           27825 |          1668.61  |                  1481.11  |     12562.5 |       99225 |                  60000 |       545763 |
|       260000 |     234000 |           28938 |          1728.69  |                  1533.69  |     13065   |      103194 |                  60000 |       565194 |
|       270000 |     243000 |           30051 |          1788.77  |                  1586.27  |     13567.5 |      107163 |                  60000 |       584624 |
|       280000 |     252000 |           31164 |          1848.85  |                  1638.85  |     14070   |      111132 |                  60000 |       604055 |
|       290000 |     261000 |           32277 |          1908.92  |                  1691.42  |     14572.5 |      115101 |                  60000 |       623485 |
|       300000 |     270000 |           33390 |          1969     |                  1744     |     15075   |      119070 |                  60000 |       642916 |
|       310000 |     279000 |           34503 |          2029.08  |                  1796.58  |     15577.5 |      123039 |                  60000 |       662346 |
|       320000 |     288000 |           35616 |          2089.16  |                  1849.16  |     16080   |      127008 |                  60000 |       681777 |
|       330000 |     297000 |           36729 |          2149.24  |                  1901.74  |     16582.5 |      130977 |                  60000 |       701207 |
|       340000 |     306000 |           37842 |          2209.31  |                  1954.31  |     17085   |      134946 |                  60000 |       720638 |
|       350000 |     315000 |           38955 |          2269.39  |                  2006.89  |     17587.5 |      138915 |                  60000 |       740068 |
|       360000 |     324000 |           40068 |          2329.47  |                  2059.47  |     18090   |      142884 |                  60000 |       759499 |
|       370000 |     333000 |           41181 |          2389.55  |                  2112.05  |     18592.5 |      146853 |                  60000 |       778929 |
|       380000 |     342000 |           42294 |          2449.62  |                  2164.62  |     19095   |      150822 |                  60000 |       798360 |
|       390000 |     351000 |           43407 |          2509.7   |                  2217.2   |     19597.5 |      154791 |                  60000 |       817790 |
|       400000 |     360000 |           44520 |          2569.78  |                  2269.78  |     20100   |      158760 |                  60000 |       837221 |

You can afford a house priced at $280000 or less.