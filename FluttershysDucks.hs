import Data.List (sort)

main = interact $ unlines . map swap . sort . map swap . drop 1 . lines
  where
    swap name = unwords $ reverse $ words name