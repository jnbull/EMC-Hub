from docx import Document
import zipfile
from bs4 import BeautifulSoup

filename = './assets/files/Offsite Equipment List - VD1.0.docx'

# if str(magLoop) == 'None':
#     print('GEMC 22')
# elif str(magLoop) == '<w:result w:val="1"/>':
#     print('GEMC 313')
# elif str(magLoop) == '<w:result w:val="2"/>':
#     print('GEMC 136')

def parseChecklist(checklist):
    # Open as XML
    unzipped = zipfile.ZipFile(checklist)
    xml_data = unzipped.read('word/document.xml')
    unzipped.close()
    soup = BeautifulSoup(xml_data, 'xml')

    # Find Tables & Rows
    assetList = []
    tables = soup.findAll('tbl')
    for i in range(len(tables)):
        rows = tables[i].findAll('tr')
        for j in range(len(rows)):
            checks = rows[j].find('checkBox')
            if checks != None:
                checked = str(checks.find('checked'))
                if checked == '<w:checked/>':
                    dropdown = rows[j].find('ddList')
                    if dropdown != None:
                        asset = dropdown.find('result')
                        output = {
                            'table': i,
                            'row': j,
                            'asset': asset
                        }
                        assetList.append(output)
                    elif dropdown == None:
                        cells = rows[j].findAll('tc')
                        asset = cells[2].find('t')
                        if asset.text != 'N/A':
                            output = {
                                'table': i,
                                'row': j,
                                'asset': asset.text
                            }
                            assetList.append(output)
                        
    
    # Return list of assets to be verified
    return assetList
                
print(parseChecklist(filename))
