from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError
from telethon.tl.functions.channels import InviteToChannelRequest
import sys
import csv
import traceback
import time
import random
import re
import os
import asyncio
from alexa.events import register

# Made by @MissAlexa_Robot
 
@register(pattern="^/addmembers (.*) (.*) (.*)")
async def _(event):
  if event.is_group or event.is_channel:
      return
  os.mkdir("memberadder")
  os.chdir("memberadder")
  appid = event.pattern_match.group(1)
  apphash = event.pattern_match.group(2)
  phone = event.pattern_match.group(3)
  memberadder = TelegramClient(phone, appid, apphash)
  
  await memberadder.send_code_request(phone)
  yy = await event.reply('Enter the code that you received')  
  logattmept = await event.get_reply_message()     
  if logattmept.from_id == 1361631434:
         payload = logattmept
  await memberadder.sign_in(phone, payload)
  await yy.edit("Logged In")  
  timeout = time.time() + 600
  if time.time() < timeout:
         chats = []
         last_date = None
         chunk_size = 200
         groups=[]
                         
         result = await memberadder(GetDialogsRequest(
                                        offset_date=last_date,
                                        offset_id=0,
                                        offset_peer=InputPeerEmpty(),
                                        limit=chunk_size,
                                        hash = 0
                                  ))
                    
         chats.extend(result.chats)
          
         for chat in chats:
                  try:
                       groups.append(chat)
                  except:
                       continue
         
         await yy.edit('Choose a group to scrape members from')
         await asyncio.sleep(10)
         i=0
         lodu = ""
         for g in groups:
                    lodu += str(i) + '- ' + g.title
                    i+=1
         await yy.edit(lodu)
         mdtd = await event.get_reply_message()
     
         if mdtd.from_id == 1361631434:
             numberchatt = mdtd
             
         target_group=groups[int(numberchatt)]
         
         await yy.edit('Fetching Members...')
          
         all_participants = []
         all_participants = await memberadder.get_participants(target_group, aggressive=True)
          
         await yy.edit('Fetching Members...\nDone')
          
         with open("alexa.csv", "w",encoding='UTF-8') as f:
                    writer = csv.writer(f,delimiter=",",lineterminator="\n")
                    writer.writerow(['username','user id', 'access hash','name','group', 'group id'])
                    for user in all_participants:
                              if user.username:
                                        username= user.username
                              else:
                                        username= ""
                              if user.first_name:
                                        first_name= user.first_name
                              else:
                                        first_name= ""
                              if user.last_name:
                                        last_name= user.last_name
                              else:
                                        last_name= ""
                              name= (first_name + ' ' + last_name).strip()
                              writer.writerow([username,user.id,user.access_hash,name,target_group.title, target_group.id])            
         await yy.edit('Members scrapped successfully.')
          
         input_file = "alexa.csv"
         users = []
         with open(input_file, encoding='UTF-8') as f:
                  rows = csv.reader(f,delimiter=",",lineterminator="\n")
                  next(rows, None)
                  for row in rows:
                           user = {}
                           user['username'] = row[0]
                           try:
                                    user['id'] = int(row[1])
                                    user['access_hash'] = int(row[2])
                           except IndexError:
                                    pass
                           users.append(user)
         
         chats = []
         last_date = None
         chunk_size = 200
         groups=[]
                   
         result = await memberadder(GetDialogsRequest(
                                        offset_date=last_date,
                                        offset_id=0,
                                        offset_peer=InputPeerEmpty(),
                                        limit=chunk_size,
                                        hash = 0
                                 ))
                                
         chats.extend(result.chats)
          
         for chat in chats:
                    try:
                        groups.append(chat)        
                    except:
                        continue
               
         await yy.edit('Choose a group to scrape members from')
         await asyncio.sleep(10)
         i=0
         lodu = ""
         for g in groups:
                    lodu += str(i) + '- ' + g.title
                    i+=1
         await yy.edit(lodu)
         mdtd = await event.get_reply_message()
     
         if mdtd.from_id == 1361631434:
             numberchatt = mdtd
             
         target_group=groups[int(numberchatt)]
          
         await yy.edit('Fetching Members...')
          
         all_participants = []
         all_participants = await memberadder.get_participants(target_group, aggressive=True)
          
         await yy.edit('Fetching Members...\nDone')
          
         with open("alexa.csv", "w",encoding='UTF-8') as f:
                    writer = csv.writer(f,delimiter=",",lineterminator="\n")
                    writer.writerow(['username','user id', 'access hash','name','group', 'group id'])
                    for user in all_participants:
                              if user.username:
                                        username= user.username
                              else:
                                        username= ""
                              if user.first_name:
                                        first_name= user.first_name
                              else:
                                        first_name= ""
                              if user.last_name:
                                        last_name= user.last_name
                              else:
                                        last_name= ""
                              name= (first_name + ' ' + last_name).strip()
                              writer.writerow([username,user.id,user.access_hash,name,target_group.title, target_group.id])    
        
         await yy.edit('Members scrapped successfully.')
          
         input_file = "alexa.csv"
         users = []
         with open(input_file, encoding='UTF-8') as f:
                  rows = csv.reader(f,delimiter=",",lineterminator="\n")
                  next(rows, None)
                  for row in rows:
                           user = {}
                           user['username'] = row[0]
                           try:
                                    user['id'] = int(row[1])
                                    user['access_hash'] = int(row[2])
                           except IndexError:
                                    pass
                           users.append(user)
        
         #random.shuffle(users)
         chats = []
         last_date = None
         chunk_size = 10
         groups=[]

         result = await memberadder(GetDialogsRequest(
                                    offset_date=last_date,
                                    offset_id=0,
                                    offset_peer=InputPeerEmpty(),
                                    limit=chunk_size,
                                    hash = 0
                           ))
         chats.extend(result.chats)

         for chat in chats:
                  try:
                           if chat.megagroup== True: # CONDITION TO ONLY LIST MEGA GROUPS.
                                    groups.append(chat)
                  except:
                           continue

         await yy.edit('Choose a group to add members')
         await asyncio.sleep(10)
         i=0
         metadata=""
         for group in groups:
                  metadata += str(i) + '- ' + group.title
                  i+=1
                  
         await yy.edit(metadata)
                 
         mdtd = await event.get_reply_message()     
         if mdtd.from_id == 1361631434:
            numberchatt = mdtd
         g_index = addnumberchatt
         target_group=groups[int(g_index)]
         #  print('\n\nGrupo elegido:\t' + groups[int(g_index)].title)
         await yy.edit("Adding members now ...\nThis process will run for 10 mins and stop automatically !")
          
         target_group_entity = InputPeerChannel(target_group.id,target_group.access_hash)

         mode = int(2)

         error_count = 0
         
         for user in users:
                  try:
                           #  print ("Adding {}".format(user['username']))
                           if mode == 1:
                                    if user['username'] == "":
                                             continue
                                    user_to_add = await memberadder.get_input_entity(user['username'])
                           elif mode == 2:
                                    user_to_add = InputPeerUser(user['id'], user['access_hash'])
                           else:
                                    await yy.edit("Invalid Mode Selected. Please Try Again.")
                                    return
                           await memberadder(InviteToChannelRequest(target_group_entity,[user_to_add]))
                           time.sleep(2)
                  except PeerFloodError:
                           await yy.edit("Getting Flood Error from telegram...\nQuitting")
                           return
                  except UserPrivacyRestrictedError:
                           pass
                  except:
                           traceback.print_exc()
                           #  print("Unexpected Error")
                           error_count += 1
                           if error_count > 10:
                                    await yy.edit('Too many errors\nQuitting...')
                                    return 
  else:
     return
  await memberadder.log_out()
  os.chdir('/app/MissAlexaRobot/MissAlexaRobot')
  os.system('rm -rf memberadder')
  
