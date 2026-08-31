import Text.Read (readMaybe)
import Data.Char (toUpper)
import Data.List (intersperse)
import Debug.Trace (traceShow)
import Data.List (maximumBy)
import Data.Ord (comparing)
import Debug.Trace (trace)


type Board = [(Int, Int, Int)]

type Move = (Pos, Pos, Pos)
type Pos = (Int, Int)

-- vraci pocatecni stav hraci desky
initialBoard :: Board
initialBoard =
    [ -- Bílé amazonky 
      (0, 3, 1), (3, 0, 1), (6, 0, 1), (9, 3, 1)

      -- Černé amazonky 
    , (0, 6, 2), (3, 9, 2), (6, 9, 2), (9, 6, 2)
    ]


parseCord :: String -> Maybe Pos
parseCord (letter:number) = do

    -- enum value letter - enum A vraci cislo x souradnice (-- z 1-10 na 0-9)
    let x = fromEnum (toUpper letter) - fromEnum 'A'


    -- cteme jedno nebo dve cifry
    yy <- readMaybe number :: Maybe Int
    let  y = yy -1  -- z 1-10 na 0-9

    if x >= 0 && x <= 9 && y >= 0 && y <= 9
        then Just (x,y)
        else Nothing
parseCord _ = Nothing


-- Bere vstup cloveka a vraci move
parseMove :: String -> Maybe Move
parseMove input = case words input of
    [start, end, arrow] -> do
        s <- parseCord start
        e <- parseCord end
        a <- parseCord arrow
        return (s,e,a)
    _ -> Nothing

-- 'playing' je číslo hráče na tahu (0 pro bileho tedy cloveka a 1 pro ai)
updateBoard :: Board -> Move -> Int -> Board
updateBoard board (pos1, pos2, pos3) playing = newBoard
  where 
    tempBoard = filter (\(bx, by, _) -> (bx, by) /= pos1) board 
    
    (x2, y2) = pos2
    (x3, y3) = pos3
    amazon = (x2, y2, playing+1)
    arrow  = (x3, y3, 3)
    
    newBoard = amazon : arrow : tempBoard


-- vraci stav desky na souradnicich 
getState :: Board -> Int -> Int -> Int
getState [] _ _ = 0
getState ((xx,yy, state):rest) x y
    | xx == x && yy == y = state
    | otherwise = getState rest x y


-- vraci znak podle stavu
getTileAt :: Board -> Int -> Int -> Char
getTileAt board x y
    | state == 0 = '.'
    | state == 1 = 'W'
    | state == 2 = 'B'
    | state == 3 = 'X'
    | otherwise  = '?'
  where
    state = getState board x y

-- vraci desku v ascii
renderBoard :: Board -> String
renderBoard board = unlines (header : rows)
  where
    header = "   A B C D E F G H I J"
    
    -- bily je dole 
    rows = [ renderRow y | y <- [9, 8 .. 0] ]
    
    renderRow y = 
        let 
            rowNumber = y + 1 
            gridContent = intersperse ' ' [ getTileAt board x y | x <- [0..9] ]
        in 
            pad rowNumber ++ " " ++ gridContent
    pad n 
        | n < 10    = show n ++ " "
        | otherwise = show n


-- vraci tru pokud je tah legalni
checkMoveLegality :: Board -> Move -> Int -> Bool
checkMoveLegality board (pos1, pos2, pos3) playing = 
   
    getState board startX startY == playing + 1
   &&
     (checkLegality board pos1 pos2
        && checkLegality tempBoard pos2 pos3)
    where
        (startX, startY) = pos1 
        tempBoard = filter (\(x, y, _) -> x /= startX || y /= startY) board

-- vraci true pokud je cesta mezi pos1 a pos2 legalni
checkLegality :: Board -> Pos -> Pos -> Bool
checkLegality [] _ _ = False
checkLegality board pos1 pos2 = case getPath pos1 pos2 of
    Nothing -> False
    Just path -> all (isPosEmpty board) path

-- vraci vsechny souradnice mezi pos1 a pos2
getPath :: Pos -> Pos -> Maybe [Pos]
getPath (x1,y1) (x2,y2)
    | isQueenMove && distance > 0 =
        Just [ (x1 + i * dirX, y1 + i * dirY) | i <- [1..distance] ]
    | otherwise = Nothing
  where
        dx = x2 - x1
        dy = y2 - y1

        dirX = signum dx
        dirY = signum dy

        distance = max (abs dx) (abs dy)

        isQueenMove = (dx == 0) || (dy == 0) || (abs dx == abs dy)

-- vraci true pokud je souradnice empty neboli stav je 0
isPosEmpty :: Board -> Pos -> Bool
isPosEmpty board (x,y) =  getState board x y == 0

gameLoop :: Board -> Int -> IO ()
gameLoop board currentPlayer = do
    putStrLn "Aktualni stav desky:"
    putStrLn (renderBoard board)

    if currentPlayer == 1
        then do
            putStrLn "AI je na tahu..."
            case getBestMove board currentPlayer 1 of
                Just move -> do
                    let newBoard = updateBoard board move currentPlayer
                    let nextPlayer = (currentPlayer + 1) `mod` 2
                    gameLoop newBoard nextPlayer
                Nothing -> do
                    putStrLn "AI nema zadny legalni tah. Hrac vyhral!"
        else do
            putStrLn "Hrac je na tahu:"

    input <- getLine

    case parseMove input of 
        Just move -> 
            if checkMoveLegality board move currentPlayer
                then do 
                    -- tah je legalni takze updatujeme board
                    let newBoard = updateBoard board move currentPlayer
                    let nextPlayer = (currentPlayer + 1) `mod` 2
                    gameLoop newBoard nextPlayer
                else do
                    -- tah neni legalni 
                    putStrLn "Neplatny tah, zkuste to znovu."
                    gameLoop board currentPlayer
