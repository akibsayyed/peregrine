#!/usr/bin/python
#--------------------------------------------------------------------------
#                           SoftGNSS v3.0
# 
# Copyright (C) Darius Plausinaitis and Dennis M. Akos
# Written by Darius Plausinaitis and Dennis M. Akos
# Converted to Python by Colin Beighley
#--------------------------------------------------------------------------
#This program is free software; you can redistribute it and/or
#modify it under the terms of the GNU General Public License
#as published by the Free Software Foundation; either version 2
#of the License, or (at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program; if not, write to the Free Software
#Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301,
#USA.
#--------------------------------------------------------------------------

from operator import itemgetter

def preRun(acqResults,settings):
  #Initialize list of tracking channel initial states
  channel = [track_chan_init_state() for i in range(min(len(acqResults),settings.numberOfChannels))]
  #Sort acqResults by peak strength
  acqResults_sorted = sorted(acqResults,reverse=True,key=itemgetter(0))
  #Assign highest peaks from acquisition to track chan init list
  for i in range(min(len(acqResults),settings.numberOfChannels)):
    channel[i].PRN = acqResults[i][3]
    channel[i].codePhase = acqResults[i][2]
    channel[i].acquiredFreq = acqResults[i][1]
    channel[i].status = 'T'
  return channel
  
class track_chan_init_state:
  PRN          = 0
  acquiredFreq = 0.0
  codePhase    = 0
  status       = '-'