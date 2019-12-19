#######################################################
#    Author:      <Ethan Glaser>
#    email:       <glasere@purdue.edu>
#    ID:           <ee364a13>
#    Date:         <9/10/19>
#######################################################
import os      # List of  module  import  statements
import sys     # Each  one on a line
from pprint import pprint
#######################################################
# No Module -Level  Variables  or  Statements!
# ONLY  FUNCTIONS  BEYOND  THIS  POINT!
#######################################################


def getTechWork(techName):
    techs, viruses, exps = techReader(), virusReader(), expReader()
    work = {}
    valid = False
    for tech in techs:
        if tech == techName:
            techID = techs[tech]
            valid = True
    if not valid:
        raise ValueError("Invalid tech name")
    for exp in exps:
        if exp == techID:
            for virus in exps[exp]:
                _, name = viruses[virus]
                if name not in work:
                    work[name] = 0
                work[name] += exps[exp][virus]
    return work


def getStrainConsumption(virusName):
    techs, viruses, exps = techReader(), virusReader(), expReader()
    use = {}
    valid = False
    for virus in viruses:
        _, name = viruses[virus]
        if name == virusName:
            virusID = virus
            valid = True
    if not valid:
        raise ValueError("Invalid virus name")
    for exp in exps:
        if virusID in exps[exp]:
            for tech in techs:
                if techs[tech] == exp:
                    if tech not in use:
                        use[tech] = 0
                    use[tech] += exps[exp][virusID]
    return use


def getTechSpending():
    costs = {}
    techs, viruses, exps = techReader(), virusReader(), expReader()
    for exp in exps:
        for tech in techs:
            if techs[tech] == exp:
                name = tech
        if name not in costs:
            costs[name] = 0
        for val in exps[exp]:
            price, _ = viruses[val]
            costs[name] += round(float(exps[exp][val]) * float(price[1:]), 2)
    for cost in costs:
        costs[cost] = round(costs[cost], 2)
    return costs


def getStrainCost():
    nums = {}
    costs = {}
    exps = expReader()
    viruses = virusReader()
    for exp in exps.values():
        for key in exp:
            if key not in nums:
                nums[key] = 0
            nums[key] += int(exp[key])
    for val in nums:
        price, name = viruses[val]
        costs[name] = round(nums[val] * float(price[1:]), 2)
    return costs


def getAbsentTechs():
    techs = techReader()
    exps = expReader()
    absent = set()
    for tech in techs:
        if techs[tech] not in exps:
            absent.add(tech)
    return absent


def getUnusedStrains():
    viruses = virusReader()
    exps = expReader()
    unused = set()
    for virus in viruses:
        status = True
        for exp in exps:
            if virus in exps[exp]:
                status = False
        if status:
            _, name = viruses[virus]
            unused.add(name)
    return unused


def expReader():
    exps = {}
    for report in os.listdir('./reports'):
        with open('reports/' + report, 'r') as f:
            key = (f.readline().split('\n')[0]).split()[2]
            if key not in exps:
                exps[key] = {}
            data = f.readlines()
            remove = ['Trial                  Virus                             Units\n',
                      '---------------------------------------------------------------\n', '\n']
            for line in data:
                if line not in remove:
                    if line.split('/n')[0].split()[1] not in exps[key]:
                        exps[key][line.split('/n')[0].split()[1]] = 0
                    exps[key][line.split('/n')[0].split()[1]] += int(line.split('/n')[0].split()[2])
    return exps


def techReader():
    with open("maps/technicians.dat") as f:
        data = f.readlines()[2:]
        realData = {}
        for line in data:
            line = line.split()
            if len(line) != 4:
                raise ValueError("name error" + str(line))
            realData[line[0] + ' ' + line[1]] = line[3]
        return realData


