import re
import enchant

class DogObjCleaner:
    def __init__(self, breedValidator):
        self.dictionary = enchant.Dict("en_US")
        self.breedValidator = breedValidator

        titles = [
            {
                "title": 'ACT1',
                "description": 'Agility Course Test 1',
                "isPrefix": False
            },
            {
                "title": 'ACT2',
                "description": 'Agility Course Test 2',
                "isPrefix": False
            },
            {
                "title": 'ACT1J',
                "description": 'Agility Course Test 1 Jumpers',
                "isPrefix": False
            },
            {
                "title": 'ACT2J',
                "description": 'Agility Course Test 2 Jumpers',
                "isPrefix": False
            },
            {
                "title": 'AE*',
                "description": 'Air Retrieve Elite',
                "isPrefix": False
            },
            {
                "title": 'AEA*',
                "description": 'Air Retrieve Elite Advanced',
                "isPrefix": False
            },
            {
                "title": 'AEX*#',
                "description": 'Air Retrieve Elite Excellent',
                "isPrefix": False
            },
            {
                "title": 'AFC',
                "description": 'Amateur Field Champion',
                "isPrefix": True
            },
            {
                "title": 'AGCH',
                "description": 'Agility Grand Champion',
                "isPrefix": True
            },
            {
                "title": 'AJ*',
                "description": 'Air Retrieve Junior',
                "isPrefix": False
            },
            {
                "title": 'AJA*',
                "description": 'Air Retrieve Junior Advanced',
                "isPrefix": False
            },
            {
                "title": 'AJP',
                "description": 'Excellent Agility Jumper Preferred',
                "isPrefix": False
            },
            {
                "title": 'AJX*#',
                "description": 'Air Retrieve Junior Excellent',
                "isPrefix": False
            },
            {
                "title": 'AM*',
                "description": 'Air Retrieve Master',
                "isPrefix": False
            },
            {
                "title": 'AMA*',
                "description": 'Air Retrieve Master Advanced',
                "isPrefix": False
            },
            {
                "title": 'AMX*#',
                "description": 'Air Retrieve Master Excellent',
                "isPrefix": False
            },
            {
                "title": 'AN*',
                "description": 'Air Retrieve Novice',
                "isPrefix": False
            },
            {
                "title": 'ANA*',
                "description": 'Air Retrieve Novice Advanced',
                "isPrefix": False
            },
            {
                "title": 'ANX*#',
                "description": 'Air Retrieve Novice Excellent',
                "isPrefix": False
            },
            {
                "title": 'AS*',
                "description": 'Air Retrieve Senior',
                "isPrefix": False
            },
            {
                "title": 'ASA*',
                "description": 'Air Retrieve Senior Advanced',
                "isPrefix": False
            },
            {
                "title": 'ASX*#',
                "description": 'Air Retrieve Senior Excellent',
                "isPrefix": False
            },
            {
                "title": 'AX',
                "description": 'Agility Excellent',
                "isPrefix": False
            },
            {
                "title": 'BCAT',
                "description": 'BCAT',
                "isPrefix": False
            },
            {
                "title": 'BDD*',
                "description": 'Brace Draft Dog',
                "isPrefix": False
            },
            {
                "title": 'BH*',
                "description": 'Basic Companion Dog',
                "isPrefix": False
            },
            {
                "title": 'BN',
                "description": 'Beginner Novice',
                "isPrefix": False
            },
            {
                "title": 'BN-V',
                "description": 'Virtual Beginner Novice',
                "isPrefix": None
            },
            {
                "title": 'CA',
                "description": 'Coursing Ability',
                "isPrefix": False
            },
            {
                "title": 'CAA',
                "description": 'Coursing Ability Advanced',
                "isPrefix": False
            },
            {
                "title": 'CAX#',
                "description": 'Coursing Ability Excellent',
                "isPrefix": False
            },
            {
                "title": 'CC*',
                "description": 'Coaching Certificate',
                "isPrefix": False
            },
            {
                "title": 'CCA*',
                "description": 'Certificate of Conformation Assessment',
                "isPrefix": False
            },
            {
                "title": 'CCH',
                "description": 'Bench Show Champion',
                "isPrefix": True
            },
            {
                "title": 'CD',
                "description": 'Companion Dog',
                "isPrefix": False
            },
            {
                "title": 'CD-V',
                "description": 'Virtual Companion Dog',
                "isPrefix": None
            },
            {
                "title": 'CDX',
                "description": 'Companion Dog Excellent',
                "isPrefix": False
            },
            {
                "title": 'CFC',
                "description": 'Field Champion',
                "isPrefix": True
            },
            {
                "title": 'CGC',
                "description": 'Canine Good Citizen',
                "isPrefix": False
            },
            {
                "title": 'CGCA',
                "description": 'Advanced Canine Good Citizen (aka Community Canine)',
                "isPrefix": False
            },
            {
                "title": 'CGCH',
                "description": 'Bench Show Grand Champion',
                "isPrefix": True
            },
            {
                "title": 'CGCU',
                "description": 'Canine Good Citizen Urban',
                "isPrefix": False
            },
            {
                "title": 'CGF',
                "description": 'Grand Field Champion',
                "isPrefix": True
            },
            {
                "title": 'CGN',
                "description": 'Grand Nite Champion',
                "isPrefix": True
            },
            {
                "title": 'CGW',
                "description": 'Grand Water Race Champion',
                "isPrefix": True
            },
            {
                "title": 'CH',
                "description": 'Champion',
                "isPrefix": True
            },
            {
                "title": 'CI*',
                "description": 'Carting Intermediate',
                "isPrefix": False
            },
            {
                "title": 'CIT*',
                "description": 'Carting Intermediate Team',
                "isPrefix": False
            },
            {
                "title": 'CJN',
                "description": 'Junior Nite Champion',
                "isPrefix": True
            },
            {
                "title": 'CM#',
                "description": 'Certificate of Merit',
                "isPrefix": False
            },
            {
                "title": 'CNC',
                "description": 'Nite Champion',
                "isPrefix": True
            },
            {
                "title": 'CRCG',
                "description": 'Retired Supreme Grand Champion',
                "isPrefix": True
            },
            {
                "title": 'CS*',
                "description": 'Carting Started',
                "isPrefix": False
            },
            {
                "title": 'CSG',
                "description": 'Bench Show Supreme Grand Champion',
                "isPrefix": True
            },
            {
                "title": 'CSGF',
                "description": 'Supreme Grand Field Champion',
                "isPrefix": True
            },
            {
                "title": 'CSGN',
                "description": 'Supreme Grand Nite Champion',
                "isPrefix": True
            },
            {
                "title": 'CSGW',
                "description": 'Supreme Grand Water Race Champion',
                "isPrefix": True
            },
            {
                "title": 'CST*',
                "description": 'Carting Started Team',
                "isPrefix": False
            },
            {
                "title": 'CT',
                "description": 'Champion Tracker',
                "isPrefix": True
            },
            {
                "title": 'CWC',
                "description": 'Water Race Champion',
                "isPrefix": True
            },
            {
                "title": 'CWGN',
                "description": 'World Champion Supreme Grand Nite Champion',
                "isPrefix": True
            },
            {
                "title": 'CWSG',
                "description": 'World Show Champion',
                "isPrefix": True
            },
            {
                "title": 'CX*',
                "description": 'Carting Excellent',
                "isPrefix": False
            },
            {
                "title": 'CXT*',
                "description": 'Carting Excellent Team',
                "isPrefix": False
            },
            {
                "title": 'DC',
                "description": 'Dual Champion',
                "isPrefix": True
            },
            {
                "title": 'DCAT',
                "description": 'DCAT',
                "isPrefix": False
            },
            {
                "title": 'DD*',
                "description": 'Draft Dog',
                "isPrefix": False
            },
            {
                "title": 'DE*',
                "description": 'Dock Elite',
                "isPrefix": False
            },
            {
                "title": 'DEA*',
                "description": 'Dock Elite Advanced',
                "isPrefix": False
            },
            {
                "title": 'DEX*#',
                "description": 'Dock Elite Excellent',
                "isPrefix": False
            },
            {
                "title": 'DJ*',
                "description": 'Dock Junior',
                "isPrefix": False
            },
            {
                "title": 'DJA*',
                "description": 'Dock Junior Advanced',
                "isPrefix": False
            },
            {
                "title": 'DJX*#',
                "description": 'Dock Junior Excellent',
                "isPrefix": False
            },
            {
                "title": 'DM*',
                "description": 'Dock Master',
                "isPrefix": False
            },
            {
                "title": 'DMA*',
                "description": 'Dock Master Advanced',
                "isPrefix": False
            },
            {
                "title": 'DMX*#',
                "description": 'Dock Master Excellent',
                "isPrefix": False
            },
            {
                "title": 'DN*',
                "description": 'Dock Novice',
                "isPrefix": False
            },
            {
                "title": 'DNA*',
                "description": 'Dock Novice Advanced',
                "isPrefix": False
            },
            {
                "title": 'DNX*#',
                "description": 'Dock Novice Excellent',
                "isPrefix": False
            },
            {
                "title": 'DS*',
                "description": 'Dock Senior',
                "isPrefix": False
            },
            {
                "title": 'DSA*',
                "description": 'Dock Senior Advanced',
                "isPrefix": False
            },
            {
                "title": 'DSX*#',
                "description": 'Dock Senior Excellent',
                "isPrefix": False
            },
            {
                "title": 'EE#',
                "description": 'Endurance Earthdog',
                "isPrefix": False
            },
            {
                "title": 'FC',
                "description": 'Field Champion (Field Trial)',
                "isPrefix": True
            },
            {
                "title": 'FC',
                "description": 'Field Champion (Lure Coursing)',
                "isPrefix": True
            },
            {
                "title": 'FCAT#',
                "description": 'FCAT',
                "isPrefix": False
            },
            {
                "title": 'FCB',
                "description": 'Field Champion – Brace',
                "isPrefix": True
            },
            {
                "title": 'FCGD',
                "description": 'Field Champion – Gundog',
                "isPrefix": True
            },
            {
                "title": 'FCLP',
                "description": 'Field Champion – Large Pack',
                "isPrefix": True
            },
            {
                "title": 'FDC',
                "description": 'Farm Dog Certified',
                "isPrefix": False
            },
            {
                "title": 'FDCH*',
                "description": 'Flyball Dog Champion',
                "isPrefix": False
            },
            {
                "title": 'FDGCH*',
                "description": 'Flyball Dog Grand Champion',
                "isPrefix": False
            },
            {
                "title": 'FH1*',
                "description": 'Advanced Tracking',
                "isPrefix": False
            },
            {
                "title": 'FH2*',
                "description": 'Superior Tracking',
                "isPrefix": False
            },
            {
                "title": 'FM*',
                "description": 'Flyball Master',
                "isPrefix": False
            },
            {
                "title": 'GAFC',
                "description": 'Grand Amateur Field Champion',
                "isPrefix": True
            },
            {
                "title": 'GCH',
                "description": 'Grand Champion',
                "isPrefix": True
            },
            {
                "title": 'GCHB',
                "description": 'Grand Champion Bronze',
                "isPrefix": True
            },
            {
                "title": 'GCHG',
                "description": 'Grand Champion Gold',
                "isPrefix": True
            },
            {
                "title": 'GCHP#',
                "description": 'Grand Champion Platinum',
                "isPrefix": True
            },
            {
                "title": 'GCHS',
                "description": 'Grand Champion Silver',
                "isPrefix": True
            },
            {
                "title": 'GFC',
                "description": 'Grand Field Champion',
                "isPrefix": True
            },
            {
                "title": 'GN',
                "description": 'Graduate Novice',
                "isPrefix": False
            },
            {
                "title": 'GO',
                "description": 'Graduate Open',
                "isPrefix": False
            },
            {
                "title": 'HC',
                "description": 'Herding Champion',
                "isPrefix": True
            },
            {
                "title": 'HI',
                "description": 'Herding Intermediate',
                "isPrefix": False
            },
            {
                "title": 'HIAC',
                "description": 'Herding Intermediate Course A Cattle',
                "isPrefix": False
            },
            {
                "title": 'HIACM',
                "description": 'Herding Intermediate Course A Cattle Master',
                "isPrefix": False
            },
            {
                "title": 'HIAD',
                "description": 'Herding Intermediate Course A Ducks',
                "isPrefix": False
            },
            {
                "title": 'HIADM',
                "description": 'Herding Intermediate Course A Ducks Master',
                "isPrefix": False
            },
            {
                "title": 'HIAS',
                "description": 'Herding Intermediate Course A Sheep',
                "isPrefix": False
            },
            {
                "title": 'HIASM',
                "description": 'Herding Intermediate Course A Sheep Master',
                "isPrefix": False
            },
            {
                "title": 'HIBC',
                "description": 'Herding Intermediate Course B Cattle',
                "isPrefix": False
            },
            {
                "title": 'HIBD',
                "description": 'Herding Intermediate Course B Ducks',
                "isPrefix": False
            },
            {
                "title": 'HIBDM',
                "description": 'Herding Intermediate Course B Ducks Master',
                "isPrefix": False
            },
            {
                "title": 'HIBS',
                "description": 'Herding Intermediate Course B Sheep',
                "isPrefix": False
            },
            {
                "title": 'HIBSM',
                "description": 'Herding Intermediate Course B Sheep Master',
                "isPrefix": False
            },
            {
                "title": 'HICS',
                "description": 'Herding Intermediate Course C Sheep',
                "isPrefix": False
            },
            {
                "title": 'HICSM',
                "description": 'Herding Intermediate Course C Sheep Master',
                "isPrefix": False
            },
            {
                "title": 'HS',
                "description": 'Herding Started',
                "isPrefix": False
            },
            {
                "title": 'HSAC',
                "description": 'Herding Started Course A Cattle',
                "isPrefix": False
            },
            {
                "title": 'HSACM',
                "description": 'Herding Started Course A Cattle Master',
                "isPrefix": False
            },
            {
                "title": 'HSAD',
                "description": 'Herding Started Course A Ducks',
                "isPrefix": False
            },
            {
                "title": 'HSADM',
                "description": 'Herding Started Course A Ducks Master',
                "isPrefix": False
            },
            {
                "title": 'HSAS',
                "description": 'Herding Started Course A Sheep',
                "isPrefix": False
            },
            {
                "title": 'HSASM',
                "description": 'Herding Started Course A Sheep Master',
                "isPrefix": False
            },
            {
                "title": 'HSBC',
                "description": 'Herding Started Course B Cattle',
                "isPrefix": False
            },
            {
                "title": 'HSBD',
                "description": 'Herding Started Course B Ducks',
                "isPrefix": False
            },
            {
                "title": 'HSBDM',
                "description": 'Herding Started Course B Ducks Master',
                "isPrefix": False
            },
            {
                "title": 'HSBS',
                "description": 'Herding Started Course B Sheep',
                "isPrefix": False
            },
            {
                "title": 'HSBSM',
                "description": 'Herding Started Course B SHeep Master',
                "isPrefix": False
            },
            {
                "title": 'HSCS',
                "description": 'Herding Started Course C Sheep',
                "isPrefix": False
            },
            {
                "title": 'HSCSM',
                "description": 'Herding Started Course C Sheep Master',
                "isPrefix": False
            },
            {
                "title": 'HT',
                "description": 'Herding Tested',
                "isPrefix": False
            },
            {
                "title": 'HX',
                "description": 'Herding Excellent',
                "isPrefix": False
            },
            {
                "title": 'HXAC',
                "description": 'Herding Excellent Course A Cattle',
                "isPrefix": False
            },
            {
                "title": 'HXACM',
                "description": 'Herding Advanced Course A Cattle Master',
                "isPrefix": False
            },
            {
                "title": 'HXAD',
                "description": 'Herding Excellent Course A Ducks',
                "isPrefix": False
            },
            {
                "title": 'HXADM',
                "description": 'Herding Advanced Course A Ducks Master',
                "isPrefix": False
            },
            {
                "title": 'HXAS',
                "description": 'Herding Excellent Course A Sheep',
                "isPrefix": False
            },
            {
                "title": 'HXASM',
                "description": 'Herding Advanced Course A Sheep Master',
                "isPrefix": False
            },
            {
                "title": 'HXBC',
                "description": 'Herding Excellent Course B Cattle',
                "isPrefix": False
            },
            {
                "title": 'HXBD',
                "description": 'Herding Excellent Course B Ducks',
                "isPrefix": False
            },
            {
                "title": 'HXBDM',
                "description": 'Herding Advanced Course B Ducks Master',
                "isPrefix": False
            },
            {
                "title": 'HXBS',
                "description": 'Herding Excellent Course A Sheep',
                "isPrefix": False
            },
            {
                "title": 'HXBSM',
                "description": 'Herding Advanced Course B Sheep Master',
                "isPrefix": False
            },
            {
                "title": 'HXCS',
                "description": 'Herding Excellent Course C Sheep',
                "isPrefix": False
            },
            {
                "title": 'HXCSM',
                "description": 'Herding Advanced Course C Sheep Master',
                "isPrefix": False
            },
            {
                "title": 'IPO1*',
                "description": 'International Novice Schutzhund',
                "isPrefix": False
            },
            {
                "title": 'IPO2*',
                "description": 'International Intermediate Schutzhund',
                "isPrefix": False
            },
            {
                "title": 'IPO3*',
                "description": 'International Master Level Schutzhund',
                "isPrefix": False
            },
            {
                "title": 'JC',
                "description": 'Junior Courser',
                "isPrefix": False
            },
            {
                "title": 'JE',
                "description": 'Junior Earthdog',
                "isPrefix": False
            },
            {
                "title": 'JH',
                "description": 'Junior Hunter',
                "isPrefix": False
            },
            {
                "title": 'JHA',
                "description": 'Junior Hunter Advanced',
                "isPrefix": False
            },
            {
                "title": 'JHR',
                "description": 'Junior Hunter Retriever',
                "isPrefix": False
            },
            {
                "title": 'JHU',
                "description": 'Junior Hunter Upland',
                "isPrefix": False
            },
            {
                "title": 'JHUA',
                "description": 'Junior Hunter Upland Advanced',
                "isPrefix": False
            },
            {
                "title": 'LCX#',
                "description": 'Lure Courser Excellent',
                "isPrefix": False
            },
            {
                "title": 'MACH#',
                "description": 'Master Agility Champion',
                "isPrefix": True
            },
            {
                "title": 'MC',
                "description": 'Master Courser',
                "isPrefix": False
            },
            {
                "title": 'ME',
                "description": 'Master Earthdog',
                "isPrefix": False
            },
            {
                "title": 'MFB#',
                "description": 'Master Bronze FAST',
                "isPrefix": False
            },
            {
                "title": 'MFC#',
                "description": 'Master Century FAST',
                "isPrefix": False
            },
            {
                "title": 'MFG#',
                "description": 'Master Gold FAST',
                "isPrefix": False
            },
            {
                "title": 'MFP',
                "description": 'Agility Master FAST Excellent Preferred',
                "isPrefix": False
            },
            {
                "title": 'MFPB#',
                "description": 'Master Bronze FAST Preferred',
                "isPrefix": False
            },
            {
                "title": 'MFPC#',
                "description": 'Master Century FAST Preferred',
                "isPrefix": False
            },
            {
                "title": 'MFPG#',
                "description": 'Master Gold FAST Preferred',
                "isPrefix": False
            },
            {
                "title": 'MFPS#',
                "description": 'Master Silver FAST Preferred',
                "isPrefix": False
            },
            {
                "title": 'MFS#',
                "description": 'Master Silver FAST',
                "isPrefix": False
            },
            {
                "title": 'MH#',
                "description": 'Master Hunter',
                "isPrefix": False
            },
            {
                "title": 'MHA',
                "description": 'Master Hunter Advanced',
                "isPrefix": False
            },
            {
                "title": 'MHR',
                "description": 'Master Hunter Retriever',
                "isPrefix": False
            },
            {
                "title": 'MHU',
                "description": 'Master Hunter Upland',
                "isPrefix": False
            },
            {
                "title": 'MHUA',
                "description": 'Master Hunter Upland Advanced',
                "isPrefix": False
            },
            {
                "title": 'MJB#',
                "description": 'Master Bronze Jumpes',
                "isPrefix": False
            },
            {
                "title": 'MJC#',
                "description": 'Master Century Jumpers',
                "isPrefix": False
            },
            {
                "title": 'MJPC#',
                "description": 'Master Century Jumpers Preferred',
                "isPrefix": False
            },
            {
                "title": 'MJG#',
                "description": 'Master Gold Jumpers',
                "isPrefix": False
            },
            {
                "title": 'MJP',
                "description": 'Master Excellent Jumper Preferred',
                "isPrefix": False
            },
            {
                "title": 'MJPB#',
                "description": 'Master Bronze Jumpers Preferred',
                "isPrefix": False
            },
            {
                "title": 'MJPG#',
                "description": 'Master Gold Jumpers Preferred',
                "isPrefix": False
            },
            {
                "title": 'MJPS#',
                "description": 'Master Silver Jumpers Preferred',
                "isPrefix": False
            },
            {
                "title": 'MJS#',
                "description": 'Master Silver Jumpers',
                "isPrefix": False
            },
            {
                "title": 'MNH#',
                "description": 'Master National Hunter',
                "isPrefix": False
            },
            {
                "title": 'MT*',
                "description": 'Mantrailer',
                "isPrefix": False
            },
            {
                "title": 'MTI*',
                "description": 'Mantrailer Intermediate',
                "isPrefix": False
            },
            {
                "title": 'MTX*',
                "description": 'Mantrailer Excellent',
                "isPrefix": False
            },
            {
                "title": 'MX',
                "description": 'Master Agility Excellent',
                "isPrefix": False
            },
            {
                "title": 'MXB#',
                "description": 'Master Bronze Agility',
                "isPrefix": False
            },
            {
                "title": 'MXC#',
                "description": 'Master Century Agility',
                "isPrefix": False
            },
            {
                "title": 'MXF',
                "description": 'Agility Master FAST Excellent',
                "isPrefix": False
            },
            {
                "title": 'MXG#',
                "description": 'Master Gold Agility',
                "isPrefix": False
            },
            {
                "title": 'MXJ',
                "description": 'Master Excellent Jumper',
                "isPrefix": False
            },
            {
                "title": 'MXP',
                "description": 'Master Agility Excellent Preferred',
                "isPrefix": False
            },
            {
                "title": 'MXPB#',
                "description": 'Master Bronze Agility Preferred',
                "isPrefix": False
            },
            {
                "title": 'MXPC#',
                "description": 'Master Century Agility Preferred',
                "isPrefix": False
            },
            {
                "title": 'MXPG#',
                "description": 'Master Gold Agility Preferred',
                "isPrefix": False
            },
            {
                "title": 'MXPS#',
                "description": 'Master Silver Agility Preferred',
                "isPrefix": False
            },
            {
                "title": 'MXS#',
                "description": 'Master Silver Agility',
                "isPrefix": False
            },
            {
                "title": 'NA',
                "description": 'Novice Agility',
                "isPrefix": False
            },
            {
                "title": 'NAC',
                "description": 'National Agility Champion',
                "isPrefix": True
            },
            {
                "title": 'NAFC',
                "description": 'National Amateur Field Champion',
                "isPrefix": True
            },
            {
                "title": 'NAGDC',
                "description": 'National Amateur Gun Dog Champion',
                "isPrefix": True
            },
            {
                "title": 'NAJ',
                "description": 'Novice Agility Jumper',
                "isPrefix": False
            },
            {
                "title": 'NAP',
                "description": 'Novice Agility Preferred',
                "isPrefix": False
            },
            {
                "title": 'NBC',
                "description": 'National Brace Champion',
                "isPrefix": True
            },
            {
                "title": 'NBDD*',
                "description": 'Novice Brace Draft Dog',
                "isPrefix": False
            },
            {
                "title": 'NDD*',
                "description": 'Novice Draft Dog',
                "isPrefix": False
            },
            {
                "title": 'NE',
                "description": 'Novice Earthdog',
                "isPrefix": False
            },
            {
                "title": 'NF',
                "description": 'Agility FAST Novice',
                "isPrefix": False
            },
            {
                "title": 'NFC',
                "description": 'National Field Champion (Field Trial)',
                "isPrefix": True
            },
            {
                "title": 'NFC',
                "description": 'National Field Champion (Lure Coursing)',
                "isPrefix": True
            },
            {
                "title": 'NFP',
                "description": 'Agility FAST Novice Preferred',
                "isPrefix": False
            },
            {
                "title": 'NGBC',
                "description": 'National Gun Dog Brace Champion',
                "isPrefix": True
            },
            {
                "title": 'NGDC',
                "description": 'National Gun Dog Champion',
                "isPrefix": True
            },
            {
                "title": 'NJP',
                "description": 'Novice Agility Jumper Preferred',
                "isPrefix": False
            },
            {
                "title": 'NLPC',
                "description": 'National Large Pack Champion',
                "isPrefix": True
            },
            {
                "title": 'NOC',
                "description": 'National Obedience Champion',
                "isPrefix": True
            },
            {
                "title": 'NSPC',
                "description": 'National Small Pack Champion',
                "isPrefix": True
            },
            {
                "title": 'NTCPC',
                "description": 'National Beagle Two-Couple Pack Champion',
                "isPrefix": True
            },
            {
                "title": 'NWGDC',
                "description": 'National Walking Gun Dog Championship',
                "isPrefix": True
            },
            {
                "title": 'OA',
                "description": 'Open Agility',
                "isPrefix": False
            },
            {
                "title": 'OAJ',
                "description": 'Open Agility Jumper',
                "isPrefix": False
            },
            {
                "title": 'OAP',
                "description": 'Open Agility Preferred',
                "isPrefix": False
            },
            {
                "title": 'OF',
                "description": 'Agility FAST Open',
                "isPrefix": False
            },
            {
                "title": 'OFP',
                "description": 'Agility FAST Open Preferred',
                "isPrefix": False
            },
            {
                "title": 'OGM',
                "description": 'Obedience Grand Master',
                "isPrefix": False
            },
            {
                "title": 'OJP',
                "description": 'Open Agility Jumper Preferred',
                "isPrefix": False
            },
            {
                "title": 'OM#',
                "description": 'Obedience Master',
                "isPrefix": False
            },
            {
                "title": 'ONYX*',
                "description": 'ONYX',
                "isPrefix": False
            },
            {
                "title": 'OTCH',
                "description": 'Obedience Trial Chaimpion',
                "isPrefix": True
            },
            {
                "title": 'PACH#',
                "description": 'Preferred Agility Champion',
                "isPrefix": True
            },
            {
                "title": 'PAD',
                "description": 'Premier Agility Dog',
                "isPrefix": False
            },
            {
                "title": 'PADP',
                "description": 'Premier Agility Dog Preferred',
                "isPrefix": False
            },
            {
                "title": 'PAX#',
                "description": 'Preferred Agility Excellent',
                "isPrefix": False
            },
            {
                "title": 'PCD',
                "description": 'Preferred Companion Dog',
                "isPrefix": False
            },
            {
                "title": 'PCDX',
                "description": 'Preferred Companion Dog Excellent',
                "isPrefix": False
            },
            {
                "title": 'PCJH*',
                "description": 'Parent Club Junior Hunter',
                "isPrefix": False
            },
            {
                "title": 'PCMH*',
                "description": 'Parent Club Master Hunter',
                "isPrefix": False
            },
            {
                "title": 'PCSH*',
                "description": 'Parent Club Senior Hunter',
                "isPrefix": False
            },
            {
                "title": 'PDB#',
                "description": 'Premier Agility Dog Bronze',
                "isPrefix": False
            },
            {
                "title": 'PDBP#',
                "description": 'Premier Agility Dog Bronze Preferred',
                "isPrefix": False
            },
            {
                "title": 'PDC#',
                "description": 'Premier Agility Dog Century',
                "isPrefix": False
            },
            {
                "title": 'PDCP#',
                "description": 'Premier Agility Dog Century Preferred',
                "isPrefix": False
            },
            {
                "title": 'PDG#',
                "description": 'Premier Agility Dog Gold',
                "isPrefix": False
            },
            {
                "title": 'PDGP#',
                "description": 'Premier Agility Dog Gold Preferred',
                "isPrefix": False
            },
            {
                "title": 'PDS#',
                "description": 'Premier Agility Dog Silver',
                "isPrefix": False
            },
            {
                "title": 'PDSP#',
                "description": 'Premier Agility Dog Silver Preferred',
                "isPrefix": False
            },
            {
                "title": 'PJB#',
                "description": 'Premier Jumpers Dog Bronze',
                "isPrefix": False
            },
            {
                "title": 'PJBP#',
                "description": 'Premier Jumpers Dog Bronze Preferred',
                "isPrefix": False
            },
            {
                "title": 'PJC#',
                "description": 'Premier Jumpers Dog Century',
                "isPrefix": False
            },
            {
                "title": 'PJCP#',
                "description": 'Premier Jumpers Dog Century Preferred',
                "isPrefix": False
            },
            {
                "title": 'PJD',
                "description": 'Premier Jumpers Dog',
                "isPrefix": False
            },
            {
                "title": 'PJDP',
                "description": 'Premier Jumpers Dog Preferred',
                "isPrefix": False
            },
            {
                "title": 'PJG#',
                "description": 'Premier Jumpers Dog Gold',
                "isPrefix": False
            },
            {
                "title": 'PJGP#',
                "description": 'Premier Jumpers Dog Gold Preferred',
                "isPrefix": False
            },
            {
                "title": 'PJS#',
                "description": 'Premier Jumpers Dog Silver',
                "isPrefix": False
            },
            {
                "title": 'PJSP#',
                "description": 'Premier Jumpers Dog Silver Preferred',
                "isPrefix": False
            },
            {
                "title": 'PNAC',
                "description": 'Preferred National Agility Champion',
                "isPrefix": True
            },
            {
                "title": 'POC#',
                "description": 'Preferred Obedience Champion',
                "isPrefix": True
            },
            {
                "title": 'PT',
                "description": 'Pre-Trial Tested',
                "isPrefix": False
            },
            {
                "title": 'PUDX#',
                "description": 'Preferred Utility Dog Excellent',
                "isPrefix": False
            },
            {
                "title": 'PUTD',
                "description": 'Preferred Utility Dog',
                "isPrefix": False
            },
            {
                "title": 'QA2',
                "description": 'Qualified All-Age 2',
                "isPrefix": False
            },
            {
                "title": 'RA',
                "description": 'Rally Advanced',
                "isPrefix": False
            },
            {
                "title": 'RACH#',
                "description": 'Rally Champion',
                "isPrefix": True
            },
            {
                "title": 'RAE#',
                "description": 'Rally Advanced Excellent',
                "isPrefix": False
            },
            {
                "title": 'RATCH*',
                "description": 'Barn Hunt Champion',
                "isPrefix": False
            },
            {
                "title": 'RATCHX*#',
                "description": 'Barn Hunt Master Champion',
                "isPrefix": False
            },
            {
                "title": 'RATM*',
                "description": 'Master Barn Hunt',
                "isPrefix": False
            },
            {
                "title": 'RATN*',
                "description": 'Novice Barn Hunt',
                "isPrefix": False
            },
            {
                "title": 'RATO*',
                "description": 'Open Barn Hunt',
                "isPrefix": False
            },
            {
                "title": 'RATS*',
                "description": 'Senior Barn Hunt',
                "isPrefix": False
            },
            {
                "title": 'RD*',
                "description": 'Road Dog',
                "isPrefix": False
            },
            {
                "title": 'RDX*',
                "description": 'Road Dog Excellent',
                "isPrefix": False
            },
            {
                "title": 'RE',
                "description": 'Rally Excellent',
                "isPrefix": False
            },
            {
                "title": 'RI',
                "description": 'Rally Intermediate',
                "isPrefix": False
            },
            {
                "title": 'RM#',
                "description": 'Rally Master',
                "isPrefix": False
            },
            {
                "title": 'RN',
                "description": 'Rally Novice',
                "isPrefix": False
            },
            {
                "title": 'RNC',
                "description": 'Rally National Champion',
                "isPrefix": True
            },
            {
                "title": 'SAR-U1',
                "description": 'Search and Rescue- Urban 1',
                "isPrefix": False
            },
            {
                "title": 'SAR-U2',
                "description": 'Search and Rescue- Urban 2',
                "isPrefix": False
            },
            {
                "title": 'SAR-U3',
                "description": 'Search and Rescue- Urban 3',
                "isPrefix": False
            },
            {
                "title": 'SAR-W',
                "description": 'Search and Rescue- Wilderness',
                "isPrefix": False
            },
            {
                "title": 'SBA',
                "description": 'Scent Work Buried Advanced',
                "isPrefix": False
            },
            {
                "title": 'SBAE',
                "description": 'Scent Work Buried Advanced Elite',
                "isPrefix": False
            },
            {
                "title": 'SBE',
                "description": 'Scent Work Buried Excellent',
                "isPrefix": False
            },
            {
                "title": 'SBEE',
                "description": 'Scent Work Buried Excellent Elite',
                "isPrefix": False
            },
            {
                "title": 'SBM',
                "description": 'Scent Work Buried Master',
                "isPrefix": False
            },
            {
                "title": 'SBME',
                "description": 'Scent Work Buried Master Elite',
                "isPrefix": False
            },
            {
                "title": 'SBN',
                "description": 'Scent Work Buried Novice',
                "isPrefix": False
            },
            {
                "title": 'SBNE',
                "description": 'Scent Work Buried Novice Elite',
                "isPrefix": False
            },
            {
                "title": 'SC',
                "description": 'Senior Courser',
                "isPrefix": False
            },
            {
                "title": 'SCA',
                "description": 'Scent Work Container Advanced',
                "isPrefix": False
            },
            {
                "title": 'SCAE',
                "description": 'Scent Work Container Advanced Elite',
                "isPrefix": False
            },
            {
                "title": 'SCE',
                "description": 'Scent Work Container Excellent',
                "isPrefix": False
            },
            {
                "title": 'SCEE',
                "description": 'Scent Work Container Excellent Elite',
                "isPrefix": False
            },
            {
                "title": 'SCHH1*',
                "description": 'Novice Schutzhund',
                "isPrefix": False
            },
            {
                "title": 'SCHH2*',
                "description": 'Intermediate Schutzhund',
                "isPrefix": False
            },
            {
                "title": 'SCHH3*',
                "description": 'Master Level Schutzhund',
                "isPrefix": False
            },
            {
                "title": 'SCHHA*',
                "description": 'Novice Schutzhund A',
                "isPrefix": False
            },
            {
                "title": 'SCM',
                "description": 'Scent Work Container Master',
                "isPrefix": False
            },
            {
                "title": 'SCME',
                "description": 'Scent Work Container Master Elite',
                "isPrefix": False
            },
            {
                "title": 'SCN',
                "description": 'Scent Work Container Novice',
                "isPrefix": False
            },
            {
                "title": 'SCNE',
                "description": 'Scent Work Container Novice Elite',
                "isPrefix": False
            },
            {
                "title": 'SD*',
                "description": 'Sled Dog',
                "isPrefix": False
            },
            {
                "title": 'SDO*',
                "description": 'Sled Dog Outstanding',
                "isPrefix": False
            },
            {
                "title": 'SDX*',
                "description": 'Sled Dog Excellent',
                "isPrefix": False
            },
            {
                "title": 'SE',
                "description": 'Senior Earthdog',
                "isPrefix": False
            },
            {
                "title": 'SEA',
                "description": 'Scent Work Exterior Advanced',
                "isPrefix": False
            },
            {
                "title": 'SEAE',
                "description": 'Scent Work Exterior Advanced Elite',
                "isPrefix": False
            },
            {
                "title": 'SEE',
                "description": 'Scent Work Exterior Excellent',
                "isPrefix": False
            },
            {
                "title": 'SEEE',
                "description": 'Scent Work Exterior Excellent Elite',
                "isPrefix": False
            },
            {
                "title": 'SEM',
                "description": 'Scent Work Exterior Master',
                "isPrefix": False
            },
            {
                "title": 'SEME',
                "description": 'Scent Work Exterior Master Elite',
                "isPrefix": False
            },
            {
                "title": 'SEN',
                "description": 'Scent Work Exterior Novice',
                "isPrefix": False
            },
            {
                "title": 'SENE',
                "description": 'Scent Work Exterior Novice Elite',
                "isPrefix": False
            },
            {
                "title": 'SH',
                "description": 'Senior Hunter',
                "isPrefix": False
            },
            {
                "title": 'SHA',
                "description": 'Senior Hunter Advanced',
                "isPrefix": False
            },
            {
                "title": 'SHDA',
                "description": 'Scent Work Handler Discrimination Advanced',
                "isPrefix": False
            },
            {
                "title": 'SHDAE',
                "description": 'Scent Work Handler Discrimination Advanced Elite',
                "isPrefix": False
            },
            {
                "title": 'SHDE',
                "description": 'Scent Work Handler Discrimination Excellent',
                "isPrefix": False
            },
            {
                "title": 'SHDEE',
                "description": 'Scent Work Handler Discrimination Excellent Elite',
                "isPrefix": False
            },
            {
                "title": 'SHDM',
                "description": 'Scent Work Handler Discrimination Master',
                "isPrefix": False
            },
            {
                "title": 'SHDME',
                "description": 'Scent Work Handler Discrimination Master Elite',
                "isPrefix": False
            },
            {
                "title": 'SHDN',
                "description": 'Scent Work Handler Discrimination Novice',
                "isPrefix": False
            },
            {
                "title": 'SHDNE',
                "description": 'Scent Work Handler Discrimination Novice Elite',
                "isPrefix": False
            },
            {
                "title": 'SHR',
                "description": 'Senior Hunter Retriever',
                "isPrefix": False
            },
            {
                "title": 'SHU',
                "description": 'Senior Hunter Upland',
                "isPrefix": False
            },
            {
                "title": 'SHUA',
                "description": 'Senior Hunter Upland Advanced',
                "isPrefix": False
            },
            {
                "title": 'SIA',
                "description": 'Scent Work Interior Advanced',
                "isPrefix": False
            },
            {
                "title": 'SIAE',
                "description": 'Scent Work Interior Advanced Elite',
                "isPrefix": False
            },
            {
                "title": 'SIE',
                "description": 'Scent Work Interior Excellent',
                "isPrefix": False
            },
            {
                "title": 'SIEE',
                "description": 'Scent Work Interior Excellent Elite',
                "isPrefix": False
            },
            {
                "title": 'SIM',
                "description": 'Scent Work Interior Master',
                "isPrefix": False
            },
            {
                "title": 'SIME',
                "description": 'Scent Work Interior Master Elite',
                "isPrefix": False
            },
            {
                "title": 'SIN',
                "description": 'Scent Work Interior Novice',
                "isPrefix": False
            },
            {
                "title": 'SINE',
                "description": 'Scent Work Interior Novice Elite',
                "isPrefix": False
            },
            {
                "title": 'SWA',
                "description": 'Scent Work Advanced',
                "isPrefix": False
            },
            {
                "title": 'SWAE',
                "description": 'Scent Work Advanced Elite',
                "isPrefix": False
            },
            {
                "title": 'SWD',
                "description": 'Scent Work Detective',
                "isPrefix": False
            },
            {
                "title": 'SWE',
                "description": 'Scent Work Excellent',
                "isPrefix": False
            },
            {
                "title": 'SWEE',
                "description": 'Scent Work Excellent Elite',
                "isPrefix": False
            },
            {
                "title": 'SWM',
                "description": 'Scent Work Master',
                "isPrefix": False
            },
            {
                "title": 'SWME',
                "description": 'Scent Work Master Elite',
                "isPrefix": False
            },
            {
                "title": 'SWN',
                "description": 'Scent Work Novice',
                "isPrefix": False
            },
            {
                "title": 'SWNE',
                "description": 'Scent Work Novice Elite',
                "isPrefix": False
            },
            {
                "title": 'T2B#',
                "description": 'Time 2 Beat',
                "isPrefix": False
            },
            {
                "title": 'T2BP#',
                "description": 'Time 2 Beat Preferred',
                "isPrefix": False
            },
            {
                "title": 'TC',
                "description": 'Triple Champion',
                "isPrefix": True
            },
            {
                "title": 'TD',
                "description": 'Tracking Dog',
                "isPrefix": False
            },
            {
                "title": 'TDD*',
                "description": 'Team Draft Dog',
                "isPrefix": False
            },
            {
                "title": 'TDU#',
                "description": 'Tracking Dog Urban',
                "isPrefix": False
            },
            {
                "title": 'TDX#',
                "description": 'Tracking Dog Excellent',
                "isPrefix": False
            },
            {
                "title": 'THD',
                "description": 'Therapy Dog',
                "isPrefix": False
            },
            {
                "title": 'THDA',
                "description": 'Therapy Dog Advanced',
                "isPrefix": False
            },
            {
                "title": 'THDD',
                "description": 'Distinguished Therapy Dog',
                "isPrefix": False
            },
            {
                "title": 'THDN',
                "description": 'Therapy Dog Novice',
                "isPrefix": False
            },
            {
                "title": 'THDX',
                "description": 'Therapy Dog Excellent',
                "isPrefix": False
            },
            {
                "title": 'TKA',
                "description": 'Trick Dog Advanced',
                "isPrefix": False
            },
            {
                "title": 'TKI',
                "description": 'Trick Dog Intermediate',
                "isPrefix": False
            },
            {
                "title": 'TKN',
                "description": 'Trick Dog Novice',
                "isPrefix": False
            },
            {
                "title": 'TKP',
                "description": 'Trick Dog Performer',
                "isPrefix": False
            },
            {
                "title": 'TQX',
                "description": 'Triple Q Excellent',
                "isPrefix": False
            },
            {
                "title": 'TQXP',
                "description": 'Triple Q Excellent Preferred',
                "isPrefix": False
            },
            {
                "title": 'TT*',
                "description": 'Temperament Test',
                "isPrefix": False
            },
            {
                "title": 'UD',
                "description": 'Utility Dog',
                "isPrefix": False
            },
            {
                "title": 'UDX#',
                "description": 'Utility Dog Excellent',
                "isPrefix": False
            },
            {
                "title": 'VCCH',
                "description": 'Versatile Companion Dog Champion',
                "isPrefix": True
            },
            {
                "title": 'VCD#',
                "description": 'Versatile Companion Dog',
                "isPrefix": False
            },
            {
                "title": 'VER',
                "description": 'Versatility',
                "isPrefix": False
            },
            {
                "title": 'VST#',
                "description": 'Variable Surface Tracker',
                "isPrefix": False
            },
            {
                "title": 'VSWB',
                "description": 'Virtual Scent Work Beginners',
                "isPrefix": False
            },
            {
                "title": 'VSWI',
                "description": 'Virtual Scent Work Intermediate',
                "isPrefix": False
            },
            {
                "title": 'VSWE',
                "description": 'Virtual Scent Work Experience',
                "isPrefix": False
            },
            {
                "title": 'WC*',
                "description": 'Working Certificate',
                "isPrefix": False
            },
            {
                "title": 'WCI*',
                "description": 'Working Certificate Intermediate',
                "isPrefix": False
            },
            {
                "title": 'WCX*',
                "description": 'Working Certificate Excellent',
                "isPrefix": False
            },
            {
                "title": 'WDS1*',
                "description": 'Working Dog Sport 1',
                "isPrefix": False
            },
            {
                "title": 'WDS2*',
                "description": 'Working Dog Sport 2',
                "isPrefix": False
            },
            {
                "title": 'WDS3*',
                "description": 'Working Dog Sport 3',
                "isPrefix": False
            },
            {
                "title": 'WNC',
                "description": 'World Nite Champion',
                "isPrefix": True
            },
            {
                "title": 'XF',
                "description": 'Agility FAST Excellent',
                "isPrefix": False
            },
            {
                "title": 'XFP',
                "description": 'Agility FAST Excellent Preferred',
                "isPrefix": False
            }]
        
        self.titleMap = {"prefix": {}, "suffix": {}}
        for title in titles:
            titlePrefix = title["title"][:4]
            if title["isPrefix"]:
                self.titleMap["prefix"][titlePrefix] = True
            else:
                self.titleMap["suffix"][titlePrefix] = True

    def titlecase(self, input):
        return re.sub(
            r"[A-Za-z]+('[A-Za-z]+)?",
            lambda word: word.group(0).capitalize(),
            input)

    def getTitleObj(self, input):
        prefixTitles = []
        suffixTitles = []

        inputParts = input.split(" ")
        # remove empty strings from the inputParts
        inputParts = [part for part in inputParts if part != ""]

        nameIndexStart = -1
        nameIndexEnd = -1

        for index, part in enumerate(inputParts):
            if input == input.upper():
                if part.upper() in self.titleMap["prefix"]:
                    prefixTitles.append(part)
                elif len(part) < 6:
                    if not self.dictionary.check(part):
                        prefixTitles.append(part)
                    else:
                        nameIndexStart = index
                        break
                else:
                    nameIndexStart = index
                    break
            elif len(part) > 1 and part[:2] == part[:2].upper():
                prefixTitles.append(part)
            else:
                nameIndexStart = index
                break


        # now reverse the inputParts and do the same thing for suffix
        inputParts.reverse()
        for index, part in enumerate(inputParts):
            if input == input.upper():
                if part.upper() in self.titleMap["suffix"]:
                    suffixTitles.append(part)
                elif len(part) < 6:
                    if not self.dictionary.check(part):
                        suffixTitles.append(part)
                    else:
                        nameIndexEnd = len(inputParts) - index
                        break
                else:
                    nameIndexEnd = len(inputParts) - index
                    break
            elif len(part) > 1 and part[:2] == part[:2].upper():
                suffixTitles.append(part)
            else:
                nameIndexEnd = len(inputParts) - index
                break


        inputParts.reverse()
        suffixTitles.reverse()
        nameParts = []

        if nameIndexStart != -1 and nameIndexEnd != -1:
            nameParts = inputParts[nameIndexStart:nameIndexEnd]
        elif nameIndexStart != -1:
            nameParts = inputParts[nameIndexStart:]
        elif nameIndexEnd != -1:
            nameParts = inputParts[:nameIndexEnd]
        else:
            nameParts = inputParts

        cleanInput = " ".join(nameParts)

        return {
            "prefixTitles": prefixTitles,
            "suffixTitles": suffixTitles,
            "input": self.titlecase(cleanInput)
        }
    

    def getNameKey(self, dogName, breed):
        if dogName is None or breed is None:
            return None
        
        # remove all non-alphanumeric characters from the dog's name
        nameKey = re.sub(r'[^a-zA-Z0-9]', '', dogName.lower()) + re.sub(r'[^a-zA-Z0-9]', '', breed.lower())
        return nameKey

    def clean(self, dogObj, breedKeyMap):
        if "dogNameTitledName" in dogObj:
            dogName = dogObj["dogNameTitledName"]
            titleObj = self.getTitleObj(dogName)
            dogObj["prefixTitles"] = titleObj["prefixTitles"]
            dogObj["suffixTitles"] = titleObj["suffixTitles"]
            dogObj["dogName"] = titleObj["input"]
            del dogObj["dogNameTitledName"]

        # rename sireDogNameTitledName to sire
        if "sireDogNameTitledName" in dogObj:
            dogObj["sire"] = dogObj["sireDogNameTitledName"]
            del dogObj["sireDogNameTitledName"]

        # rename damDogNameTitledName to dam
        if "damDogNameTitledName" in dogObj:
            dogObj["dam"] = dogObj["damDogNameTitledName"]
            del dogObj["damDogNameTitledName"]

        if "sire" in dogObj:
            # remove all titles from the sire's name
            sireTitleObj = self.getTitleObj(dogObj["sire"])
            dogObj["sire"] = sireTitleObj["input"]

        if "dam" in dogObj:
            # remove all titles from the dam's name
            damTitleObj = self.getTitleObj(dogObj["dam"])
            dogObj["dam"] = damTitleObj["input"]

        # rename the key breedDescription to breed
        if "breedDescription" in dogObj:
            dogObj["breed"] = dogObj["breedDescription"]
            del dogObj["breedDescription"]

        dogObj["breed"] = self.breedValidator.getOfficialBreedName(dogObj["breed"], breedKeyMap)


        # add a nameKey property that removes all non-alphanumeric characters from the dog's name
        if "dogName" in dogObj:
            nameKey = self.getNameKey(dogObj["dogName"], dogObj["breed"])
            if nameKey is None:
                return None
            
            dogObj["nameKey"] = self.getNameKey(dogObj["dogName"], dogObj["breed"])

        validKeysMap = {
            "breed": True,
            "sex": True,
            "dogName": True,
            "prefixTitles": True,
            "suffixTitles": True,
            "registrationNumber": True,
            "whelpDate": True,
            "breeders": True,
            "sire": True,
            "dam": True,
            "nameKey": True
        }

        keys = list(dogObj.keys())
        for key in keys:
            if key not in validKeysMap:
                del dogObj[key]

        return dogObj


