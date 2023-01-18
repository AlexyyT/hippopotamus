import pickle

filename = 'C:\\Users\\ATOU\\OneDrive - Axess OnLine\\Documents\\1. PROJETS\\PYTHON - ANALYSE DE SENTIMENTS\\CODE\\DATA\\df_Yext'
infile = open(filename, 'rb')
df = pickle.load(infile)
infile.close()


#print(reviews[0][0])
print(df["Review"].values[0])



