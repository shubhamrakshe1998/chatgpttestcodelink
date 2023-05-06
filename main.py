# Make a master file from 1. SOE fields, then 2. GDC fields
# Has RegNum, Bdate, FN,LN, formatted address, Phone, PCT, Party,RegDate, House, Senate
# GDC doesnt have Bdate,REgDate;  SOE doesnt have Party strength,Cell Phones
#
# add Address sub fields( Street Number, Street Number Suffix, Street Dir, Street NAme, Street Type, Street Dir Suffix)
# add (Unit Type, Apartment Number)
# add Voting History from SOE file; New file run 6/26/21
# add age
# add Commission District and City Code, status[ina or act], email, race

import csv
import datetime
dir(datetime)


SOE_f = open("SOE_Voter_csv_txt.txt", 'r')
#SOE_Voter_txt_csv.txt was saved as csv-dos, then opened in Notepad to save as text.

SOE_VoterDataIn = csv.reader(SOE_f)
#Read each record into this Class of csv.reader OBJECT[SOE_VoterDataIn] in Ram

SOE_voters = []
#initialize new list 

for voter in SOE_VoterDataIn:
    
     SOE_voters.append(voter)

#Append voter record to new list voters, 192K+ records

    
print("SOE File ", len(SOE_voters))

SOE_f.close()
print('SOE Read file closed')

print()

# SOE LIST CREATED
#____________________________________________


# Read in GDC file
GDC_f = open("GDC AC_Sept 2020_TXT.txt", 'r')
#GDC_Voter_csvdostxt.txt was saved as csv-dos, then opened in Notepad to save as text.

GDC_VoterDataIn = csv.reader(GDC_f)
#Read each record into this Class of csv.reader OBJECT[GDC_VoterDataIn] in Ram

GDC_voters = []
#initialize new list 

for voter in GDC_VoterDataIn:
    
     GDC_voters.append(voter)

   
print("GDC File ", len(GDC_voters))

GDC_f.close()
print('GDC Read file closed')

print()
#_________________________________________________________
# GDC LIST CREATED

#___________________________________________________________
# Update Master file with phonenumbers from both Lists[SOE and GDC}
# Flag No Match when SOE Regnum not in GDC

writefile = "Master_voters.txt"

count = 0
with open(writefile, 'w', newline='') as csvfile:  

     csvwriter = csv.writer(csvfile) 

     GDC_tc = 0          # GDC phone number count Added to Master
     GDC_Overlay_tc = 0  # GDC Phone overlays SOE with GDC cell phone
     SOE_tc = 0          # SOE phone number count Added to Master

     NoMatchCt = 0  # No Match from SOE to GDC files: Wasn't in GDC
     
     for V in range(len(SOE_voters)):  

         voter_bd = datetime.datetime.strptime(SOE_voters[V][30],"%m/%d/%Y")
         voter_Regdt = datetime.datetime.strptime(SOE_voters[V][31],"%m/%d/%Y")

         #Make datetime a string , yyyy-mm-dd (time)
         stringvoter_bd = str(voter_bd)
         stringvoter_rd = str(voter_Regdt)
          
         #format of first 10 chars, date only
         v_bdate = stringvoter_bd[0:10]
         RegDt = stringvoter_rd[0:10]


         bd_yr = v_bdate[0:4]
         now_yr = "2023"

