

import pandas as pd


#read in supplementary table
drugInfo = pd.read_csv("Drug_Info_Supp_Table.csv")

#group all drugs by their type and turn into dictionary
    # do we want to group by type or to group by targets specifically? (would create many more groups/duplicates)
drugTypes = drugInfo.groupby("Type")["Drug"].apply(list).to_dict()

#print dictionary
# for type, drugs in drugTypes.items():
#     print(f"{type}: {drugs}")


# loop through the dictionary
for type, drugNames in drugTypes.items():
    # for each key (drug type), go through each of the drugs
    for drug in drugNames:
        # make a string with the drug name + _ALL.txt 
        drugFileName = f"{drug}_ALL.txt"

        # use FTP to get that file from the server
        from ftplib import FTP

        ftp = FTP("massive-ftp.ucsd.edu")
        ftp.login()
    
        ftp.cwd("/v06/MSV000093659/other/Dose response data - Jurkat proteome")

        drugPath = f"{drug}/TXTs_Classified"
        ftp.cwd(drugPath)
        print(drugPath)

        # write the file in binary mode
        with open(drugFileName, "wb") as file:
            # download the file "RETR fileName"
            ftp.retrbinary(f"RETR {drugFileName}", file.write)
        ftp.quit()

        drugData = pd.read_csv(drugFileName, delimiter = "\t")

        # select the gene column
        # select the IC50 column
        # select the mean intensity column
        # rename the columns (IC50 and intensity) to include the name of the drug
        # add both of those columns to a new combined dataframe (Create this before the for loop!)
        # add any genes that aren't included as rows (??) how would this be possible if they all have slightly different genes? 


        # combining for just 2 drugs (SIRT inhibitors)

        selis = pd.read_csv("Selisistat_ALL.txt", delimiter = "\t")
        srt = pd.read_csv("SRT2104_ALL.txt", delimiter = "\t")

        #rename IC50 column to be the name of the drug
        selisRenamed = selis[["gene", "stdIC50", "Mean_Intensity"]].rename(columns={"stdIC50": "Selisistat_IC50", "Mean_Intensity" : "Selisistat_Intensity"})
        srtRenamed = srt[["gene", "stdIC50", "Mean_Intensity"]].rename(columns={"stdIC50": "SRT2104_IC50", "Mean_Intensity" : "SRT2104_Intensity"})

        # merge the 2 IC50 columns on the "gene" column
        combined = pd.merge(selisRenamed, srtRenamed, on="gene", how="outer")

        #set gene as index
        combined = combined.set_index("gene")

        combined.head()
    # start with just 1 drug type and try to combine them all (see code below) 


