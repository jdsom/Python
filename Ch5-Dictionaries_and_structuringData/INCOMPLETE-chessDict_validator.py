import pprint

board = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop',
         '5h': 'bqueen', '3e': 'wking'}


pieces = {'black':{'bpawn': 8,  'bbishop': 2, 'bknight': 2, 'bbrook': 2, 
        'bking': 1, 'bqueen': 1}, 
        'white': {'wpawn': 8, 'wbishop': 2, 'wrook': 2,  'wking': 1,  
        'wqueen': 1}}


def isValidChessBoard(dict):
        wking, bking, wpieces, bpieces = 0, 0, 0, 0
        wpawns, bpawns, spaces, check = 0, 0, [], True 
        for i in range(1,9):
                for j in ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'):
                        spaces.append(i+j)
        
        for space, piece in board.items():
                if space not in spaces:
                        check = False
                if piece == wking:
                        wking += 1
                if piece == bking:
                        bking += 1
                if piece == wpawns:
                        wpawns += 1
                if piece == bpawns:
                        bpawns += 1
                if piece == piece.startswith('w'):
                        wpieces += 1
                if piece == piece.startswith('b'):
                        bpieces += 1
        #for k, v in pieces.items():
