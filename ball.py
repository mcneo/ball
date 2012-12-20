#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ball.py
#  
#  Copyright 2012 Jeremy <jeremyrandallmcneal@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  


from random import choice, randint, triangular
from batterdata import *

#~ Baseball is a strange game. The difference between an average hitter
#~ and a great hitter is one more hit a week. I wonder if a player's plate
#~ discipline numbers can help achieve a more accurate representation of their 
#~ actual offensive capability. 

BALLS = 0
STRIKES = 0

class season:
	"""
	"""
	def __init__(self, teams=[]):
		self.teams = teams
		self.games_played = []
		self.season_length = 162
		
	def play_season(self):
		games_to_play = self.season_length / 2 * len(self.teams)
		while len(self.games_played) < games_to_play:
			# This will eventually be a scheduler
			matchup = self.choose_teams()
			active_game = game(matchup[0],matchup[1])
			active_game.play_game()
			self.games_played.append(active_game)
			
	def choose_teams(self):
		home_team = choice(self.teams)
		away_team = choice(self.teams)
		while home_team.name == away_team.name:
			home_team = choice(self.teams)
			away_team = choice(self.teams)
		teams = [away_team, home_team]
		return teams
		
	def __str__(self):
		mvp_ops = 0
		mvp = ''
		for team in self.teams:
			print "\n%s's Record: %s-%s %s" % (team.name,team.wins, team.losses, team.wins * 100 / (team.wins+team.losses))
			for i_batter in team.batters:
				first = i_batter.first_name
				last = i_batter.last_name
				avg = '%s' % (i_batter.hits / 1.0 / (i_batter.plate_appearances - i_batter.walks))
				obp = '%s' % ((i_batter.hits + i_batter.walks) / 1.0 / i_batter.plate_appearances)
				slg = '%s' % ((i_batter.hits + i_batter.doubles_hit + (i_batter.triples_hit *2) + (i_batter.homeruns_hit * 3) + i_batter.walks) / 1.0 / i_batter.plate_appearances)
				pas = i_batter.plate_appearances
				hrs = i_batter.homeruns_hit
				walk_per = i_batter.walks * 100 / i_batter.plate_appearances
				k_per = i_batter.strikeouts * 100 / i_batter.plate_appearances
				if float(obp)+float(slg) > mvp_ops:
					mvp_ops = float(obp)+float(slg)
					mvp = 'MVP is %s %s' % (i_batter.first_name, i_batter.last_name)
				print '%s %s %s/%s/%s PA:%s; HRs:%s; W:%s%%, K:%s%%' % (first, last, avg[2:5],obp[2:5],slg[2:5], pas, hrs, walk_per, k_per)
				
		return mvp
		
