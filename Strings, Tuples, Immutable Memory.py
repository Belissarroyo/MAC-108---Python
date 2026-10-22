#Warm-Up Exercise
#Standardized Flagged Usernames

user_input = ["SOLar   "," NOVA   TITAn ","TiTAn   ",
"   COsMiCBLAze  "," CosMIC ","phoeNIX   BlAZE   ",
"   SOLaR   ","gHOSt "," LuNAR  VoRTEX","  ROGUe   ","  ghosT  "," cOsmIc","  vorTEx LUNAR "," eCHO   gHOST","  sOlARshADOW  ","omegA","   nOVAVOrTEx  "," vOrtEX ","  shadoW"," OMeGa VoRTeX "," nINjA"," PiXElbLaZE  "," oMEGaNiNJa ",    "COsmIc","   aLpHa ","   GHOstrOGUE  "," NInjA StORM  ","  LUnaR   "," PIXEL","   cOSmIC ","   voRtEx   aLpHa ","tItAN","  VORTeX   FRosT ","   SoLArGhoST"," gHOsTNova ","  cOsmiC","   GhOsT   eChO   ","VOrteX","  NoVA ALPHA   "," VoRteX   ","lUNaR  FrosT  "," NinjA   lUNar   ","TItAN   ","  sTORM  "," PIXEL ","   qUAntumomeGA  "," ROGUE OmEGA "," OMeGa CoSmIC"," NInJA  noVa ","  VoRTEx   quaNTUM"]
#Using .split to creat structured list
#ITS NOT A STRING ANYMORE ITS A LIST ITEM!!!!
atRisk_user_list = [user_input.split("|")[1] for 
print(atRisk_user_list)

#Using .lower() to convert all characters to lowercase
atRisk_list_lower = [atRisk_user_list.lower()
print(atRisk_list_lower)

#Using .strip to eliminate empty spaces
clean_atRisk_list = atRisk_list_lower.strip()
print(clean_atRisk_list)

