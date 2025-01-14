# -*- coding: utf-8 -*-
"""
New paradigm Rubik's Cube Solving algorithm

Charles Thomas Wallace Truscott
(Computational Thinking with Python MITx, Using Python for Research Harvard T.H. Chan School of Medicine)

"If I had six hours to chop down a tree, I would spend the first four sharpening the axe" - Benjamin Franklin

Thank you so much Byron Central Hospital, John Flynn Private Hospital, Gold Coast University Hospital.

Very proud of my optimal, dynamic programming, matrix computation algorithm to solve the 2 x 2 Rubik's cube. 

Copyright Charles Truscott, 2024 December

Suffolk Park / Byron Bay, NSW 2481

I love you Tai, I love you Mark - beloved father. I love you Rodney.

Thank you so much United States Department of Defence, Offensive Security, MIT faculty.

I have been on the Centrelink Disability pension for 12 years because of Schizophrenia, and a brain injury, sleep disorder and memory disorder.

I recently walked into an employment agency and I was very tickled pink to put MITx and HarvardX on the resume.

I may get my dream tech career here in Byron Bay, but there is not circumstantially the industry locally to need to hire a full-wage programmer, data scientist or cybersecurity consultant.

I may be the only one in the nation or globally working on this problem on Christmas Eve 2024.

Very excited to return to society after forced disappearance.

Thank you General Michael Hayden CIA NSA ODNI

Thank you Carl Joseph Truscott former Assistant Director General of the United States Secret Service, BATF

Solved: ['D', 'D', 'D', 'B inverse']
Initial State:
Front Face: ['G', 'G', 'W', 'O']
Left Face: ['W', 'O', 'B', 'B']
Right Face: ['R', 'Y', 'G', 'G']
Back Face: ['B', 'B', 'R', 'Y']
Up Face: ['R', 'R', 'W', 'W']
Down Face:['O', 'Y', 'O', 'Y']
Solved State: Front Face: ['G', 'G', 'G', 'G'], Left Face: ['O', 'O', 'O', 'O'], Right Face:['R', 'R', 'R', 'R'] Back Face: ['B', 'B', 'B', 'B'], Up face: ['W', 'W', 'W', 'W'], Down face: ['Y', 'Y', 'Y', 'Y']

********
Moves: ['D', 'D', 'D', 'B inverse']
*******
Charles Truscott Watters, Byron Bay NSW 2481

[Program finished]

 n = RubiksState(["W", "O", "G"], ["O", "B", "W"],  ["W", "R", "G"], ["Y", "G", "O"], ["R", "W", "B"], ["O", "B", "Y"], ["R", "Y", "B"], ["Y", "G", "R"], [])
 
"""
import itertools
# n = RubiksState([], [], [], [], [], [], [], [])
# n = RubiksState(['W', 'O', 'G'], ['B', 'O', 'Y'], ['W', 'R', 'G'], ['O', 'Y', 'G'], ['W', 'O', 'B'], ['B', 'R', 'Y'], ['W', 'R', 'B'], ['R', 'Y', 'G'], [])
class RubiksState(object):
    def __init__(self, tlf, blf, trf, brf, tlb, blb, trb, brb, moves):
        self.tlf = tlf
        self.blf = blf
        self.trf = trf
        self.brf = brf
        self.tlb = tlb
        self.blb = blb
        self.trb = trb
        self.brb = brb
        
        self.left_face = [self.tlb[1], self.tlf[1], self.blb[1], self.blf[1]]
        self.right_face = [self.trf[1], self.trb[1], self.brf[1], self.brb[1]]
        self.front_face = [self.tlf[2], self.trf[2], self.blf[2], self.brf[2]]
        self.back_face = [self.trb[2], self.tlb[2], self.brb[2], self.blb[2]]
        self.up_face  = [self.tlb[0], self.trb[0], self.tlf[0], self.trf[0]]
        self.down_face = [self.blf[0], self.brf[0], self.blb[0], self.brb[0]]
        self.orientation = [self.front_face, self.left_face, self.right_face, self.back_face, self.up_face, self.down_face]
        print("Front face: {}".format(self.front_face))
        print("Left Face: {}".format(self.left_face))
        print("Right Face: {}".format(self.right_face))
        print("Back Face: {}".format(self.back_face))
        print("Up face: {}".format(self.up_face))
        print("Down face:{}".format(self.down_face))
        self.moves = moves
        if self.is_solved():
        	print("SOLVED: {}".format(self.moves))
    def L(self):
        """ TLF to TLB, TLB to BLB, BLB to BLF, BLF to TLF """
        ntlf, nblf, ntlb, nblb = [0] * 3, [0] * 3, [0] * 3, [0] * 3
        ttlf, tblf, ttlb, tblb = self.tlf, self.blf, self.tlb, self.blb
        ntlf[0], ntlf[1], ntlf[2] = tblf[2], tblf[1], tblf[0]
        nblf[0], nblf[1], nblf[2] = tblb[2], tblb[1], tblb[0]
        ntlb[0], ntlb[1], ntlb[2] = ttlf[2], ttlf[1], ttlf[0]
        nblb[0], nblb[1], nblb[2] = ttlb[2], ttlb[1], ttlb[0]
        moves = self.moves.copy()
        moves.append('L')
        n = RubiksState(ntlf, nblf, self.trf.copy(), self.brf.copy(), ntlb, nblb, self.trb.copy(), self.brb.copy(), moves)
        #tlf, blf, trf, brf, tlb, blb, trb, brb, moves
        return n
    def L2(self):
        """ TLF to BLB, BLB to TLF, TLB to BLF, BLF to TLB """
        ntlf, nblf, ntlb, nblb = [0] * 3, [0] * 3, [0] * 3, [0] * 3
        ttlf, tblf, ttlb, tblb = self.tlf, self.blf, self.tlb, self.blb
        nblb[0], nblb[1], nblb[2] = ttlf[0], ttlf[1], ttlf[2]
        ntlf[0], ntlf[1], ntlf[2] = tblb[0], tblb[1], tblb[2]
        nblf[0], nblf[1], nblf[2] = ttlb[0], ttlb[1], ttlb[2]
        ntlb[0], ntlb[1], ntlb[2] = tblf[0], tblf[1], tblf[2]
        moves = self.moves.copy()
        moves.append('L2')
        n = RubiksState(ntlf, nblf, self.trf.copy(), self.brf.copy(), ntlb, nblb, self.trb.copy(), self.brb.copy(), moves)
        return n
    def Linv(self):
        """ TLF to BLF, BLF to BLB, BLB to TLB, TLB to TLF """
        
        ntlf, nblf, ntlb, nblb = [0] * 3, [0] * 3, [0] * 3, [0] * 3
        ttlf, tblf, ttlb, tblb = self.tlf, self.blf, self.tlb, self.blb
        nblf[0], nblf[1], nblf[2] = ttlf[2], ttlf[1], ttlf[0]
        nblb[0], nblb[1], nblb[2] = tblf[2], tblf[1], tblf[0]
        ntlb[0], ntlb[1], ntlb[2] = tblb[2], tblb[1], tblb[0]
        ntlf[0], ntlf[1], ntlf[2] = ttlb[2], ttlb[1], ttlb[0]
        moves = self.moves.copy()
        moves.append('L inverse')
        n = RubiksState(ntlf, nblf, self.trf.copy(), self.brf.copy(), ntlb, nblb, self.trb.copy(), self.brb.copy(), moves)
        #tlf, blf, trf, brf, tlb, blb, trb, brb, moves
        return n
        
        pass
    def R(self):
        """ TRF to TRB, TRB to BRB, BRB to BRF, BRF to TRF """
        ttrf, tbrf, ttrb, tbrb = self.trf, self.brf, self.trb, self.brb
        ntrf, nbrf, ntrb, nbrb = [0] * 3, [0] * 3, [0] * 3, [0] * 3
        ntrb[2], ntrb[1], ntrb[0] = ttrf[0], ttrf[1], ttrf[2]
        nbrb[2], nbrb[1], nbrb[0] = ttrb[0], ttrb[1], ttrb[2]
        nbrf[2], nbrf[1], nbrf[0] = tbrb[0], tbrb[1], tbrb[2]
        ntrf[2], ntrf[1], ntrf[0] = tbrf[0], tbrf[1], tbrf[2]
        moves = self.moves.copy()
        moves.append('R')
        n = RubiksState(self.tlf.copy(), self.blf.copy(), ntrf, nbrf, self.tlb.copy(), self.blb.copy(), ntrb, nbrb, moves)
        #tlf, blf, trf, brf, tlb, blb, trb, brb, moves
        return n
    def R2(self):
        """ TRF to BRB, BRB to TRF, BRF to TRB, TRB to BRF """
        ttrf, tbrf, ttrb, tbrb = self.trf, self.brf, self.trb, self.brb
        ntrf, nbrf, ntrb, nbrb = [0] * 3, [0] * 3, [0] * 3, [0] * 3
        nbrb[0], nbrb[1], nbrb[2] = ttrf[0], ttrf[1], ttrf[2]
        ntrf[0], ntrf[1], ntrf[2] = tbrb[0], tbrb[1], tbrb[2]
        ntrb[0], ntrb[1], ntrb[2] = tbrf[0], tbrf[1], tbrf[2]
        nbrf[0], nbrf[1], nbrf[2] = ttrb[0], ttrb[1], ttrb[2]
        moves = self.moves.copy()
        moves.append('R2')
        n = RubiksState(self.tlf.copy(), self.blf.copy(), ntrf, nbrf, self.tlb.copy(), self.blb.copy(), ntrb, nbrb, moves)
        #tlf, blf, trf, brf, tlb, blb, trb, brb, moves
        return n
    def Rinv(self):
        """ TRF to BRF, BRF to BRB, BRB to TRB, TRB to TRF """
        ttrf, tbrf, ttrb, tbrb = self.trf, self.brf, self.trb, self.brb
        ntrf, nbrf, ntrb, nbrb = [0] * 3, [0] * 3, [0] * 3, [0] * 3
        nbrf[0], nbrf[1], nbrf[2] = ttrf[2], ttrf[1], ttrf[0]
        nbrb[0], nbrb[1], nbrb[2] = tbrf[2], tbrf[1], tbrf[0]
        ntrb[0], ntrb[1], ntrb[2] = tbrb[2], tbrb[1], tbrb[0]
        ntrf[0], ntrf[1], ntrf[2] = ttrb[2], ttrb[1], ttrb[0]
        moves = self.moves.copy()
        moves.append('R inverse')
        n = RubiksState(self.tlf.copy(), self.blf.copy(), ntrf, nbrf, self.tlb.copy(), self.blb.copy(), ntrb, nbrb, moves)
        #tlf, blf, trf, brf, tlb, blb, trb, brb, moves
        return n
