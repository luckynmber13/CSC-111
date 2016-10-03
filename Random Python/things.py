#
#   

'''
Program:  lab6.py - Arcturian Darts
Author:  V Manes
Class:   CSC 111
Instructor:  V Manes
Due:     <date>
Written  10/2/16

Program description - Dart game, based on relation of first player throw and
    second player throw. Demonstrates Booleans and nested branching

Program usage: <any special instructions>

Todo: <list anything yet to be done>

Bugs: <list any known bugs>

Modifications: <list significant work>
'''



'''
Function:  <function name>
Author:  <author name>
Function description:  <brief description>

Parameters: <list inputs>

Return: <describe return value,if any>
'''
def main( ):

    #variable declarations
    hit_a_x = 0
    hit_a_y = 0
    hit_b_y = 0
    hit_b_x = 0
    a_score = 0
    b_score = 0

    #function body
    print( "Arcturian Darts - try to hit the other player's dart" )

    #get dart throws
    print( "First player up." )
    hit_a_x = int( input( "Player 1 x: " ) )
    hit_a_y = int( input( "Player 1 y: " ) )

    print( "\nSecond player up. " )
    print( "Shooting for (%d, %d) " % (hit_a_x, hit_a_y) )
    hit_b_x = int( input( "Player 2 x: " ) )
    hit_b_y = int( input( "Player 2 y: " ) )

    #test for direct hit
    if hit_a_x == hit_b_x and hit_a_y == hit_b_y:
        print( "Player 2 scores a direct hit! 50 points" )
        b_score += 50
        
    #test horizontal or vertical line
    elif hit_a_x == hit_b_x or hit_a_y == hit_b_y:
        print( "Player 2 hit on line, 20 points, 1 gets 30" )
        a_score += 30
        b_score += 20
    
    #test perfect square
    elif abs( hit_a_x -hit_b_x ) == abs( hit_a_y - hit_b_y ):
        print( "Player 2 hit on square, 40 points, 1 gets 10" )
        a_score += 10
        b_score += 40
    else:
        #test for 3:2 rectangle
        if abs( hit_a_x -hit_b_x ) <= (2/3) * abs( hit_a_y - hit_b_y ) and \
            abs( hit_a_y - hit_b_y ) <= 1.5 * abs( hit_a_x -hit_b_x ) or \
            abs( hit_a_y -hit_b_y ) <= (2/3) * abs( hit_a_x - hit_b_x ) and \
            abs( hit_a_x - hit_b_x ) <= 1.5 * abs( hit_a_y -hit_b_y ):
            print( "Player 2 hit in safe rectangle, 30 points, 1 gets 20" )
            a_score += 20
            b_score += 30
        else:
            print( "Player 2 misses, 0 points, 1 gets 50" )
            a_score += 50
            b_score += 0
           
         
    





#DO NOT DELETE THESE LINES, THEY MUST BE LAST LINES IN FILE           
if __name__ == '__main__':
   main()