main :: IO ()
main = do

    putStrLn "==============================="
    putStrLn "   Vitejte ve hre Amazonky!    "
    putStrLn "==============================="

    gameLoop initialBoard 0

    -- Spustíme nekonečnou smyčku s počátečním stavem
getPlayerAmazons :: Board -> Int -> [Pos]
getPlayerAmazons board player = [(x,y) | (x,y,state) <- board, state == player +1]

allPositions :: [Pos]
allPositions = [(x,y) | x <- [0..9], y <- [0..9]]

directions :: [(Int, Int)]
directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

-- Pomocná kontrola, jestli jsme nevyjeli mimo desku (0-9)
onBoard :: (Int, Int) -> Bool
onBoard (x, y) = x >= 0 && x <= 9 && y >= 0 && y <= 9

-- jdeme ve smeru dx,dy dokud nenarazime a pridavame vsechny souradnice do listu
walk :: Board -> (Int, Int) -> (Int, Int) -> [(Int, Int)]
walk board (x, y) (dx, dy) =
    let nextPos = (x + dx, y + dy)
    in if onBoard nextPos && isPosEmpty board nextPos
       then nextPos : walk board nextPos (dx, dy) -- Přidáme políčko a jdeme dál
       else []

getReachable :: Board -> Pos -> [Pos]
getReachable board pos = concatMap (walk board pos) directions

getAllLegalMoves :: Board -> Int-> [Move]
getAllLegalMoves board player = do
    let playerAmazons = getPlayerAmazons board player

    amazon <- playerAmazons
    destination <- getReachable board amazon
    let tempBoard = filter (\(bx, by, _) -> (bx, by) /= amazon) board 

    arrow <- getReachable tempBoard destination

    return  (amazon, destination, arrow)


-- Heuristika pro vyhodnoceni stavu desky. Rozdil moves mezi hrace a protihracem
evaluateBoard :: Board -> Int -> Int
evaluateBoard board player = 
    let 
        playerMoves = length (getAllLegalMoves board player)
        opponentMoves = length (getAllLegalMoves board ((player + 1) `mod` 2))
    in
        playerMoves - opponentMoves


-- vraci best move pro hrace na tahu s hloubkou depth pomoci minimax
getBestMove :: Board -> Int -> Int -> Maybe Move
getBestMove board player depth =
    let legalMoves = getAllLegalMoves board player

    in  
        if null legalMoves
        then Nothing 
        else 
            let 
                nextPlayer = (player + 1) `mod` 2

                -- scoreMove je pomocna funkce ktera pouziva minimax na score tahu
                scoreMove move =
                    let newBoard = updateBoard board move player
                    in minimax newBoard (depth - 1) player nextPlayer
                
                scoresMoves = [(move, scoreMove move) | move <- legalMoves]
                bestMove = maximumBy (comparing snd) scoresMoves
            in Just (fst bestMove)

minimax :: Board -> Int -> Int -> Int -> Int
minimax board 0 ai _ = evaluateBoard board ai
minimax board depth ai currentPlayer =
    let legalMoves = getAllLegalMoves board currentPlayer
    in if null legalMoves 
        then 
            -- hra konci protoze nemame zadny tah
            if currentPlayer == ai 
                then -99999 -- AI prohrava
                else 100000  -- AI vyhrava
            
        else
            let nextPlayer = (currentPlayer + 1) `mod` 2
                scores = [minimax (updateBoard board move currentPlayer) (depth -1) ai nextPlayer | move <- legalMoves]
            in
                if currentPlayer == ai 
                    then maximum scores -- AI se snazi maximalizovat
                    else minimum scores -- protihrac se snazi minimalizovat



-- board depth ai curplayer alpha beta 
alphabeta :: Board -> Int -> Int -> Int -> Int -> Int -> Int
alphabeta board 0 ai _ _ _ = evaluateBoard board ai
alphabeta board depth ai currentPlayer alpha beta =
    let legalMoves = getAllLegalMoves board currentPlayer
    in if null legalMoves
        then
             if currentPlayer == ai 
                then -99999 -- AI prohrava
                else 100000  -- AI vyhrava
        else
            let nextPlayer = (currentPlayer + 1) `mod` 2
            in if currentPlayer == ai
                then evaluateMax board legalMoves depth nextPlayer alpha beta (-99999)
                else evaluateMin board legalMoves depth nextPlayer alpha beta 99999
            where
                evaluateMax [] _ _ _ _ _ bestValue = bestValue
                evaluateMax (move:moves) depth nextPlayer alpha beta bestValue = 
                    let newBoard = updateBoard board move currentPlayer
                        score = alphabeta newBoard (depth -1) ai nextPlayer alpha beta
                        newAlpha = max alpha score
                        newBestValue = max bestValue score
                    in if newAlpha >= beta
                        then newAlpha -- beta cut-off
                        else  
               