class batter:
	"""
	"""
	def __init__(self, data=[]):
		#Of 1000
		self.first_name = 'Albert'
		self.last_name = 'Pujols'
		self.foulball_chance = 370 # Chance that a ball swung at is fouled off
		self.babip = 280 #Batting Average for Balls in Play
		self.oswing = 254 #Swing Percent outside the zone
		self.zswing = 654 #Swing Percent inside the zone
		self.swing = 459 #Overall Swign Percentage
		self.ocontact = 617 #Percentage to make contact outside the zone
		self.zcontact = 879 #Percentage to make contact inside the zone
		self.contact = 808 #Percentage to make contact overall
		self.zone = 511 #Percentage of Pitches seen in the strike zone
		self.fstrike = 586 #Percentage of First Pitch strikes
		self.swinging_strike = 86 #Percentage of Swinging Strikes
		self.doubles = 145 #Percentage of Doubles Hit
		self.triples = 50 #Percentage of Triples Hit
		self.homeruns = 50 #Percentage of Homeruns Hit
		self.hits = 0
		self.walks = 0
		self.doubles_hit = 0
		self.triples_hit = 0
		self.homeruns_hit = 0
		self.strikeouts = 0
		self.plate_appearances = 0
		
		if len(data) > 0:
			self.load_batter(data)
		
	def isHit(self, objPitch):
		global BALLS, STRIKES
		if not objPitch.is_ball: #it's a strike
			STRIKES += 1
			swingchance = randint(0,1000)
			if swingchance < self.zswing:
				#Batter swings at the strike
				if randint(0,1000) < self.foulball_chance:
					return 'foul'
				else:
					hitchance = randint(0,1000)
					if hitchance < self.zcontact:
						#Batter makes contact!
						singlechance = randint(0,1000)
						if singlechance < self.babip:
							if singlechance < self.homeruns:
								return 'homerun'
							if singlechance < (self.homeruns + self.triples):
								return 'triple'
							if singlechance < (self.homeruns + self.triples + self.doubles):
								return 'double'
							else:
								return 'single'
						else:
							return 'out'
					else:
						#batter swings and misses
						return 'swinging strike'
			else:
				#Batter does not swing at strike
				return 'called strike'
		else:
			#it's a ball
			BALLS += 1
			swingchance = randint(0,1000)
			if swingchance < self.oswing:
				#Batter swings at the ball
				if randint(0,1000) < self.foulball_chance:
					return 'foul'
				else:
					hitchance = randint(0,1000)
					if hitchance < self.ocontact:
						#Batter Makes contact
						singlechance = randint(0,1000)
						if singlechance < self.babip:
							if singlechance < (self.homeruns*1000/185):
								return 'homerun'
							if singlechance < (self.homeruns + self.triples):
								return 'triple'
							if singlechance < (self.homeruns + self.triples + self.doubles):
								return 'double'
							else:
								return 'single'
						else:
							return 'out'
					else:
						#batter swings and misses
						return 'swinging strike'
			else:
				#batter does not swing
				return 'ball'
			
	def create(self):
		self.foulball_chance = triangular(100,300)
		self.babip = triangular(250,350)
		self.oswing = triangular(150,400)
		self.zswing = triangular(500,800)
		self.swing = triangular(300,600)
		self.ocontact = triangular(700,900)
		self.zcontact = triangular(800,950)
		self.contact = triangular(750,870)
		self.zone = triangular(450,600)
		self.fstrike = triangular(550,620)
		self.swinging_strike = triangular(50,100)
		self.doubles = triangular(100,200)
		self.triples = triangular(5,100)
		self.homeruns = triangular(5,110)
		
	def load_batter(self, lstBatter):
		if len(lstBatter) > 0:
			self.first_name = lstBatter[0]
			self.last_name = lstBatter[1]
			self.babip = lstBatter[2]
			self.oswing = lstBatter[3]
			self.zswing = lstBatter[4]
			self.swing = lstBatter[5]
			self.ocontact = lstBatter[6]
			self.zcontact = lstBatter[7]
			self.contact = lstBatter[8]
			self.zone = lstBatter[9]
			self.fstrike = lstBatter[10]
			self.swinging_strike = lstBatter[11]
			self.doubles = lstBatter[12]*100/185
			self.triples = lstBatter[13]*100/185
			self.homeruns = lstBatter[14]*100/185
		else:
			print 'Batter Data incomplete to load.'
		
class team:
	"""
	"""
	def __init__(self, name='NoName', first=batter(), second=batter(), 
					third=batter(), fourth=batter(), fifth=batter(),
					sixth=batter(), seventh=batter(), eighth=batter(),
					ninth=batter()):
						
		self.name = name
		self.batters = (first, second, third, fourth, fifth, sixth,
						seventh, eighth, ninth)
		self.wins = 0
		self.losses = 0
		
	def get_batter(self, pos=0):
		return self.batters[pos]
		
class pitch:
	"""
	"""
	def __init__(self, zone):
		self.pitch_type = choice(['fastball','slider','changeup'])
		self.speed = randint(60,88)
		if self.pitch_type == 'fastball':
			self.speed += 10
		if self.pitch_type == 'slider':
			self.speed += 5
		self.distance_from_center = randint(1,1000)
		self.is_ball = False
		if self.distance_from_center > zone:
			self.is_ball = True
		self.pitch_angle = randint(0,360)
		
class pitcher:
	"""
	Not yet implemented.
	"""
	def __init__():
		pass

