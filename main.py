


# # loop through the dictionary
# for type, drugNames in drugTypes.items():
#     combined = pd.DataFrame()
#     # for each key (drug type), go through each of the drugs
#     for drug in drugNames:
#         # make a string with the drug name + _ALL.txt 
#         drugFileName = f"{drug}_ALL.txt"

#         # use FTP to get that file from the server

#         drugPath = f"{drug}/TXTs_Classified"
#         ftp.cwd(drugPath)
#         print(drugPath)

#         # write the file in binary mode
#         with open(drugFileName, "wb") as file:
#             # download the file "RETR fileName"
#             ftp.retrbinary(f"RETR {drugFileName}", file.write)
#         ftp.quit()


#         drugData = pd.read_csv(drugFileName, delimiter = "\t") 
#         # select the gene and mean intensity columns (maybe add IC50 later?)     
#         meanData = drugData[["gene", "Mean_Intensity"]]
#         # rename mean intensity column to include the name of the drug
#         renamedData = meanData.rename(columns = {"Mean_Intensity":f"{drug}_Mean_Intensity"})
#         # add both of those columns to a new combined dataframe (Create this before the for loop?)
#         combined = pd.merge(combined, renamedData, how = "outer", on = "gene")

#         combined.head()

