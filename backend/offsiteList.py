from docx import Document
import zipfile
from bs4 import BeautifulSoup


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
                
def dropdownHandler(assetList):
    finalsList = []
    for item in assetList:
        if type(item['asset']) != str:
            value = str(item['asset'])

            # Table 2 - Verifications
            if item['table'] == 2:
                # Item 1 - Signal Generator
                if item['row'] == 5:
                    if value == 'None':
                        finalsList.append('GEMC 236')
                    elif value == '<w:result w:val="1"/>':
                        finalsList.append('GEMC 238')

            # Table 3 - Conducted Emissions
            if item['table'] == 3:
                # Item 1 - Spectrum Analyzer
                if item['row'] == 2:
                    if value == 'None':
                        finalsList.append('GEMC 160')
                    elif value == '<w:result w:val="1"/>':
                        finalsList.append('GEMC 198')
                    elif value == '<w:result w:val="2"/>':
                        finalsList.append('GEMC 232')
                    elif value == '<w:result w:val="3"/>':
                        finalsList.append('GEMC 234')

                # Item 1 - 10dB Attenuator
                if item['row'] == 7:
                    if value == 'None':
                        finalsList.append('GEMC 322')
                    elif value == '<w:result w:val="1"/>':
                        finalsList.append('GEMC 323')
                    elif value == '<w:result w:val="2"/>':
                        finalsList.append('GEMC 223')
                    elif value == '<w:result w:val="3"/>':
                        finalsList.append('GEMC 224')
                    elif value == '<w:result w:val="4"/>':
                        finalsList.append('GEMC 225')
                    elif value == '<w:result w:val="5"/>':
                        finalsList.append('GEMC 226')
                    elif value == '<w:result w:val="6"/>':
                        finalsList.append('GEMC 42')

            # Table 4 - Radiated Emissions
            if item['table'] == 4:
                # Item 1 - Spectrum Analyzer
                if item['row'] == 2:
                    if value == 'None':
                        finalsList.append('GEMC 160')
                    elif value == '<w:result w:val="1"/>':
                        finalsList.append('GEMC 198')
                    elif value == '<w:result w:val="2"/>':
                        finalsList.append('GEMC 232')
                    elif value == '<w:result w:val="3"/>':
                        finalsList.append('GEMC 234')
                
                # Item 2 - Preamplifier
                if item['row'] == 3:
                    if value == 'None':
                        finalsList.append('GEMC 168')
                    elif value == '<w:result w:val="1"/>':
                        finalsList.append('GEMC 221')
                    elif value == '<w:result w:val="2"/>':
                        finalsList.append('GEMC 243')
                    elif value == '<w:result w:val="3"/>':
                        finalsList.append('GEMC 244')
                    elif value == '<w:result w:val="4"/>':
                        finalsList.append('GEMC 301')

                # Item 3 - BiLog Antenna
                if item['row'] == 4:
                    if value == 'None':
                        finalsList.append('GEMC 8')
                    elif value == '<w:result w:val="1"/>':
                        finalsList.append('GEMC 137')
                    elif value == '<w:result w:val="2"/>':
                        finalsList.append('GEMC 201')
                    elif value == '<w:result w:val="3"/>':
                        finalsList.append('GEMC 231')

                # Item 4 - Horn Antenna
                if item['row'] == 5:
                    if value == 'None':
                        finalsList.append('GEMC 214')
                    elif value == '<w:result w:val="1"/>':
                        finalsList.append('GEMC 235')
                
                # Item 5 - 6dB Attenuator
                if item['row'] == 6:
                    if value == 'None':
                        finalsList.append('GEMC 286')
                    elif value == '<w:result w:val="1"/>':
                        finalsList.append('GEMC 287')
                    elif value == '<w:result w:val="2"/>':
                        finalsList.append('GEMC 288')
                    elif value == '<w:result w:val="3"/>':
                        finalsList.append('GEMC 289')
                    elif value == '<w:result w:val="4"/>':
                        finalsList.append('GEMC 290')
                    elif value == '<w:result w:val="5"/>':
                        finalsList.append('GEMC 41')
                 

            # Table 5 - ESD
            if item['table'] == 5:
                # Item 1 - ESD Gun
                if item['row'] == 2:
                    if value == 'None':
                        finalsList.append('GEMC 1')
                    elif value == '<w:result w:val="1"/>':
                        finalsList.append('GEMC 130')
                    elif value == '<w:result w:val="2"/>':
                        finalsList.append('GEMC 299')

            # Table 6 - Conducted Immunity
            if item['table'] == 6:
                # Item 1 - Signal Generator
                if item['row'] == 2:
                    if value == 'None':
                        finalsList.append('GEMC 236')
                    elif value == '<w:result w:val="1"/>':
                        finalsList.append('GEMC 238')

                # Item 2 - LF Amplifier
                if item['row'] == 3:
                    if value == 'None':
                        finalsList.append('GEMC 298')
                    elif value == '<w:result w:val="1"/>':
                        finalsList.append('GEMC 192')
                    elif value == '<w:result w:val="2"/>':
                        finalsList.append('GEMC 179')
                
                # Item 3 - HF Amplifier
                if item['row'] == 4:
                    if value == 'None':
                        finalsList.append('GEMC 263')
                    elif value == '<w:result w:val="1"/>':
                        finalsList.append('GEMC 185')

                # Item 4 - BiLog Antenna
                if item['row'] == 5:
                    if value == 'None':
                        finalsList.append('GEMC 8')
                    elif value == '<w:result w:val="1"/>':
                        finalsList.append('GEMC 137')
                    elif value == '<w:result w:val="2"/>':
                        finalsList.append('GEMC 201')
                    elif value == '<w:result w:val="3"/>':
                        finalsList.append('GEMC 231')

                # Item 5 - Horn Antenna
                if item['row'] == 6:
                    if value == 'None':
                        finalsList.append('GEMC 214')
                    elif value == '<w:result w:val="1"/>':
                        finalsList.append('GEMC 235')
            
            # Table 9 - Conducted Immunity
            if item['table'] == 9:
                # Item 1 - Signal Generator
                if item['row'] == 2:
                    if value == 'None':
                        finalsList.append('GEMC 155')
                    elif value == '<w:result w:val="1"/>':
                        finalsList.append('GEMC 236')
                    elif value == '<w:result w:val="2"/>':
                        finalsList.append('GEMC 6330')

                # Item 2 - Amplifier
                if item['row'] == 3:
                    if value == 'None':
                        finalsList.append('GEMC 14')
                    elif value == '<w:result w:val="1"/>':
                        finalsList.append('GEMC 266')

                # Item 3 - BCI
                if item['row'] == 4:
                    if value == 'None':
                        finalsList.append('GEMC 20')
                    elif value == '<w:result w:val="1"/>':
                        finalsList.append('GEMC 294')

            # Table 10 - Magnetic Immunity
            if item['table'] == 10 and item['row'] == 2:
                if value == 'None':
                    finalsList.append('GEMC 22')
                elif value == '<w:result w:val="1"/>':
                    finalsList.append('GEMC 313')
                elif value == '<w:result w:val="2"/>':
                    finalsList.append('GEMC 136')

        else:
            finalsList.append(item['asset'])
    
    return(finalsList)