# From here below
    def U(self):
        """ TLF to TRF, TRF to TRB, TRB to TLB, TLB to TLF """
        ntlf, ntlb, ntrf, ntrb = [0] * 3, [0] * 3, [0] * 3, [0] * 3
        ttlf, ttrf, ttlb, ttrb = self.tlf, self.trf, self.tlb, self.trb
        ntrf[0], ntrf[1], ntrf[2] = ttlf[0], ttlf[2], ttlf[1]
        ntrb[0], ntrb[1], ntrb[2] = ttrf[0], ttrf[2], ttrf[1]
        ntlb[0], ntlb[1], ntlb[2] = ttrb[0], ttrb[2], ttrb[1]
        ntlf[0], ntlf[1], ntlf[2] = ttlb[0], ttlb[2], ttlb[1]
        moves = self.moves.copy()
        moves.append('U')
        n = RubiksState(ntlf, self.blf, ntrf, self.brf, ntlb, self.blb, ntrb, self.brb, moves)
        return n
    def U2(self):
        """ TLF to TRB, TRB to TLF, TRF to TLB, TLB to TRF """
        ttlf, ttrf, ttlb, ttrb = self.tlf, self.trf, self.tlb, self.trb
        ntlf, ntlb, ntrf, ntrb = [0] * 3, [0] * 3, [0] * 3, [0] * 3
        ntrb[0], ntrb[1], ntrb[2] = ttlf[0], ttlf[1], ttlf[2]
        ntlf[0], ntlf[1], ntlf[2] = ttrb[0], ttrb[1], ttrb[2]
        ntlb[0], ntlb[1], ntlb[2] = ttrf[0], ttrf[1], ttrf[2]
        ntrf[0], ntrf[1], ntrf[2] = ttlb[0], ttlb[1], ttlb[2]
        moves = self.moves.copy()
        moves.append('U2')
        n = RubiksState(ntlf, self.blf, ntrf, self.brf, ntlb, self.blb, ntrb, self.brb, moves)
        return n
    def Uinv(self):
        """ TLF to TLB, TLB to TRB, TRB to TRF, TRF to TLF """
        ntlf, ntlb, ntrf, ntrb = [0] * 3, [0] * 3, [0] * 3, [0] * 3
        ttlf, ttrf, ttlb, ttrb = self.tlf, self.trf, self.tlb, self.trb
        ntlb[0], ntlb[1], ntlb[2] = ttlf[0], ttlf[2], ttlf[1]
        ntrb[0], ntrb[1], ntrb[2] = ttlb[0], ttlb[2], ttlb[1]
        ntrf[0], ntrf[1], ntrf[2] = ttrb[0], ttrb[2], ttrb[1]
        ntlf[0], ntlf[1], ntlf[2] = ttrf[0], ttrf[2], ttrf[1]
        moves = self.moves.copy()
        moves.append('U inverse')
        n = RubiksState(ntlf, self.blf, ntrf, self.brf, ntlb, self.blb, ntrb, self.brb, moves)
        return n
    
    def D(self):
        """ BLF to BRF, BRF to BRB, BRB to BLB, BLB to BLF """
        nblf, nblb, nbrf, nbrb = [0] * 3, [0] * 3, [0] * 3, [0] * 3
        tblf, tbrf, tbrb, tblb = self.blf, self.brf, self.brb, self.blb
        nbrf[0], nbrf[1], nbrf[2] = tblf[0], tblf[2], tblf[1]
        nbrb[0], nbrb[1], nbrb[2] = tbrf[0], tbrf[2], tbrf[1]
        nblb[0], nblb[1], nblb[2] = tbrb[0], tbrb[2], tbrb[1]
        nblf[0], nblf[1], nblf[2] = tblb[0], tblb[2], tblb[1]
        moves = self.moves.copy()
        moves.append('D')
        n = RubiksState(self.tlf, nblf, self.trf, nbrf, self.tlb, nblb, self.trb, nbrb, moves)
        #tlf, blf, trf, brf, tlb, blb, trb, brb, moves
        return n
    def D2(self):
        """ BLF to BRB, BRB to BLF, BRF to BLB, BLB to BRF """
        nblf, nblb, nbrf, nbrb = [0] * 3, [0] * 3, [0] * 3, [0] * 3
        tblf, tbrf, tbrb, tblb = self.blf, self.brf, self.brb, self.blb
        nbrb[0], nbrb[1], nbrb[2] = tblf[0], tblf[1], tblf[2]
        nblf[0], nblf[1], nblf[2] = tbrb[0], tbrb[1], tbrb[2]
        nblb[0], nblb[1], nblb[2] = tbrf[0], tbrf[1], tbrf[2]
        nbrf[0], nbrf[1], nbrf[2] = tblb[0], tblb[1], tblb[2]
        moves = self.moves.copy()
        moves.append('D2')
        n = RubiksState(self.tlf, nblf, self.trf, nbrf, self.tlb, nblb, self.trb, nbrb, moves)
        #tlf, blf, trf, brf, tlb, blb, trb, brb, moves
        return n
    def Dinv(self):
        """ BLF to BLB, BLB to BRB, BRB to BRF, BRF to BLF """
        nblf, nblb, nbrf, nbrb = [0] * 3, [0] * 3, [0] * 3, [0] * 3
        tblf, tbrf, tbrb, tblb = self.blf, self.brf, self.brb, self.blb
        nblb[0], nblb[1], nblb[2] = tblf[0], tblf[2], tblf[1]
        nbrb[0], nbrb[1], nbrb[2] = tblb[0], tblb[2], tblb[1]
        nbrf[0], nbrf[1], nbrf[2] = tbrb[0], tbrb[2], tbrb[1]
        nblf[0], nblf[1], nblf[2] = tbrf[0], tbrf[2], tbrf[1]
        moves = self.moves.copy()
        moves.append('D inverse')
        n = RubiksState(self.tlf, nblf, self.trf, nbrf, self.tlb, nblb, self.trb, nbrb, moves)
        #tlf, blf, trf, brf, tlb, blb, trb, brb, moves
        return n
