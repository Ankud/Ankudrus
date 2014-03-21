class piece(object):
    def __init__(self):
        self.player = None   # Какому игроку принадлежит шашка
        self.alive = False   # Жива ли ещё она (не побили)
        self.king = False    # В дамках?
        self.symbol = ''     # Для дебаг-вывода, обозначение шашки символом
class gameSquare(object):
    def __init__(self):
        self.validSquare = False    # Можно ли ходить на эту клетку
        self.occupied = False       # Занята ли клетка шашкой

        self.occupier = piece()     # Если клетка занята, указатель на шашку

    def printSymbol(self):
        print (self.occupier.symbol), # Выводим состояние текущей клетки
class gameBoard(object):
    def __init__(self):
        self._prepareBoard()     # Подготовка доски (создание объектов клетки)
        self._validateSquares()  # Метка клеток, по которым можно ходить
        self._populateSquares()  # Расстановка шашек
# Создаём двумерный массив [8][8]
def _prepareBoard(self):
    self._matrix = []
    for i in xrange(8):
        self._matrix.append( [gameSquare() for _ in xrange(8)] )
def _validateSquares(self):
    for row in xrange(8):
        for col in xrange(8):
            if self._darkQuad(row, col) == True:
                self._matrix[row][col].validSquare = False
                self._matrix[row][col].occupier.symbol = '.'
            else:
                self._matrix[row][col].validSquare = True
                self._matrix[row][col].occupier.symbol = '.'
def _darkQuad(self, row, col):
        return ((row%2) == (col%2))
# Tick areas on the board (shapes, empty, unmovable)
def _populateSquares(self):
    for row in xrange(8):
        for col in xrange(8):
            # Make up black squares
            if self._matrix[row][col].validSquare and row <= 2:
                self._matrix[row][col].occupied = True
                self._matrix[row][col].occupier.symbol = 'x'
                self._matrix[row][col].occupier.alive = True
                self._matrix[row][col].occupier.king = False
                self._matrix[row][col].occupier.player = 2

            # Make up white squares
            if self._matrix[row][col].validSquare and row >= 5:
                self._matrix[row][col].occupied = True
                self._matrix[row][col].occupier.symbol = 'o'
                self._matrix[row][col].occupier.alive = True
                self._matrix[row][col].occupier.king = False
                self._matrix[row][col].occupier.player = 1

            # Fill empty quads with empty space
            if self._matrix[row][col].validSquare and row > 2 and row < 5:
                self._matrix[row][col].ocuppied = False
def _printDebugBoard(self):
    for row in xrange(8):
        for col in xrange(8):
            self._matrix[row][col].printSymbol()
        print ('')
if __name__ == '__main__':
    # Активный игрок
    player = 1

    # Координаты фишки, которую нужно передвинуть
    old_row = 5
    old_col = 4

    # Координаты, куда нужно совершить ход
    new_row = 4
    new_col = 5

    board = gameBoard()
    board._printDebugBoard()
def occupySquare(self, player, row, col):
    return ((self._matrix[row][col].occupier.player == player) and
            (self._matrix[row][col].occupier.alive))
def squareOccupied(self, new_row, new_col):
    return self._matrix[new_row][new_col].occupied
def validDirection(self, old_row, old_col, new_row, new_col, player):
    # Vertical movement
    if not self._matrix[old_row][old_col].occupier.king:
        if player == 1:
            if not (old_row > new_row and (old_row - new_row) <= 2):
                return False
        elif player == 2:
            if not (old_row < new_row and (new_row - old_row) <= 2):
                return False
    elif self._matrix[old_row][old_col].occupier.king:
        if math.fabs(old_row - new_row) > 2:
            return False

    # Horizontal movement
    if math.fabs(old_row - new_row) != math.fabs(old_col - new_col):
        return False

    return True
if math.fabs(old_row - new_row) == 1:
    board.movePiece(old_row, old_col, new_row, new_col)
def movePiece(self, old_row, old_col, new_row, new_col):
    # Занимаем новую клетку, копируем указатель на шашку в клетку
    self._matrix[new_row][new_col].occupied = True
    self._matrix[new_row][new_col].occupier = self._matrix[old_row][old_col].occupier

    # Старое место теперь свободно
    self._matrix[old_row][old_col].occupied = False
    self._matrix[old_row][old_col].occupier.alive = False
if __name__ == '__main__':
    player = 1

    old_row = 5
    old_col = 4

    new_row = 4
    new_col = 5

    board = gameBoard()

    board._matrix[old_row][old_col].occupier.symbol = '!'
    board._matrix[new_row][new_col].occupier.symbol = '&'

    board._printDebugBoard()

    for i in range(1):
        # These should be in game cycle
        if not board.occupySquare(player, old_row, old_col):
            print ('Player ' + str(player) + ' doesn`t have square at given coordinates!')
            continue

        if board.squareOccupied(new_row, new_col):
            print ('Player ' + str(player) + ' can`t move the square to given coordinates!')
            continue

        if not board.validDirection(old_row, old_col, new_row, new_col, player):
            print ('Player ' + str(player) + ' chosen movement is invalid!')
            continue

        # If chosen movement is just a single step
        if math.fabs(old_row - new_row) == 1:
            board.movePiece(old_row, old_col, new_row, new_col)
if math.fabs(old_row - new_row) == 2:
    if not board.checkJump(old_row, old_col, new_row, new_col, player):
        print ('Player + ' + str(player) + ' jump is invalid moving')
        continue
    else:
        board.jumpPiece(old_row, old_col, new_row, new_col)
