main = interact $ unlines . map (res . palindrome) . takeWhile (/= "0") . lines 
  where 
    res x = if x then "yes" else "no" 
    palindrome = (==) <*> reverse