# From here
    def F(self):
        """ TLF to BLF, BLF to BRF, BRF to TRF, TRF to TLF """
        ntlf, nblf, ntrf, nbrf = [0] * 3, [0] * 3, [0] * 3, [0] * 3
        ttlf, ttrf, tblf, tbrf = self.tlf, self.trf, self.blf, self.brf
        nblf[0], nblf[1], nblf[2] = ttlf[1], ttlf[0], ttlf[2]
        nbrf[0], nbrf[1], nbrf[2] = tblf[1], tblf[0], tblf[2]
        ntrf[0], ntrf[1], ntrf[2] = tbrf[1], tbrf[0], tbrf[2]
        ntlf[0], ntlf[1], ntlf[2] = ttrf[1], ttrf[0], ttrf[2]
        moves = self.moves.copy()
        moves.append('F')
        n = RubiksState(ntlf, nblf, ntrf, nbrf, self.tlb, self.blb, self.trb, self.brb, moves)
        #tlf, blf, trf, brf, tlb, blb, trb, brb, moves
        return n
    def F2(self):
        """ TLF to BRF, BRF to TLF, TRF to BLF, BLF to TRF """
        ttlf, ttrf, tblf, tbrf = self.tlf, self.trf, self.blf, self.brf
        ntlf, nblf, ntrf, nbrf = [0] * 3, [0] * 3, [0] * 3, [0] * 3
        nbrf[0], nbrf[1], nbrf[2] = ttlf[0], ttlf[1], ttlf[2]
        ntlf[0], ntlf[1], ntlf[2] = tbrf[0], tbrf[1], tbrf[2]
        nblf[0], nblf[1], nblf[2] = ttrf[0], ttrf[1], ttrf[2]
        ntrf[0], ntrf[1], ntrf[2] = tblf[0], tblf[1], tblf[2]
        moves = self.moves.copy()
        moves.append('F2')
        n = RubiksState(ntlf, nblf, ntrf, nbrf, self.tlb, self.blb, self.trb, self.brb, moves)
        #tlf, blf, trf, brf, tlb, blb, trb, brb, moves
        return n
    def Finv(self):
        """ TLF to TRF, TRF to BRF, BRF to BLF, BLF to TLF """
        ntlf, nblf, ntrf, nbrf = [0] * 3, [0] * 3, [0] * 3, [0] * 3
        ttlf, ttrf, tblf, tbrf = self.tlf, self.trf, self.blf, self.brf
        ntrf[0], ntrf[1], ntrf[2] = ttlf[1], ttlf[0], ttlf[2]
        nbrf[0], nbrf[1], nbrf[2] = ttrf[1], ttrf[0], ttrf[2]
        nblf[0], nblf[1], nblf[2] = tbrf[1], tbrf[0], tbrf[2]
        ntlf[0], ntlf[1], ntlf[2] = tblf[1], tblf[0], tblf[2]
        moves = self.moves.copy()
        moves.append('F inverse')
        n = RubiksState(ntlf, nblf, ntrf, nbrf, self.tlb, self.blb, self.trb, self.brb, moves)
        #tlf, blf, trf, brf, tlb, blb, trb, brb, moves
        return n
    def B(self):
        """ TLB to BLB, BLB to BRB, BRB to TRB, TRB to TLB """
        ntlb, nblb, ntrb, nbrb = [0] * 3, [0] * 3, [0] * 3, [0] * 3
        ttlb, tblb, ttrb, tbrb = self.tlb, self.blb, self.trb, self.brb
        nblb[0], nblb[1], nblb[2] = ttlb[1], ttlb[0], ttlb[2]
        nbrb[0], nbrb[1], nbrb[2] = tblb[1], tblb[0], tblb[2]
        ntrb[0], ntrb[1], ntrb[2] = tbrb[1], tbrb[0], tbrb[2]
        ntlb[0], ntlb[1], ntlb[2] = ttrb[1], ttrb[0], ttrb[2]
        moves = self.moves.copy()
        moves.append('B')
        n = RubiksState(self.tlf, self.blf, self.trf, self.brf, ntlb, nblb, ntrb, nbrb, moves)
        #tlf, blf, trf, brf, tlb, blb, trb, brb, moves
        return n
    def B2(self):
        """ TLB to BRB, BRB to TLB, TRB to BLB, BLB to TRB """
        ttlb, tblb, ttrb, tbrb = self.tlb, self.blb, self.trb, self.brb
        ntlb, nblb, ntrb, nbrb = [0] * 3, [0] * 3, [0] * 3, [0] * 3
        nbrb[0], nbrb[1], nbrb[2] = ttlb[0], ttlb[1], ttlb[2]
        ntlb[0], ntlb[1], ntlb[2] = tbrb[0], tbrb[1], tbrb[2]
        nblb[0], nblb[1], nblb[2] = ttrb[0], ttrb[1], ttrb[2]
        ntrb[0], ntrb[1], ntrb[2] = tblb[0], tblb[1], tblb[2]
        moves = self.moves.copy()
        moves.append('B2')
        n = RubiksState(self.tlf, self.blf, self.trf, self.brf, ntlb, nblb, ntrb, nbrb, moves)
        #tlf, blf, trf, brf, tlb, blb, trb, brb, moves
        return n
    def Binv(self):
        """ BLB to TLB, TLB to TRB, TRB to BRB, BRB to BLB"""
        ntlb, nblb, ntrb, nbrb = [0] * 3, [0] * 3, [0] * 3, [0] * 3
        ttlb, tblb, ttrb, tbrb = self.tlb, self.blb, self.trb, self.brb
        ntlb[1], ntlb[0], ntlb[2] = tblb[0], tblb[1], tblb[2] 
        ntrb[1], ntrb[0], ntrb[2] = ttlb[0], ttlb[1], ttlb[2]
        nbrb[1], nbrb[0], nbrb[2] = ttrb[0], ttrb[1], ttrb[2]
        nblb[1], nblb[0], nblb[2] = tbrb[0], tbrb[1], tbrb[2]

        moves = self.moves.copy()
        moves.append("B inverse")
        n = RubiksState(self.tlf, self.blf, self.trf, self.brf, ntlb, nblb, ntrb, nbrb, moves)
        #tlf, blf, trf, brf, tlb, blb, trb, brb, moves
        return n
    def is_solved(self):
        if self.blb == ['Y', 'O', 'B'] and self.tlb == ['W', 'O', 'B'] and self.brb == ['Y', 'R', 'B'] and self.trb == ['W', 'R', 'B'] and self.blf == ['Y', 'O', 'G'] and self.tlf == ['W', 'O', 'G'] and self.brf == ['Y', 'R', 'G'] and self.trf == ['W', 'R', 'G']:
            print('Solved: {}'.format(self.moves))