def checkJump(old_row, old_col, new_row, new_col, player):
    # Бой вперёд
    if old_row > new_row:
        if old_col > new_col:
            # Если бъем вправо
            if ((self._matrix[old_row-1][old_col-1].occupied) or
               (self._matrix[old_row-1][old_col-1].occupier.player == player)):
                    return False
        elif old_col < new_col:
            # Бьем влево
            if ((self._matrix[old_row-1][old_col+1].occupied) or
               (self._matrix[old_row-1][old_col+1].occupier.player == player)):
                   return False
    # Бой назад
    elif old_row < new_row:
        if old_col > new_col:
            if ((self._matrix[old_row+1][old_col-1].occupied) or
            (self._matrix[old_row+1][old_col-1].occupier.player == player)):
                return False
        elif old_col < new_col:
            if ((self._matrix[old_row+1][old_col+1].occupied) or
                (self._matrix[old_row+1][old_col+1].occupier.player == player)):
                    return False

    return True
def jumpPiece(old_row, old_col, new_row, new_col):
    # Занимаем клетку, куда собираемся идти
    self._matrix[new_row][new_col].occupied = True
    self._matrix[new_row][new_col].occupier = self._matrix[old_row][old_col].occupier

    # Освобождаем старую
    self._matrix[old_row][old_col].occupied = False
    self._matrix[old_row][old_col].occupier.alive = False

    # Вычисляем координаты фишки, которую мы побили
    if old_row > new_row:
        jumpRow = old_row - 1
        if old_col > new_col:
            jumpCol = old_col - 1
        elif old_col < new_col:
            jumpCol = old_col + 1
    elif old_row < new_row:
        jumpRow = old_row + 1
        if old_col > new_col:
            jumpCol = old_col - 1
        elif old_col < new_col:
            jumpCol = old_col + 1

    # Битую фишку позначаем, как неактивную
    self._matrix[jumpRow][jumpCol].occupied = False
    self._matrix[jumpRow][jumpCol].occupier.alive = False
if ((player == 1 and new_row == 0) or
   (player == 2 and new_row == 7)):
        board.kingMe(new_row, new_col, player)
def kingMe(row, col, player):
    self._matrix[row][col].occupier.king = True

    if player == 1:
        self._matrix[row][col].occupier.symbol = 'O'
    elif player == 2:
        self._matrix[row][col].occupier.symbol = 'X'
player = (player%2) + 1

board.gameEnded(player):
    print ('Player: ' + str(player) + ' has won the game')
def gameEnded(player):
    moves = 0

    for row in xrange(8):
            for col in xrange(8):
                if self._matrix[row][col].validSquare and
                   self._matrix[row][col].occupied and
                   self._matrox[row][col].occupier.player == player and
                   (
                        self.moveSingleSpace(player, row, col) or
                        self.jumpAvailable(player, row, col, 0, 0, 0)
                   ):
                   moves += 1

    if not piecesLeft(player):
        return True
    elif not moves:
        return True
    else:
        return False
piecesLeft – остались ли ещё шашки
moveSingleSpace – есть ли ещё хода для какой-либо шашки
jumpAvailable – может ли какая-либо шашка сделать бой
Самая простая – piecesLeft, с неё и начнём:

def piecesLeft(player):
    pieces = 0

    for row in xrange(8):
            for col in xrange(8):
                if self._matrix[row][col].validSquare and
                self._matrix[row][col].occupied and
                self._matrix[row][col].occupier.player == player:
                    pieces += 1

    return pieces
def moveSingleSpace(player, row, col):
    if
       (
            not self._matrix[row-1][col-1].occupied and
            not (row-1) < 0 and
            not (col-1) < 0 and
            self.validDirection(row, col, row-1, col-1, player)
       ) or
       (
            not self._matrix[row-1][col+1].occupied and
            not (row-1) < 0 and
            not (col+1) > 7 and
            self.validDirection(row, col, row-1, col+1, player)
       ) or
       (
            not self._matrix[row+1][col-1].occupied and
            not (row+1) > 7 and
            not (col-1) < 0 and
            self.validDirection(row, col, row+1, col-1, player)
       ) or
       (
            not self._matrix[row+1][col+1].occupied and
            not (row+1) > 7 and
            not (col+1) > 7 and
            self.validDirection(row, col, row+1, col+1, player)
       ):
        return True
    else:
        return False
def jumpAvailable(player, row, col, flag, old_row, old_col):
    if
       (
            not self._matrix[row-2][col-2].occupied and
            not (row-2) < 0 and
            not (col-2) < 0 and
            self.validDirection(row, col, row-2, col-2, player) and
            self.checkJump(row, col, row-2, col-2, player)
       ) or
       (
            not self._matrix[row-2][col+2].occupied and
            not (row-2) < 0 and
            not (col+2) > 7 and
            self.validDirection(row, col, row-2, col+2, player) and
            self.checkJump(row, col, row-2, col+2, player)
       ) or
       (
            not self._matrix[row+2][col-2].occupied and
            not (row+2) > 7 and
            not (col-2) < 0 and
            self.validDirection(row, col, row+2, col-2, player) and
            self.checkJump(row, col, row+2, col-2, player)
       ) or
       (
            not self._matrix[row+2][col+2].occupied and
            not (row+2) > 7 and
            not (col+2) > 7 and
            self.validDirection(row, col, row+2, col+2, player) and
            self.checkJump(row, col, row+2, col+2, player)
       ):
        return True
    else:
        return False