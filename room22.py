A,B,C,D,E=1,2,3,4,5
F,G,H,I,J=6,7,8,9,10
K,L,M,N,O=11,12,13,14,15
P,Q,R,S,T=16,17,18,19,20
U,V,W,X,Y=21,22,23,24,25
Z        = 26

letters = [[J,A,W,I,D,T,M,X,P,B,W,S,A,V,A,N,N,A,H,X],
           [M,A,Q,S,H,A,N,E,A,X,Z,P,A,T,R,I,C,K,M,A],
           [X,S,B,Y,S,V,E,A,N,Y,O,E,N,A,J,R,I,I,N,Y],
           [D,N,M,I,L,Z,I,Y,N,U,E,R,N,R,I,S,C,Y,M,V],
           [T,L,E,I,G,E,Y,Y,A,N,F,I,S,E,E,H,A,Z,E,M],
           [H,E,I,D,L,A,I,U,I,A,E,A,J,Z,A,Z,X,G,I,V],
           [C,I,W,X,J,L,I,R,G,N,G,L,R,E,V,M,B,C,I,S],
           [O,N,V,Z,N,F,E,L,B,N,Y,C,L,D,A,Y,M,R,X,N],
           [O,A,N,N,A,H,I,R,E,A,Q,A,O,R,S,A,O,A,M,B],
           [L,D,K,P,T,N,A,V,W,I,G,U,C,G,T,N,U,A,X,Y],
           [I,Q,V,A,R,C,L,E,D,V,H,U,K,T,N,K,D,E,C,X],
           [V,R,C,N,Y,L,E,A,K,P,S,D,H,O,M,E,I,K,C,R],
           [I,J,P,Z,D,A,X,K,V,C,L,E,C,V,L,L,X,S,N,B],
           [A,J,A,A,N,O,A,A,N,A,W,H,U,E,A,M,A,R,O,N],
           [S,O,U,C,A,G,N,N,K,R,A,M,I,T,C,O,N,E,C,I],
           [S,S,L,H,L,Z,D,O,N,R,X,N,A,U,E,E,K,C,A,Z],
           [Y,H,Q,A,Y,N,E,K,L,A,E,N,Y,D,F,T,L,W,R,B],
           [L,U,I,R,R,L,R,I,T,V,B,X,D,W,S,T,L,I,A,M],
           [A,A,T,Y,D,Y,E,M,J,M,W,E,C,W,D,A,J,U,N,P],
           [W,Y,L,J,M,M,L,I,E,H,N,C,L,F,E,M,J,F,X,E]]



height = len(letters)
width = len(letters[0])


def a(name_ii):
    return ord(name_ii)-ord('@')

def is_name_in_box_xy(name, box, top, left):
    len_name = len(name)

    if len_name <= width - left:
        # Check left-to-right
        if all(a(name[ii]) == box[top][left+ii] for ii in range(len_name)):
            print(f'Row {top} Column {left} -> : {name}')
        # Check right-to-left
        if all(a(name[ii]) == box[top][left+len_name-ii-1] for ii in range(len_name)):
            print(f'Row {top} Column {left+len_name-1} <- : {name}')
            
    if len_name <= height - top:
    # Check top-to-bottom
        if all(a(name[ii]) == box[top+ii][left] for ii in range(len_name)):
            print(f'Row {top} Column {left} |v : {name}')
    # Check bottom-to-top
        if all(a(name[ii]) == box[top+len_name-ii-1][left] for ii in range(len_name)):
            print(f'Row {top+len_name-1} Column {left} |^ : {name}')

    if len_name <= height - top and len_name <= width - left:
    # Check topleft-to-bottomright
        if all(a(name[ii]) == box[top+ii][left+ii] for ii in range(len_name)):
            print(f'Row {top} Column {left} \\> : {name}')

    # Check topright-to-bottomleft
        if all(a(name[ii]) == box[top+ii][left+len_name-ii-1] for ii in range(len_name)):
            print(f'Row {top} Column {left+len_name-1} </ : {name}')

    # Check bottomleft-to-topright
        if all(a(name[ii]) == box[top+len_name-ii-1][left+ii] for ii in range(len_name)):
            print(f'Row {top+len_name-1} Column {left} /> : {name}')

    # Check bottomright-to-topleft
        if all(a(name[ii]) == box[top+len_name-ii-1][left+len_name-ii-1] for ii in range(len_name)):
            print(f'Row {top+len_name-1} Column {left+len_name-1} <\\ : {name}')

def is_name_in_box(name, letter):
    for ii in range(height):
        for jj in range(width):
            is_name_in_box_xy(name, letters, ii, jj)

# # Test
# for name in ['JAY','JLI','ELL','FLA','YAJ','YII','RILJ','LLE']:
#     is_name_in_box(name, letters)
if __name__ == '__main__':
    import sys
    if len(sys.argv)<2: 
        print('python3 room22.py <name>')
        sys.exit()
    is_name_in_box(sys.argv[1], letters)

