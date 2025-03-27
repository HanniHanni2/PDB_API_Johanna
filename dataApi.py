import os
import requests  # installera requests "pip install requests"

def download_pdb(pdb_ids, save_dir= "/home/ocra/Documents/pdb_files"): ##skapa mappen pdb_files själv för hand. byt till rätt user
    base_url = "https://files.rcsb.org/download/{}.pdb"



    for pdb_id in pdb_ids:
        pdb_id =pdb_id.strip().upper()
        url= base_url.format(pdb_id)
        response= requests.get(url)

        if response.status_code == 200:
            file_path = os.path.join(save_dir, f"{pdb_id}.pdb")
            with open(file_path, "wb") as f:
                f.write(response.content)
        else: print("failed")


pdb_list= ["1CRN", "4HHB"] ##byt mot önskad lista
download_pdb(pdb_list)