import math
import pandas as pd
import csv
from datetime import datetime
from pathlib import Path
from colored import Fore,Style,Back
from barcode import Code39,UPCA,EAN8,EAN13
import barcode,qrcode,os,sys,argparse
from datetime import datetime,timedelta,date
import zipfile,tarfile
import base64,json
from ast import literal_eval
import sqlalchemy
from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base as dbase
from sqlalchemy.ext.automap import automap_base
from pathlib import Path
import upcean
from MobileInventoryCLI.CodeProcessing.RecordCodesAndBarcodes.ExtractPkg.ExtractPkg2 import *
from MobileInventoryCLI.CodeProcessing.RecordCodesAndBarcodes.Lookup.Lookup import *
from MobileInventoryCLI.CodeProcessing.RecordCodesAndBarcodes.DayLog.DayLogger import *
from MobileInventoryCLI.CodeProcessing.RecordCodesAndBarcodes.DB.db import *
from MobileInventoryCLI.CodeProcessing.RecordCodesAndBarcodes.ConvertCode.ConvertCode import *
from MobileInventoryCLI.CodeProcessing.RecordCodesAndBarcodes.setCode.setCode import *
from MobileInventoryCLI.CodeProcessing.RecordCodesAndBarcodes.Locator.Locator import *
from MobileInventoryCLI.CodeProcessing.RecordCodesAndBarcodes.ListMode2.ListMode2 import *
from MobileInventoryCLI.CodeProcessing.RecordCodesAndBarcodes.TasksMode.Tasks import *
from MobileInventoryCLI.CodeProcessing.RecordCodesAndBarcodes.ExportList.ExportListCurrent import *
from MobileInventoryCLI.CodeProcessing.RecordCodesAndBarcodes.DB.Prompt import *
from MobileInventoryCLI.CodeProcessing.RecordCodesAndBarcodes.DB.DatePicker import *
from MobileInventoryCLI.CodeProcessing.RecordCodesAndBarcodes.PunchCard.CalcTimePad import *

import MobileInventoryCLI.CodeProcessing.RecordCodesAndBarcodes.possibleCode as pc
from MobileInventoryCLI.CodeProcessing.RecordCodesAndBarcodes.FB.FBMTXT import *
import requests

