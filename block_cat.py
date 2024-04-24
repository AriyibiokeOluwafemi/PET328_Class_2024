def classify_block(i, j, nx, ny):
   i = int(input('What is the column index of the gridblock?'))
   j = int(input('What is the row index of the gridblock?'))
   nx = int(input('How may columns are there in the discerized reservoir?'))
   ny = int(input('How may rows are there in the discerized reservoir?'))
   if (i == 1 and j == 1) or (i == 1 and j == ny) or (i == nx and j == 1) or (i == nx and j == ny):
       block_cat = 'IV'
   elif j==1 or j==ny:
        block_cat = 'II'
   elif i==1 or i==nx:
        block_cat = 'III'
   else:
        block_cat = 'I'
   return block_cat
   return classify_block
