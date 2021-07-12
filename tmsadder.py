import time,os
try:
    pyautogui=__import__('pyautogui')
except:
    os.system("pip install "+"pyautogui")
# import pyautogui
try:
    np = __import__('gooey', globals(), locals(), ['Gooey', 'GooeyParser'], 0)

    Gooey = np.Gooey
    GooeyParser = np.GooeyParser

except:
    os.system("pip install " + "gooey")
from gooey import Gooey,GooeyParser
def type(turns):
    time.sleep(3)
    sector={
    "Commerical_Bank":"ADBL,BOKL,civil bank,CCBL,CZBIL,EBL,GBIME,KBL,LBL,MBL,MEGA,NABIL,NBB,NBL,NCCB,NICA,NMB,PCBL,PRVU,SANIMA,SBI,SBL,SCB,SRBL",
    "Development_Bank":"CORBL,EDBL,GBBL,GRDBL,JBBL,KRBL,KSBBL,LBBL,MDB,MLBL,MNBBL,NABBC,SADBL,SAPDBL,SHINE,SINDU",
    "Microfinance": "ACLBSL,ALBSL,CBBL,civil lag,DDBL,FMDBL,FOWAD,GBLBS,GILB,GLBSL,GMFBS,ILBS,JSLBB,KLBSL,KMCDB,LLBS,MERO,MLBBL,MLBSL,MMFDB,MSLB,NICLBSL,NLBBL,NMBMF,NMFBS,NUBL,RMDC,RSDC,SABSL,SDLBSL,SKBBL,SLBBL,SLBS,SLBSL,SMATA,SMB,SMFBS,SMFDB,SNLB,SWBBL,USLB,VLBS,WOMI",
    "Finance":"BFC,CFCL,GFCL,GMFIL,GUFL,ICFC,JFL,MFIL,MPFL,NFS,pok,PROFL,RLFL,SFCL,SIFC",
    "Others": "NRIC,NTC",
    "Hotel_Tourism":"CGH,OHL,SHL,TRH",
    "Life_Insurance":"ALICL,GLICL,JLI,LICN,nepal life,NLICL,PLI,PLIC,RLI,SLICL",
    "Non_Life_Insurance":"AIL,EIC,GIC,HGI,IGI,LGIL,NICL,NIL,NLG,PIC,PICL,PRIN,RBCL,SGI,SIC,SICL,SIL,UIC",
    "Hydropower":"AHPC,AKJCL,AKPL,API,BARUN,BPCL,CHCL,CHL,DHPL,GHL,GLH,HDHPC,HPPL,HURJA,JOSHI,KKHC,KPCL,LEC,mountain,MHNL,NGPL,NHDL,NHPC,PMHPL,PPCL,RADHI,RHPC,RHPL,RRHP,RURU,SHEL,SHPC,SJCL,SPDL,SSHL,UMHL,UMRH,UNHPL,UPCL,UPPER"
    }

    for sector in sector[turns].split(','):
        pyautogui.write(sector,0.2)
        pyautogui.press('enter')
        pyautogui.press('tab')
        pyautogui.press('enter')
        pyautogui.hotkey('shift','tab')
        time.sleep(1)
@Gooey(program_name="Tms Watchlist Adder",default_size=(500,350))
def main():
    parser=GooeyParser()
    sector=parser.add_argument_group('Nepse Listed Sectors')
    sector.add_argument("Sector",
                             metavar='Select Sector',
                             action='store',
                             choices=['Commerical_Bank', 'Development_Bank', 'Finance', 'Hotel_Tourism', 'Microfinance','Others','Life_Insurance','Non_Life_Insurance','Hydropower'],
                             default='Commerical_Bank'
                        )

    arg=parser.parse_args()
    type(arg.Sector)

if __name__ == '__main__':
    main()