#            exit(1)
        if self.front_face == ['G', 'G', 'G', 'G'] and self.back_face == ['B', 'B', 'B', 'B'] and self.left_face == ['O', 'O', 'O', 'O'] and self.right_face == ['R', 'R', 'R', 'R'] and self.up_face == ['W', 'W', 'W', 'W'] and self.down_face == ['Y', 'Y', 'Y', 'Y']:
            return True
        else:
            return False
from queue import deque
import sys
def Charles():
    States = deque([])
#    n = RubiksState(['O', 'B', 'Y'], ['R', 'B', 'Y', ], ['O', 'G', 'Y'], ['R', 'G', 'Y'], ['O', 'B', 'W'], ['R', 'B', 'W'], ['O', 'G', 'W'], ['R', 'G', 'W'], [])
    all_states = [n for n in itertools.permutations([['G', 'G', 'G', 'G'], ['B', 'B', 'B', 'B'], ['O', 'O', 'O', 'O'], ['R', 'R', 'R', 'R'], ['W', 'W', 'W', 'W'], ['Y', 'Y', 'Y', 'Y']])]
    n = RubiksState(["W", "O", "G"], ["O", "B", "W"],  ["W", "R", "G"], ["Y", "G", "O"], ["R", "W", "B"], ["O", "B", "Y"], ["R", "Y", "B"], ["Y", "G", "R"], [])
    initial_state = n.orientation