class RosterUi:
	def fromBlog(self):
		src="https://kl11-sw156.blogspot.com/2024/10/schedule.html"
		page=requests.get(src)
		if page.status_code == 200:
			soup=BS(page.content,"html.parser")
			#print(soup)
			paragraphs=soup.find_all("p")
			broker=''
			for num,i in enumerate(paragraphs):
				para=num,i.text
				for num2,i2 in enumerate(para[1].split("\n")):
					print(i2)
					
	def addShift(self):
		with Session(ENGINE) as session:
				while True:
					try:
						shift_range=Prompt.__init2__(None,func=FormBuilderMkText,ptext=f"Shift DateString [mm/day/year@hh:mm(start)-hh:mm(end)]",data="datetime~")
						print(shift_range)
						if shift_range in [None,'d']:
							return
						elif shift_range in ['RETRY',]:
							continue
						break
					except Exception as e:
						print(e)
				while True:
					try:
						lunch_range=Prompt.__init2__(None,func=FormBuilderMkText,ptext=f"Shift Lunch DateString [mm/day/year@hh:mm(start)-hh:mm(end)]",data="datetime~")
						if lunch_range in [None,]:
							return
						elif lunch_range in ['d',]:
							lunch_range=[None,None]
						elif lunch_range in ['RETRY',]:
							continue
						break
					except Exception as e:
						print(e)
				while True:
					whoId=None
					whoSearch=Prompt.__init2__(None,func=FormBuilderMkText,ptext="Who are you scheduling?",helpText="firstname/lastname",data="string")
					if whoSearch in [None,]:
						return
					elif whoSearch in ['d',]:
						who=session.query(Roster).order_by(Roster.LastName).all()
					else:
						who=session.query(Roster).filter(or_(Roster.FirstName.icontains(whoSearch),Roster.LastName.icontains(whoSearch))).order_by(Roster.LastName.asc()).all()
						whoCt=len(who)
						if whoCt == 0:
							print("There is no one by that name")
							continue
						for num,i in enumerate(who):
							msg=f"""{Fore.light_green}{num}/{Fore.light_yellow}{num+1} {Fore.orange_red_1}of {whoCt} -> {Fore.cyan}{i.LastName},{Fore.light_magenta}{i.FirstName}{Style.reset}"""
							print(msg)
						which=Prompt.__init2__(None,func=FormBuilderMkText,ptext="which index?",helpText="the number farthest to the left of the screen",data="integer")
						if which in [None,]:
							return
						elif which in ['d']:
							which=0
						selectedPerson=who[which]
						whoId=selectedPerson.RoId
						break
				while True:
					dptId=None
					dptSearch=Prompt.__init2__(None,func=FormBuilderMkText,ptext="What Department?",helpText="name",data="string")
					if dptSearch in [None,]:
						return
					elif dptSearch in ['d']:
						dpts=session.query(Department).order_by(Department.Name.asc())
					else:
						dpts=session.query(Department).filter(or_(Department.Position.icontains(dptSearch),Department.Name.icontains(dptSearch)))
					try:
						dptSearchInteger=int(eval(dptSearch))
						dpts=dpts.filter(or_(Department.Number==dptSearchInteger))
					except Exception as e:
						print(e)
						try:
							dptSearchInteger=int(dptSearch)
							dpts=dpts.filter(or_(Department.Number==dptSearchInteger))
						except Exception as ee:
							print(ee)



					dpts=dpts.all()
					dptsCt=len(dpts)
					if dptsCt == 0:
						print("There is no one by that name")
						continue
					for num,i in enumerate(dpts):
						msg=f"""{Fore.light_green}{num}/{Fore.light_yellow}{num+1} {Fore.orange_red_1}of {dptsCt} -> {Fore.cyan}{i.Name} {i.Position} {Fore.light_magenta}{i.Number}"""
						print(msg)
					which=Prompt.__init2__(None,func=FormBuilderMkText,ptext="which index?",helpText="the number farthest to the left of the screen",data="integer")
					if which in [None,]:
						return
					elif which in ['d']:
						which=0
					selectedDpt=dpts[which]
					dptId=selectedDpt.dptId
					break
				RoSh=RosterShift(dptId=dptId,RoId=whoId,ShiftStart=shift_range[0],ShiftEnd=shift_range[1],ShiftLunchStart=lunch_range[0],ShiftLunchEnd=lunch_range[1],DTOE=datetime.now())
				session.add(RoSh)
				session.commit()
				session.refresh(RoSh)
				print(RoSh)

	def legend(self):
		header=f"""\n{Fore.grey_50}DAYNAME of {Fore.grey_70}Week WEEK_NUMBER|{Fore.light_green}Index/{Fore.light_yellow}Count {Fore.orange_red_1}of TOTAL -> {Fore.cyan}LastName,{Fore.light_magenta}FirstName [{Fore.light_yellow}DPT{Fore.light_magenta}] - {Fore.light_green}SS(SHIFT START)/{Fore.light_red}SE(SHIFT END)/{Fore.light_yellow}LS(LunchStart)/{Fore.dark_goldenrod}LE(LunchEnd){Style.reset}"""
		print(header)

	def caRosterShift(self):
		with Session(ENGINE) as session:
			session.query(RosterShift).delete()
			session.commit()
			session.flush()
			
	def caPeople(self):
		with Session(ENGINE) as session:
			session.query(Roster).delete()
			session.commit()
			session.flush()

	def caDepartments(self):
		with Session(ENGINE) as session:
			session.query(Department).delete()
			session.commit()
			session.flush()
	
	def laRosterShift(self):
		with Session(ENGINE) as session:
			RS=session.query(RosterShift).order_by(RosterShift.ShiftStart.asc()).all()
			rsCt=len(RS)
			if rsCt == 0:
				print("No Shifts scheduled")
				return
			for num,i in enumerate(RS):
				selectedPerson=session.query(Roster).filter(Roster.RoId==i.RoId).first()
				if not selectedPerson:
					continue
				dpt=session.query(Department).filter(Department.dptId==i.dptId).first()
				if dpt:
					dptName=f"{dpt.Name}.{dpt.Position} - {dpt.Number}"
				else:
					dptName=f"N/A - N/A"
				msg=f"""{Fore.grey_50}{i.ShiftStart.strftime("%A")} of {Fore.grey_70}Week {i.ShiftStart.strftime("%W")}|{Fore.light_green}{num}/{Fore.light_yellow}{num+1} {Fore.orange_red_1}of {rsCt} -> {Fore.cyan}{selectedPerson.LastName},{Fore.light_magenta}{selectedPerson.FirstName} [{Fore.light_yellow}{dptName}{Fore.light_magenta}] - {Fore.light_green}SS({i.ShiftStart})/{Fore.light_red}SE({i.ShiftEnd})/{Fore.light_yellow}LS({i.ShiftLunchStart})/{Fore.dark_goldenrod}LE({i.ShiftLunchEnd}){Style.reset}"""
				#msg=f'''{num}/{num+1} of {rsCt} -> {selectedPerson.LastName},{selectedPerson.FirstName} [{dptName}] - SS({i.ShiftStart})/SE({i.ShiftEnd})/LS({i.ShiftLunchStart})/LE({i.ShiftLunchEnd})'''
				print(msg)
		self.legend()

	def saRosterShift(self):
		with Session(ENGINE) as session:
			while True:
				whoSearch=Prompt.__init2__(None,func=FormBuilderMkText,ptext="Who are you searching?",helpText="firstname/lastname",data="string")
				if whoSearch in [None,]:
					return
				elif whoSearch in ['d',]:
					who=session.query(Roster).order_by(Roster.LastName).all()
				else:
					who=session.query(Roster).filter(or_(Roster.FirstName.icontains(whoSearch),Roster.LastName.icontains(whoSearch))).order_by(Roster.LastName.asc()).all()
				whoCt=len(who)
				if whoCt == 0:
					print("There is no one by that name")
					continue
				for num,i in enumerate(who):
					msg=f"""{Fore.light_green}{num}/{Fore.light_yellow}{num+1} {Fore.orange_red_1}of {whoCt} -> {Fore.cyan}{i.LastName},{Fore.light_magenta}{i.FirstName}{Style.reset}"""
					print(msg)
				which=Prompt.__init2__(None,func=FormBuilderMkText,ptext="which index?",helpText="the number farthest to the left of the screen",data="integer")
				if which in [None,]:
					return
				elif which in ['d']:
					which=0
				selectedPerson=who[which]
				RS=session.query(RosterShift).filter(RosterShift.RoId==selectedPerson.RoId).order_by(RosterShift.ShiftStart.asc()).all()
				rsCt=len(RS)
				if rsCt == 0:
					print("No Shifts scheduled")
					return
				for num,i in enumerate(RS):
					dpt=session.query(Department).filter(Department.dptId==i.dptId).first()
					if dpt:
						dptName=f"{dpt.Name}.{dpt.Position} - {dpt.Number}"
					else:
						dptName=f"N/A - N/A"
					msg=f"""{Fore.grey_50}{i.ShiftStart.strftime("%A")} of {Fore.grey_70}Week {i.ShiftStart.strftime("%W")}|{Fore.light_green}{num}/{Fore.light_yellow}{num+1} {Fore.orange_red_1}of {whoCt} -> {Fore.cyan}{selectedPerson.LastName},{Fore.light_magenta}{selectedPerson.FirstName} [{Fore.light_yellow}{dptName}{Fore.light_magenta}] - {Fore.light_green}SS({i.ShiftStart})/{Fore.light_red}SE({i.ShiftEnd})/{Fore.light_yellow}LS({i.ShiftLunchStart})/{Fore.dark_goldenrod}LE({i.ShiftLunchEnd}){Style.reset}"""
					#msg=f'''{num}/{num+1} of {rsCt} -> {selectedPerson.LastName},{selectedPerson.FirstName} [{dptName}] - SS({i.ShiftStart})/SE({i.ShiftEnd})/LS({i.ShiftLunchStart})/LE({i.ShiftLunchEnd})'''
					print(msg)
		self.legend()

	def whosHere(self):
		with Session(ENGINE) as session:
			today=datetime.today()
			RS=session.query(RosterShift).filter(RosterShift.ShiftStart>=today,datetime(today.year,today.month,today.day+1)>=RosterShift.ShiftStart).all()
			rsCt=len(RS)
			if rsCt == 0:
				print("No Shifts scheduled")
				return
			for num,i in enumerate(RS):
				dpt=session.query(Department).filter(Department.dptId==i.dptId).first()
				selectedPerson=session.query(Roster).filter(Roster.RoId==i.RoId).first()
				if not selectedPerson:
					continue
				if dpt:
					dptName=f"{dpt.Name}.{dpt.Position} - {dpt.Number}"
				else:
					dptName=f"N/A - N/A"
				msg=f"""{Fore.light_green}{num}/{Fore.light_yellow}{num+1} {Fore.orange_red_1}of {rsCt} -> {Fore.cyan}{selectedPerson.LastName},{Fore.light_magenta}{selectedPerson.FirstName} [{Fore.light_yellow}{dptName}{Fore.light_magenta}] - {Fore.light_green}SS({i.ShiftStart})/{Fore.light_red}SE({i.ShiftEnd})/{Fore.light_yellow}LS({i.ShiftLunchStart})/{Fore.dark_goldenrod}LE({i.ShiftLunchEnd}){Style.reset}"""
				#msg=f'''{num}/{num+1} of {rsCt} -> {selectedPerson.LastName},{selectedPerson.FirstName} [{dptName}] - SS({i.ShiftStart})/SE({i.ShiftEnd})/LS({i.ShiftLunchStart})/LE({i.ShiftLunchEnd})'''
				print(msg)
		self.legend()

	def rmRosterShift(self):
		with Session(ENGINE) as session:
			while True:
				whoSearch=Prompt.__init2__(None,func=FormBuilderMkText,ptext="Who are you searching?",helpText="firstname/lastname",data="string")
				if whoSearch in [None,]:
					return
				elif whoSearch in ['d',]:
					who=session.query(Roster).order_by(Roster.LastName).all()
				else:
					who=session.query(Roster).filter(or_(Roster.FirstName.icontains(whoSearch),Roster.LastName.icontains(whoSearch))).order_by(Roster.LastName.asc()).all()
				whoCt=len(who)
				if whoCt == 0:
					print("There is no one by that name")
					continue
				for num,i in enumerate(who):
					msg=f"""{Fore.light_green}{num}/{Fore.light_yellow}{num+1} {Fore.orange_red_1}of {whoCt} -> {Fore.cyan}{i.LastName},{Fore.light_magenta}{i.FirstName}{Style.reset}"""
					print(msg)
				which=Prompt.__init2__(None,func=FormBuilderMkText,ptext="which index?",helpText="the number farthest to the left of the screen",data="integer")
				if which in [None,]:
					return
				elif which in ['d']:
					which=0
				selectedPerson=who[which]
				RS=session.query(RosterShift).filter(RosterShift.RoId==selectedPerson.RoId).order_by(RosterShift.ShiftStart.asc()).all()
				rsCt=len(RS)
				if rsCt == 0:
					print("No Shifts scheduled")
					return
				for num,i in enumerate(RS):
					dpt=session.query(Department).filter(Department.dptId==i.dptId).first()
					if dpt:
						dptName=f"{dpt.Name}.{dpt.Position} - {dpt.Number}"
					else:
						dptName=f"N/A - N/A"
					#msg=f'''{num}/{num+1} of {rsCt} -> {selectedPerson.LastName},{selectedPerson.FirstName} [{dptName}] - SS({i.ShiftStart})/SE({i.ShiftEnd})/LS({i.ShiftLunchStart})/LE({i.ShiftLunchEnd})'''
					msg=f"""{Fore.light_green}{num}/{Fore.light_yellow}{num+1} {Fore.orange_red_1}of {whoCt} -> {Fore.cyan}{selectedPerson.LastName},{Fore.light_magenta}{selectedPerson.FirstName} [{Fore.light_yellow}{dptName}{Fore.light_magenta}] - {Fore.light_green}SS({i.ShiftStart})/{Fore.light_red}SE({i.ShiftEnd})/{Fore.light_yellow}LS({i.ShiftLunchStart})/{Fore.dark_goldenrod}LE({i.ShiftLunchEnd}){Style.reset}"""
					print(msg)
				which=Prompt.__init2__(None,func=FormBuilderMkText,ptext="which index?",helpText="the number farthest to the left of the screen",data="integer")
				if which in [None,]:
					return
				elif which in ['d']:
					which=0
				selectedShift=RS[which]
				session.delete(selectedShift)
				session.commit()
				session.flush()
				break


	def saPerson(self):
		with Session(ENGINE) as session:
			while True:
				whoSearch=Prompt.__init2__(None,func=FormBuilderMkText,ptext="Who are you searching?",helpText="firstname/lastname",data="string")
				if whoSearch in [None,]:
					return
				elif whoSearch in ['d',]:
					who=session.query(Roster).order_by(Roster.LastName).all()
				else:
					who=session.query(Roster).filter(or_(Roster.FirstName.icontains(whoSearch),Roster.LastName.icontains(whoSearch))).order_by(Roster.LastName.asc()).all()
				whoCt=len(who)
				if whoCt == 0:
					print("There is no one by that name")
					continue
				for num,i in enumerate(who):
					msg=f"""{Fore.light_green}{num}/{Fore.light_yellow}{num+1} {Fore.orange_red_1}of {whoCt} -> {Fore.cyan}{i.LastName},{Fore.light_magenta}{i.FirstName}{Style.reset}"""
					print(msg)

	def rmPerson(self):
		with Session(ENGINE) as session:
			while True:
				whoSearch=Prompt.__init2__(None,func=FormBuilderMkText,ptext="Who are you removing?",helpText="firstname/lastname",data="string")
				if whoSearch in [None,]:
					return
				elif whoSearch in ['d',]:
					who=session.query(Roster).order_by(Roster.LastName).all()
				else:
					who=session.query(Roster).filter(or_(Roster.FirstName.icontains(whoSearch),Roster.LastName.icontains(whoSearch))).order_by(Roster.LastName.asc()).all()
				whoCt=len(who)
				if whoCt == 0:
					print("There is no one by that name")
					continue
				for num,i in enumerate(who):
					msg=f"""{Fore.light_green}{num}/{Fore.light_yellow}{num+1} {Fore.orange_red_1}of {whoCt} -> {Fore.cyan}{i.LastName},{Fore.light_magenta}{i.FirstName}{Style.reset}"""
					print(msg)
				which=Prompt.__init2__(None,func=FormBuilderMkText,ptext="which index?",helpText="the number farthest to the left of the screen",data="integer")
				if which in [None,]:
					return
				elif which in ['d']:
					which=0
				selectedPerson=who[which]
				session.delete(selectedPerson)
				session.commit()
				session.flush()
				break


	def saDepartment(self):
		with Session(ENGINE) as session:
			while True:
				whoSearch=Prompt.__init2__(None,func=FormBuilderMkText,ptext="What Department are you searching?",helpText="Name/Position/Number",data="string")
				if whoSearch in [None,]:
					return
				elif whoSearch in ['d',]:
					who=session.query(Department).order_by(Department.Name)
				else:
					who=session.query(Department).filter(or_(Department.Position.icontains(whoSearch),Department.Name.icontains(whoSearch)))
					try:
						whoSearchInteger=int(eval(whoSearch))
						who=who.filter(or_(Department.Number==whoSearchInteger))
					except Exception as e:
						print(e)
						try:
							whoSearchInteger=int(whoSearch)
							who=who.filter(or_(Department.Number==whoSearchInteger))
						except Exception as ee:
							print(ee)

				who=who.all()
				whoCt=len(who)
				if whoCt == 0:
					print("There is no one by that name")
					continue
				for num,i in enumerate(who):
					#msg=f"""{Fore.light_green}{num}/{Fore.light_yellow}{num+1} of {Fore.light_red}{whoCt} -> {Fore.cyan}{i.Name} {Fore.light_magenta}{i.Number}{Style.reset}"""
					msg=f"""{Fore.light_green}{num}/{Fore.light_yellow}{num+1} of {Fore.light_red}{whoCt} -> {Fore.cyan}{i.Name}.{i.Position} {Fore.light_magenta}{i.Number}{Style.reset}"""
					print(msg)

	def rmDepartment(self):
		with Session(ENGINE) as session:
			while True:
				whoSearch=Prompt.__init2__(None,func=FormBuilderMkText,ptext="what department are you removing?",helpText="name",data="string")
				if whoSearch in [None,]:
					return
				elif whoSearch in ['d',]:
					who=session.query(Department).order_by(Department.Name).all()
				else:
					who=session.query(Department).filter(or_(Department.Position.icontains(whoSearch),Department.Name.icontains(whoSearch))).order_by(Department.Name.asc()).all()
				whoCt=len(who)
				if whoCt == 0:
					print("There is no dptment by that name")
					continue
				for num,i in enumerate(who):
					msg=f"""{Fore.light_green}{num}/{Fore.light_yellow}{num+1} of {Fore.light_red}{whoCt} -> {Fore.cyan}{i.Name}.{i.Position} {Fore.light_magenta}{i.Number}{Style.reset}"""
					print(msg)
				which=Prompt.__init2__(None,func=FormBuilderMkText,ptext="which index?",helpText="the number farthest to the left of the screen",data="integer")
				if which in [None,]:
					return
				elif which in ['d']:
					which=0
				selectedDepartment=who[which]
				session.delete(selectedDepartment)
				session.commit()
				session.flush()
				break

	def addDepartment(self):
		with Session(ENGINE) as session:
			excludes=['dptId',]
			fields={str(i.name):{'default':None,'type':str(i.type)} for i in Department.__table__.columns if str(i.name) not in excludes}
			fields['DTOE']['type']='datetime-'
			fd=FormBuilder(data=fields)
			department=Department(**fd)
			session.add(department)
			session.commit()
			session.flush()
			session.refresh(department)
			print(department)

	def addPerson(self):
		with Session(ENGINE) as session:
			excludes=['RoId',]
			fields={str(i.name):{'default':None,'type':str(i.type)} for i in Roster.__table__.columns if str(i.name) not in excludes}
			fields['DTOE']['type']='datetime-'
			fd=FormBuilder(data=fields)
			person=Roster(**fd)
			session.add(person)
			session.commit()
			session.flush()
			session.refresh(person)
			print(person)
	def __init__(self):
		fieldname='Menu'
		mode='Roster'
		h=f'{Prompt.header.format(Fore=Fore,mode=mode,fieldname=fieldname,Style=Style)}'
		menutext=f'''
{Fore.cyan}'ap','ad person','add person','add personnel','ad personnl' {Fore.light_red}-{Fore.orange_red_1} add a person to Roster table, checking to ensure that name is not duplicated before adding{Style.reset}
{Fore.cyan}'rp','rm person','rmperson','del person','delperson','del taco','deltaco' {Fore.light_red}-{Fore.orange_red_1} remove a person{Style.reset}
{Fore.cyan}'sap','sa person','saperson','sa person','walk the planck' {Fore.light_red}-{Fore.orange_red_1} search persons{Style.reset}

{Fore.cyan}'ad','ad dpt','add department','add dpt','addpt' {Fore.light_red}-{Fore.orange_red_1} add a department to tables{Style.reset}
{Fore.cyan}'rd','rm department','rmdpt','del dpt','deldpt'{Fore.light_red}-{Fore.orange_red_1} remove a department{Style.reset}
{Fore.cyan}'sad','sa department','sadpt','sa dpt' {Fore.light_red}-{Fore.orange_red_1} search department{Style.reset}

{Fore.cyan}'rars','rm roster shift'{Fore.light_red}-{Fore.orange_red_1} delete a scheduled day{Style.reset}
{Fore.cyan}'whos here','personel','prsnl','today','tdy'{Fore.light_red}-{Fore.orange_red_1} show who's here today{Style.reset}
{Fore.cyan}'sars','sa rostershift'{Fore.light_red}-{Fore.orange_red_1} search RosterShift{Style.reset}
{Fore.cyan}'cars','ca rostershift','clear all rostershift'{Fore.light_red}-{Fore.orange_red_1}clear all schedules{Style.reset}
{Fore.cyan}'cad','ca dpt','clear all departments'{Fore.light_red}-{Fore.orange_red_1}clear all dpts{Style.reset}
{Fore.cyan}'cap','ca personnl','clear all people'{Fore.light_red}-{Fore.orange_red_1}clear all people{Style.reset}
{Fore.cyan}'ars','ad roster shift','add roster shift','adrstrshft' {Fore.light_red}-{Fore.orange_red_1} using Roster and Departments tables, update the RosterShift table with available shift data{Style.reset}
{Fore.cyan}'lars','list all roster shift','ls * rs' {Fore.light_red}-{Fore.orange_red_1} list ALL RosterShift's/Schedules{Style.reset}
		'''
		while True:
			try:
				cmd=Prompt.__init2__(self,func=FormBuilderMkText,ptext=f"{h}Do what?",helpText=menutext,data="string")
				if cmd in [None,]:
					return
				elif cmd.lower() in ['d',]:
					print(menutext)
				elif cmd.lower() in ['ap','ad person','add person','add personnel','ad personnl']:
					self.addPerson()
				elif cmd.lower() in ['rp','rm person','rmperson','del person','delperson','del taco','deltaco']:
					self.rmPerson()
				elif cmd.lower() in ['sap','sa person','saperson','sa person','walk the planck']:
					self.saPerson()	
				elif cmd.lower() in ['ad','ad dpt','add department','add dpt','addpt']:
					self.addDepartment()
				elif cmd.lower() in ['rd','rm department','rmdpt','del dpt','deldpt']:
					self.rmDepartment()
				elif cmd.lower() in ['sad','sa department','sadpt','sa dpt']:
					self.saDepartment()
				elif cmd.lower() in ['ars','ad roster shift','add roster shift','adrstrshft']:
					self.addShift()
				elif cmd.lower() in ['sars','sa roster shift']:
					self.saRosterShift()
				elif cmd.lower() in ['cars','ca rostershift','clear all rostershift']:
					self.caRosterShift()
				elif cmd.lower() in ['cad','ca dpt','clear all departments']:
					self.caDepartments()
				elif cmd.lower() in ['cap','ca personnl','clear all people']:
					self.caPeople()
				elif cmd.lower() in ['lars','list all roster shift','ls * rs']:
					self.laRosterShift()
				elif cmd.lower() in ['whos here','personel','prsnl','prsnl','today','tdy']:
					self.whosHere()
				elif cmd.lower() in ['rars','rm roster shift']:
					self.rmRosterShift()
				elif cmd.lower() in ['fromblog',]:
					self.fromBlog()
				elif cmd.lower() in ['drangetest',]:
					drange=Prompt.__init2__(None,func=FormBuilderMkText,ptext="schedule format text:",helpText="month/day/year@hh:mm(FROM)-hh:mm(TO)",data="datetime~")
					print(drange)
				else:
					print(menutext)
			except Exception as e:
				print(e)