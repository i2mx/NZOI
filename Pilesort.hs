main = interact $ solve . map read .  drop 1  . lines 
  where 
    solve :: [Int] -> Int
    solve [] = 0
    solve x = 1
    solve 