#    print(all_states)
#    sys.exit(1)
    #tlf, blf, trf, brf, tlb, blb, trb, brb, moves
    moves = [lambda s: s.L(), lambda s: s.Linv(), lambda s: s.R(), lambda s: s.Rinv(), lambda s: s.U(), lambda s: s.Uinv(), lambda s: s.D(), lambda s: s.F(), lambda s: s.Finv(), lambda s: s.B(), lambda s: s.Binv()]
 #   moves = [lambda s: s.L(), lambda s: s.L2(), lambda s: s.Linv(), lambda s: s.R(), lambda s: s.R2(), lambda s: s.Rinv(), lambda s: s.U(), lambda s: s.U2(), lambda s: s.Uinv(), lambda s: s.D(), lambda s: s.D2(), lambda s: s.Dinv(), lambda s: s.F(), lambda s: s.F2(), lambda s: s.Finv(), lambda s: s.B(), lambda s: s.B2(), lambda s: s.Binv()]
    States.append(n)
    c = 0
    solved = False
    print(States)
    for move in moves:
        print(move(States[0]))
    for move in moves:
        States.append(move(States[0]))
    print(States)
#    for state in States:
#        print("Is solved: {} Front Face: {}, Left Face: {}, Right Face:{} Back Face: {}, Up face: {}, Down face: {}".format(state.is_solved(), state.front_face, state.left_face, state.right_face, state.back_face, state.up_face, state.down_face))
#    while n < 8 ** 6:
#        state = States.popleft()
#        for move in moves:
#            new_move = move(state)
#            print(new_move.moves)
#            States.append(new_move)
#            if new_move.front_face == ['G', 'G', 'G', 'G'] and new_move.back_face == ['B', 'B', 'B', 'B'] and new_move.left_face == ['O', 'O', 'O', 'O'] and new_move.right_face == ['R', 'R', 'R', 'R'] and new_move.up_face == ['W', 'W', 'W', 'W'] and new_move.down_face == ['Y', 'Y', 'Y', 'Y']:
#                print('Solved, {}'.format(new_move.moves))
#                break
#        n += 1
    while solved != True:
        state = States.popleft()
        for move in moves:
            t = move(state)
            print(t.moves)
            States.append(t)
