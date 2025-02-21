width '1' = 2
width '0' = 4
width _ = 3

main = interact $ unlines . map (show . wordWidth) . takeWhile (/= "0") . lines
  where
    wordWidth word = ((+ 1) . sum . map width) word + length word