#Make datetime a string , yyyy-mm-dd (time) calc Age
         str_bdYr = str(bd_yr)
                                                        
         age = int(now_yr) - int(str_bdYr) 


         phone = SOE_voters[V][43]
         regnum = SOE_voters[V][0]
         LName = SOE_voters[V][2]
         FName = SOE_voters[V][3]
         address = SOE_voters[V][6]
         cityST = SOE_voters[V][7]
         Zip = SOE_voters[V][8]
         Pct = SOE_voters[V][34]
         party = SOE_voters[V][33]
         House = SOE_voters[V][35]
         Senate = SOE_voters[V][36]
         Cnty_District = SOE_voters[V][37]
         City_code = SOE_voters[V][41]                              
         StreetNum = SOE_voters[V][10]
         StreetNumSuf = SOE_voters[V][11]
         StreetDir = SOE_voters[V][12]
         StreetDirSuf = SOE_voters[V][15]
         StreetName = SOE_voters[V][13]
         StreetType = SOE_voters[V][14]


         StreetType = StreetType.lower().capitalize()


                  
         UnitType = SOE_voters[V][16]        
         ApptNum = SOE_voters[V][17]
         Res_Zip = SOE_voters[V][18]
         Res_City = SOE_voters[V][19]
         status = SOE_voters[V][44]
         race = SOE_voters[V][28]

         
         vote_history = SOE_voters[V][47]

         vote_history2 = SOE_voters[V][48]
         vote_history3 = SOE_voters[V][49]
         vote_history4 = SOE_voters[V][50]
         vote_history5 = SOE_voters[V][51]
         vote_history6 = SOE_voters[V][52]
         vote_history7 = SOE_voters[V][53]
         vote_history8 = SOE_voters[V][54]

         email = SOE_voters[V][46]
         
             
              
       
         if (len(phone) == 10): 
              S_phone = phone
         else:
              if (len(phone) == 7):
                  S_phone = "352" + phone
              else:
                  S_phone = ""

         S_regnum = regnum
          

         for G in range(len(GDC_voters)):
             
             G_regnum = GDC_voters[G][26]
             
             G_PartyStrength = GDC_voters[G][17]
             PrimaryPhone = ""
            
             
             if  S_regnum != G_regnum:          #RegNum Not Equal, continue search through range

                 Match = 0
                 
             else:    

                 Match = 1
                 Gcell_phone = GDC_voters[G][30]   # Cell Phone
                 G_phone = GDC_voters[G][12]       # Primary Phone

                 if (len(GDC_voters[G][30]) == 10): 
                     Gcell_phone = GDC_voters[G][30]
                 else:
                     if (len(GDC_voters[G][30]) == 7):
                         Gcell_phone = "352" + GDC_voters[G][30] 
                     else:
                         Gcell_phone = ""  
                 
                 
                 if (len(GDC_voters[G][12]) == 10): # Primary Phone
                     G_phone = GDC_voters[G][12]
                 else:
                     if (len(GDC_voters[G][12]) == 7):
                         G_phone = "352" + GDC_voters[G][12] 
                     else:
                         G_phone = ""  

                    
                 if S_phone == "":                 # SOE Phone is blank

                    if Gcell_phone == "":         #GDC cell is blank 
                          S_phone = G_phone       #use primary phone
                          if S_phone != "":
                             GDC_tc = GDC_tc + 1
                             PrimaryPhone = "P"

                    else:
                          S_phone = Gcell_phone    #use cell phone
                          GDC_tc = GDC_tc + 1 

                 else:
                      if (Gcell_phone != ""):
                         GDC_Overlay_tc = GDC_Overlay_tc + 1 
                         S_phone = Gcell_phone      #use cell phone
                      else:
                         SOE_tc = SOE_tc + 1   
                         
                 fields1 = [regnum, LName, FName, address, cityST, Zip, Pct, party, StreetNum, StreetNumSuf, StreetDir, StreetDirSuf, StreetName, StreetType, UnitType, ApptNum]

                 fields2 = [Res_Zip, Res_City, v_bdate, RegDt, G_PartyStrength, S_phone, PrimaryPhone, House, Senate, Cnty_District, City_code]

                 fields3 = [vote_history, vote_history2, vote_history3, vote_history4, vote_history5, vote_history6, vote_history7, vote_history8, age, status, email, race]


                 csvwriter.writerow(fields1 + fields2 + fields3)   #writing the fields

                 if Match == 1:    # True
                    break    
                 

#________# End For Loop on break___________________________

         # Match is 0.  SOE regnum not in GDC
         
         if Match == 0: 

              fields1 = [regnum, LName, FName, address, cityST, Zip, Pct, party, StreetNum, StreetNumSuf, StreetDir, StreetDirSuf, StreetName, StreetType, UnitType, ApptNum]
              
              fields2 = [Res_Zip, Res_City, v_bdate, RegDt, " ", S_phone, PrimaryPhone, House, Senate, Cnty_District, City_code]

              fields3 = [vote_history, vote_history2, vote_history3, vote_history4, vote_history5, vote_history6, vote_history7, vote_history8, age, status, email, race]

              csvwriter.writerow(fields1 + fields2 + fields3)   #writing the fields

     
              NoMatchCt = NoMatchCt + 1
                    
              if (S_phone != " "):
                 SOE_tc = SOE_tc + 1

              print(count)
              count = count +1



csvfile.close()
print("Close Write File")
print()
print("Phone Counts: SOE: ", SOE_tc)
print("Phone Counts: GDC: ", GDC_tc)
print()
print("GDC_Overlay Phone: ", GDC_Overlay_tc)
print()
print("SOE Regnum not in GDC ", NoMatchCt)


#_______





     #     if StreetType == "AVE":
     #          StreetType = "Ave"

     #     if StreetType == "BLVD":
     #          StreetType = "Blvd"

     #     if StreetType == "CIR":
     #          StreetType = "CIR"

     #     if StreetType == "CT":
     #          StreetType = "Ct"

     #     if StreetType == "DR":
     #          StreetType = "Dr"

     #     if StreetType == "LN":
     #          StreetType = "Ln"

     #     if StreetType == "PL":
     #          StreetType = "Pl"

     #     if StreetType == "RD":
     #          StreetType = "Rd"

     #     if StreetType == "ST":
     #          StreetType = "St"

     #     if StreetType == "TER":
     #          StreetType = "Ter"

     #     if StreetType == "WAY":
     #          StreetType = "Way"