#            if t.front_face == ['G', 'G', 'G', 'G'] and t.back_face == ['B', 'B', 'B', 'B'] and t.left_face == ['O', 'O', 'O', 'O'] and t.right_face == ['R', 'R', 'R', 'R'] and t.up_face == ['W', 'W', 'W', 'W'] and t.down_face == ['Y', 'Y', 'Y', 'Y']:
#                print('Solved, {}'.format(t.moves))
#                break
# #               sys.exit(1)
#            if t.is_solved() == True:
#                print('Solved, {}'.format(t.moves))
#                break
##                sys.exit(1)
#            if t.orientation in all_states:
#                print('Solved: {}'.format(t.moves))
#                break
        if state.orientation in all_states:
            solved = True
            print("Initial State:\nFront Face: {}\nLeft Face: {}\nRight Face: {}\nBack Face: {}\nUp Face: {}\nDown Face:{}".format(n.front_face, n.left_face, n.right_face, n.back_face, n.up_face, n.down_face))
            print("Solved State: Front Face: {}, Left Face: {}, Right Face:{} Back Face: {}, Up face: {}, Down face: {}\n".format(state.front_face, state.left_face, state.right_face, state.back_face, state.up_face, state.down_face))
            print("********")
            print("Moves: {}".format(state.moves))
            print("*******")
            print("Charles Truscott Watters, Byron Bay NSW 2481")
        if state.is_solved() == True:
            solved = True
            print("Initial State:\nFront Face: {}\nLeft Face: {}\nRight Face: {}\nBack Face: {}\nUp Face: {}\nDown Face:{}".format(n.front_face, n.left_face, n.right_face, n.back_face, n.up_face, n.down_face))
            print("Solved State: Front Face: {}, Left Face: {}, Right Face:{} Back Face: {}, Up face: {}, Down face: {}\n".format(state.front_face, state.left_face, state.right_face, state.back_face, state.up_face, state.down_face))
            print("********")
            print("Moves: {}".format(state.moves))
            print("*******")
            print("Charles Truscott Watters, Byron Bay NSW 2481")
            break
#        c += 1

Charles()