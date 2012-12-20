#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  batterdata.py
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


#~ template = {first_name:'',last_name:'',babip:,
				#~ oswing:, zswing:, swing:, ocontact:,
				#~ zcontact:, contact:, zone:, fstrike:,
				#~ swingstrike:, doubles:, triples:, homeruns:}
				
billy_butler = {'first nam':'Billy', 'last name':'Butler', 'babip':322,
				'oswing':273, 'zswing':634, 'swing':434, 'ocontact':733,
				'zcontact':917, 'contact':853, 'zone':445, 'fstrike':527,
				'swingstrike':63, 'doubles':72, 'triples':1, 'homeruns':24}
				
josh_hamilton = ('Josh','Hamilton',343,356,820,560,606,827,749,440,568,135,82,8,59)
vlad_guerrero = ('Vlad','Guerrero',318,472,800,606,716,894,812,407,626,109,43,1,54)
jose_guillen = ('Jose','Guillen',299,371,649,500,686,841,779,463,580,106,44,5,44)
wilson_betemit = ('Wilson','Betemit',330,231,600,390,544,922,794,430,573,77,10,1,45)

#2012 KCR
alex_gordon = ('Alex','Gordon',356,281,652,447,656,876,800,448,560,87,51,5,14)
alex_gordon = ('Alex','Gordon',340,281,652,447,656,876,800,448,560,87,51,5,14) # normalized
salvador_perez = ('Sal','Perez',299,376,631,498,883,928,910,481,633,44,32,1,22)
billy_butler = ('Billy','Butler',341,299,598,436,711,894,826,456,558,74,32,1,29)
jeff_franceour = ('Jeff','Franceour',272,427,706,541,738,863,805,409,620,103,26,3,16) 
jeff_franceour = ('Jeff','Franceour',300,427,706,541,738,863,805,409,620,103,26,3,16) #normalized
eric_hosmer = ('Eric','Hosmer',255,335,670,475,745,863,815,418,559,85,22,2,14)
eric_hosmer = ('Eric','Hosmer',300,335,670,475,745,863,815,418,559,85,22,2,14) #normalized
mike_moustakas = ('Mike','Moustakas',274,376,667,497,662,871,779,416,544,108,34,1,20)
mike_moustakas = ('Mike','Moustakas',300,376,667,497,662,871,779,416,544,108,34,1,20) #normalized
alcides_escobar = ('Alcides','Escobar',344,327,647,483,725,873,822,486,613,85,30,7,5)
lorenzo_cain = ('Lorenzo','Cain',319,319,582,439,552,871,745,456,574,111,25,4,15)
johnny_giavotella = ('Johnny','Giavotella',290,312,621,456,758,886,839,468,646,71,30,3,10)
johnny_giavotella = ('Johnny','Giavotella',300,312,621,456,758,886,839,468,646,71,30,3,10) #normalized

#2012 STL
yadier_molina = ('Yadier','Molina',316,312,744,519,788,886,855,480,618,72,35,1,26)
matt_holiday = ('Matt','Holiday',337,317,731,477,684,859,788,387,564,98,36,2,27)
david_freese = ('David','Freese',352,322,648,469,592,850,753,451,591,113,27,1,22)
jon_jay = ('Jon','Jay',355,281,598,431,731,948,873,473,604,53,27,7,7)
carlos_beltran = ('Carlos','Beltran',291,314,702,472,636,898,795,408,577,93,26,1,32)
allen_craig = ('Allen','Craig',334,286,611,436,738,894,839,462,566,69,42,0,26)
matt_carpenter = ('Matt','Carpenter',346,221,656,415,643,908,830,446,550,67,30,8,11)
pete_kozma = ('Pete','Kozma',415,189,621,390,600,910,830,465,598,65,40,8,10) #ACTUAL
pete_kozma = ('Pete','Kozma',315,187,641,415,525,908,825,490,578,71,35,8,10) #NORMALIZED
skip_schumaker = ('Skip','Schumaker',332,299,665,443,755,938,863,393,592,59,30,8,3)

# Others
sam_fuld = ('Sam','Fuld',298,229,538,372,755,981,906,460,617,33,18,8,2)
albert_pujols = ('Albert','Pujols',320,364,626,477,770,907,848,431,563,70,50,1,30)
perfect_hitter = ('Perfect','Hitter',330,196,849,354,890,980,953,333,504,18,50,10,30) #Turns out I really like Marco Scutaro
# On a side note, if I ever finish this, I may have to call it the scutaro projections.
# Turns out the perfect hitter is mostly made up of Marco Scutaro, and a tad of Josh Hamilton.