class game:
	"""
	"""
	def __init__(self, home_team, away_team):
		self.game_over = False
		self.inning = 0
		self.half = 'bottom'
		self.outs = 0
		self.balls = 0
		self.strikes = 0
		self.pitches = 0
		self.total_strikes = 0
		self.total_balls = 0
		self.away_score = []
		self.home_score = []
		self.visitor_hits = []
		self.home_hits = []
		self.first_base = 0
		self.second_base = 0
		self.third_base = 0
		self.plate_appearances = 0
		self.walks = 0
		self.hits = 0
		self.singles = 0
		self.doubles = 0
		self.triples = 0
		self.homeruns = 0
		self.new_half()
		self.home_team = home_team
		self.away_team = away_team
		self.home_at_bats = 0
		self.away_at_bats = 0
		self.current_batter = self.away_team.get_batter(self.away_at_bats % 9)
		
	def play_game(self):
		while self.game_over == False:
			active_pitch = pitch(self.current_batter.zone)
			self.pitch(active_pitch)
		if sum(self.home_score) > sum(self.away_score):
			self.home_team.wins += 1
			self.away_team.losses += 1
		else:
			self.away_team.wins += 1
			self.home_team.losses += 1
		
	def pitch(self, objPitch):
		if self.half == 'bottom':
			self.current_batter = self.home_team.get_batter(self.home_at_bats % 9)
			self.home_at_bats += 1
		else:
			self.current_batter = self.away_team.get_batter(self.away_at_bats % 9)
			self.away_at_bats += 1
		self.pitches += 1
		result = self.current_batter.isHit(objPitch)
		if result == 'ball':
			self.ball()
		elif result == 'swinging strike':
			self.strike()
		elif result == 'called strike':
			self.strike()
		elif result == 'foul':
			if self.strikes < 2:
				self.strikes += 1
		elif result == 'single':
			self.single()
		elif result == 'double':
			self.double()
		elif result == 'triple':
			self.triple()
		elif result == 'homerun':
			self.homerun()
		elif result == 'out':
			self.out()
		
	def batter_on_base(self):			
		if self.first_base == 0:
			self.first_base = 1
		elif self.second_base == 0:
			self.second_base = 1
		elif self.third_base == 0:
			self.third_base = 1
		else:
			self.record_run()
		self.new_batter()
		
	def record_hit(self):
		self.hits += 1
		self.current_batter.hits += 1
		if self.half == 'top':
			self.visitor_hits[self.inning - 1] += 1
		else:
			self.home_hits[self.inning - 1] += 1
			
	def record_run(self):
		if self.half == 'top':
			self.away_score[self.inning - 1] += 1
		else:
			self.home_score[self.inning - 1] += 1
		
	def single(self):
		self.record_hit()
		self.singles += 1
			
		if self.first_base == 0:
			self.first_base = 1
		elif self.second_base == 0:
			self.second_base = 1
		elif self.third_base == 0:
			self.third_base = 1
		else:
			self.record_run()
		self.new_batter()
	
	def double(self):
		self.record_hit()
		self.current_batter.doubles_hit += 1
		self.doubles += 1
		
		if self.third_base == 1:
			self.record_run()
		if self.second_base == 1:
			self.record_run()
		if self.first_base == 1:
			self.third_base = 1
		self.second_base = 1
		
		self.new_batter()
	
	def triple(self):
		self.record_hit()
		self.current_batter.triples_hit += 1
		self.triples += 1
		
		if self.third_base == 1:
			self.record_run()
		if self.second_base == 1:
			self.record_run()
		if self.first_base == 1:
			self.record_run()
		self.third_base = 1
		
		self.new_batter()
	
	def homerun(self):
		self.record_hit()
		self.current_batter.homeruns_hit += 1
		self.homeruns += 1
		
		if self.third_base == 1:
			self.record_run()
		if self.second_base == 1:
			self.record_run()
		if self.first_base == 1:
			self.record_run()
		self.record_run()
		
		self.new_batter()
		
	def new_batter(self):
		self.current_batter.plate_appearances += 1
		self.strikes = 0
		self.balls = 0
		self.plate_appearances += 1
		
	def ball(self):
		self.balls += 1
		self.total_balls += 1
		if self.balls > 3:
			self.current_batter.walks += 1
			self.walks += 1
			self.batter_on_base()
			
	def strike(self):
		self.strikes += 1
		self.total_strikes += 1
		if self.strikes > 2:
			self.current_batter.strikeouts += 1
			self.out()
			
	def out(self):
		self.outs += 1
		if self.outs > 2:
			self.new_half()
		self.new_batter()
			
	def new_half(self):
		self.outs = 0
		self.first_base = 0
		self.second_base = 0
		self.third_base = 0
		
		if self.inning >= 9:
			if self.home_score > self.away_score:
				self.game_over = True
			
		if not self.game_over:
			if self.half == 'top':
				self.half = 'bottom'
				self.home_score.append(0)
				self.home_hits.append(0)
			else:
				if self.inning >= 9:
					self.game_over = True
				else:
					self.inning += 1
					self.half = 'top'
					self.away_score.append(0)
					self.visitor_hits.append(0)
	
	def __str__(self):
		visitor_score_record = ''
		visitor_runs = 0
		for score in self.away_score:
			visitor_score_record += ' %s ' % score
			visitor_runs += score
		home_score_record = ''
		home_team_runs = 0
		for score in self.home_score:
			home_score_record += ' %s ' % score
			home_team_runs += score
		output = '\t\t\t 1  2  3  4  5  6  7  8  9\t |\n'
		output += self.away_team.name,':\t',visitor_score_record,'\t | ',visitor_runs,'\n'
		output += self.home_team.name,':\t',home_score_record,'\t | ',home_team_runs,'\n'
		return output

KCR = team('Kansas City Royals', batter(alex_gordon), batter(johnny_giavotella), 
			batter(billy_butler), batter(mike_moustakas),
			batter(albert_pujols), batter(salvador_perez),
			batter(perfect_hitter), batter(lorenzo_cain),
			batter(alcides_escobar))
STL = team('St Louis Cardinals', batter(jon_jay), batter(david_freese), 
			batter(allen_craig), batter(matt_holiday),
			batter(carlos_beltran), batter(yadier_molina),
			batter(matt_carpenter), batter(skip_schumaker),
			batter(pete_kozma))
			
objSeason = season([KCR,STL])
objSeason.play_season()

print objSeason
	
	
