import pygame
pygame.init()

def GToC(Gray):
    Gray *= 3
    v = 0
    if Gray < 256:
        color = [[0,0,Gray]]
        while color[v][0] < Gray:
            v += 1
            color.append([color[v - 1][0], color[v - 1][1] + 1, color[v - 1][2] - 1])
            if color[v][1] == Gray - color[v][0] + 1:
                color[v] = [color[v][0] + 1, 0, Gray - color[v][0] - 1]
    elif 255 < Gray < 511:
        '''
        I con't figure out how to make this section
        '''
    else:
        '''
        Or this section
        '''
    '''
    formula for length of list of colors of an given Gray
    G = Gray
    1 + (9*1) + (9*2) ... (9*G) = length of color list
    or 
    1+\sum_{n=0}^{G}n\cdot9 or https://www.desmos.com/calculator/ebe8xbcwas
    '''
    factors = []
    for f in range(1, len(color) + 1):
        if not len(color)%f:
            factors.append(f)

    return color#, factors[int(len(factors)/2)], factors[int(len(factors)/2) - 1]
def window_set(W,H):
    global window
    window = pygame.display.set_mode((W,H))
def dot(color):
    dot = pygame.Surface((1,1))
    dot.fill(color)
    return dot
def chunker(seq, size):
    '''
    Chunks the list of colors to make an x and y list using the W,H made from the closest factors
    '''
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))
'''
run = True
while run:
    for c in range(0, 256):
        color, W, H = GToC(c)
        colors = []
        for group in chunker(color, H):
            colors.append(group)
        window_set(W, H)
        window.fill((255,0,0))
        pygame.display.flip()
        for x in range(0, len(colors)):
            for y in range(0, len(colors[x])):
                window.blit(dot(colors[x][y]), (x,y))
        file = f"""GToC/{c}.jpg"""
        pygame.image.save(window, file)
        print(c)
    run = False
    """
    Makes a screen with the W,H from the closest factors and draws every possible combination
    of colors made from the gray values. (only Can go up to Gray 85)
    0 - 85
    86 - 170
    171 - 255
    before the screen changes pygame saves it and places it in the GToC file
    """
'''


test = True
if test:
    print(len(GToC(86)))
    with open("colors.txt", "w") as f:
        f.write(str(GToC(86)))
        f.flush()
        f.close()

    '''
    test section are just for debugging
    
    using the formula will give you the exact number that len(GToC(Gray)) will give; if
    it prints the wrong number the code is wrong
    '''
test = False