def virusReader():
    with open("maps/viruses.dat") as f:
        data = f.readlines()[2:]
        realData = {}
        for line in data:
            line = line.split()
            if len(line) != 5:
                raise ValueError("name error" + str(line))
            realData[line[2]] = line[4], line[0]
        return realData


# This  block  is  optional  and  can be used  for  testing.
# We will  NOT  look  into  its  content.
#######################################################
if __name__  == "__main__":
    # Write  anything  here to test  your  code.
    problem1 = True
    work1 = {'Mupapillomavirus': 1015, 'Gammatorquevirus': 210, 'Varicellovirus': 703, 'Phlebovirus': 165, 'Caliciviridae': 237, 'Togaviridae': 101, 'Parechovirus': 386, 'Ebolavirus': 163, 'Alphavirus': 341, 'Polyomavirus': 552, 'Orthobunyavirus': 683, 'Cytomegalovirus': 393, 'Seadornavirus': 162, 'Influenzavirus-B': 555, 'Coronaviridae': 382, 'Mamastrovirus': 245, 'Retroviridae': 571, 'Molluscipoxvirus': 674, 'Hepadnaviridae': 163, 'Mastadenovirus': 492, 'Gammaretrovirus': 426, 'Hantavirus': 612, 'Hepacivirus': 312, 'Orthopoxvirus': 313, 'Simplexvirus': 839, 'Henipavirus': 316, 'Alphacoronavirus': 242, 'Roseolovirus': 248, 'Deltaretrovirus': 343, 'Coxsackievirus': 616, 'Picornaviridae': 468, 'Betatorquevirus': 280, 'Rotavirus': 33, 'Orthohepadnavirus': 312, 'Rhadinovirus': 10, 'Betacoronavirus': 323, 'Anelloviridae': 446, 'Lymphocryptovirus': 99, 'Alphatorquevirus': 733, 'Filoviridae': 480, 'Metapneumovirus': 580, 'Arenavirus': 334, 'Papillomaviridae': 629, 'Marburgvirus': 308, 'Spumavirus': 559, 'Vesiculovirus': 268, 'Thogotovirus': 177, 'Paramyxoviridae': 98, 'Poxviridae': 804, 'Coltivirus': 341, 'Rubulavirus': 510, 'Nairovirus': 471, 'Kobuvirus': 249, 'Enterovirus': 79, 'Flaviviridae': 638, 'Respirovirus': 62, 'Astroviridae': 118, 'Pneumovirus': 563, 'Dependovirus': 106, 'Lentivirus': 412, 'Torovirus': 254, 'Deltavirus': 189, 'Herpesviridae': 403, 'Morbilivirus': 486, 'Betapapillomavirus': 279, 'Zikavirus': 100, 'Nupapillomavirus': 320, 'Orthomyxoviridae': 561, 'Hepevirus': 398, 'Influenzavirus-C': 563, 'Gammapapilloma-virus': 233, 'Hepatovirus': 401, 'Bocavirus': 453, 'Arenaviridae': 508, 'Sapovirus': 127, 'Influenzavirus-A': 106, 'Alphapapillomavirus': 230, 'Norovirus': 79, 'Reoviridae': 403, 'Cardiovirus': 216, 'Rhabdoviridae': 375, 'Parvoviridae': 297, 'Flavivirus': 3}
    work2 = getTechWork('Morris, Heather')
    for w in work1:
        if work1[w] - work2[w] or work2[w] - work1[w]:
            problem1 = False
    print("Problem 1: ", problem1)

    problem2 = True
    cons = {'Bell, Kathryn': 629, 'Ross, Frances': 1210, 'Lee, Julie': 144, 'Morgan, Edward': 989, 'Gonzales, Arthur': 1520, 'Phillips, Brenda': 896, 'Howard, Shawn': 949, 'Campbell, Eugene': 539, 'Sanders, Emily': 614, 'Wilson, Howard': 1436, 'Baker, Craig': 705, 'Jones, Stephanie': 2049, 'Brooks, Carol': 1453, 'Hall, Beverly': 772, 'Edwards, Rachel': 399, 'Washington, Annie': 1182, 'Adams, Keith': 516, 'Cox, Shirley': 1169, 'Torres, Betty': 397, 'Carter, Sarah': 462, 'Bailey, Catherine': 1237, 'Gray, Tammy': 435, 'Morris, Heather': 245, 'Scott, Michael': 927, 'King, Carolyn': 1223, 'Roberts, Teresa': 1276, 'White, Diana': 477, 'Bennett, Nancy': 863, 'Thomas, Mark': 528, 'Butler, Julia': 523, 'Sanchez, Deborah': 1203, 'Griffin, Charles': 436, 'Barnes, Sean': 748, 'Miller, Aaron': 909, 'Green, Roy': 1150, 'Martinez, David': 1574, 'Cook, Margaret': 1127, 'Lewis, William': 2226, 'Hill, Jose': 142, 'Rivera, Patricia': 38, 'Jenkins, Paul': 581, 'Russell, Scott': 672, 'Moore, John': 340, 'Johnson, Roger': 628, 'Lopez, Juan': 185, 'Williams, Mary': 410, 'Coleman, Lori': 392, 'Taylor, Brian': 607, 'Parker, Raymond': 1641, 'Diaz, Tina': 543, 'Watson, Martin': 687, 'Evans, Johnny': 451, 'Richardson, George': 220, 'Flores, Andrea': 210, 'Simmons, Cynthia': 1505, 'Stewart, Earl': 653, 'Alexander, Carlos': 463, 'Ward, Sandra': 901, 'Foster, Benjamin': 369, 'Harris, Anne': 1402, 'Jackson, Doris': 298, 'Thompson, Michelle': 452, 'Allen, Amanda': 584, 'Young, Frank': 369, 'Rodriguez, Jeffrey': 818, 'Rogers, Elizabeth': 289, 'Perry, Marie': 517, 'Brown, Robert': 476, 'Perez, Kathleen': 209, 'Henderson, Christopher': 67, 'Robinson, Pamela': 149, 'Peterson, Daniel': 189, 'Reed, Bobby': 178, 'Anderson, Debra': 1294, 'Smith, Jimmy': 165, 'Hughes, James': 846, 'Long, Joshua': 421, 'Garcia, Martha': 606, 'Wood, Kevin': 417, 'Lowe, Karen': 120, 'Mitchell, Judith': 90, 'Hernandez, Lawrence': 114, 'Turner, Theresa': 454, 'Martin, Richard': 466, 'Collins, Anthony': 273, 'James, Randy': 693, 'Patterson, Peter': 167, 'Murphy, Donna': 390, 'Powell, Gregory': 216, 'Davis, Douglas': 241, 'Wright, Eric': 118}
    cons2 = getStrainConsumption('Mamastrovirus')
    for c in cons:
        if cons[c] - cons2[c] or cons2[c] - cons[c]:
            problem2 = False
    print("Problem 2: ", problem2)

    problem3 = True
    tech1 = {'Bell, Kathryn': 229623.78, 'Ross, Frances': 457942.3, 'Lee, Julie': 173269.93, 'Morgan, Edward': 306693.24, 'Gonzales, Arthur': 405817.27, 'Phillips, Brenda': 280421.22, 'Howard, Shawn': 182615.3, 'Campbell, Eugene': 338111.81, 'Sanders, Emily': 283529.29, 'Wilson, Howard': 374402.26, 'Baker, Craig': 239963.94, 'Jones, Stephanie': 461394.9, 'Brooks, Carol': 238324.91, 'Hall, Beverly': 231424.36, 'Edwards, Rachel': 269463.19, 'Washington, Annie': 321437.31, 'Adams, Keith': 242833.87, 'Cox, Shirley': 414224.29, 'Torres, Betty': 147001.69, 'Carter, Sarah': 184439.42, 'Bailey, Catherine': 546139.11, 'Gray, Tammy': 233536.06, 'Morris, Heather': 135020.93, 'Scott, Michael': 353779.02, 'King, Carolyn': 418384.46, 'Roberts, Teresa': 520842.29, 'White, Diana': 318632.13, 'Bennett, Nancy': 421254.63, 'Thomas, Mark': 343717.88, 'Butler, Julia': 187334.34, 'Sanchez, Deborah': 416178.02, 'Griffin, Charles': 257768.28, 'Barnes, Sean': 288146.96, 'Miller, Aaron': 280966.21, 'Green, Roy': 517317.69, 'Martinez, David': 323578.41, 'Cook, Margaret': 343312.53, 'Lewis, William': 619715.42, 'Hill, Jose': 281493.62, 'Rivera, Patricia': 227607.4, 'Jenkins, Paul': 140982.16, 'Russell, Scott': 187995.5, 'Moore, John': 235974.33, 'Johnson, Roger': 230130.32, 'Lopez, Juan': 147316.71, 'Williams, Mary': 93615.87, 'Coleman, Lori': 327600.77, 'Taylor, Brian': 412625.84, 'Parker, Raymond': 270615.19, 'Diaz, Tina': 195833.53, 'Watson, Martin': 269113.77, 'Evans, Johnny': 179619.65, 'Richardson, George': 214706.53, 'Flores, Andrea': 188834.24, 'Simmons, Cynthia': 384102.02, 'Stewart, Earl': 133578.05, 'Alexander, Carlos': 297306.29, 'Ward, Sandra': 470033.6, 'Foster, Benjamin': 192447.63, 'Harris, Anne': 380846.56, 'Jackson, Doris': 130595.55, 'Thompson, Michelle': 238498.53, 'Allen, Amanda': 168451.98, 'Young, Frank': 219034.16, 'Rodriguez, Jeffrey': 218932.2, 'Rogers, Elizabeth': 83802.67, 'Perry, Marie': 180422.89, 'Brown, Robert': 228107.67, 'Perez, Kathleen': 145466.56, 'Henderson, Christopher': 187727.4, 'Robinson, Pamela': 177301.99, 'Peterson, Daniel': 137805.06, 'Reed, Bobby': 131404.89, 'Anderson, Debra': 329276.06, 'Smith, Jimmy': 142032.48, 'Hughes, James': 326833.53, 'Long, Joshua': 180915.45, 'Garcia, Martha': 306941.06, 'Wood, Kevin': 138960.37, 'Lowe, Karen': 242022.77, 'Mitchell, Judith': 89915.64, 'Hernandez, Lawrence': 153946.06, 'Turner, Theresa': 190670.41, 'Martin, Richard': 182815.13, 'Collins, Anthony': 176882.44, 'James, Randy': 185753.62, 'Patterson, Peter': 44582.95, 'Murphy, Donna': 190055.9, 'Powell, Gregory': 86454.2, 'Davis, Douglas': 46361.12, 'Wright, Eric': 42007.66}
    tech2 = getTechSpending()
    for t in tech1:
        if tech1[t] - tech2[t] or tech2[t] - tech1[t]:
            problem3 = False
    print("Problem 3: ", problem3)

    problem4 = True
    strain = {'Hepadnaviridae': 5642.55, 'Deltavirus': 6540.5, 'Lentivirus': 82083.55, 'Hepacivirus': 65598.5, 'Vesiculovirus': 170383.41, 'Parechovirus': 163929.15, 'Hepevirus': 327882.48, 'Enterovirus': 559765.65, 'Polyomavirus': 472981.88, 'Spumavirus': 434305.3, 'Influenzavirus-B': 148168.44, 'Alphavirus': 419749.8, 'Torovirus': 185501.23, 'Gammapapilloma-virus': 236106.24, 'Hantavirus': 56412.65, 'Roseolovirus': 21443.76, 'Alphapapillomavirus': 218006.1, 'Sapovirus': 470026.8, 'Marburgvirus': 190857.68, 'Influenzavirus-A': 285240.3, 'Simplexvirus': 38339.84, 'Phlebovirus': 129538.36, 'Flaviviridae': 97914.9, 'Cytomegalovirus': 486484.25, 'Molluscipoxvirus': 159267.78, 'Thogotovirus': 65981.52, 'Retroviridae': 4125.03, 'Respirovirus': 142329.78, 'Zikavirus': 120456.69, 'Morbilivirus': 480171.29, 'Picornaviridae': 179471.15, 'Betapapillomavirus': 68381.5, 'Metapneumovirus': 527093.0, 'Papillomaviridae': 275970.1, 'Pneumovirus': 310768.12, 'Paramyxoviridae': 64432.2, 'Influenzavirus-C': 69400.8, 'Bocavirus': 588019.6, 'Alphacoronavirus': 243050.11, 'Deltaretrovirus': 328438.8, 'Orthopoxvirus': 338133.55, 'Kobuvirus': 337621.68, 'Alphatorquevirus': 112472.01, 'Coltivirus': 406440.54, 'Orthomyxoviridae': 567115.92, 'Flavivirus': 183945.27, 'Caliciviridae': 589006.6, 'Gammaretrovirus': 566041.28, 'Mastadenovirus': 477573.42, 'Henipavirus': 492639.84, 'Mamastrovirus': 431612.23, 'Nupapillomavirus': 297490.26, 'Betacoronavirus': 440138.16, 'Arenavirus': 278328.05, 'Norovirus': 265811.0, 'Rubulavirus': 380047.04, 'Ebolavirus': 35998.86, 'Herpesviridae': 626452.4, 'Reoviridae': 407898.04, 'Parvoviridae': 427860.16, 'Rhabdoviridae': 57493.57, 'Coxsackievirus': 32108.45, 'Betatorquevirus': 517957.42, 'Rhadinovirus': 37798.02, 'Nairovirus': 200135.33, 'Varicellovirus': 289581.98, 'Filoviridae': 472977.86, 'Astroviridae': 204558.48, 'Lymphocryptovirus': 350010.75, 'Mupapillomavirus': 78232.92, 'Seadornavirus': 477061.2, 'Dependovirus': 238765.78, 'Poxviridae': 21686.0, 'Orthobunyavirus': 614030.95, 'Coronaviridae': 253295.19, 'Orthohepadnavirus': 136298.51, 'Anelloviridae': 240653.94, 'Cardiovirus': 325058.56, 'Togaviridae': 325045.0, 'Arenaviridae': 435558.2, 'Gammatorquevirus': 390977.2, 'Hepatovirus': 251236.86, 'Rotavirus': 561507.36}
    strain2 = getStrainCost()
    for s in strain:
        if strain[s] - strain2[s] or strain2[s] - strain[s]:
            problem4 = False
    print("Problem 4: ", problem4)
    print("Problem 3 & 4: ", 0 == int(sum(strain2.values()) - sum(tech2.values())))

    absent = {'Ramirez, Linda', 'Walker, Terry', 'Kelly, Joyce', 'Cooper, Kelly', 'Price, Dorothy', 'Nelson, Louise', 'Clark, Joe', 'Gonzalez, Kimberly', 'Bryant, Evelyn'}
    print("Problem 5: ", len(absent - getAbsentTechs()) == 0 and len(getAbsentTechs() - absent) == 0)

    unused = {'Erythrovirus', 'Parapoxvirus', 'Rubivirus', 'Lyssavirus', 'Polyomaviridae', 'Bunyaviridae', 'Adenoviridae'}
    print("Problem 6: ", len(unused - getUnusedStrains()) == 0 and len(getUnusedStrains() - unused) == 0)
